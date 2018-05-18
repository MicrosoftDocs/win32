---
Description: 'The QueryAllTraces function retrieves the properties and statistics for all event tracing sessions started on the computer for which the caller has permissions to query.'
ms.assetid: '6b6144b0-9152-4b5e-863d-06e823fbe084'
title: QueryAllTraces function
---

# QueryAllTraces function

The **QueryAllTraces** function retrieves the properties and statistics for all event tracing sessions started on the computer for which the caller has permissions to query.

## Syntax


```C++
ULONG QueryAllTraces(
  _Out_ PEVENT_TRACE_PROPERTIES *PropertyArray,
  _In_  ULONG                   PropertyArrayCount,
  _Out_ PULONG                  SessionCount
);
```



## Parameters

<dl> <dt>

*PropertyArray* \[out\]
</dt> <dd>

An array of pointers to [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structures that receive session properties and statistics for the event tracing sessions.

You only need to set the **Wnode.BufferSize**, **LoggerNameOffset** , and **LogFileNameOffset** members of the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure. The other members should all be set to zero.

</dd> <dt>

*PropertyArrayCount* \[in\]
</dt> <dd>

Number of structures in the *PropertyArray* array. This value must be less than or equal to 64, the maximum number of event tracing sessions that ETW supports.

</dd> <dt>

*SessionCount* \[out\]
</dt> <dd>

Actual number of event tracing sessions started on the computer.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](base.system_error_codes). The following table includes some common errors and their causes.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>PropertyArrayCount</em> is zero or greater than the maximum number of supported sessions</li>
<li><em>PropertyArray</em> is <strong>NULL</strong></li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_MORE_DATA</strong></dt> </dl></td>
<td>The property array is too small to receive information for all sessions (<em>SessionCount</em> is greater than <em>PropertyArrayCount</em>). The function fills the property array with the number of property structures specified in <em>PropertyArrayCount</em>.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

This function retrieves the trace sessions that the caller has permissions to query. Users running with elevated administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can view all tracing sessions.

This function does not return private logging sessions.

To retrieve information for a single session, use the [**ControlTrace**](controltrace.md) function and set the *ControlCode* parameter to **EVENT\_TRACE\_CONTROL\_QUERY**.

## Examples

The following example shows how to call this function.


```C++
#include <windows.h>
#include <stdio.h>
#include <wmistr.h>
#include <evntrace.h>

#define MAX_SESSIONS 64
#define MAX_SESSION_NAME_LEN 1024
#define MAX_LOGFILE_PATH_LEN 1024

void wmain(void)
{
    ULONG status = ERROR_SUCCESS;
    PEVENT_TRACE_PROPERTIES pSessions[MAX_SESSIONS];    // Array of pointers to property structures
    PEVENT_TRACE_PROPERTIES pBuffer = NULL;             // Buffer that contains all the property structures
    ULONG SessionCount = 0;                             // Actual number of sessions started on the computer
    ULONG BufferSize = 0;
    ULONG PropertiesSize = 0;
    WCHAR SessionGuid[50];


    // The size of the session name and log file name used by the
    // controllers are not known, therefore create a properties structure that allows
    // for the maximum size of both.

    PropertiesSize = sizeof(EVENT_TRACE_PROPERTIES) +
        (MAX_SESSION_NAME_LEN*sizeof(WCHAR)) +
        (MAX_LOGFILE_PATH_LEN*sizeof(WCHAR));

    BufferSize = PropertiesSize * MAX_SESSIONS;

    pBuffer = (PEVENT_TRACE_PROPERTIES) malloc(BufferSize);

    if (pBuffer)
    {
        ZeroMemory(pBuffer, BufferSize);

        for (USHORT i = 0; i < MAX_SESSIONS; i++)
        {
            pSessions[i] = (EVENT_TRACE_PROPERTIES*)((BYTE*)pBuffer + (i*PropertiesSize));
            pSessions[i]->Wnode.BufferSize = PropertiesSize;
            pSessions[i]->LoggerNameOffset = sizeof(EVENT_TRACE_PROPERTIES);
            pSessions[i]->LogFileNameOffset = sizeof(EVENT_TRACE_PROPERTIES) + (MAX_SESSION_NAME_LEN*sizeof(WCHAR));
        }
    }
    else
    {
        wprintf(L"Error allocating memory for properties.\n");
        goto cleanup;
    }

    status = QueryAllTraces(pSessions, (ULONG)MAX_SESSIONS, &amp;SessionCount);

    if (ERROR_SUCCESS == status || ERROR_MORE_DATA == status)
    {
        wprintf(L"Requested session count, %d. Actual session count, %d.\n\n", MAX_SESSIONS, SessionCount);

        for (USHORT i = 0; i < SessionCount; i++)
        {
            StringFromGUID2(pSessions[i]->Wnode.Guid, SessionGuid, (sizeof(SessionGuid) / sizeof(SessionGuid[0])));

                wprintf(L"Session GUID: %s\nSession ID: %d\nSession name: %s\nLog file: %s\n"
                    L"min buffers: %d\nmax buffers: %d\nbuffers: %d\nbuffers written: %d\n"
                    L"buffers lost: %d\nevents lost: %d\n\n",
                    SessionGuid,
                    pSessions[i]->Wnode.HistoricalContext,
                    (LPWSTR)((char*)pSessions[i] + pSessions[i]->LoggerNameOffset),
                    (LPWSTR)((char*)pSessions[i] + pSessions[i]->LogFileNameOffset),
                    pSessions[i]->MinimumBuffers,
                    pSessions[i]->MaximumBuffers,
                    pSessions[i]->NumberOfBuffers,
                    pSessions[i]->BuffersWritten,
                    pSessions[i]->LogBuffersLost,
                    pSessions[i]->EventsLost);
        }
    }
    else
    {
        wprintf(L"Error calling QueryAllTraces, %d.\n", status);
        goto cleanup;
    }

cleanup:

    if (pBuffer)
    {
        free(pBuffer);
        pBuffer = NULL;
    }
}
```



## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                   |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                                                                                                                                                                         |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| Unicode and ANSI names<br/>   | **QueryAllTracesW** (Unicode) and **QueryAllTracesA** (ANSI)<br/>                                                                                                                                                                                                                                                      |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> <dt>

[**EnumerateTraceGuids**](enumeratetraceguids.md)
</dt> <dt>

[**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md)
</dt> </dl>

 

 




