---
description: Performance objects can define one or more counters.
ms.assetid: a3a598b2-5623-4472-a814-620c6a003a7e
title: Retrieving Counter Data
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Counter Data

Performance objects can define one or more counters. The counter data for the counters is located in the [**PERF\_COUNTER\_BLOCK**](/windows/desktop/api/Winperf/ns-winperf-perf_counter_block) memory block. The location of the counter block within the object block depends on whether the object contains single instance counters or multiple instance counters. For details, see [Performance Data Format](performance-data-format.md).

You use the **CounterOffset** and **CounterSize** members of [**PERF\_COUNTER\_DEFINITION**](/windows/desktop/api/Winperf/ns-winperf-perf_counter_definition) to access the counter's data within the counter block. Currently, counter data is limited to **DWORD** and **ULONGLONG** data types (these are the only types that the Performance tool supports).

The **CounterType** member of [**PERF\_COUNTER\_DEFINITION**](/windows/desktop/api/Winperf/ns-winperf-perf_counter_definition) tells you what other information you need from the performance object in order to use the counter data. For some counters, you can use the counter data directly, but for others, you may need time base information or data from another counter in order to calculate a displayable value.

The following example shows how to use the counter type to determine the information you need to retrieve from the performance data for a counter in order to calculate a displayable counter value. For an example that calculates a displayable value based on the counter type, see [Calculating Counter Values](calculating-counter-values.md).


