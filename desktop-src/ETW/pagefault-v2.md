---
description: This class is the parent class for page fault events. The following syntax is simplified from MOF code.
ms.assetid: cc349e75-fe81-427e-8cf9-15c76e8e4dad
title: PageFault_V2 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PageFault_V2
api_type: 
- NA
api_location: 
---

# PageFault\_V2 class

This class is the parent class for page fault events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{3d6fa8d3-fe05-11d0-9dda-00c04fd7ba7c}"), EventVersion(2)]
class PageFault_V2 : MSNT_SystemTrace
{
};
```

## Members

The **PageFault\_V2** class does not define any members.

## Remarks

To enable all page fault events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_MEMORY\_PAGE\_FAULTS** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function. You can also specify the following flags:

-   **EVENT\_TRACE\_FLAG\_MEMORY\_HARD\_FAULTS**
-   **EVENT\_TRACE\_FLAG\_VIRTUAL\_ALLOC**

Event trace consumers can implement special processing for all page fault events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**PageFaultGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual memory event when consuming events.



| Event type                                                     | Description                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EVENT\_TRACE\_TYPE\_MM\_COW(Event type value is 12)<br/> | Copy-on-write event. The [**PageFault\_TypeGroup1**](pagefault-typegroup1.md) MOF class defines the event data for this event. Prior to Windows Vista, the [**PageFault\_TransitionFault**](pagefault-transitionfault.md) MOF class defines the event.     |
| EVENT\_TRACE\_TYPE\_MM\_DZF(Event type value is 11)<br/> | Demand zero fault event. The [**PageFault\_TypeGroup1**](pagefault-typegroup1.md) MOF class defines the event data for this event. Prior to Windows Vista, the [**PageFault\_TransitionFault**](pagefault-transitionfault.md) MOF class defines the event. |
| EVENT\_TRACE\_TYPE\_MM\_GPF(Event type value is 13)<br/> | Guard page fault event. The [**PageFault\_TypeGroup1**](pagefault-typegroup1.md) MOF class defines the event data for this event. Prior to Windows Vista, the [**PageFault\_TransitionFault**](pagefault-transitionfault.md) MOF class defines the event.  |
| EVENT\_TRACE\_TYPE\_MM\_HPF(Event type value is 14)<br/> | Hard page fault event. The [**PageFault\_TypeGroup1**](pagefault-typegroup1.md) MOF class defines the event data for this event. Prior to Windows Vista, the [**PageFault\_TransitionFault**](pagefault-transitionfault.md) MOF class defines the event.   |
| EVENT\_TRACE\_TYPE\_MM\_TF(Event type value is 10)<br/>  | Transition fault event. The [**PageFault\_TypeGroup1**](pagefault-typegroup1.md) MOF class defines the event data for this event. Prior to Windows Vista, the [**PageFault\_TransitionFault**](pagefault-transitionfault.md) MOF class defines the event.  |
| EVENT\_TRACE\_TYPE\_MM\_AV(Event type value is 15)<br/>  | Access violation event. The [**PageFault\_TypeGroup1**](pagefault-typegroup1.md) MOF class defines the event data for this event.                                                                                                                           |
| Event type value, 32                                           | Hard page fault event.The [**PageFault\_HardFault**](pagefault-hardfault.md) MOF class defines the event data for this event.                                                                                                                               |
| Event type value, 105                                          | Image load in page file event. The [**PageFault\_ImageLoadBacked**](pagefault-imageloadbacked.md) MOF class defines the event data for this event.                                                                                                          |
| Event type value, 98                                           | Virtual allocation event. The [**VirtualAlloc**](pagefault-virtualalloc.md) MOF class defines the event data for this event.                                                                                                                                |
| Event type value, 99                                           | Virtual free event. The [**VirtualAlloc**](pagefault-virtualalloc.md) MOF class defines the event data for this event.                                                                                                                                      |



 

You can use the **ProcessId** and **ThreadId** members of [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) to identify the faulting process or thread.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 
