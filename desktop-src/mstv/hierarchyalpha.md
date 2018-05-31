---
title: HierarchyAlpha enumeration
description: Specifies the hierarchy alpha on a Digital Video Broadcasting-Terrestrial (DVB-T) system.
ms.assetid: e2804158-ffe3-4a9b-af6f-b3e4a3d5c1ea
keywords:
- HierarchyAlpha enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- HierarchyAlpha
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

# HierarchyAlpha enumeration

Specifies the hierarchy alpha on a Digital Video Broadcasting-Terrestrial (DVB-T) system.

## Syntax


```C++
typedef enum HierarchyAlpha { 
  BDA_HALPHA_NOT_SET      = -1,
  BDA_HALPHA_NOT_DEFINED  = 0,
  BDA_HALPHA_1            = 1,
  BDA_HALPHA_2            = 2,
  BDA_HALPHA_4            = 3,
  BDA_HALPHA_MAX          = 4
} HierarchyAlpha;
```



## Constants

<dl> <dt>

<span id="BDA_HALPHA_NOT_SET"></span><span id="bda_halpha_not_set"></span>**BDA\_HALPHA\_NOT\_SET**
</dt> <dd>

The hierarchy alpha is not set.

</dd> <dt>

<span id="BDA_HALPHA_NOT_DEFINED"></span><span id="bda_halpha_not_defined"></span>**BDA\_HALPHA\_NOT\_DEFINED**
</dt> <dd>

The hierarchy alpha is not defined.

</dd> <dt>

<span id="BDA_HALPHA_1"></span><span id="bda_halpha_1"></span>**BDA\_HALPHA\_1**
</dt> <dd>

The hierarchy alpha is 1.

</dd> <dt>

<span id="BDA_HALPHA_2"></span><span id="bda_halpha_2"></span>**BDA\_HALPHA\_2**
</dt> <dd>

The hierarchy alpha is 2.

</dd> <dt>

<span id="BDA_HALPHA_4"></span><span id="bda_halpha_4"></span>**BDA\_HALPHA\_4**
</dt> <dd>

The hierarchy alpha is 4.

</dd> <dt>

<span id="BDA_HALPHA_MAX"></span><span id="bda_halpha_max"></span>**BDA\_HALPHA\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDVBTLocator::get\_HAlpha**](/previous-versions/windows/desktop/api/tuner/nf-tuner-idvbtlocator-get_halpha)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