```C++
#include <windows.h>
#include <stdio.h>
#include <strsafe.h>

#pragma comment(lib, "advapi32.lib")

// Contains the elements required to calculate a counter value.
typedef struct _rawdata
{
    DWORD CounterType;
    ULONGLONG Data;          // Raw counter data
    LONGLONG Time;           // Is a time value or a base value
    DWORD MultiCounterData;  // Second raw counter value for multi-valued counters
    LONGLONG Frequency;
}RAW_DATA, *PRAW_DATA;

#define INIT_OBJECT_BUFFER_SIZE 48928   // Initial buffer size to use when querying specific objects.
#define INIT_GLOBAL_BUFFER_SIZE 122880  // Initial buffer size to use when using "Global" to query all objects.
#define BUFFER_INCREMENT 16384          // Increment buffer size in 16K chunks.
#define MAX_INSTANCE_NAME_LEN      255  // Max length of an instance name.
#define MAX_FULL_INSTANCE_NAME_LEN 511  // Form is parentinstancename/instancename#nnn.

LPBYTE GetPerformanceData(LPWSTR pwszSource, DWORD dwInitialBufferSize);
BOOL GetCounterValues(DWORD dwObjectIndex, DWORD dwCounterIndex, LPWSTR pInstanceName, RAW_DATA* pRawData);
BOOL GetValue(PERF_OBJECT_TYPE* pObject, PERF_COUNTER_DEFINITION* pCounter, PERF_COUNTER_BLOCK* pCounterDataBlock, PRAW_DATA pRawData);
PERF_COUNTER_BLOCK* GetCounterBlock(PERF_OBJECT_TYPE* pObject, LPWSTR pInstanceName);
PERF_COUNTER_DEFINITION* GetCounter(PERF_OBJECT_TYPE* pObject, DWORD dwCounterToFind);
PERF_OBJECT_TYPE* GetObject(DWORD dwObjectToFind);
PERF_INSTANCE_DEFINITION* GetObjectInstance(PERF_OBJECT_TYPE* pObject, LPWSTR pInstanceName);
DWORD GetSerialNo(LPWSTR pInstanceName);
BOOL GetFullInstanceName(PERF_INSTANCE_DEFINITION* pInstance, DWORD CodePage, WCHAR* pName);
BOOL ConvertNameToUnicode(UINT CodePage, LPCSTR pNameToConvert, DWORD dwNameToConvertLen, LPWSTR pConvertedName);
PERF_INSTANCE_DEFINITION* GetParentInstance(PERF_OBJECT_TYPE* pObject, DWORD dwInstancePosition);
BOOL DisplayCalculatedValue(RAW_DATA* pSample1, RAW_DATA* pSample2);

//Global variables
LPBYTE g_pPerfDataHead = NULL;   // Head of the performance data.

void wmain(void)
{
    RAW_DATA Sample1;
    RAW_DATA Sample2;
    BOOL fSuccess = FALSE;

    // Retrieve counter data for the Processor object.
    g_pPerfDataHead = (LPBYTE)GetPerformanceData(L"238", INIT_OBJECT_BUFFER_SIZE);
    if (NULL == g_pPerfDataHead)
    {
        wprintf(L"GetPerformanceData failed.\n");
        goto cleanup;
    }

    // Then, sample the "% Processor Time" counter for instance "0" of the Processor object.
    fSuccess = GetCounterValues(238, 6, L"0", &Sample1);
    if (FALSE == fSuccess)
    {
        wprintf(L"GetCounterValues failed.\n");
        goto cleanup;
    }

    // Display five data points for the counter.
    for (DWORD i = 0; i < 5; i++)
    {
        Sleep(1000);  // Wait one second before taking the next sample

        // Retrieve the object data again and get the next sample.
        g_pPerfDataHead = (LPBYTE)GetPerformanceData(L"238", INIT_OBJECT_BUFFER_SIZE);
        if (NULL == g_pPerfDataHead)
        {
            wprintf(L"GetPerformanceData in loop failed.\n");
            goto cleanup;
        }

        fSuccess = GetCounterValues(238, 6, L"0", &Sample2);
        if (FALSE == fSuccess)
        {
            wprintf(L"GetCounterValues failed.\n");
            goto cleanup;
        }

        // Calculate the value based on the two samples. For counter
        // types that do not use two samples, set the second parameter
        // to NULL.
        fSuccess = DisplayCalculatedValue(&Sample1, &Sample2);
        if (FALSE == fSuccess)
        {
            wprintf(L"DisplayCalculatedValue failed.\n");
            goto cleanup;
        }

        // Sample2 becomes Sample1 for the next iteration.
        memcpy(&Sample1, &Sample2, sizeof(RAW_DATA));
    }

cleanup:

    if (g_pPerfDataHead)
        free(g_pPerfDataHead);
}


// Retrieve a buffer that contains the specified performance data.
// The pwszSource parameter determines the data that GetRegistryBuffer returns.
//
// Typically, when calling RegQueryValueEx, you can specify zero for the size of the buffer
// and the RegQueryValueEx will set your size variable to the required buffer size. However, 
// if the source is "Global" or one or more object index values, you will need to increment
// the buffer size in a loop until RegQueryValueEx does not return ERROR_MORE_DATA. 
LPBYTE GetPerformanceData(LPWSTR pwszSource, DWORD dwInitialBufferSize)
{
    LPBYTE pBuffer = NULL;
    DWORD dwBufferSize = 0;        //Size of buffer, used to increment buffer size
    DWORD dwSize = 0;              //Size of buffer, used when calling RegQueryValueEx
    LPBYTE pTemp = NULL;           //Temp variable for realloc() in case it fails
    LONG status = ERROR_SUCCESS; 

    dwBufferSize = dwSize = dwInitialBufferSize;

    pBuffer = (LPBYTE)malloc(dwBufferSize);
    if (pBuffer)
    {
        while (ERROR_MORE_DATA == (status = RegQueryValueEx(HKEY_PERFORMANCE_DATA, pwszSource, NULL, NULL, pBuffer, &dwSize)))
        {
            //Contents of dwSize is unpredictable if RegQueryValueEx fails, which is why
            //you need to increment dwBufferSize and use it to set dwSize.
            dwBufferSize += BUFFER_INCREMENT;

            pTemp = (LPBYTE)realloc(pBuffer, dwBufferSize);
            if (pTemp)
            {
                pBuffer = pTemp;
                dwSize = dwBufferSize;
            }
            else
            {
                wprintf(L"Reallocation error.\n");
                free(pBuffer);
                pBuffer = NULL;
                goto cleanup;
            }
        }

        if (ERROR_SUCCESS != status)
        {
            wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
            free(pBuffer);
            pBuffer = NULL;
        }
    }
    else
    {
        wprintf(L"malloc failed to allocate initial memory request.\n");
    }

cleanup:

    RegCloseKey(HKEY_PERFORMANCE_DATA);

    return pBuffer;
}


// Use the object index to find the object in the performance data. Then, use the
// counter index to find the counter definition. The definition contains the offset
// to the counter data in the counter block. The location of the counter block 
// depends on whether the counter is a single instance counter or multiple instance counter.
// After finding the counter block, retrieve the counter data.
BOOL GetCounterValues(DWORD dwObjectIndex, DWORD dwCounterIndex, LPWSTR pInstanceName, RAW_DATA* pRawData)
{
    PERF_OBJECT_TYPE* pObject = NULL;
    PERF_COUNTER_DEFINITION* pCounter = NULL;
    PERF_COUNTER_BLOCK* pCounterDataBlock = NULL;
    BOOL fSuccess = FALSE;

    pObject = GetObject(dwObjectIndex);
    if (NULL == pObject)
    {
        wprintf(L"Object  %d not found.\n", dwObjectIndex);
        goto cleanup;
    }

    pCounter = GetCounter(pObject, dwCounterIndex);
    if (NULL == pCounter)
    {
        wprintf(L"Counter %d not found.\n", dwCounterIndex);
        goto cleanup;
    }

    // Retrieve a pointer to the beginning of the counter data block. The counter data
    // block contains all the counter data for the object.
    pCounterDataBlock = GetCounterBlock(pObject, pInstanceName);
    if (NULL == pCounterDataBlock)
    {
        wprintf(L"Instance %s not found.\n", pInstanceName);
        goto cleanup;
    }

    ZeroMemory(pRawData, sizeof(RAW_DATA));
    pRawData->CounterType = pCounter->CounterType;
    fSuccess = GetValue(pObject, pCounter, pCounterDataBlock, pRawData);

cleanup:

    return fSuccess;
}


// Use the object index to find the object in the performance data.
PERF_OBJECT_TYPE* GetObject(DWORD dwObjectToFind)
{
    LPBYTE pObject = g_pPerfDataHead + ((PERF_DATA_BLOCK*)g_pPerfDataHead)->HeaderLength;
    DWORD dwNumberOfObjects = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->NumObjectTypes;
    BOOL fFoundObject = FALSE;

    for (DWORD i = 0; i < dwNumberOfObjects; i++)
    {
        if (dwObjectToFind == ((PERF_OBJECT_TYPE*)pObject)->ObjectNameTitleIndex)
        {
            fFoundObject = TRUE;
            break;
        }

        pObject += ((PERF_OBJECT_TYPE*)pObject)->TotalByteLength;
    }

    return (fFoundObject) ? (PERF_OBJECT_TYPE*)pObject : NULL;  
}

// Use the counter index to find the object in the performance data.
PERF_COUNTER_DEFINITION* GetCounter(PERF_OBJECT_TYPE* pObject, DWORD dwCounterToFind)
{
    PERF_COUNTER_DEFINITION* pCounter = (PERF_COUNTER_DEFINITION*)((LPBYTE)pObject + pObject->HeaderLength);
    DWORD dwNumberOfCounters = pObject->NumCounters;
    BOOL fFoundCounter = FALSE;

    for (DWORD i = 0; i < dwNumberOfCounters; i++)
    {
        if (pCounter->CounterNameTitleIndex == dwCounterToFind)
        {
            fFoundCounter = TRUE;
            break;
        }

        pCounter++;
    }

    return (fFoundCounter) ? pCounter : NULL;
}


// Returns a pointer to the beginning of the PERF_COUNTER_BLOCK. The location of the 
// of the counter data block depends on whether the object contains single instance
// counters or multiple instance counters (see PERF_OBJECT_TYPE.NumInstances).
PERF_COUNTER_BLOCK* GetCounterBlock(PERF_OBJECT_TYPE* pObject, LPWSTR pInstanceName)
{
    PERF_COUNTER_BLOCK* pBlock = NULL;
    PERF_INSTANCE_DEFINITION* pInstance = NULL;

    // If there are no instances, the block follows the object and counter structures.
    if (0 == pObject->NumInstances || PERF_NO_INSTANCES == pObject->NumInstances) 
    {                                
        pBlock = (PERF_COUNTER_BLOCK*)((LPBYTE)pObject + pObject->DefinitionLength);
    }
    else if (pObject->NumInstances > 0 && pInstanceName)  // Find the instance. The block follows the instance
    {                                                     // structure and instance name.
        pInstance = GetObjectInstance(pObject, pInstanceName);
        if (pInstance)
        {
            pBlock = (PERF_COUNTER_BLOCK*)((LPBYTE)pInstance + pInstance->ByteLength);
        }
    }

    return pBlock;
}


// If the instance names are unique (there will never be more than one instance
// with the same name), then finding the same instance is not an issue. However, 
// if the instance names are not unique, there is no guarantee that the instance 
// whose counter value you are retrieving is the same instance from which you previously
// retrieved data. This function expects the instance name to be well formed. For 
// example, a process object could have four instances with each having svchost as its name.
// Since service hosts come and go, there is no way to determine if you are dealing with 
// the same instance.
// Starting in Windows 20 20H2, use the "Process V2" counterset to avoid this issue.
//
// The convention for specifying an instance is parentinstancename/instancename#nnn.
// If only instancename is specified, the first instance found that matches the name is used.
// Specify parentinstancename if the instance is the child of a parent instance.
PERF_INSTANCE_DEFINITION* GetObjectInstance(PERF_OBJECT_TYPE* pObject, LPWSTR pInstanceName)
{
    PERF_INSTANCE_DEFINITION* pInstance = (PERF_INSTANCE_DEFINITION*)((LPBYTE)pObject + pObject->DefinitionLength);
    BOOL fSuccess = FALSE;
    WCHAR szName[MAX_FULL_INSTANCE_NAME_LEN + 1];
    PERF_COUNTER_BLOCK* pCounterBlock = NULL;
    DWORD dwSerialNo = GetSerialNo(pInstanceName);
    DWORD dwOccurrencesFound = 0;
    DWORD dwNameLen = 0;
    DWORD dwInputNameLen = (DWORD)wcslen(pInstanceName);

    for (LONG i = 0; i < pObject->NumInstances; i++)
    {
        GetFullInstanceName(pInstance, pObject->CodePage, szName);
        if ((dwNameLen = (DWORD)wcslen(szName)) <= dwInputNameLen)
        {
            if (0 == _wcsnicmp(szName, pInstanceName, dwNameLen))  // The name matches
            {
                dwOccurrencesFound++;

                // If the input name does not specify an nth instance or
                // the nth instance has been found, return the instance.
                // It is 'dwSerialNo+1' because cmd#3 is the fourth occurrence.
                if (0 == dwSerialNo || dwOccurrencesFound == (dwSerialNo+1))
                {
                    return pInstance;
                }
            }
        }

        pCounterBlock = (PERF_COUNTER_BLOCK*)((LPBYTE)pInstance + pInstance->ByteLength);
        pInstance = (PERF_INSTANCE_DEFINITION*)((LPBYTE)pInstance + pInstance->ByteLength + pCounterBlock->ByteLength);
    }

    return NULL;
}


// Parses the instance name for the serial number. The convention is to use
// a serial number appended to the instance name to identify a specific
// instance when the instance names are not unique. For example, to specify
// the fourth instance of svchost, use svchost#3 (the first occurrence does
// not include a serial number).
DWORD GetSerialNo(LPWSTR pInstanceName)
{
    LPWSTR pSerialNo = NULL;
    DWORD dwLength = 0;
    DWORD value = 0;

    pSerialNo = wcschr(pInstanceName, '#');
    if (pSerialNo)
    {
        pSerialNo++;
        value = _wtoi(pSerialNo);
    }

    return value;
}


// Retrieve the full name of the instance. The full name of the instance includes
// the name of this instance and its parent instance, if this instance is a 
// child instance. The full name is in the form, "parent name/child name".
// For example, a thread instance is a child of a process instance. 
//
// Providers are encouraged to use Unicode strings for instance names. If 
// PERF_INSTANCE_DEFINITION.CodePage is zero, the name is in Unicode; otherwise,
// use the CodePage value to convert the string to Unicode.
BOOL GetFullInstanceName(PERF_INSTANCE_DEFINITION* pInstance, DWORD CodePage, WCHAR* pName)
{
    BOOL fSuccess = TRUE;
    PERF_INSTANCE_DEFINITION *pParentInstance = NULL;
    PERF_OBJECT_TYPE *pParentObject = NULL;
    DWORD dwLength = 0;
    WCHAR wszInstanceName[MAX_INSTANCE_NAME_LEN+1];
    WCHAR wszParentInstanceName[MAX_INSTANCE_NAME_LEN+1];

    if (CodePage == 0)  // Instance name is a Unicode string
    {
        // PERF_INSTANCE_DEFINITION->NameLength is in bytes, so convert to characters.
        dwLength = (MAX_INSTANCE_NAME_LEN < (pInstance->NameLength/2)) ? MAX_INSTANCE_NAME_LEN : pInstance->NameLength/2;
        StringCchCopyN(wszInstanceName, MAX_INSTANCE_NAME_LEN+1, (LPWSTR)(((LPBYTE)pInstance)+pInstance->NameOffset), dwLength);
        wszInstanceName[dwLength] = '\0';
    }
    else  // Convert the multi-byte instance name to Unicode
    {
        fSuccess = ConvertNameToUnicode(CodePage, 
            (LPCSTR)(((LPBYTE)pInstance)+pInstance->NameOffset),  // Points to string
            pInstance->NameLength,
            wszInstanceName);

        if (FALSE == fSuccess)
        {
            wprintf(L"ConvertNameToUnicode for instance failed.\n");
            goto cleanup;
        }
    }

    if (pInstance->ParentObjectTitleIndex)
    {
        // Use the index to find the parent object. The pInstance->ParentObjectInstance
        // member tells you that the parent instance is the nth instance of the 
        // parent object.
        pParentObject = GetObject(pInstance->ParentObjectTitleIndex);
        pParentInstance = GetParentInstance(pParentObject, pInstance->ParentObjectInstance);

        if (CodePage == 0)  // Instance name is a Unicode string
        {
            dwLength = (MAX_INSTANCE_NAME_LEN < pParentInstance->NameLength/2) ? MAX_INSTANCE_NAME_LEN : pParentInstance->NameLength/2;
            StringCchCopyN(wszParentInstanceName, MAX_INSTANCE_NAME_LEN+1, (LPWSTR)(((LPBYTE)pParentInstance)+pParentInstance->NameOffset), dwLength);
            wszParentInstanceName[dwLength] = '\0';
        }
        else  // Convert the multi-byte instance name to Unicode
        {
            fSuccess = ConvertNameToUnicode(CodePage, 
                (LPCSTR)(((LPBYTE)pParentInstance)+pParentInstance->NameOffset),  //Points to string.
                pInstance->NameLength,
                wszParentInstanceName);

            if (FALSE == fSuccess)
            {
                wprintf(L"ConvertNameToUnicode for parent instance failed.\n");
                goto cleanup;
            }
        }

        StringCchPrintf(pName, MAX_FULL_INSTANCE_NAME_LEN+1, L"%s/%s", wszParentInstanceName, wszInstanceName);
    }
    else
    {
        StringCchPrintf(pName, MAX_INSTANCE_NAME_LEN+1, L"%s", wszInstanceName);
    }

cleanup:

    return fSuccess;
}


// Converts a multi-byte string to a Unicode string. If the input string is longer than 
// MAX_INSTANCE_NAME_LEN, the input string is truncated.
BOOL ConvertNameToUnicode(UINT CodePage, LPCSTR pNameToConvert, DWORD dwNameToConvertLen, LPWSTR pConvertedName)
{
    BOOL fSuccess = FALSE;
    int CharsConverted = 0;
    DWORD dwLength = 0;

    // dwNameToConvertLen is in bytes, so convert MAX_INSTANCE_NAME_LEN to bytes.
    dwLength = (MAX_INSTANCE_NAME_LEN*sizeof(WCHAR) < (dwNameToConvertLen)) ? MAX_INSTANCE_NAME_LEN*sizeof(WCHAR) : dwNameToConvertLen;

    CharsConverted = MultiByteToWideChar((UINT)CodePage, 0, pNameToConvert, dwLength, pConvertedName, MAX_INSTANCE_NAME_LEN);
    if (CharsConverted)
    {
        pConvertedName[dwLength] = '\0';
        fSuccess = TRUE;
    }

    return fSuccess;
}


// Find the nth instance of an object.
PERF_INSTANCE_DEFINITION* GetParentInstance(PERF_OBJECT_TYPE* pObject, DWORD dwInstancePosition)
{
    LPBYTE pInstance = (LPBYTE)pObject + pObject->DefinitionLength;
    PERF_COUNTER_BLOCK* pCounter = NULL;

    for (DWORD i = 0; i < dwInstancePosition; i++)
    {
        pCounter = (PERF_COUNTER_BLOCK*)(pInstance + ((PERF_INSTANCE_DEFINITION*)pInstance)->ByteLength);
        pInstance += ((PERF_INSTANCE_DEFINITION*)pInstance)->ByteLength + pCounter->ByteLength;
    }

    return (PERF_INSTANCE_DEFINITION*)pInstance;
}


// Retrieve the raw counter value and any supporting data needed to calculate
// a displayable counter value. Use the counter type to determine the information
// needed to calculate the value.
BOOL GetValue(PERF_OBJECT_TYPE* pObject, 
    PERF_COUNTER_DEFINITION* pCounter, 
    PERF_COUNTER_BLOCK* pCounterDataBlock, 
    PRAW_DATA pRawData)
{
    PVOID pData = NULL;
    UNALIGNED ULONGLONG* pullData = NULL;
    PERF_COUNTER_DEFINITION* pBaseCounter = NULL;
    BOOL fSuccess = TRUE;

    //Point to the raw counter data.
    pData = (PVOID)((LPBYTE)pCounterDataBlock + pCounter->CounterOffset);

    //Now use the PERF_COUNTER_DEFINITION.CounterType value to figure out what
    //other information you need to calculate a displayable value.
    switch (pCounter->CounterType) {

    case PERF_COUNTER_COUNTER:
    case PERF_COUNTER_QUEUELEN_TYPE:
    case PERF_SAMPLE_COUNTER:
        pRawData->Data = (ULONGLONG)(*(DWORD*)pData);
        pRawData->Time = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfTime.QuadPart;
        if (PERF_COUNTER_COUNTER == pCounter->CounterType || PERF_SAMPLE_COUNTER == pCounter->CounterType)
        {
            pRawData->Frequency = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfFreq.QuadPart;
        }
        break;

    case PERF_OBJ_TIME_TIMER:
        pRawData->Data = (ULONGLONG)(*(DWORD*)pData);
        pRawData->Time = pObject->PerfTime.QuadPart;
        break;

    case PERF_COUNTER_100NS_QUEUELEN_TYPE:
        pRawData->Data = *(UNALIGNED ULONGLONG *)pData;
        pRawData->Time = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfTime100nSec.QuadPart;
        break;

    case PERF_COUNTER_OBJ_TIME_QUEUELEN_TYPE:
        pRawData->Data = *(UNALIGNED ULONGLONG *)pData;
        pRawData->Time = pObject->PerfTime.QuadPart;
        break;

    case PERF_COUNTER_TIMER:
    case PERF_COUNTER_TIMER_INV:
    case PERF_COUNTER_BULK_COUNT:
    case PERF_COUNTER_LARGE_QUEUELEN_TYPE:
        pullData = (UNALIGNED ULONGLONG *)pData;
        pRawData->Data = *pullData;
        pRawData->Time = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfTime.QuadPart;
        if (pCounter->CounterType == PERF_COUNTER_BULK_COUNT)
        {
            pRawData->Frequency = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfFreq.QuadPart;
        }
        break;

    case PERF_COUNTER_MULTI_TIMER:
    case PERF_COUNTER_MULTI_TIMER_INV:
        pullData = (UNALIGNED ULONGLONG *)pData;
        pRawData->Data = *pullData;
        pRawData->Frequency = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfFreq.QuadPart;
        pRawData->Time = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfTime.QuadPart;

        //These counter types have a second counter value that is adjacent to
        //this counter value in the counter data block. The value is needed for
        //the calculation.
        if ((pCounter->CounterType & PERF_MULTI_COUNTER) == PERF_MULTI_COUNTER)
        {
            ++pullData;
            pRawData->MultiCounterData = *(DWORD*)pullData;
        }
        break;

    //These counters do not use any time reference.
    case PERF_COUNTER_RAWCOUNT:
    case PERF_COUNTER_RAWCOUNT_HEX:
    case PERF_COUNTER_DELTA:
        pRawData->Data = (ULONGLONG)(*(DWORD*)pData);
        pRawData->Time = 0;
        break;

    case PERF_COUNTER_LARGE_RAWCOUNT:
    case PERF_COUNTER_LARGE_RAWCOUNT_HEX:
    case PERF_COUNTER_LARGE_DELTA:
        pRawData->Data = *(UNALIGNED ULONGLONG*)pData;
        pRawData->Time = 0;
        break;
    
    //These counters use the 100ns time base in their calculation.
    case PERF_100NSEC_TIMER:
    case PERF_100NSEC_TIMER_INV:
    case PERF_100NSEC_MULTI_TIMER:
    case PERF_100NSEC_MULTI_TIMER_INV:
        pullData = (UNALIGNED ULONGLONG*)pData;
        pRawData->Data = *pullData;
        pRawData->Time = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfTime100nSec.QuadPart;

        //These counter types have a second counter value that is adjacent to
        //this counter value in the counter data block. The value is needed for
        //the calculation.
        if ((pCounter->CounterType & PERF_MULTI_COUNTER) == PERF_MULTI_COUNTER)
        {
            ++pullData;
            pRawData->MultiCounterData = *(DWORD*)pullData;
        }
        break;

    //These counters use two data points, this value and one from this counter's
    //base counter. The base counter should be the next counter in the object's 
    //list of counters.
    case PERF_SAMPLE_FRACTION:
    case PERF_RAW_FRACTION:
        pRawData->Data = (ULONGLONG)(*(DWORD*)pData);
        pBaseCounter = pCounter+1;  //Get base counter
        if ((pBaseCounter->CounterType & PERF_COUNTER_BASE) == PERF_COUNTER_BASE)
        {
            pData = (PVOID)((LPBYTE)pCounterDataBlock + pBaseCounter->CounterOffset);
            pRawData->Time = (LONGLONG)(*(DWORD*)pData);
        }
        else
        {
            fSuccess = FALSE;
        }
        break;

    case PERF_LARGE_RAW_FRACTION:
        pRawData->Data = *(UNALIGNED ULONGLONG*)pData;
        pBaseCounter = pCounter+1;
        if ((pBaseCounter->CounterType & PERF_COUNTER_BASE) == PERF_COUNTER_BASE)
        {
            pData = (PVOID)((LPBYTE)pCounterDataBlock + pBaseCounter->CounterOffset);
            pRawData->Time = *(LONGLONG*)pData;
        }
        else
        {
            fSuccess = FALSE;
        }
        break;

    case PERF_PRECISION_SYSTEM_TIMER:
    case PERF_PRECISION_100NS_TIMER:
    case PERF_PRECISION_OBJECT_TIMER:
        pRawData->Data = *(UNALIGNED ULONGLONG*)pData;
        pBaseCounter = pCounter+1;
        if ((pBaseCounter->CounterType & PERF_COUNTER_BASE) == PERF_COUNTER_BASE)
        {
            pData = (PVOID)((LPBYTE)pCounterDataBlock + pBaseCounter->CounterOffset);
            pRawData->Time = *(LONGLONG*)pData;
        }
        else
        {
            fSuccess = FALSE;
        }
        break;

    case PERF_AVERAGE_TIMER:
    case PERF_AVERAGE_BULK:
        pRawData->Data = *(UNALIGNED ULONGLONG*)pData;
        pBaseCounter = pCounter+1;
        if ((pBaseCounter->CounterType & PERF_COUNTER_BASE) == PERF_COUNTER_BASE)
        {
            pData = (PVOID)((LPBYTE)pCounterDataBlock + pBaseCounter->CounterOffset);
            pRawData->Time = *(DWORD*)pData;
        }
        else
        {
            fSuccess = FALSE;
        }

        if (pCounter->CounterType == PERF_AVERAGE_TIMER)
        {
            pRawData->Frequency = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->PerfFreq.QuadPart;
        }
        break;

    //These are base counters and are used in calculations for other counters.
    //This case should never be entered.
    case PERF_SAMPLE_BASE:
    case PERF_AVERAGE_BASE:
    case PERF_COUNTER_MULTI_BASE:
    case PERF_RAW_BASE:
    case PERF_LARGE_RAW_BASE:
        pRawData->Data = 0;
        pRawData->Time = 0;
        fSuccess = FALSE;
        break;

    case PERF_ELAPSED_TIME:
        pRawData->Data = *(UNALIGNED ULONGLONG*)pData;
        pRawData->Time = pObject->PerfTime.QuadPart;
        pRawData->Frequency = pObject->PerfFreq.QuadPart;
        break;

    //These counters are currently not supported.
    case PERF_COUNTER_TEXT:
    case PERF_COUNTER_NODATA:
    case PERF_COUNTER_HISTOGRAM_TYPE:
        pRawData->Data = 0;
        pRawData->Time = 0;
        fSuccess = FALSE;
        break;

    //Encountered an unidentified counter.
    default:
        pRawData->Data = 0;
        pRawData->Time = 0;
        fSuccess = FALSE;
        break;
    }

    return fSuccess;
}
```



 

 



