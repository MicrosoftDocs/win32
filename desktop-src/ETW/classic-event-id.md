---
Description: Identifies the kernel event for which you want to enable call stack tracing.
ms.assetid: cbd77002-466b-40e6-85a5-cd872aef7d51
title: CLASSIC_EVENT_ID structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CLASSIC_EVENT_ID
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# CLASSIC\_EVENT\_ID structure

Identifies the kernel event for which you want to enable call stack tracing.

## Syntax


```C++
typedef struct _CLASSIC_EVENT_ID {
  GUID  EventGuid;
  UCHAR Type;
  UCHAR Reserved[7];
} CLASSIC_EVENT_ID, *PCLASSIC_EVENT_ID;
```



## Members

<dl> <dt>

**EventGuid**
</dt> <dd>

The GUID that identifies the kernel event class.

</dd> <dt>

**Type**
</dt> <dd>

The event type that identifies the event within the kernel event class to enable.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

To enable the [**read**](diskio-typegroup1.md) event type for [**disk IO**](diskio.md)events, set **GUID** to 3d6fa8d4-fe05-11d0-9dda-00c04fd7ba7c and **Type** to 10.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TraceSetInformation**](tracesetinformation.md)
</dt> </dl>

 

 




