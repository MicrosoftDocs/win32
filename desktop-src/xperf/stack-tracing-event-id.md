---
title: STACK\_TRACING\_EVENT\_ID structure
description: The STACK\_TRACING\_EVENT\_ID structure tells the kernel logger to include the call stack for the named events.
ms.assetid: 'da399d8c-1e8c-48e6-b042-f3c7fa79a80d'
keywords: ["STACK_TRACING_EVENT_ID structure Windows Performance Analyzer", "PSTACK_TRACING_EVENT_ID structure pointer Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- STACK_TRACING_EVENT_ID
api_location:
- KernelTraceControl.h
api_type:
- HeaderDef
---

# STACK\_TRACING\_EVENT\_ID structure

The **STACK\_TRACING\_EVENT\_ID** structure tells the kernel logger to include the call stack for the named events.

## Syntax


```C++
typedef struct {
  GUID  EventGuid;
  UCHAR Type;
  UCHAR Reserved[7];
} STACK_TRACING_EVENT_ID, *PSTACK_TRACING_EVENT_ID;
```



## Members

<dl> <dt>

**EventGuid**
</dt> <dd>

The GUID that identifies a specific kernel event that is configured to generate call stacks.

For more information on GUID values for the **EventGuid** member, see the [NT Kernel Logger Constants](http://go.microsoft.com/fwlink/p/?linkid=141503) discussion of NT Kernel Logger Constants. Additionally, **EventGuid** GUID values are listed in Evntrace.h.

</dd> <dt>

**Type**
</dt> <dd>

The Kernel Trace Control **Type** member introduces three new event types.

-   **EVENT\_TRACE\_TYPE\_READYTHREAD**

-   **EVENT\_TRACE\_TYPE\_VIRTUAL\_ALLOC**

-   **EVENT\_TRACE\_TYPE\_VIRTUAL\_FREE**

For more information on these new event types, see [**New Trace Event Types**](new-trace-event-types.md).

</dd> <dt>

**Reserved**
</dt> <dd>

This member is used to pad the structure and is reserved for future use only; it should not be used.

</dd> </dl>

## Remarks

The **STACK\_TRACING\_EVENT\_ID** structure members are identical to the [**CLASSIC\_EVENT\_ID**](https://msdn.microsoft.com/library/windows/desktop/dd392304) structure that is available in the following versions of the SDK:

-   Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1

-   Microsoft Windows SDK for Windows Server 2008 and .NET Framework 3.5


```
typedef struct _CLASSIC_EVENT_ID {
 GUID  EventGuid; 
    UCHAR Type; 
    UCHAR Reserved[7]; 
} CLASSIC_EVENT_ID, *PCLASSIC_EVENT_ID; 
```



## Requirements



|                    |                                                                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows Vista and later versions of the Windows operating system. This structure is distributed with the Windows Performance Analyzer. <br/> |
| Header<br/>  | <dl> <dt>KernelTraceControl.h (include KernelTraceControl.h or Evntrace.h)</dt> </dl>                    |



## See also

<dl> <dt>

[**StartKernelTrace**](startkerneltrace.md)
</dt> </dl>

 

 





