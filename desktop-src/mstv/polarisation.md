---
title: Polarisation enumeration
description: Specifies the polarization type.
ms.assetid: adb9d7b6-5876-4b3f-9d82-f5e740feb1eb
keywords:
- Polarisation enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- Polarisation
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

# Polarisation enumeration

Specifies the polarization type.

## Syntax


```C++
typedef enum Polarisation { 
  BDA_POLARISATION_NOT_SET      = -1,
  BDA_POLARISATION_NOT_DEFINED  = 0,
  BDA_POLARISATION_LINEAR_H     = 1,
  BDA_POLARISATION_LINEAR_V     = 2,
  BDA_POLARISATION_CIRCULAR_L   = 3,
  BDA_POLARISATION_CIRCULAR_R   = 4,
  BDA_POLARISATION_MAX          = 5
} Polarisation;
```



## Constants

<dl> <dt>

<span id="BDA_POLARISATION_NOT_SET"></span><span id="bda_polarisation_not_set"></span>**BDA\_POLARISATION\_NOT\_SET**
</dt> <dd>

Polarization not set.

</dd> <dt>

<span id="BDA_POLARISATION_NOT_DEFINED"></span><span id="bda_polarisation_not_defined"></span>**BDA\_POLARISATION\_NOT\_DEFINED**
</dt> <dd>

Polarization not defined.

</dd> <dt>

<span id="BDA_POLARISATION_LINEAR_H"></span><span id="bda_polarisation_linear_h"></span>**BDA\_POLARISATION\_LINEAR\_H**
</dt> <dd>

Linear horizontal polarization.

</dd> <dt>

<span id="BDA_POLARISATION_LINEAR_V"></span><span id="bda_polarisation_linear_v"></span>**BDA\_POLARISATION\_LINEAR\_V**
</dt> <dd>

Linear vertical polarization.

</dd> <dt>

<span id="BDA_POLARISATION_CIRCULAR_L"></span><span id="bda_polarisation_circular_l"></span>**BDA\_POLARISATION\_CIRCULAR\_L**
</dt> <dd>

Circular left polarization.

</dd> <dt>

<span id="BDA_POLARISATION_CIRCULAR_R"></span><span id="bda_polarisation_circular_r"></span>**BDA\_POLARISATION\_CIRCULAR\_R**
</dt> <dd>

Circular right polarization.

</dd> <dt>

<span id="BDA_POLARISATION_MAX"></span><span id="bda_polarisation_max"></span>**BDA\_POLARISATION\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDVBSLocator::get\_SignalPolarisation**](/windows/previous-versions/tuner/nf-tuner-idvbslocator-get_signalpolarisation?branch=master)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





