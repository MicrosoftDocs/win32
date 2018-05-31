---
title: RollOff enumeration
description: Specifies the roll-off factor.
ms.assetid: 4b1cd08a-50fd-48e9-9e97-8460e6c990c1
keywords:
- RollOff enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- RollOff
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# RollOff enumeration

Specifies the roll-off factor.

## Syntax


```C++
typedef enum RollOff { 
  BDA_ROLL_OFF_NOT_SET      = -1,
  BDA_ROLL_OFF_NOT_DEFINED  = 0,
  BDA_ROLL_OFF_20           = 1,
  BDA_ROLL_OFF_25,
  BDA_ROLL_OFF_35,
  BDA_ROLL_OFF_MAX
} RollOff;
```



## Constants

<dl> <dt>

<span id="BDA_ROLL_OFF_NOT_SET"></span><span id="bda_roll_off_not_set"></span>**BDA\_ROLL\_OFF\_NOT\_SET**
</dt> <dd>

The roll-off factor is not set.

</dd> <dt>

<span id="BDA_ROLL_OFF_NOT_DEFINED"></span><span id="bda_roll_off_not_defined"></span>**BDA\_ROLL\_OFF\_NOT\_DEFINED**
</dt> <dd>

The roll-off factor is not defined.

</dd> <dt>

<span id="BDA_ROLL_OFF_20"></span><span id="bda_roll_off_20"></span>**BDA\_ROLL\_OFF\_20**
</dt> <dd>

20 percent roll-off factor (Digital Video Broadcasting - S2 (DVB-S2) only).

</dd> <dt>

<span id="BDA_ROLL_OFF_25"></span><span id="bda_roll_off_25"></span>**BDA\_ROLL\_OFF\_25**
</dt> <dd>

25 percent roll-off factor (DVB-S2 only).

</dd> <dt>

<span id="BDA_ROLL_OFF_35"></span><span id="bda_roll_off_35"></span>**BDA\_ROLL\_OFF\_35**
</dt> <dd>

35 percent roll-off factor (DVB-S2 only).

</dd> <dt>

<span id="BDA_ROLL_OFF_MAX"></span><span id="bda_roll_off_max"></span>**BDA\_ROLL\_OFF\_MAX**
</dt> <dd>

Reserved. Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



 

 





