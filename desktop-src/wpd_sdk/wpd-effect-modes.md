---
description: The WPD\_EFFECT\_MODES enumeration type describes various visual effects that can be applied to an image.
ms.assetid: 7624fccb-e416-4db4-978e-410c4c236328
title: WPD_EFFECT_MODES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_EFFECT_MODES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_EFFECT\_MODES enumeration

The **WPD\_EFFECT\_MODES** enumeration type describes various visual effects that can be applied to an image.

## Syntax


```C++
typedef enum WPD_EFFECT_MODES { 
  WPD_EFFECT_MODE_UNDEFINED        = 0,
  WPD_EFFECT_MODE_COLOR            = 1,
  WPD_EFFECT_MODE_BLACK_AND_WHITE  = 2,
  WPD_EFFECT_MODE_SEPIA            = 3
} ;
```



## Constants

<dl> <dt>

<span id="WPD_EFFECT_MODE_UNDEFINED"></span><span id="wpd_effect_mode_undefined"></span>**WPD\_EFFECT\_MODE\_UNDEFINED**
</dt> <dd>

No effect has been specified.

</dd> <dt>

<span id="WPD_EFFECT_MODE_COLOR"></span><span id="wpd_effect_mode_color"></span>**WPD\_EFFECT\_MODE\_COLOR**
</dt> <dd>

The image should be color.

</dd> <dt>

<span id="WPD_EFFECT_MODE_BLACK_AND_WHITE"></span><span id="wpd_effect_mode_black_and_white"></span>**WPD\_EFFECT\_MODE\_BLACK\_AND\_WHITE**
</dt> <dd>

The image should be black and white.

</dd> <dt>

<span id="WPD_EFFECT_MODE_SEPIA"></span><span id="wpd_effect_mode_sepia"></span>**WPD\_EFFECT\_MODE\_SEPIA**
</dt> <dd>

The image should be sepia.

</dd> </dl>

## Remarks

This enumeration is used by the [WPD\_STILL\_IMAGE\_EFFECT\_MODE](still-image-properties.md) property.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




