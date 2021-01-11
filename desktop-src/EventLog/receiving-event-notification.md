---
description: Receiving Event Notification
ms.assetid: 3200d666-d927-4198-b1f6-1636971f5f07
title: Receiving Event Notification
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Event Notification

The following example shows how to use the [**NotifyChangeEventLog**](/windows/desktop/api/Winbase/nf-winbase-notifychangeeventlog) function to receive notification when an event is logged. This example filters for the events written by the example in [Reporting an Event](reporting-an-event.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>

#pragma comment(lib, "advapi32.lib")

#define PROVIDER_NAME L"MyEventProvider"
#define RESOURCE_DLL  L"<path>\\Provider.dll"
#define KEYBOARD_EVENT     0
#define NOTIFICATION_EVENT 1

HANDLE GetMessageResources();
DWORD SeekToLastRecord(HANDLE hEventLog);
DWORD GetLastRecordNumber(HANDLE hEventLog, DWORD* pdwMarker);
DWORD ReadRecord(HANDLE hEventLog, PBYTE & pBuffer, DWORD dwRecordNumber, DWORD dwFlags);
DWORD DumpNewRecords(HANDLE hEventLog);
DWORD GetEventTypeName(DWORD EventType);
LPWSTR GetMessageString(DWORD Id, DWORD argc, LPWSTR args);
DWORD ApplyParameterStringsToMessage(CONST LPCWSTR pMessage, LPWSTR & pFinalMessage);
BOOL IsKeyEvent(HANDLE hStdIn);


CONST LPWSTR pEventTypeNames[] = {L"Error", L"Warning", L"Informational", L"Audit Success", L"Audit Failure"};
HANDLE g_hResources = NULL;


void wmain(void)
{
    HANDLE hEventLog = NULL;
    HANDLE aWaitHandles[2];
    DWORD status = ERROR_SUCCESS;
    DWORD dwWaitReason = 0;
    DWORD dwLastRecordNumber = 0;

    // Get the DLL that contains the message table string resources for the provider.
    g_hResources = GetMessageResources();
    if (NULL == g_hResources)
    {
        wprintf(L"GetMessageResources failed.\n");
        goto cleanup;
    }

    // Get a handle for console input, so you can break out of the loop.
    aWaitHandles[KEYBOARD_EVENT] = GetStdHandle(STD_INPUT_HANDLE);
    if (INVALID_HANDLE_VALUE == aWaitHandles[0])
    {
        wprintf(L"GetStdHandle failed with %lu.\n", GetLastError());
        goto cleanup;
    }

    // Get a handle to a manual reset event object that will be signal
    // when events are written to the log.
    aWaitHandles[NOTIFICATION_EVENT] = CreateEvent(NULL, TRUE, FALSE, NULL);
    if (NULL == aWaitHandles[1])
    {
        wprintf(L"CreateEvent failed with %lu.\n", GetLastError());
        goto cleanup;
    }

    // Open the log file. The source name (provider) must exist as 
    // a subkey of Application.
    hEventLog = OpenEventLog(NULL, PROVIDER_NAME);
    if (NULL == hEventLog)
    {
        wprintf(L"OpenEventLog failed with 0x%x.\n", GetLastError());
        goto cleanup;
    }

    // Seek to the last record in the event log and read it in order
    // to position the cursor for reading any new records when the
    // service notifies you that new records have been written to the 
    // log file.
    status = SeekToLastRecord(hEventLog);
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"SeekToLastRecord failed with %lu.\n", status);
        goto cleanup;
    }

    // Request notification when events are written to the log.
    if (!NotifyChangeEventLog(hEventLog, aWaitHandles[1]))
    {
        wprintf(L"NotifyChangeEventLog failed with %lu.\n", GetLastError());
        goto cleanup;
    }

    wprintf(L"Waiting for notification of new events (press any key to quit)...\n\n");

    // Loop until the user presses a key or there is an error.
    while (true)
    {
        dwWaitReason = WaitForMultipleObjects(sizeof(aWaitHandles)/sizeof(HANDLE), aWaitHandles, FALSE, INFINITE);

        if (KEYBOARD_EVENT == dwWaitReason - WAIT_OBJECT_0)  // Console input
        {
            if (IsKeyEvent(aWaitHandles[0]))
                break;
        }
        else if (NOTIFICATION_EVENT == dwWaitReason - WAIT_OBJECT_0) // Notification results
        {
            if (ERROR_SUCCESS != (status = DumpNewRecords(hEventLog)))
            {
                wprintf(L"DumpNewRecords failed.\n");
                break;
            }

            wprintf(L"\nWaiting for notification of new events (press any key to quit)...\n");
            ResetEvent(aWaitHandles[NOTIFICATION_EVENT]);
        }
        else
        {
            if (WAIT_FAILED == dwWaitReason)
            {
                wprintf(L"WaitForSingleObject failed with %lu\n", GetLastError());
            }
            break;
        }
    }

cleanup:

    if (hEventLog)
        CloseEventLog(hEventLog);

    if (aWaitHandles[0])
        CloseHandle(aWaitHandles[0]);

    if (aWaitHandles[1])
        CloseHandle(aWaitHandles[1]);
}


// Get the last record number in the log file and read it.
// This positions the cursor, so that we can begin reading 
// new records when the service notifies us that new records were 
// written to the log file.
DWORD SeekToLastRecord(HANDLE hEventLog)
{
    DWORD status = ERROR_SUCCESS;
    DWORD dwLastRecordNumber = 0;
    PBYTE pRecord = NULL;  

    status = GetLastRecordNumber(hEventLog, &dwLastRecordNumber);
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"GetLastRecordNumber failed.\n");
        goto cleanup;
    }

    status = ReadRecord(hEventLog, pRecord, dwLastRecordNumber, EVENTLOG_SEEK_READ | EVENTLOG_FORWARDS_READ);
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"ReadRecord failed seeking to record %lu.\n", dwLastRecordNumber);
        goto cleanup;
    }

