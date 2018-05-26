---
title: PIDListSpanningEvent structure
description: Contains a list of packet identifiers (PIDs).
ms.assetid: 7c2a8e24-0919-4fe6-9a31-a1d4b1d119ed
keywords:
- PIDListSpanningEvent structure Microsoft TV Technologies
topic_type:
- apiref
api_name:
- PIDListSpanningEvent
api_location:
- bdamedia.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PIDListSpanningEvent structure

Contains a list of packet identifiers (PIDs).

## Syntax


```C++
typedef struct _PIDListSpanningEvent {
  WORD  wPIDCount;
  ULONG pulPIDs[1];
} PIDListSpanningEvent;
```



## Members

<dl> <dt>

**wPIDCount**
</dt> <dd>

The number of elements in the **pulPIDs** array.

</dd> <dt>

**pulPIDs**
</dt> <dd>

An array of PIDs. The array might be larger than the size given in the structure declaration. Use the value of **wPIDCount** to determine the size.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





