---
title: New Trace Event Types
description: These new types \ 0034;turn on \ 0034; stack tracing events in the STACK\_TRACING\_EVENT\_ID structure.\ define EVENT\_TRACE\_TYPE\_READYTHREAD 0x32This flag enables stack tracing for Ready Thread events.
ms.assetid: 31e467d2-1d63-4a3d-b0d1-cff9f777e4b1
keywords:
- New Trace Event Types Windows Performance Analyzer
topic_type:
- apiref
api_name:
- New Trace Event Types
api_location:
- KernelTraceControl.dll
- KernelTraceControl.dll.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# New Trace Event Types

These new types "turn on" stack tracing events in the [**STACK\_TRACING\_EVENT\_ID**](stack-tracing-event-id.md) structure.


```
#define EVENT_TRACE_TYPE_READYTHREAD        0x32
```



This flag enables stack tracing for Ready Thread events. The trace type is also published in wmicore.mof file for Windows 7 and Windows Server 2008.


```
#define EVENT_TRACE_TYPE_VIRTUAL_ALLOC      0x62
```



This flag enables stack tracing for virtual memory allocation events. The trace type is also published in wmicore.mof file for Windows 7 and Windows Server 2008.


```
#define EVENT_TRACE_TYPE_VIRTUAL_FREE       0x63
```



This flag enables stack tracing for virtual memory free events. The trace type is also published in wmicore.mof file for Windows 7 and Windows Server 2008.

## Remarks

These event types are similar to the event types used in the **EVENT\_TRACE\_PROPERTIES.EnableFlags** member but are particular to the Kernel Trace Control API.

## Requirements



|                    |                                                                                                                                                                |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows Vista and later versions of the Windows operating system. This structure is distributed with the Windows Performance Analyzer.<br/> |
| Header<br/>  | <dl> <dt>KernelTraceControl.h (include KernelTraceControl.h)</dt> </dl>                                 |
| Library<br/> | <dl> <dt>KernelTraceControl.dll</dt> </dl>                                                              |



## See also

<dl> <dt>

[EVENT\_INSTANCE\_HEADER](http://go.microsoft.com/fwlink/p/?linkid=141513)
</dt> </dl>

 

 