cleanup:

    if (pRecord)
        free(pRecord);

    return status;
}


// Get the record number to the last record in the log file.
DWORD GetLastRecordNumber(HANDLE hEventLog, DWORD* pdwRecordNumber)
{
    DWORD status = ERROR_SUCCESS;
    DWORD OldestRecordNumber = 0;
    DWORD NumberOfRecords = 0;

    if (!GetOldestEventLogRecord(hEventLog, &OldestRecordNumber))
    {
        wprintf(L"GetOldestEventLogRecord failed with %lu.\n", status = GetLastError());
        goto cleanup;
    }

    if (!GetNumberOfEventLogRecords(hEventLog, &NumberOfRecords))
    {
        wprintf(L"GetOldestEventLogRecord failed with %lu.\n", status = GetLastError());
        goto cleanup;
    }

    *pdwRecordNumber = OldestRecordNumber + NumberOfRecords - 1;

cleanup:

    return status;
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



// Read a single record from the event log.
DWORD ReadRecord(HANDLE hEventLog, PBYTE & pBuffer, DWORD dwRecordNumber, DWORD dwFlags)
{
    DWORD status = ERROR_SUCCESS;
    DWORD dwBytesToRead = sizeof(EVENTLOGRECORD);
    DWORD dwBytesRead = 0;
    DWORD dwMinimumBytesToRead = 0;
    PBYTE pTemp = NULL;

    // The initial size of the buffer is not big enough to read a record, but ReadEventLog
    // requires a valid pointer. The ReadEventLog function will fail and return the required 
    // buffer size; reallocate the buffer to the required size.
    pBuffer= (PBYTE)malloc(sizeof(EVENTLOGRECORD));

    // Get the required buffer size, reallocate the buffer and then read the event record.
    if (!ReadEventLog(hEventLog, dwFlags, dwRecordNumber, pBuffer, dwBytesToRead, &dwBytesRead, &dwMinimumBytesToRead))
    {
        status = GetLastError();
        if (ERROR_INSUFFICIENT_BUFFER == status)
        {
            status = ERROR_SUCCESS;

            pTemp = (PBYTE)realloc(pBuffer, dwMinimumBytesToRead);
            if (NULL == pTemp)
            {
                wprintf(L"Failed to reallocate memory for the record buffer (%d bytes).\n", dwMinimumBytesToRead);
                goto cleanup;
            }

            pBuffer = pTemp;

            dwBytesToRead = dwMinimumBytesToRead;

            if (!ReadEventLog(hEventLog, dwFlags, dwRecordNumber, pBuffer, dwBytesToRead, &dwBytesRead, &dwMinimumBytesToRead))
            {
                wprintf(L"Second ReadEventLog failed with %lu.\n", status = GetLastError());
                goto cleanup;
            }
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

cleanup:

    return status;
}


// Write the contents of each event record that was written to the log since
// the last notification. The service signals the event object every five seconds
// if an event has been written to the log.
DWORD DumpNewRecords(HANDLE hEventLog)
{
    DWORD status = ERROR_SUCCESS;
    DWORD dwLastRecordNumber = 0;
    LPWSTR pMessage = NULL;
    LPWSTR pFinalMessage = NULL;
    PBYTE pRecord = NULL;

    // Read the first record to prime the loop.
    status = ReadRecord(hEventLog, pRecord, 0, EVENTLOG_SEQUENTIAL_READ | EVENTLOG_FORWARDS_READ);
    if (ERROR_SUCCESS != status && ERROR_HANDLE_EOF != status)
    {
        wprintf(L"ReadRecord (priming read) failed.\n");
        goto cleanup;
    }

    // During the five second notification period, one or more records could
    // have been written to the log. Read all the records that have been 
    // written since the last notification. 
    while (ERROR_HANDLE_EOF != status)
    {
        // If the event was written by our provider, write the contents of the event.
        if (0 == wcscmp(PROVIDER_NAME, (LPWSTR)(pRecord + sizeof(EVENTLOGRECORD))))
        {
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

        // Read sequentially through the records.
        status = ReadRecord(hEventLog, pRecord, 0, EVENTLOG_SEQUENTIAL_READ | EVENTLOG_FORWARDS_READ);
        if (ERROR_SUCCESS != status && ERROR_HANDLE_EOF != status)
        {
            wprintf(L"ReadRecord sequential failed.\n");
            goto cleanup;
        }
    }

    if (ERROR_HANDLE_EOF == status)
    {
        status = ERROR_SUCCESS;
    }

cleanup:

    if (pRecord)
        free(pRecord);

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
//
// In this example, the message string for message ID 0x103 is "%1 %%4096 = %2 %%4097.".
// When you call FormatMessage to get the message string, FormatMessage returns 
// "8 %4096 = 2 %4097.". You need to replace %4096 and %4097 with the message strings
// associated with message IDs 4096 and 4097, respectively.
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

    // Append the last segment from pMessage, which in this example is ".".
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


// Determines whether the console input was a key event.
BOOL IsKeyEvent(HANDLE hStdIn)
{
    INPUT_RECORD Record[128];
    DWORD dwRecordsRead = 0;
    BOOL fKeyPress = FALSE;

    if (ReadConsoleInput(hStdIn, Record, 128, &dwRecordsRead))
    {
        for (DWORD i = 0; i < dwRecordsRead; i++)
        {
            if (KEY_EVENT == Record[i].EventType)
            {
                fKeyPress = TRUE;
                break;
            }
        }
    }

    return fKeyPress;
}
```



 

 



