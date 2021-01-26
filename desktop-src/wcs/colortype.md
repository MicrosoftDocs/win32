---
title: COLORTYPE enumeration
description: The values of the COLORTYPE enumeration are used by several WCS functions. Variables of type COLOR are defined in the color spaces enumerated by the COLORTYPE enumeration.
ms.assetid: 9735e4e5-362b-4542-9285-887279cc6499
keywords:
- COLORTYPE enumeration Windows Color System
- PCOLORTYPE enumeration pointer Windows Color System
- LPCOLORTYPE enumeration pointer Windows Color System
topic_type:
- apiref
api_name:
- COLORTYPE
api_location:
- Icm.h
api_type:
- HeaderDef
ms.localizationpriority: high
ms.topic: enumeration
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# COLORTYPE enumeration

The values of the **COLORTYPE** enumeration are used by several WCS functions. Variables of type **COLOR** are defined in the color spaces enumerated by the **COLORTYPE** enumeration.

## Syntax


```C++
typedef enum tagCOLORTYPE { 
  COLOR_GRAY       = 1,
  COLOR_RGB,
  COLOR_XYZ,
  COLOR_Yxy,
  COLOR_Lab,
  COLOR_3_CHANNEL,
  COLOR_CMYK,
  COLOR_5_CHANNEL,
  COLOR_6_CHANNEL,
  COLOR_7_CHANNEL,
  COLOR_8_CHANNEL,
  COLOR_NAMED
} COLORTYPE, *PCOLORTYPE, *LPCOLORTYPE;
```



## Constants

<dl> <dt>

<span id="COLOR_GRAY"></span><span id="color_gray"></span>**COLOR\_GRAY**
</dt> <dd>

The **COLOR** is in the GRAYCOLOR color space.

</dd> <dt>

<span id="COLOR_RGB"></span><span id="color_rgb"></span>**COLOR\_RGB**
</dt> <dd>

The **COLOR** is in the RGBCOLOR color space.

</dd> <dt>

<span id="COLOR_XYZ"></span><span id="color_xyz"></span>**COLOR\_XYZ**
</dt> <dd>

The **COLOR** is in the XYZCOLOR color space.

</dd> <dt>

<span id="COLOR_Yxy"></span><span id="color_yxy"></span><span id="COLOR_YXY"></span>**COLOR\_Yxy**
</dt> <dd>

The **COLOR** is in the YxyCOLOR color space.

</dd> <dt>

<span id="COLOR_Lab"></span><span id="color_lab"></span><span id="COLOR_LAB"></span>**COLOR\_Lab**
</dt> <dd>

The **COLOR** is in the LabCOLOR color space.

</dd> <dt>

<span id="COLOR_3_CHANNEL"></span><span id="color_3_channel"></span>**COLOR\_3\_CHANNEL**
</dt> <dd>

The **COLOR** is in the GENERIC3CHANNEL color space.

</dd> <dt>

<span id="COLOR_CMYK"></span><span id="color_cmyk"></span>**COLOR\_CMYK**
</dt> <dd>

The **COLOR** is in the CMYKCOLOR color space.

</dd> <dt>

<span id="COLOR_5_CHANNEL"></span><span id="color_5_channel"></span>**COLOR\_5\_CHANNEL**
</dt> <dd>

The **COLOR** is in a five channel color space.

</dd> <dt>

<span id="COLOR_6_CHANNEL"></span><span id="color_6_channel"></span>**COLOR\_6\_CHANNEL**
</dt> <dd>

The **COLOR** is in a six channel color space.

</dd> <dt>

<span id="COLOR_7_CHANNEL"></span><span id="color_7_channel"></span>**COLOR\_7\_CHANNEL**
</dt> <dd>

The **COLOR** is in a seven channel color space.

</dd> <dt>

<span id="COLOR_8_CHANNEL"></span><span id="color_8_channel"></span>**COLOR\_8\_CHANNEL**
</dt> <dd>

The **COLOR** is in an eight channel color space.

</dd> <dt>

<span id="COLOR_NAMED"></span><span id="color_named"></span>**COLOR\_NAMED**
</dt> <dd>

The **COLOR** is in a named color space.

</dd> </dl>

## Remarks

In addition to managing the common two, three, and four channel color spaces, WCS 1.0 is able to perform color management with device profiles that contain five through eight [color channels](c.md). It is also able to use named color spaces. When five, six, seven, or eight color channels are used, the provider of the device profile is free to determine what the color channels represent. The same is true of named color spaces. WCS 1.0 is able to manage these color spaces as long as there is a mapping in the device profile that maps the channels or the name space into the [PCS](p.md). The device profile must also contain a mapping from the PCS into the five, size, seven, or eight channel space, or into the named color space.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



 

 





