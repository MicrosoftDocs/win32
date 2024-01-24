---
description: Thread_V2 class - This class is the parent class for thread events. The following syntax is simplified from MOF code.
ms.assetid: 63e52cba-42a5-44f0-8eb6-e1bac8414a83
title: Thread_V2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Thread_V2
api_type: 
- NA
api_location: 
---

# Thread\_V2 class

This class is the parent class for thread events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{3d6fa8d1-fe05-11d0-9dda-00c04fd7ba7c}"), EventVersion(2)]
class Thread_V2 : MSNT_SystemTrace
{
};
```

## Members

The **Thread\_V2** class does not define any members.

## Remarks

To enable thread events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_THREAD** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function. You can also specify the following flags:

-   **EVENT\_TRACE\_FLAG\_CSWITCH**
-   **EVENT\_TRACE\_FLAG\_DISPATCHER**

Event trace consumers can implement special processing for thread events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**ThreadGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual thread event when consuming events.



| Event type                                                      | Description                                                                                                                                                                                                                          |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_END**(Event type value is 2)<br/>   | End thread event. The [**Thread\_V2\_TypeGroup1**](thread-v2-typegroup1.md) MOF class defines the event data for this event.                                                                                                        |
| **EVENT\_TRACE\_TYPE\_START**(Event type value is 1)<br/> | Start thread event. The [**Thread\_V2\_TypeGroup1**](thread-v2-typegroup1.md) MOF class defines the event data for this event.                                                                                                      |
| Event type value, 3                                             | Start data collection thread event. Enumerates threads that are currently running at the time the kernel session starts. The [**Thread\_V2\_TypeGroup1**](thread-v2-typegroup1.md) MOF class defines the event data for this event. |
| Event type value, 4                                             | End data collection thread event. Enumerates threads that are currently running at the time the kernel session ends. The [**Thread\_V2\_TypeGroup1**](thread-v2-typegroup1.md) MOF class defines the event data for this event.     |
| Event type value, 36                                            | Context switch event. The [**CSwitch**](cswitch.md) MOF class defines the event data for this event.                                                                                                                                |
| Event type value, 50                                            | Ready thread event. The [**ReadyThread**](readythread.md) MOF class defines the event data for this event.                                                                                                                          |



 

Process and thread start events may be logged in the context of the parent process or thread. As a result, the **ProcessId** and **ThreadId** members of [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) may not correspond to the process and thread being created. This is why these events contain the process and thread identifiers in the event data (in addition to those in the event header).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**CSwitch**](cswitch.md)
</dt> <dt>

[**Thread**](thread.md)
</dt> <dt>

[**Thread\_TypeGroup1**](thread-typegroup1.md)
</dt> <dt>

[**Thread\_V0**](thread-v0.md)
</dt> <dt>

[**Thread\_V1**](thread-v1.md)
</dt> </dl>

 

 
