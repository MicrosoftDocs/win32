---
title: SpectralInversion enumeration
description: Indicates the type of spectral inversion on Quadrature Phase Shift Keying (QPSK) in a Broadcast Driver Architecture (BDA) capture device.
ms.assetid: eaab17e3-8070-4f70-a31c-cd130edf1a4a
keywords:
- SpectralInversion enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- SpectralInversion
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- Bdatypes.h
api_type:
- HeaderDef
---

# SpectralInversion enumeration

Indicates the type of spectral inversion on Quadrature Phase Shift Keying (QPSK) in a Broadcast Driver Architecture (BDA) capture device.

## Syntax


```C++
typedef enum SpectralInversion { 
  BDA_SPECTRAL_INVERSION_NOT_SET      = -1,
  BDA_SPECTRAL_INVERSION_NOT_DEFINED  = 0,
  BDA_SPECTRAL_INVERSION_AUTOMATIC    = 1,
  BDA_SPECTRAL_INVERSION_NORMAL       = 2,
  BDA_SPECTRAL_INVERSION_INVERTED     = 3,
  BDA_SPECTRAL_INVERSION_MAX          = 4
} SpectralInversion;
```



## Constants

<dl> <dt>

<span id="BDA_SPECTRAL_INVERSION_NOT_SET"></span><span id="bda_spectral_inversion_not_set"></span>**BDA\_SPECTRAL\_INVERSION\_NOT\_SET**
</dt> <dd>

Spectral Inversion is not set.

</dd> <dt>

<span id="BDA_SPECTRAL_INVERSION_NOT_DEFINED"></span><span id="bda_spectral_inversion_not_defined"></span>**BDA\_SPECTRAL\_INVERSION\_NOT\_DEFINED**
</dt> <dd>

Spectral Inversion is not defined.

</dd> <dt>

<span id="BDA_SPECTRAL_INVERSION_AUTOMATIC"></span><span id="bda_spectral_inversion_automatic"></span>**BDA\_SPECTRAL\_INVERSION\_AUTOMATIC**
</dt> <dd>

Spectral Inversion is automatic.

</dd> <dt>

<span id="BDA_SPECTRAL_INVERSION_NORMAL"></span><span id="bda_spectral_inversion_normal"></span>**BDA\_SPECTRAL\_INVERSION\_NORMAL**
</dt> <dd>

Spectral Inversion is normal.

</dd> <dt>

<span id="BDA_SPECTRAL_INVERSION_INVERTED"></span><span id="bda_spectral_inversion_inverted"></span>**BDA\_SPECTRAL\_INVERSION\_INVERTED**
</dt> <dd>

Spectral Inversion is inverted.

</dd> <dt>

<span id="BDA_SPECTRAL_INVERSION_MAX"></span><span id="bda_spectral_inversion_max"></span>**BDA\_SPECTRAL\_INVERSION\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IDVBSTuningSpace::get\_SpectralInversion**](idvbstuningspace-get-spectralinversion.md)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





