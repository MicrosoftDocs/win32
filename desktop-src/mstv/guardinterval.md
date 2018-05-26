---
title: GuardInterval enumeration
description: Specifies the guard interval on a Digital Video Broadcasting-Terrestrial (DVB-T) system.
ms.assetid: a3ff1c61-f80d-40f2-a22f-069f0690fb1b
keywords:
- GuardInterval enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- GuardInterval
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GuardInterval enumeration

Specifies the guard interval on a Digital Video Broadcasting-Terrestrial (DVB-T) system.

## Syntax


```C++
typedef enum GuardInterval { 
  BDA_GUARD_NOT_SET      = -1,
  BDA_GUARD_NOT_DEFINED  = 0,
  BDA_GUARD_1_32         = 1,
  BDA_GUARD_1_16         = 2,
  BDA_GUARD_1_8          = 3,
  BDA_GUARD_1_4          = 4,
  BDA_GUARD_MAX          = 5
} GuardInterval;
```



## Constants

<dl> <dt>

<span id="BDA_GUARD_NOT_SET"></span><span id="bda_guard_not_set"></span>**BDA\_GUARD\_NOT\_SET**
</dt> <dd>

The guard interval is not set.

</dd> <dt>

<span id="BDA_GUARD_NOT_DEFINED"></span><span id="bda_guard_not_defined"></span>**BDA\_GUARD\_NOT\_DEFINED**
</dt> <dd>

The guard interval is not defined.

</dd> <dt>

<span id="BDA_GUARD_1_32"></span><span id="bda_guard_1_32"></span>**BDA\_GUARD\_1\_32**
</dt> <dd>

The guard interval is 1/32.

</dd> <dt>

<span id="BDA_GUARD_1_16"></span><span id="bda_guard_1_16"></span>**BDA\_GUARD\_1\_16**
</dt> <dd>

The guard interval is 1/16.

</dd> <dt>

<span id="BDA_GUARD_1_8"></span><span id="bda_guard_1_8"></span>**BDA\_GUARD\_1\_8**
</dt> <dd>

The guard interval is 1/8.

</dd> <dt>

<span id="BDA_GUARD_1_4"></span><span id="bda_guard_1_4"></span>**BDA\_GUARD\_1\_4**
</dt> <dd>

The guard interval is 1/4.

</dd> <dt>

<span id="BDA_GUARD_MAX"></span><span id="bda_guard_max"></span>**BDA\_GUARD\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDVBTLocator::get\_Guard**](/windows/previous-versions/tuner/nf-tuner-idvbtlocator-get_guard?branch=master)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





