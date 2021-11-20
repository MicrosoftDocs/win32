---
description: Process_V2 class - This class is the parent class for process events. The following syntax is simplified from MOF code.
ms.assetid: 75596278-43cc-4040-a43d-6958d0935b68
title: Process_V2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Process
api_type: 
- NA
api_location: 
---

# Process\_V2 class

This class is the parent class for process events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{3d6fa8d0-fe05-11d0-9dda-00c04fd7ba7c}"), EventVersion(2)]
class Process_V2 : MSNT_SystemTrace
{
};
```

## Members

The **Process** class does not define any members.

## Remarks

To enable process events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_PROCESS** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function. You can also specify the following flag:

-   **EVENT\_TRACE\_FLAG\_PROCESS\_COUNTERS**

Event trace consumers can implement special processing for process events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**ProcessGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual process event when consuming events.



| Event type                                                      | Description                                                                                                                                                                                                                        |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_END**(Event type value is 2)<br/>   | End process event. The [**Process\_TypeGroup1**](process-typegroup1.md) MOF class defines the event data for this event.                                                                                                          |
| **EVENT\_TRACE\_TYPE\_START**(Event type value is 1)<br/> | Start process event. The [**Process\_TypeGroup1**](process-typegroup1.md) MOF class defines the event data for this event.                                                                                                        |
| Event type value, 3                                             | Start data collection process event. Enumerates processes that are currently running at the time the kernel session starts. The [**Process\_TypeGroup1**](process-typegroup1.md) MOF class defines the event data for this event. |
| Event type value, 4                                             | End data collection process event. Enumerates processes that are currently running at the time the kernel session ends. The [**Process\_TypeGroup1**](process-typegroup1.md) MOF class defines the event data for this event.     |
| Event type value, 32                                            | Performance counters event. The [**Process\_V2\_TypeGroup2**](process-v2-typegroup2.md) MOF class defines the event data for this event.                                                                                          |
| Event type value, 33                                            | Rundown of the performance counters at the start of the session. The [**Process\_V2\_TypeGroup2**](process-v2-typegroup2.md) MOF class defines the event data for this event.                                                     |
| Event type value, 39                                            | Defunct process event. The [**Process\_TypeGroup1**](process-typegroup1.md) MOF class defines the event data for this event.                                                                                                      |



 

Process and thread start events may be logged in the context of the parent process or thread. As a result, the **ProcessId** and **ThreadId** members of [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) may not correspond to the process and thread being created. This is why these events contain the process and thread identifiers in the event data (in addition to those in the event header).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**Process**](process.md)
</dt> <dt>

[**Process\_TypeGroup1**](process-typegroup1.md)
</dt> <dt>

[**Process\_V0**](process-v0.md)
</dt> <dt>

[**Process\_V1**](process-v1.md)
</dt> </dl>

 

 
