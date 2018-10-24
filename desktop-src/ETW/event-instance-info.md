---
Description: The EVENT\_INSTANCE\_INFO structure maps a unique transaction identifier to a registered event trace class.
ms.assetid: 83a3802c-b992-43a2-a98a-bdee2ecfef24
title: EVENT_INSTANCE_INFO structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EVENT_INSTANCE_INFO
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# EVENT\_INSTANCE\_INFO structure

The **EVENT\_INSTANCE\_INFO** structure maps a unique transaction identifier to a registered event trace class.

## Syntax


```C++
typedef struct EVENT_INSTANCE_INFO {
  HANDLE RegHandle;
  ULONG  InstanceId;
} EVENT_INSTANCE_INFO, *PEVENT_INSTANCE_INFO;
```



## Members

<dl> <dt>

**RegHandle**
</dt> <dd>

Handle to a registered event trace class.

</dd> <dt>

**InstanceId**
</dt> <dd>

Unique transaction identifier that maps an event to a specific transaction.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**CreateTraceInstanceId**](createtraceinstanceid.md)
</dt> <dt>

[**TraceEventInstance**](traceeventinstance.md)
</dt> </dl>

 

 




