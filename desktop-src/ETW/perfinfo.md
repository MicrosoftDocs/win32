---
description: This class is the parent class for performance counter events. The following syntax is simplified from MOF code.
ms.assetid: 2606fea3-0651-4f7f-83a6-63021039eb95
title: PerfInfo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PerfInfo
api_type: 
- NA
api_location: 
---

# PerfInfo class

This class is the parent class for performance counter events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{ce1dbfb4-137e-4da6-87b0-3f59aa102cbc}"), EventVersion(2)]
class PerfInfo : MSNT_SystemTrace
{
};
```

## Members

The **PerfInfo** class does not define any members.

## Remarks

To enable deferred procedure call (DPC) events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_DPC** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function. You can also specify one or more of the following flags:

-   **EVENT\_TRACE\_FLAG\_INTERRUPT**
-   **EVENT\_TRACE\_FLAG\_PROFILE**
-   **EVENT\_TRACE\_FLAG\_SYSTEMCALL**

Event trace consumers can implement special processing for DPC events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**PerfInfoGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual event when consuming events.



| Event type           | Description                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| Event type value, 46 | Sampled profile event. The [**SampledProfile**](sampledprofile.md) MOF class defines the event data for this event. |
| Event type value, 51 | System call enter event. The [**SysCallEnter**](syscallenter.md) MOF class defines the event data for this event.   |
| Event type value, 52 | System call exit event. The [**SysCallExit**](syscallexit.md) MOF class defines the event data for this event.      |
| Event type value, 66 | Threaded DPC event. The [**DPC**](dpc.md) MOF class defines the event data for this event.                          |
| Event type value, 67 | Interrupt service routine (ISR) event. The [**ISR**](isr.md) MOF class defines the event data for this event.       |
| Event type value, 68 | DPC event. The [**DPC**](dpc.md) MOF class defines the event data for this event.                                   |
| Event type value, 69 | DPC timer event. The [**DPC**](dpc.md) MOF class defines the event data for this event.                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 
