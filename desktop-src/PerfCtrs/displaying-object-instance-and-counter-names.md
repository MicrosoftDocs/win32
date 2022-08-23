---
description: If you want to display a list of objects and their counters in a user interface, you must retrieve the performance data.
ms.assetid: 0d122fa8-2ed8-4bd8-a52e-6cb20fe81741
title: Displaying Object, Instance, and Counter Names
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Object, Instance, and Counter Names

If you want to display a list of objects and their counters in a user interface, you must retrieve the performance data. The performance data contains a variable number of performance objects and their instances and counters. For information on the format of the performance data, see [Performance Data Format](performance-data-format.md).

The performance data does not contain the object and counter names. Instead, the data contains index values that you use to retrieve the names of the objects and counters, which are stored in resources known to the performance counters infrastructure. However, the instance names are stored in performance data. For an example that reads the object and counter names from the registry and creates an index table for accessing the names later, see [Retrieving Counter Names and Help Text](retrieving-counter-names-and-help-text.md).

The following example shows how to retrieve the object, instance, and counter blocks from the performance data. After retrieving the object names, instance names, and counter names, the example sorts the objects by name and for each object, sorts its instances and counters by name. The example then prints the sorted lists.


```C++
#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>
#include <strsafe.h>

#pragma comment(lib, "advapi32.lib")

#define INIT_OBJECT_BUFFER_SIZE 48928   // Initial buffer size to use when querying specific objects.
#define INIT_GLOBAL_BUFFER_SIZE 122880  // Initial buffer size to use when using "Global" to query all objects.
#define BUFFER_INCREMENT 16384          // Increment buffer size in 16K chunks.
#define MAX_INSTANCE_NAME_LEN      255  // Max length of an instance name.
#define MAX_FULL_INSTANCE_NAME_LEN 511  // Form is parentinstancename/instancename#nnn.

//Identifies a performance object and its counters and instances. 
typedef struct _perf_object
{
  DWORD dwObjectIndex;          // Index to the name of the object.
  LPDWORD pdwCounterIndexes;    // Array of counter index values.
  DWORD dwNumberOfCounters;
  LPWSTR pInstanceNames;        // Array of instance name strings.
  DWORD dwNumberofInstances;
} PERF_OBJECT, *PPERF_OBJECT;

LPBYTE GetPerformanceData(LPWSTR pwszSource, DWORD dwInitialBufferSize);
BOOL GetCounterTextStrings(LPWSTR & pCounterTextHead, LPWSTR & pHelpTextHead, LPDWORD & pTextOffsets, DWORD* pdwNumberOfOffsets);
LPWSTR GetText(LPWSTR pwszSource);
BOOL BuildTextTable(LPWSTR pCounterHead, LPWSTR pHelpHead, LPDWORD* pOffsetsHead, LPDWORD pNumberOfOffsets);
DWORD GetNumberOfTextEntries(LPWSTR pwszSource);
PPERF_OBJECT LoadObjects(LPBYTE pObject, DWORD* dwNumberOfObjects, LPBYTE pEndObject);
BOOL LoadCounters(LPDWORD* ppdwCounterIndexes, LPBYTE pCounter, DWORD* pdwNumberOfCounters);
BOOL LoadInstances(LPWSTR* pInstanceNames, LPBYTE pInstance, DWORD dwNumberofInstances, DWORD CodePage);
BOOL GetFullInstanceName(PERF_INSTANCE_DEFINITION* pInstance, DWORD CodePage, WCHAR* pName);
BOOL ConvertNameToUnicode(UINT CodePage, LPCSTR pNameToConvert, DWORD dwNameToConvertLen, LPWSTR pConvertedName);
PERF_INSTANCE_DEFINITION* GetParentInstance(PERF_OBJECT_TYPE* pObject, DWORD dwInstancePosition);
PERF_OBJECT_TYPE* GetObject(DWORD dwObjectToFind);
int CompareObjects(const void *pObject1, const void *pObject2);
int CompareCounters(const void *pCounter1, const void *pCounter2);
int CompareInstances(const void *pInstance1, const void *pInstance2);
void PrintObjectNames(DWORD dwNumberOfObjects, BOOL fIncludeCounters, BOOL fIncludeInstances);
void FreePerfObjects(PPERF_OBJECT pObjects, DWORD dwNumberOfObjects);

// Globals
LPBYTE g_pPerfDataHead = NULL;    // Head of the performance data.
LPWSTR g_pCounterTextHead = NULL; // Head of the MULTI_SZ buffer that contains the Counter text.
LPWSTR g_pHelpTextHead = NULL;    // Head of the MULTI_SZ buffer that contains the Help text.
LPDWORD g_pTextOffsets = NULL;    // Array of DWORDS that contain the offsets to the text in
                                  // pCounterTextHead and pHelpTextHead. The text index 
                                  // values mirror the array index.
PPERF_OBJECT g_pObjects = NULL;   // Array of PERF_OBJECTs.



void wmain(void)
{
    DWORD dwNumberOfOffsets = 0;    // Number of elements in the pTextOffsets array.
    DWORD dwNumberOfObjects = 0;    // Number of elements in the pObjects array.

    g_pPerfDataHead = (LPBYTE)GetPerformanceData(L"Global", INIT_GLOBAL_BUFFER_SIZE);
    if (NULL == g_pPerfDataHead)
    {
        wprintf(L"GetPerformanceData failed.\n");
        goto cleanup;
    }

    if (!GetCounterTextStrings(g_pCounterTextHead, g_pHelpTextHead, g_pTextOffsets, &dwNumberOfOffsets))
    {
        wprintf(L"GetCounterTextStrings failed.\n");
        goto cleanup;
    }

    dwNumberOfObjects = ((PERF_DATA_BLOCK*)g_pPerfDataHead)->NumObjectTypes;

    g_pObjects = LoadObjects(g_pPerfDataHead + ((PERF_DATA_BLOCK*)g_pPerfDataHead)->HeaderLength,
                             &dwNumberOfObjects,
                             g_pPerfDataHead + ((PERF_DATA_BLOCK*)g_pPerfDataHead)->TotalByteLength);
    
    if (NULL == g_pObjects)
    {
        wprintf(L"LoadObjects failed.\n");
        goto cleanup;
    }

    PrintObjectNames(dwNumberOfObjects, TRUE, TRUE);

cleanup:

    if (g_pPerfDataHead)
        free(g_pPerfDataHead);

    if (g_pCounterTextHead)
        free(g_pCounterTextHead);

    if (g_pHelpTextHead)
        free(g_pHelpTextHead);

    if (g_pTextOffsets)
        free(g_pTextOffsets);

    if (g_pObjects)
        FreePerfObjects(g_pObjects, dwNumberOfObjects);
}

//Retrieve a buffer that contains the specified performance data.
//The pwszSource parameter determines the data that GetRegistryBuffer returns.
//
//Typically, when calling RegQueryValueEx, you can specify zero for the size of the buffer
//and the RegQueryValueEx will set your size variable to the required buffer size. However, 
//if the source is "Global" or one or more object index values, you will need to increment
//the buffer size in a loop until RegQueryValueEx does not return ERROR_MORE_DATA. 
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


BOOL GetCounterTextStrings(LPWSTR & pCounterTextHead, LPWSTR & pHelpTextHead, LPDWORD & pTextOffsets, DWORD* pdwNumberOfOffsets)
{
    BOOL status = TRUE;

    pCounterTextHead = GetText(L"Counter");
    if (NULL == pCounterTextHead)
    {
        wprintf(L"GetText(L\"Counter\") failed.\n");
        status = FALSE;
        goto cleanup;
    }

    pHelpTextHead = GetText(L"Help");
    if (NULL == pHelpTextHead)
    {
        wprintf(L"GetText(L\"Help\") failed.\n");
        status = FALSE;
        goto cleanup;
    }

    if (!BuildTextTable(pCounterTextHead, pHelpTextHead, &pTextOffsets, pdwNumberOfOffsets))
    {
        wprintf(L"BuildTextTable failed.\n");
        status = FALSE;
    }

cleanup:

    return status;
}


// Get the text based on the source value. This function uses the
// HKEY_PERFORMANCE_NLSTEXT key to get the strings.
LPWSTR GetText(LPWSTR pwszSource)
{
    LPWSTR pBuffer = NULL;
    DWORD dwBufferSize = 0;
    LONG status = ERROR_SUCCESS;

    // Query the size of the text data so you can allocate the buffer.
    status = RegQueryValueEx(HKEY_PERFORMANCE_NLSTEXT, pwszSource, NULL, NULL, NULL, &dwBufferSize);
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegQueryValueEx failed getting required buffer size. Error is 0x%x.\n", status);
        goto cleanup;
    }

    // Allocate the text buffer and query the text.
    pBuffer = (LPWSTR)malloc(dwBufferSize);
    if (pBuffer)
    {
        status = RegQueryValueEx(HKEY_PERFORMANCE_NLSTEXT, pwszSource, NULL, NULL, (LPBYTE)pBuffer, &dwBufferSize);
        if (ERROR_SUCCESS != status)
        {
            wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
            free(pBuffer);
            pBuffer = NULL;
            goto cleanup;
        }
    }
    else
    {
        wprintf(L"malloc failed to allocate memory.\n");
    }

cleanup:

    return pBuffer;
}


// Build a table of offsets into the counter and help text buffers. Use the index
// values from the performance data queries to access the offsets.
BOOL BuildTextTable(LPWSTR pCounterHead, LPWSTR pHelpHead, LPDWORD* pOffsetsHead, LPDWORD pNumberOfOffsets)
{
    BOOL fSuccess = FALSE;
    LPWSTR pwszCounterText = NULL;  // Used to cycle through the Counter text
    LPWSTR pwszHelpText = NULL;     // Used to cycle through the Help text
    LPDWORD pOffsets = NULL;
    DWORD dwCounterIndex = 0;       // Index value of the Counter text
    DWORD dwHelpIndex = 0;          // Index value of the Help text
    DWORD dwSize = 0;               // Size of the block of memory that holds the offset array

    pwszCounterText = pCounterHead;
    pwszHelpText = pHelpHead;

    *pNumberOfOffsets = GetNumberOfTextEntries(L"Last Help");
    if (0 == *pNumberOfOffsets)
    {
        wprintf(L"GetNumberOfTextEntries failed; returned 0 for number of entries.\n");
        goto cleanup;
    }

    dwSize = sizeof(DWORD) * (*pNumberOfOffsets + 1);  // Add one to make the array one-based

    pOffsets = (LPDWORD)malloc(dwSize);
    if (pOffsets)
    {
        ZeroMemory(pOffsets, dwSize);
        *pOffsetsHead = pOffsets;

        // Bypass first record (pair) of the counter data - contains upper bounds of system counter index.
        pwszCounterText += (wcslen(pwszCounterText)+1);
        pwszCounterText += (wcslen(pwszCounterText)+1);

        for (; *pwszCounterText; pwszCounterText += (wcslen(pwszCounterText)+1))
        {
            dwCounterIndex = _wtoi(pwszCounterText);
            dwHelpIndex = _wtoi(pwszHelpText);

            // Use the counter's index value as an indexer into the pOffsets array.
            // Store the offset to the counter text in the array element.
            pwszCounterText += (wcslen(pwszCounterText)+1);  //Skip past index value
            pOffsets[dwCounterIndex] = (DWORD)(pwszCounterText - pCounterHead);

            // Some help indexes for system counters do not have a matching counter, so loop
            // until you find the matching help index or the index is greater than the corresponding
            // counter index. For example, if the indexes were as follows, you would loop
            // until the help index was 11.
            //
            // Counter index       Help Index
            //   2                    3
            //   4                    5
            //   6                    7
            //                        9   (skip because there is no matching Counter index)
            //   10                   11
            while (*pwszHelpText && dwHelpIndex < dwCounterIndex)
            {
                pwszHelpText += (wcslen(pwszHelpText)+1);  // Skip past index value
                pwszHelpText += (wcslen(pwszHelpText)+1);  // Skip past help text to the next index value
                dwHelpIndex = _wtoi(pwszHelpText);
            }

            // Use the Help index value as an indexer into the pOffsets array.
            // Store the offset to the help text in the array element.
            if (dwHelpIndex == (dwCounterIndex + 1))
            {
                pwszHelpText += (wcslen(pwszHelpText)+1);  //Skip past index value
                pOffsets[dwHelpIndex] = (DWORD)(pwszHelpText - pHelpHead);
                pwszHelpText += (wcslen(pwszHelpText)+1);  //Skip past help text to next index value
            }
        }

        fSuccess = TRUE;
    }

cleanup:

    return fSuccess;
}


// Retrieve the last help index used from the registry. Use this number
// to allocate an array of DWORDs. Note that index values are not contiguous.
DWORD GetNumberOfTextEntries(LPWSTR pwszSource)
{
    DWORD dwEntries = 0;
    LONG status = ERROR_SUCCESS;
    HKEY hkey = NULL;
    DWORD dwSize = sizeof(DWORD);
    LPWSTR pwszMessage = NULL;

    status = RegOpenKeyEx(HKEY_LOCAL_MACHINE,
        L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Perflib",
        0,
        KEY_READ,
        &hkey);
    
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegOpenKeyEx failed with 0x%x.\n", status);
        goto cleanup;
    }

    status = RegQueryValueEx(hkey, pwszSource, NULL, 0, (LPBYTE)&dwEntries, &dwSize);

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
    }

cleanup:

    if (hkey)
        RegCloseKey(hkey);

    return dwEntries;
}


// Allocate a block of memory that will contain one or more PERF_OBJECT structures.
// For each object, also load its counters and instances.

PPERF_OBJECT LoadObjects(LPBYTE pPerfDataObject, DWORD* pdwNumberOfObjects, LPBYTE pEndObject)
{
    BOOL fSuccess = FALSE;
    DWORD dwSize = sizeof(PERF_OBJECT) * *pdwNumberOfObjects;
    PPERF_OBJECT pObjects = NULL;
    DWORD i = 0;

    pObjects = (PERF_OBJECT*)malloc(dwSize);
    if (NULL == pObjects)
    {
        wprintf(L"malloc failed to allocate memory for pObjects.\n");
        goto cleanup;
    }

    ZeroMemory(pObjects, dwSize);
    for (; i < *pdwNumberOfObjects; i++)
    {
        pObjects[i].dwObjectIndex = ((PERF_OBJECT_TYPE*)pPerfDataObject)->ObjectNameTitleIndex;
        // Load Counter indexes.

        pObjects[i].dwNumberOfCounters = ((PERF_OBJECT_TYPE*)pPerfDataObject)->NumCounters;

        fSuccess = LoadCounters(&(pObjects[i].pdwCounterIndexes),
            pPerfDataObject + ((PERF_OBJECT_TYPE*)pPerfDataObject)->HeaderLength,  // Points to the first counter
            &(pObjects[i].dwNumberOfCounters));

        if (FALSE == fSuccess)
        {
            wprintf(L"LoadCounters failed.\n");
            goto cleanup;
        }

        if ( ((PERF_OBJECT_TYPE*)pPerfDataObject)->NumInstances != 0 && 
             ((PERF_OBJECT_TYPE*)pPerfDataObject)->NumInstances != PERF_NO_INSTANCES )
        {

            // Load instance indexes.

            pObjects[i].dwNumberofInstances = ((PERF_OBJECT_TYPE*)pPerfDataObject)->NumInstances;

            fSuccess = LoadInstances(&(pObjects[i].pInstanceNames),
                pPerfDataObject + ((PERF_OBJECT_TYPE*)pPerfDataObject)->DefinitionLength, // Points to the first instance
                ((PERF_OBJECT_TYPE*)pPerfDataObject)->NumInstances,
                ((PERF_OBJECT_TYPE*)pPerfDataObject)->CodePage);

            if (FALSE == fSuccess)
            {
                wprintf(L"LoadInstances failed.\n");
                goto cleanup;
            }
        }

        pPerfDataObject += ((PERF_OBJECT_TYPE*)pPerfDataObject)->TotalByteLength;
        if (pPerfDataObject >= pEndObject)
        {
            // The end of the counter objects array was reached.
            break;
        }
    }

    *pdwNumberOfObjects = i;

    //After all the data is loaded, sort the list of objects, so you can print
    //them in alphabetical order.

    qsort(pObjects, *pdwNumberOfObjects, sizeof(PERF_OBJECT), CompareObjects);

cleanup:

    if (FALSE == fSuccess)
    {
        FreePerfObjects(pObjects, i);
        pObjects = NULL;
    }

    return pObjects;
}


// Allocate of block of memory and load the index values for the counters that
// the object defines.
BOOL LoadCounters(LPDWORD* ppdwIndexes, LPBYTE pCounter, DWORD* pdwNumberOfCounters)
{
    BOOL fSuccess = FALSE;
    DWORD dwSize = sizeof(DWORD) * *pdwNumberOfCounters;
    LPDWORD pIndexes = NULL;
    DWORD dwSkippedBaseRecords = 0;

    pIndexes = (LPDWORD)malloc(dwSize);
    if (NULL == pIndexes)
    {
        wprintf(L"malloc failed to allocate memory for pIndexes.\n");
        goto cleanup;
    }

    ZeroMemory(pIndexes, dwSize);

    for (DWORD i = 0, j = 0; i < *pdwNumberOfCounters; i++)
    {
        // Ignore base counters.
        if ((((PERF_COUNTER_DEFINITION*)pCounter)->CounterType & PERF_COUNTER_BASE) == PERF_COUNTER_BASE)
        {
            dwSkippedBaseRecords++;
        }
        else
        {
            pIndexes[j]  = ((PERF_COUNTER_DEFINITION*)pCounter)->CounterNameTitleIndex;
            j++;  
        }

        pCounter += ((PERF_COUNTER_DEFINITION*)pCounter)->ByteLength;
    }

    // Decrement so the sort works.
    *pdwNumberOfCounters -= dwSkippedBaseRecords;

    // Sort the index values of the object's counters.
    qsort(pIndexes, *pdwNumberOfCounters, sizeof(DWORD), CompareCounters);
    *ppdwIndexes = pIndexes;
    fSuccess = TRUE;

cleanup:

    return fSuccess;
}

// Allocate a block of memory and load the full instance name for each instance
// of the object.
BOOL LoadInstances(LPWSTR* ppNames, LPBYTE pInstance, DWORD dwNumberofInstances, DWORD CodePage)
{
    BOOL fSuccess = FALSE;
    DWORD dwSize = (sizeof(WCHAR) * (MAX_FULL_INSTANCE_NAME_LEN+1)) * dwNumberofInstances;
    PERF_COUNTER_BLOCK* pCounter = NULL;
    LPWSTR pName = NULL;

    *ppNames = (LPWSTR)malloc(dwSize);
    if (NULL == *ppNames)
    {
        wprintf(L"malloc failed to allocate memory for *ppNames.\n");
        goto cleanup;
    }

    ZeroMemory(*ppNames, dwSize);
    pName = *ppNames;

    for (DWORD i = 0; i < dwNumberofInstances; i++)
    {
        fSuccess = GetFullInstanceName((PERF_INSTANCE_DEFINITION*)pInstance, CodePage, pName);
        if (FALSE == fSuccess)
        {
            wprintf(L"GetFullInstanceName failed.\n");
            goto cleanup;
        }

        pName = pName + (MAX_FULL_INSTANCE_NAME_LEN+1);

        pCounter = (PERF_COUNTER_BLOCK*)(pInstance + ((PERF_INSTANCE_DEFINITION*)pInstance)->ByteLength);
        pInstance += ((PERF_INSTANCE_DEFINITION*)pInstance)->ByteLength + pCounter->ByteLength;
    }

    // Sort the instance names of the object's instances.
    qsort(*ppNames, dwNumberofInstances, sizeof(WCHAR) * (MAX_FULL_INSTANCE_NAME_LEN+1), CompareInstances);

cleanup:

    return fSuccess;
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
    } else 
    {
        // If the specified code page didn't work, try one more time, assuming that the input string is Unicode.
        dwLength = (MAX_INSTANCE_NAME_LEN < (dwNameToConvertLen/2)) ? MAX_INSTANCE_NAME_LEN : dwNameToConvertLen/2;
        if (SUCCEEDED(StringCchCopyN(pConvertedName, MAX_INSTANCE_NAME_LEN+1, (LPWSTR)pNameToConvert, dwLength))) 
        {
            pConvertedName[dwLength] = '\0';
            fSuccess = TRUE;
        }
    }

    return fSuccess;
}


// Find the object using the specified index value.
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


// Used by qsort to put the object names in alphabetical order.
int CompareObjects(const void *pObject1, const void *pObject2)
{
    DWORD index1 = ((PPERF_OBJECT)pObject1)->dwObjectIndex;
    DWORD index2 = ((PPERF_OBJECT)pObject2)->dwObjectIndex;
    LPWSTR pName1 = g_pCounterTextHead+g_pTextOffsets[index1];
    LPWSTR pName2 = g_pCounterTextHead+g_pTextOffsets[index2];
    DWORD dwName1Len = (DWORD)wcslen(pName1);
    DWORD dwName2Len = (DWORD)wcslen(pName2);

  return _wcsnicmp(pName1, pName2, (dwName1Len < dwName2Len) ? dwName1Len : dwName2Len);
}


// Used by qsort to put the counter names in alphabetical order.
int CompareCounters(const void *pCounter1, const void *pCounter2)
{
    DWORD index1 = *(DWORD*)pCounter1;
    DWORD index2 = *(DWORD*)pCounter2;
    LPWSTR pName1 = g_pCounterTextHead+g_pTextOffsets[index1];
    LPWSTR pName2 = g_pCounterTextHead+g_pTextOffsets[index2];
    DWORD dwName1Len = (DWORD)wcslen(pName1);
    DWORD dwName2Len = (DWORD)wcslen(pName2);

    return _wcsnicmp(pName1, pName2, (dwName1Len < dwName2Len) ? dwName1Len : dwName2Len);
}


// Used by qsort to put the instance names in alphabetical order.
int CompareInstances(const void *pName1, const void *pName2)
{
    return _wcsicmp((LPWSTR)pName1, (LPWSTR)pName2);
}


// Print the object names and optionally print their counter and instance names.
void PrintObjectNames(DWORD dwNumberOfObjects, BOOL fIncludeCounters, BOOL fIncludeInstances)
{
    PERF_INSTANCE_DEFINITION* pInstance = NULL;
    DWORD dwIncrementSize = sizeof(WCHAR) * (MAX_FULL_INSTANCE_NAME_LEN+1);
    DWORD index = 0;
    DWORD dwSerialNo = 0;

    for (DWORD i = 0; i < dwNumberOfObjects; i++)
    {
        index = g_pObjects[i].dwObjectIndex;
        wprintf(L"%d %s\n", index, g_pCounterTextHead+g_pTextOffsets[index]);

        // There can be multiple instances with duplicate names. For example, the
        // Process object can have multiple instance of svchost. To differentiate
        // the instances, append a serial number to the name of duplicate instances
        // If the object contained three svchost names, the function prints them
        // as svchost, svchost#1, and svchost#2.
        // If running on Windows 10 20H2 or later, you can avoid this issue by
        // using the "Process V2" counterset.
        if (fIncludeInstances && g_pObjects[i].dwNumberofInstances > 0)
        {
            dwSerialNo = 0;

            for (DWORD j = 0; j < g_pObjects[i].dwNumberofInstances; j++)
            {
                if (j > 0)
                {
                    if ( !CompareInstances( (void*)(g_pObjects[i].pInstanceNames + ((j-1) * (MAX_FULL_INSTANCE_NAME_LEN+1))), 
                        (void*)(g_pObjects[i].pInstanceNames + (j * (MAX_FULL_INSTANCE_NAME_LEN+1))) ) )
                    {
                        dwSerialNo++;
                    }
                    else
                    {
                        dwSerialNo = 0;
                    }
                }

                if (dwSerialNo)
                    wprintf(L"\t%s#%d\n", g_pObjects[i].pInstanceNames + (j * (MAX_FULL_INSTANCE_NAME_LEN+1)), dwSerialNo);
                else
                    wprintf(L"\t%s\n", g_pObjects[i].pInstanceNames + (j * (MAX_FULL_INSTANCE_NAME_LEN+1)));
            }

            wprintf(L"\n");
        }

        if (fIncludeCounters)
        {
            for (DWORD j = 0; j < g_pObjects[i].dwNumberOfCounters; j++)
            {
                index = g_pObjects[i].pdwCounterIndexes[j];
                wprintf(L"\t%d %s\n", index, g_pCounterTextHead+g_pTextOffsets[index]);
            }

            wprintf(L"\n\n");
        }
    }

    wprintf(L"\n\n");
}


void FreePerfObjects(PPERF_OBJECT pObjects, DWORD dwNumberOfObjects)
{
    if (pObjects)
    {
        for (DWORD i=0; i < dwNumberOfObjects; i++)
        {
            if (pObjects[i].pInstanceNames)
            {
                free(pObjects[i].pInstanceNames);
            }

            if (pObjects[i].pdwCounterIndexes)
            {
                free(pObjects[i].pdwCounterIndexes);
            }
        }

        free(pObjects);
        pObjects = NULL;
    }
}
```



 

 



