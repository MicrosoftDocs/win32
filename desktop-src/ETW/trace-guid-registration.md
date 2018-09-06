---
Description: The TRACE\_GUID\_REGISTRATION structure is used to register event trace classes.
ms.assetid: fc7b61fb-ef1c-48ec-8523-5f3114b5407a
title: TRACE_GUID_REGISTRATION structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRACE_GUID_REGISTRATION
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# TRACE\_GUID\_REGISTRATION structure

The **TRACE\_GUID\_REGISTRATION** structure is used to register event trace classes.

## Syntax


```C++
typedef struct _TRACE_GUID_REGISTRATION {
  LPCGUID Guid;
  HANDLE  RegHandle;
} TRACE_GUID_REGISTRATION;
```



## Members

<dl> <dt>

**Guid**
</dt> <dd>

Class GUID of an event trace class that you are registering.

</dd> <dt>

**RegHandle**
</dt> <dd>

Handle to the registered event trace class. The [**RegisterTraceGuids**](registertraceguids.md) function generates this value.

Use this handle when you call the [**CreateTraceInstanceId**](createtraceinstanceid.md) function and to set the **RegHandle** member of [**EVENT\_INSTANCE\_HEADER**](event-instance-header.md) when calling the [**TraceEventInstance**](traceeventinstance.md) function.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**CreateTraceInstanceId**](createtraceinstanceid.md)
</dt> <dt>

[**RegisterTraceGuids**](registertraceguids.md)
</dt> </dl>

 

 




