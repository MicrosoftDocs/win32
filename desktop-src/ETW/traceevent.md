---
Description: The TraceEvent function sends an event to an event tracing session.
ms.assetid: '9b21f6f0-dd9b-4f9c-a879-846901a3bab7'
title: TraceEvent function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TraceEvent
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- API-MS-Win-DownLevel-AdvApi32-l1-1-0.dll
- KernelBase.dll
- API-MS-Win-DownLevel-AdvApi32-l1-1-1.dll
- API-MS-Win-eventing-classicprovider-l1-1-0.dll
---

# TraceEvent function

The **TraceEvent** function sends an event to an event tracing session.

## Syntax


```C++
ULONG TraceEvent(
  _In_ TRACEHANDLE         SessionHandle,
  _In_ PEVENT_TRACE_HEADER EventTrace
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session that records the event. The provider obtains the handle when it calls the [**GetTraceLoggerHandle**](gettraceloggerhandle.md) function in its [*ControlCallback*](controlcallback.md) implementation.

</dd> <dt>

*EventTrace* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_TRACE\_HEADER**](event-trace-header.md) structure. Event-specific data is optionally appended to the structure. The largest event you can log is 64K. You must specify values for the following members of the **EVENT\_TRACE\_HEADER** structure.

-   **Size**
-   **Guid** or **GuidPtr**
-   **Flags**

Depending on the complexity of the information your provider provides, you should also consider specifying values for the following members.

-   **Class.Type**
-   **Class.Level**

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



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
<td><dl> <dt><strong>ERROR_INVALID_FLAG_NUMBER</strong></dt> </dl></td>
<td>The <strong>Flags</strong> member of the <a href="event-trace-header"><strong>EVENT_TRACE_HEADER</strong></a> structure is incorrect.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_HANDLE</strong></dt> </dl></td>
<td><em>SessionHandle</em> is not valid or specifies the NT Kernel Logger session handle.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_NOT_ENOUGH_MEMORY</strong></dt> </dl></td>
<td>The session ran out of free buffers to write to. This can occur during high event rates because the disk subsystem is overloaded or the number of buffers is too small. Rather than blocking until more buffers become available, <a href="traceevent"><strong>TraceEvent</strong></a> discards the event. <br/> Consider increasing the number and size of the buffers for the session, or reducing the number of events written or the size of the events.<br/> <strong>Windows 2000:</strong> Not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_OUTOFMEMORY</strong></dt> </dl></td>
<td>The event is discarded because, although the buffer pool has not reached its maximum size, there is insufficient available memory to allocate an additional buffer and there is no buffer available to receive the event. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>SessionHandle</em> is <strong>NULL</strong>.</li>
<li><em>EventTrace</em> is <strong>NULL</strong>.</li>
<li>The <strong>Size</strong> member of the <a href="event-trace-header"><strong>EVENT_TRACE_HEADER</strong></a> structure is incorrect.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_MORE_DATA</strong></dt> </dl></td>
<td>Data from a single event cannot span multiple buffers. A trace event is limited to the size of the event tracing session's buffer minus the size of the <a href="event-trace-header"><strong>EVENT_TRACE_HEADER</strong></a> structure. <br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Providers call this function.

Before the provider can call this function, the provider

-   Must call the [**RegisterTraceGuids**](registertraceguids.md) function to register itself and the event trace class.
-   Must be enabled. A controller calls the [**EnableTrace**](enabletrace.md) function to enable a provider.

The event is either written to a log file, sent to event trace consumers in real time, or both. The **LogFileMode** member of the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure passed to the [**StartTrace**](starttrace.md) defines where the event is sent.

The trace events are written in the order in which they occur.

To trace a set of related events, use the [**TraceEventInstance**](traceeventinstance.md) function.

On Windows Vista, you should use the [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) function to log events.

## Examples

For an example that uses **TraceEvent**, see [Tracing Events](tracing-events.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**EnableTrace**](enabletrace.md)
</dt> <dt>

[**EVENT\_TRACE\_HEADER**](event-trace-header.md)
</dt> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> <dt>

[**TraceEventInstance**](traceeventinstance.md)
</dt> </dl>

 

 




