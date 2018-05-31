---
title: Pilot enumeration
description: Specifies the pilot mode for Digital Video Broadcasting - S2 (DVB-S2).
ms.assetid: c24b7b56-b6f4-44d7-a2d3-be7d12eb2335
keywords:
- Pilot enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- Pilot
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# Pilot enumeration

Specifies the pilot mode for Digital Video Broadcasting - S2 (DVB-S2).

## Syntax


```C++
typedef enum Pilot { 
  BDA_PILOT_NOT_SET      = -1,
  BDA_PILOT_NOT_DEFINED  = 0,
  BDA_PILOT_OFF          = 1,
  BDA_PILOT_ON,
  BDA_PILOT_MAX
} Pilot;
```



## Constants

<dl> <dt>

<span id="BDA_PILOT_NOT_SET"></span><span id="bda_pilot_not_set"></span>**BDA\_PILOT\_NOT\_SET**
</dt> <dd>

The pilot mode is not set.

</dd> <dt>

<span id="BDA_PILOT_NOT_DEFINED"></span><span id="bda_pilot_not_defined"></span>**BDA\_PILOT\_NOT\_DEFINED**
</dt> <dd>

The pilot mode is not defined.

</dd> <dt>

<span id="BDA_PILOT_OFF"></span><span id="bda_pilot_off"></span>**BDA\_PILOT\_OFF**
</dt> <dd>

Pilot off (DVB-S2 only).

</dd> <dt>

<span id="BDA_PILOT_ON"></span><span id="bda_pilot_on"></span>**BDA\_PILOT\_ON**
</dt> <dd>

Pilot on (DVB-S2 only).

</dd> <dt>

<span id="BDA_PILOT_MAX"></span><span id="bda_pilot_max"></span>**BDA\_PILOT\_MAX**
</dt> <dd>

Reserved. Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



 

 





