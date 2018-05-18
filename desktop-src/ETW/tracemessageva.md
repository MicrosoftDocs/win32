---
Description: 'The TraceMessageVa function sends an informational message with variable arguments to an event tracing session.'
ms.assetid: '2cfb7226-fd29-432e-abfd-bd10c6344a67'
title: TraceMessageVa function
---

# TraceMessageVa function

The **TraceMessageVa** function sends an informational message with variable arguments to an event tracing session.

## Syntax


```C++
ULONG TraceMessageVa(
  _In_ TRACEHANDLE SessionHandle,
  _In_ ULONG       MessageFlags,
  _In_ LPGUID      MessageGuid,
  _In_ USHORT      MessageNumber,
  _In_ va_list     MessageArgList
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session that records the event. The provider obtains the handle when it calls the [**GetTraceLoggerHandle**](gettraceloggerhandle.md) function in its [*ControlCallback*](controlcallback.md) implementation.

</dd> <dt>

*MessageFlags* \[in\]
</dt> <dd>

Adds additional information to the beginning of the provider-specific data section of the event. The provider-specific data section of the event will contain data only for those flags that are set. The variable list of argument data will follow this information. This parameter can be one or more of the following values.



| Flag                                                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TRACE_MESSAGE_GUID"></span><span id="trace_message_guid"></span><dl> <dt>**TRACE\_MESSAGE\_GUID**</dt> </dl>                   | Include the event trace class GUID in the message. The *MessageGuid* parameter contains the event trace class GUID.<br/>                                                                                                                                        |
| <span id="TRACE_MESSAGE_SEQUENCE"></span><span id="trace_message_sequence"></span><dl> <dt>**TRACE\_MESSAGE\_SEQUENCE**</dt> </dl>       | Include a sequence number in the message. The sequence number starts at one. To use this flag, the controller must have set the **EVENT\_TRACE\_USE\_GLOBAL\_SEQUENCE** or **EVENT\_TRACE\_USE\_LOCAL\_SEQUENCE** log file mode when creating the session.<br/> |
| <span id="TRACE_MESSAGE_SYSTEMINFO"></span><span id="trace_message_systeminfo"></span><dl> <dt>**TRACE\_MESSAGE\_SYSTEMINFO**</dt> </dl> | Include the thread identifier and process identifier in the message.<br/>                                                                                                                                                                                       |
| <span id="TRACE_MESSAGE_TIMESTAMP"></span><span id="trace_message_timestamp"></span><dl> <dt>**TRACE\_MESSAGE\_TIMESTAMP**</dt> </dl>    | Include a time stamp in the message.<br/>                                                                                                                                                                                                                       |



 

The information is included in the event data in the following order:

-   Sequence number
-   Event trace class GUID
-   Time stamp
-   Thread identifier
-   Process identifier

</dd> <dt>

*MessageGuid* \[in\]
</dt> <dd>

Class GUID that identifies the event trace message.

</dd> <dt>

*MessageNumber* \[in\]
</dt> <dd>

Number that uniquely identifies each occurrence of the message. You must define the value specified for this parameter; the value should be meaningful to the application.

</dd> <dt>

*MessageArgList* \[in\]
</dt> <dd>

List of variable arguments to be appended to the message. The list must be composed of pairs of arguments, as described in the following table.



| Data Type                                                                                                                                | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="PVOID"></span><span id="pvoid"></span><dl> <dt>**PVOID**</dt> </dl>     | Pointer to the argument data.<br/>            |
| <span id="size_t"></span><span id="SIZE_T"></span><dl> <dt>**size\_t**</dt> </dl> | The size of the argument data, in bytes.<br/> |



 

Terminate the list using an argument pair consisting of a pointer to **NULL** and zero.

The caller must ensure that the sum of the sizes of the arguments + 72 does not exceed the size of the event tracing session's buffer.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](base.system_error_codes). The following table includes some common errors and their causes.



| Return code                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_HANDLE**</dt> </dl>     | Either the *SessionHandle* is **NULL** or specifies the NT Kernel Logger session handle. <br/>                                                                                                                                                                                                                                                             |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | The session ran out of free buffers to write to. This can occur during high event rates because the disk subsystem is overloaded or the number of buffers is too small. Rather than blocking until more buffers become available, [**TraceMessage**](tracemessage.md) discards the event.<br/> **Windows 2000 and Windows XP:** Not supported.<br/> |
| <dl> <dt>**ERROR\_OUTOFMEMORY**</dt> </dl>         | The event is discarded because, although the buffer pool has not reached its maximum size, there is insufficient available memory to allocate an additional buffer and there is no buffer available to receive the event. <br/>                                                                                                                            |
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>  | *MessageFlags* contains a value that is not valid.<br/>                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**ERROR\_MORE\_DATA**</dt> </dl>          | Data from a single event cannot span multiple buffers. A trace event is limited to the size of the event tracing session's buffer minus the size of the [**EVENT\_TRACE\_HEADER**](event-trace-header.md) structure. <br/>                                                                                                                                |



 

## Remarks

Providers call this function.

Using the [**TraceEvent**](traceevent.md) function is the preferred way to log an event. On Windows Vista, you should use the [**EventWrite**](eventwrite-func.md) function to log events.

The trace events are written in the order in which they occur.

If you do not need to access the message tracing functionality from a wrapper function, you can call the [**TraceMessage**](tracemessage.md) version of this function.

Consumers will have to use the [*EventCallback*](eventcallback.md) callback to receive and process the events if the *MessageFlags* parameter does not contain the TRACE\_MESSAGE\_GUID flag. If you do not specify the TRACE\_MESSAGE\_GUID flag, the consumer will not be able to use the [*EventClassCallback*](eventclasscallback.md) because the **Header.Guid** member of the [**EVENT\_TRACE**](event-trace.md) structure will not contain the event trace class GUID.

Note that the members of the [**EVENT\_TRACE**](event-trace.md) and [**EVENT\_TRACE\_HEADER**](event-trace-header.md) structures that correspond to the *MessageFlags* flags are set only if the corresponding flag is specified. For example, the **ThreadId** and **ProcessId** members of **EVENT\_TRACE\_HEADER** are populated only if you specify the TRACE\_MESSAGE\_SYSTEMINFO flag.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**TraceEvent**](traceevent.md)
</dt> <dt>

[**TraceEventInstance**](traceeventinstance.md)
</dt> <dt>

[**TraceMessage**](tracemessage.md)
</dt> </dl>

 

 




