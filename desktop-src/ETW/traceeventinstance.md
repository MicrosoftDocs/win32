---
Description: The TraceEventInstance function sends an event to an event tracing session. The event uses an instance identifier to associate the event with a transaction. This function may also be used to trace hierarchical relationships between related events.
ms.assetid: e8361bdc-21dd-47a0-bdbf-56f4d6195689
title: TraceEventInstance function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TraceEventInstance
api_type: 
- DllExport
api_location: 
- Advapi32.dll
---

# TraceEventInstance function

The **TraceEventInstance** function sends an event to an event tracing session. The event uses an instance identifier to associate the event with a transaction. This function may also be used to trace hierarchical relationships between related events.

## Syntax


```C++
ULONG TraceEventInstance(
  _In_ TRACEHANDLE            SessionHandle,
  _In_ PEVENT_INSTANCE_HEADER EventTrace,
  _In_ PEVENT_INSTANCE_INFO   pInstInfo,
  _In_ PEVENT_INSTANCE_INFO   pParentInstInfo
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session that records the event instance. The provider obtains the handle when it calls the [**GetTraceLoggerHandle**](gettraceloggerhandle.md) function in its [*ControlCallback*](controlcallback.md) implementation.

</dd> <dt>

*EventTrace* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_INSTANCE\_HEADER**](event-instance-header.md) structure. Event-specific data is optionally appended to the structure. The largest event you can log is 64K. You must specify values for the following members of the **EVENT\_INSTANCE\_HEADER** structure.

-   **Size**
-   **Flags**
-   **RegHandle**

Depending on the complexity of the information your provider provides, you should also consider specifying values for the following members.

-   **Class.Type**
-   **Class.Level**

To trace hierarchical relationships between related events, also set the **ParentRegHandle** member.

</dd> <dt>

*pInstInfo* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_INSTANCE\_INFO**](event-instance-info.md) structure, which contains the registration handle for this event trace class and the instance identifier. Use the [**CreateTraceInstanceId**](createtraceinstanceid.md) function to initialize the structure.

</dd> <dt>

*pParentInstInfo* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_INSTANCE\_INFO**](event-instance-info.md) structure, which contains the registration handle for the parent event trace class and its instance identifier. Use the [**CreateTraceInstanceId**](createtraceinstanceid.md) function to initialize the structure. Set to **NULL** if you are not tracing a hierarchical relationship.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/en-us/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



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
<td><dl> <dt><strong>ERROR_INVALID_FLAGS</strong></dt> </dl></td>
<td>The <strong>Flags</strong> member of the <a href="event-instance-header"><strong>EVENT_INSTANCE_HEADER</strong></a> does not contain <strong>WNODE_FLAG_TRACED_GUID</strong>.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_OUTOFMEMORY</strong></dt> </dl></td>
<td>There was insufficient memory to complete the function call. The causes for this error code are described in the following Remarks section.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>EventTrace</em> is <strong>NULL</strong>.</li>
<li><em>pInstInfo</em> is <strong>NULL</strong>.</li>
<li>The members of <em>pInstInfo</em> are <strong>NULL</strong>.</li>
<li><em>SessionHandle</em> is <strong>NULL</strong>.</li>
<li>The <strong>Size</strong> member of the <a href="event-instance-header"><strong>EVENT_INSTANCE_HEADER</strong></a> is incorrect.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_HANDLE</strong></dt> </dl></td>
<td><em>SessionHandle</em> is not valid or specifies the NT Kernel Logger session handle.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_NOT_ENOUGH_MEMORY</strong></dt> </dl></td>
<td>The session ran out of free buffers to write to. This can occur during high event rates because the disk subsystem is overloaded or the number of buffers is too small. Rather than blocking until more buffers become available, <a href="traceevent"><strong>TraceEvent</strong></a> discards the event.<br/> <strong>Windows 2000 and Windows XP:</strong> Not supported.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_OUTOFMEMORY</strong></dt> </dl></td>
<td>The event is discarded because, although the buffer pool has not reached its maximum size, there is insufficient available memory to allocate an additional buffer and there is no buffer available to receive the event. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_MORE_DATA</strong></dt> </dl></td>
<td>Data from a single event cannot span multiple buffers. A trace event is limited to the size of the event tracing session's buffer minus the size of the <a href="event-instance-header"><strong>EVENT_INSTANCE_HEADER</strong></a> structure. <br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Providers call this function.

Before the provider can call this function, the provider

-   Must call the [**RegisterTraceGuids**](registertraceguids.md) function to register itself and the event trace class.
-   Must call the [**CreateTraceInstanceId**](createtraceinstanceid.md) function to create an instance identifier for the registered event trace class.
-   Must be enabled. A controller calls the [**EnableTrace**](enabletrace.md) function to enable a provider.

The event is either written to a log file, sent to event trace consumers in real time, or both. The **LogFileMode** member of the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure passed to the [**StartTrace**](starttrace.md) defines where the event is sent.

The trace events are written in the order in which they occur.

To trace unrelated events, use the [**TraceEvent**](traceevent.md) function.

**Windows XP:** Does not work correctly.

## Examples

For an example of generating related sets of events using [**CreateTraceInstanceId**](createtraceinstanceid.md) and **TraceEventInstance**, see [Tracing Event Instances](tracing-event-instances.md).

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

[**CreateTraceInstanceId**](createtraceinstanceid.md)
</dt> <dt>

[**EVENT\_INSTANCE\_HEADER**](event-instance-header.md)
</dt> <dt>

[**EVENT\_INSTANCE\_INFO**](event-instance-info.md)
</dt> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> <dt>

[**TraceEvent**](traceevent.md)
</dt> </dl>

 

 




