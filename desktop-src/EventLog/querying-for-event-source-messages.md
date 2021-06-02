---
description: Querying for Event Information
ms.assetid: e03d2ab5-50ea-4916-9774-850506714538
title: Querying for Event Information
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Event Information

The following example shows how to open an event log, read events from the log, print information about the events, and then close the event log. This example filters for the events written by the example in [Reporting an Event](reporting-an-event.md).


```C++
#include <windows.h>
#include <stdio.h>
#include <strsafe.h>

#define PROVIDER_NAME           L"MyEventProvider"
#define RESOURCE_DLL            L"<path>\\Provider.dll"
#define MAX_TIMESTAMP_LEN       23 + 1   // mm/dd/yyyy hh:mm:ss.mmm
#define MAX_RECORD_BUFFER_SIZE  0x10000  // 64K

HANDLE GetMessageResources();
DWORD DumpRecordsInBuffer(PBYTE pBuffer, DWORD dwBytesRead);
DWORD GetEventTypeName(DWORD EventType);
LPWSTR GetMessageString(DWORD Id, DWORD argc, LPWSTR args);
void GetTimestamp(const DWORD Time, WCHAR DisplayString[]);
DWORD ApplyParameterStringsToMessage(CONST LPCWSTR pMessage, LPWSTR & pFinalMessage);

CONST LPWSTR pEventTypeNames[] = {L"Error", L"Warning", L"Informational", L"Audit Success", L"Audit Failure"};


HANDLE g_hResources = NULL;


void wmain(void)
{
    HANDLE hEventLog = NULL;
    DWORD status = ERROR_SUCCESS;
    DWORD dwBytesToRead = 0;
    DWORD dwBytesRead = 0;
    DWORD dwMinimumBytesToRead = 0;
    PBYTE pBuffer = NULL;
    PBYTE pTemp = NULL;

    // The source name (provider) must exist as a subkey of Application.
    hEventLog = OpenEventLog(NULL, PROVIDER_NAME);
    if (NULL == hEventLog)
    {
        wprintf(L"OpenEventLog failed with 0x%x.\n", GetLastError());
        goto cleanup;
    }

    // Get the DLL that contains the string resources for the provider.
    g_hResources = GetMessageResources();
    if (NULL == g_hResources)
    {
        wprintf(L"GetMessageResources failed.\n");
        goto cleanup;
    }

    // Allocate an initial block of memory used to read event records. The number 
    // of records read into the buffer will vary depending on the size of each event.
    // The size of each event will vary based on the size of the user-defined
    // data included with each event, the number and length of insertion 
    // strings, and other data appended to the end of the event record.
    dwBytesToRead = MAX_RECORD_BUFFER_SIZE;
    pBuffer = (PBYTE)malloc(dwBytesToRead);
    if (NULL == pBuffer)
    {
        wprintf(L"Failed to allocate the initial memory for the record buffer.\n");
        goto cleanup;
    }

    // Read blocks of records until you reach the end of the log or an 
    // error occurs. The records are read from newest to oldest. If the buffer
    // is not big enough to hold a complete event record, reallocate the buffer.
    while (ERROR_SUCCESS == status)
    {
        if (!ReadEventLog(hEventLog, 
            EVENTLOG_SEQUENTIAL_READ | EVENTLOG_BACKWARDS_READ,
            0, 
            pBuffer,
            dwBytesToRead,
            &dwBytesRead,
            &dwMinimumBytesToRead))
        {
            status = GetLastError();
            if (ERROR_INSUFFICIENT_BUFFER == status)
            {
                status = ERROR_SUCCESS;

                pTemp = (PBYTE)realloc(pBuffer, dwMinimumBytesToRead);
                if (NULL == pTemp)
                {
                    wprintf(L"Failed to reallocate the memory for the record buffer (%d bytes).\n", dwMinimumBytesToRead);
                    goto cleanup;
                }

                pBuffer = pTemp;
                dwBytesToRead = dwMinimumBytesToRead;
            }
            else 
            {
                if (ERROR_HANDLE_EOF != status)
                {
                    wprintf(L"ReadEventLog failed with %lu.\n", status);
                    goto cleanup;
                }
            }
        }
        else
        {
            // Print the contents of each record in the buffer.
            DumpRecordsInBuffer(pBuffer, dwBytesRead);
        }
    }

cleanup:

    if (hEventLog)
        CloseEventLog(hEventLog);

    if (pBuffer)
        free(pBuffer);
}


// Get the provider DLL that contains the string resources for the
// category strings, event message strings, and parameter insert strings.
// For this example, the path to the DLL is hardcoded but typically,
// you would read the CategoryMessageFile, EventMessageFile, and 
// ParameterMessageFile registry values under the source's registry key located 
// under \SYSTEM\CurrentControlSet\Services\Eventlog\Application in
// the HKLM registry hive. In this example, all resources are included in
// the same resource-only DLL.
HANDLE GetMessageResources()
{
    HANDLE hResources = NULL;

    hResources = LoadLibraryEx(RESOURCE_DLL, NULL, LOAD_LIBRARY_AS_IMAGE_RESOURCE | LOAD_LIBRARY_AS_DATAFILE);
    if (NULL == hResources)
    {
        wprintf(L"LoadLibrary failed with %lu.\n", GetLastError());
    }

    return hResources;
}


// Loop through the buffer and print the contents of each record 
// in the buffer.
DWORD DumpRecordsInBuffer(PBYTE pBuffer, DWORD dwBytesRead)
{
    DWORD status = ERROR_SUCCESS;
    PBYTE pRecord = pBuffer;
    PBYTE pEndOfRecords = pBuffer + dwBytesRead;
    LPWSTR pMessage = NULL;
    LPWSTR pFinalMessage = NULL;
    WCHAR TimeStamp[MAX_TIMESTAMP_LEN];

    while (pRecord < pEndOfRecords)
    {
        // If the event was written by our provider, write the contents of the event.
        if (0 == wcscmp(PROVIDER_NAME, (LPWSTR)(pRecord + sizeof(EVENTLOGRECORD))))
        {
            GetTimestamp(((PEVENTLOGRECORD)pRecord)->TimeGenerated, TimeStamp);
            wprintf(L"Time stamp: %s\n", TimeStamp);
            wprintf(L"record number: %lu\n", ((PEVENTLOGRECORD)pRecord)->RecordNumber);
            wprintf(L"status code: %d\n", ((PEVENTLOGRECORD)pRecord)->EventID & 0xFFFF);
            wprintf(L"event type: %s\n", pEventTypeNames[GetEventTypeName(((PEVENTLOGRECORD)pRecord)->EventType)]);

            pMessage = GetMessageString(((PEVENTLOGRECORD)pRecord)->EventCategory, 0, NULL);

            if (pMessage)
            {
                wprintf(L"event category: %s", pMessage);
                LocalFree(pMessage);
                pMessage = NULL;
            }

            pMessage = GetMessageString(((PEVENTLOGRECORD)pRecord)->EventID, 
                ((PEVENTLOGRECORD)pRecord)->NumStrings, (LPWSTR)(pRecord + ((PEVENTLOGRECORD)pRecord)->StringOffset));

            if (pMessage)
            {
                status = ApplyParameterStringsToMessage(pMessage, pFinalMessage);

                wprintf(L"event message: %s", (pFinalMessage) ? pFinalMessage : pMessage);
                LocalFree(pMessage);
                pMessage = NULL;

                if (pFinalMessage)
                {
                    free(pFinalMessage);
                    pFinalMessage = NULL;
                }
            }


            // To write the event data, you need to know the format of the data. In
            // this example, we know that the event data is a null-terminated string.
            if (((PEVENTLOGRECORD)pRecord)->DataLength > 0)
            {
                wprintf(L"event data: %s\n", (LPWSTR)(pRecord + ((PEVENTLOGRECORD)pRecord)->DataOffset));
            }

            wprintf(L"\n");
        }

        pRecord += ((PEVENTLOGRECORD)pRecord)->Length;
    }

    return status;
}


// Get an index value to the pEventTypeNames array based on 
// the event type value.
DWORD GetEventTypeName(DWORD EventType)
{
    DWORD index = 0;

    switch (EventType)
    {
        case EVENTLOG_ERROR_TYPE:
            index = 0;
            break;
        case EVENTLOG_WARNING_TYPE:
            index = 1;
            break;
        case EVENTLOG_INFORMATION_TYPE:
            index = 2;
            break;
        case EVENTLOG_AUDIT_SUCCESS:
            index = 3;
            break;
        case EVENTLOG_AUDIT_FAILURE:
            index = 4;
            break;
    }

    return index;
}


// Formats the specified message. If the message uses inserts, build
// the argument list to pass to FormatMessage.
LPWSTR GetMessageString(DWORD MessageId, DWORD argc, LPWSTR argv)
{
    LPWSTR pMessage = NULL;
    DWORD dwFormatFlags = FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_FROM_HMODULE | FORMAT_MESSAGE_ALLOCATE_BUFFER;
    DWORD_PTR* pArgs = NULL;
    LPWSTR pString = argv;

    // The insertion strings appended to the end of the event record
    // are an array of strings; however, FormatMessage requires
    // an array of addresses. Create an array of DWORD_PTRs based on
    // the count of strings. Assign the address of each string
    // to an element in the array (maintaining the same order).
    if (argc > 0)
    {
        pArgs = (DWORD_PTR*)malloc(sizeof(DWORD_PTR) * argc);
        if (pArgs)
        {
            dwFormatFlags |= FORMAT_MESSAGE_ARGUMENT_ARRAY;

            for (DWORD i = 0; i < argc; i++)
            {
                pArgs[i] = (DWORD_PTR)pString;
                pString += wcslen(pString) + 1;
            }
        }
        else
        {
            dwFormatFlags |= FORMAT_MESSAGE_IGNORE_INSERTS;
            wprintf(L"Failed to allocate memory for the insert string array.\n");
        }
    }

    if (!FormatMessage(dwFormatFlags,
                       g_hResources,
                       MessageId,
                       0,  
                       (LPWSTR)&pMessage, 
                       0, 
                       (va_list*)pArgs))
    {
        wprintf(L"Format message failed with %lu\n", GetLastError());
    }

    if (pArgs)
        free(pArgs);

    return pMessage;
}

// If the message string contains parameter insertion strings (for example, %%4096),
// you must perform the parameter substitution yourself. To get the parameter message 
// string, call FormatMessage with the message identifier found in the parameter insertion 
// string (for example, 4096 is the message identifier if the parameter insertion string
// is %%4096). You then substitute the parameter insertion string in the message 
// string with the actual parameter message string. 
DWORD ApplyParameterStringsToMessage(CONST LPCWSTR pMessage, LPWSTR & pFinalMessage)
{
    DWORD status = ERROR_SUCCESS;
    DWORD dwParameterCount = 0;  // Number of insertion strings found in pMessage
    size_t cbBuffer = 0;         // Size of the buffer in bytes
    size_t cchBuffer = 0;        // Size of the buffer in characters
    size_t cchParameters = 0;    // Number of characters in all the parameter strings
    size_t cch = 0;
    DWORD i = 0;
    LPWSTR* pStartingAddresses = NULL;  // Array of pointers to the beginning of each parameter string in pMessage
    LPWSTR* pEndingAddresses = NULL;    // Array of pointers to the end of each parameter string in pMessage
    DWORD* pParameterIDs = NULL;        // Array of parameter identifiers found in pMessage
    LPWSTR* pParameters = NULL;         // Array of the actual parameter strings
    LPWSTR pTempMessage = (LPWSTR)pMessage;
    LPWSTR pTempFinalMessage = NULL;

    // Determine the number of parameter insertion strings in pMessage.
    while (pTempMessage = wcschr(pTempMessage, L'%'))
    {
        dwParameterCount++;
        pTempMessage++;
    }

    // If there are no parameter insertion strings in pMessage, return.
    if (0 == dwParameterCount)
    {
        pFinalMessage = NULL;
        goto cleanup;
    }

    // Allocate an array of pointers that will contain the beginning address 
    // of each parameter insertion string.
    cbBuffer = sizeof(LPWSTR) * dwParameterCount;
    pStartingAddresses = (LPWSTR*)malloc(cbBuffer);
    if (NULL == pStartingAddresses)
    {
        wprintf(L"Failed to allocate memory for pStartingAddresses.\n");
        status = ERROR_OUTOFMEMORY;
        goto cleanup;
    }

    RtlZeroMemory(pStartingAddresses, cbBuffer);

    // Allocate an array of pointers that will contain the ending address (one
    // character past the of the identifier) of the each parameter insertion string.
    pEndingAddresses = (LPWSTR*)malloc(cbBuffer);
    if (NULL == pEndingAddresses)
    {
        wprintf(L"Failed to allocate memory for pEndingAddresses.\n");
        status = ERROR_OUTOFMEMORY;
        goto cleanup;
    }

    RtlZeroMemory(pEndingAddresses, cbBuffer);

    // Allocate an array of pointers that will contain pointers to the actual
    // parameter strings.
    pParameters = (LPWSTR*)malloc(cbBuffer);
    if (NULL == pParameters)
    {
        wprintf(L"Failed to allocate memory for pEndingAddresses.\n");
        status = ERROR_OUTOFMEMORY;
        goto cleanup;
    }

    RtlZeroMemory(pParameters, cbBuffer);

    // Allocate an array of DWORDs that will contain the message identifier
    // for each parameter.
    pParameterIDs = (DWORD*)malloc(cbBuffer);
    if (NULL == pParameterIDs)
    {
        wprintf(L"Failed to allocate memory for pParameterIDs.\n");
        status = ERROR_OUTOFMEMORY;
        goto cleanup;
    }

    RtlZeroMemory(pParameterIDs, cbBuffer);

    // Find each parameter in pMessage and get the pointer to the
    // beginning of the insertion string, the end of the insertion string,
    // and the message identifier of the parameter.
    pTempMessage = (LPWSTR)pMessage;
    while (pTempMessage = wcschr(pTempMessage, L'%'))
    {
        if (isdigit(*(pTempMessage+1)))
        {
            pStartingAddresses[i] = pTempMessage;

            pTempMessage++;
            pParameterIDs[i] = (DWORD)_wtoi(pTempMessage);

            while (isdigit(*++pTempMessage))
                ;

            pEndingAddresses[i] = pTempMessage;

            i++;
        }
    }

    // For each parameter, use the message identifier to get the
    // actual parameter string.
    for (DWORD i = 0; i < dwParameterCount; i++)
    {
        pParameters[i] = GetMessageString(pParameterIDs[i], 0, NULL);
        if (NULL == pParameters[i])
        {
            wprintf(L"GetMessageString could not find parameter string for insert %lu.\n", i);
            status = ERROR_INVALID_PARAMETER;
            goto cleanup;
        }

        cchParameters += wcslen(pParameters[i]);
    }

    // Allocate enough memory for pFinalMessage based on the length of pMessage
    // and the length of each parameter string. The pFinalMessage buffer will contain 
    // the completed parameter substitution.
    pTempMessage = (LPWSTR)pMessage;
    cbBuffer = (wcslen(pMessage) + cchParameters + 1) * sizeof(WCHAR);
    pFinalMessage = (LPWSTR)malloc(cbBuffer);
    if (NULL == pFinalMessage)
    {
        wprintf(L"Failed to allocate memory for pFinalMessage.\n");
        status = ERROR_OUTOFMEMORY;
        goto cleanup;
    }

    RtlZeroMemory(pFinalMessage, cbBuffer);
    cchBuffer = cbBuffer / sizeof(WCHAR);
    pTempFinalMessage = pFinalMessage;

    // Build the final message string.
    for (DWORD i = 0; i < dwParameterCount; i++)
    {
        // Append the segment from pMessage. In the first iteration, this is "8 " and in the
        // second iteration, this is " = 2 ".
        wcsncpy_s(pTempFinalMessage, cchBuffer, pTempMessage, cch = (pStartingAddresses[i] - pTempMessage));
        pTempMessage = pEndingAddresses[i];
        cchBuffer -= cch;

        // Append the parameter string. In the first iteration, this is "quarts" and in the
        // second iteration, this is "gallons"
        pTempFinalMessage += cch;
        wcscpy_s(pTempFinalMessage, cchBuffer, pParameters[i]);
        cchBuffer -= cch = wcslen(pParameters[i]);

        pTempFinalMessage += cch;
    }

    // Append the last segment from pMessage, which is ".".
    wcscpy_s(pTempFinalMessage, cchBuffer, pTempMessage);

cleanup:

    if (ERROR_SUCCESS != status)
        pFinalMessage = (LPWSTR)pMessage;

    if (pStartingAddresses)
        free(pStartingAddresses);

    if (pEndingAddresses)
        free(pEndingAddresses);

    if (pParameterIDs)
        free(pParameterIDs);

    for (DWORD i = 0; i < dwParameterCount; i++)
    {
        if (pParameters[i])
            LocalFree(pParameters[i]);
    }

    return status;
}


// Get a string that contains the time stamp of when the event 
// was generated.
void GetTimestamp(const DWORD Time, WCHAR DisplayString[])
{
    ULONGLONG ullTimeStamp = 0;
    ULONGLONG SecsTo1970 = 116444736000000000;
    SYSTEMTIME st;
    FILETIME ft, ftLocal;

    ullTimeStamp = Int32x32To64(Time, 10000000) + SecsTo1970;
    ft.dwHighDateTime = (DWORD)((ullTimeStamp >> 32) & 0xFFFFFFFF);
    ft.dwLowDateTime = (DWORD)(ullTimeStamp & 0xFFFFFFFF);
    
    FileTimeToLocalFileTime(&ft, &ftLocal);
    FileTimeToSystemTime(&ftLocal, &st);
    StringCchPrintf(DisplayString, MAX_TIMESTAMP_LEN, L"%d/%d/%d %.2d:%.2d:%.2d", 
        st.wMonth, st.wDay, st.wYear, st.wHour, st.wMinute, st.wSecond);
}
```



 

 



