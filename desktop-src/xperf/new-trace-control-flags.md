---
title: New Trace Control Flags
description: The following two WPT/ETW trace control flags have been added.
ms.assetid: '6afe8c1e-1375-4412-a38e-7b40f2e4a950'
keywords: ["New Trace Control Flags Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- New Trace Control Flags
api_location:
- KernelTraceControl.dll
- KernelTraceControl.dll.dll
api_type:
- LibDef
---

# New Trace Control Flags

The following two WPT/ETW trace control flags have been added. These flags are set in the **EVENT\_TRACE\_PROPERTIES.EnableFlags** member of the [EVENT\_TRACE\_HEADER](http://go.microsoft.com/fwlink/p/?linkid=141511) structure. For more information about flags that can be used to set **EVENT\_TRACE\_PROPERTIES.EnableFlags**, see [MSDN](http://go.microsoft.com/fwlink/p/?linkid=141500).


```
#define EVENT_TRACE_FLAG_DISPATCHER         0x00000800
```



This flag enables capture of Ready Thread events.


```
#define EVENT_TRACE_FLAG_VIRTUAL_ALLOC      0x00004000
```



This flag enables capture of Virtual Allocations and Free events.

## Remarks

**EVENT\_TRACE\_FLAG\_DISPATCHER** and **EVENT\_TRACE\_FLAG\_VIRTUAL\_ALLOC** are also published in header file evntrace.h file for Windows 7 and Windows Server 2008.

A single kernel trace control flag enables or disables logging of a kernel event type. For more information on kernel flags and corresponding kernel events, see [MSDN](http://go.microsoft.com/fwlink/p/?linkid=141500).

## Requirements



|                    |                                                                                                                                                                |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows Vista and later versions of the Windows operating system. This structure is distributed with the Windows Performance Analyzer.<br/> |
| Header<br/>  | <dl> <dt>KernelTraceControl.h (include KernelTraceControl.h or Evntrace.h)</dt> </dl>                   |
| Library<br/> | <dl> <dt>KernelTraceControl.dll</dt> </dl>                                                              |



## See also

<dl> <dt>

[EVENT\_TRACE\_HEADER](http://go.microsoft.com/fwlink/p/?linkid=141511)
</dt> <dt>

[EVENT\_TRACE\_PROPERTIES](http://go.microsoft.com/fwlink/p/?linkid=141500)
</dt> </dl>

 

 





