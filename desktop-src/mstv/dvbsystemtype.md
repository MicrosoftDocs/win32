---
title: DVBSystemType enumeration
description: Specifies the type of Digital Video Broadcasting (DVB) system supported in a tuning space.
ms.assetid: b547ace8-5c6d-43c1-bfa8-2dd162227730
keywords:
- DVBSystemType enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- DVBSystemType
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

# DVBSystemType enumeration

Specifies the type of Digital Video Broadcasting (DVB) system supported in a tuning space.

## Syntax


```C++
typedef enum DVBSystemType { 
  DVB_Cable        = 0,
  DVB_Terrestrial  = 1,
  DVB_Satellite    = 2
} DVBSystemType;
```



## Constants

<dl> <dt>

<span id="DVB_Cable"></span><span id="dvb_cable"></span><span id="DVB_CABLE"></span>**DVB\_Cable**
</dt> <dd>

Indicates a cable DVB system (DVB-c).

</dd> <dt>

<span id="DVB_Terrestrial"></span><span id="dvb_terrestrial"></span><span id="DVB_TERRESTRIAL"></span>**DVB\_Terrestrial**
</dt> <dd>

Indicates a terrestrial DVB system (DVB-T).

</dd> <dt>

<span id="DVB_Satellite"></span><span id="dvb_satellite"></span><span id="DVB_SATELLITE"></span>**DVB\_Satellite**
</dt> <dd>

Indicates a satellite DVB system (DVB-S).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDVBTuningSpace::get\_SystemType**](/windows/previous-versions/tuner/nf-tuner-idvbtuningspace-get_systemtype?branch=master)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





