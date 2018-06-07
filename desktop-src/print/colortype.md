---
Description: The values of the COLORTYPE enumeration are used by WCS functions to indicate the format of vector content. Most values have equivalent structures that are contained in the ICM COLOR structure (described in the Microsoft Windows SDK documentation).
ms.assetid: aa7d8d32-7bbe-4091-82a2-32ade463dd9e
title: COLORTYPE enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# COLORTYPE enumeration

The values of the COLORTYPE enumeration are used by WCS functions to indicate the format of vector content. Most values have equivalent structures that are contained in the ICM COLOR structure (described in the Microsoft Windows SDK documentation).

## Syntax


```C++
typedef enum  { 
  COLOR_GRAY       = 1,
  COLOR_RGB        = 2,
  COLOR_XYZ        = 3,
  COLOR_Yxy        = 4,
  COLOR_Lab        = 5,
  COLOR_3_CHANNEL  = 6,
  COLOR_CMYK       = 7,
  COLOR_5_CHANNEL  = 8,
  COLOR_6_CHANNEL  = 9,
  COLOR_7_CHANNEL  = 10,
  COLOR_8_CHANNEL  = 11,
  COLOR_NAMED      = 12
} COLORTYPE;
```



## Constants

<dl> <dt>

<span id="COLOR_GRAY"></span><span id="color_gray"></span>**COLOR\_GRAY**
</dt> <dd>

Specifies a 16-bit gray-scale pixel value. Correlates to the ICM GRAYCOLOR.

</dd> <dt>

<span id="COLOR_RGB"></span><span id="color_rgb"></span>**COLOR\_RGB**
</dt> <dd>

Specifies a 48-bit RGB pixel value. Correlates to the ICM RGBCOLOR structure.

</dd> <dt>

<span id="COLOR_XYZ"></span><span id="color_xyz"></span>**COLOR\_XYZ**
</dt> <dd>

Specifies a 48-bit CIEXYZ pixel value. Correlates to the ICM XYZCOLOR structure.

</dd> <dt>

<span id="COLOR_Yxy"></span><span id="color_yxy"></span><span id="COLOR_YXY"></span>**COLOR\_Yxy**
</dt> <dd>

Specifies a 48-bit CIE Yxy pixel value. Correlates to the ICM YxyCOLOR structure.

</dd> <dt>

<span id="COLOR_Lab"></span><span id="color_lab"></span><span id="COLOR_LAB"></span>**COLOR\_Lab**
</dt> <dd>

Specifies a 48-bit CIELAB pixel value. Correlates to the ICM LabCOLOR structure.

</dd> <dt>

<span id="COLOR_3_CHANNEL"></span><span id="color_3_channel"></span>**COLOR\_3\_CHANNEL**
</dt> <dd>

Specifies a 48-bit generic three-channel pixel value. Correlates to the ICM GENERIC3CHANNEL structure.

</dd> <dt>

<span id="COLOR_CMYK"></span><span id="color_cmyk"></span>**COLOR\_CMYK**
</dt> <dd>

Specifies a 48-bit CMYK pixel value. Correlates to the ICM CMYKCOLOR structure.

</dd> <dt>

<span id="COLOR_5_CHANNEL"></span><span id="color_5_channel"></span>**COLOR\_5\_CHANNEL**
</dt> <dd>

Specifies a 64-bit generic five-channel pixel value.

</dd> <dt>

<span id="COLOR_6_CHANNEL"></span><span id="color_6_channel"></span>**COLOR\_6\_CHANNEL**
</dt> <dd>

Specifies a 64-bit generic six-channel pixel value.

</dd> <dt>

<span id="COLOR_7_CHANNEL"></span><span id="color_7_channel"></span>**COLOR\_7\_CHANNEL**
</dt> <dd>

Specifies a 64-bit generic seven-channel pixel value.

</dd> <dt>

<span id="COLOR_8_CHANNEL"></span><span id="color_8_channel"></span>**COLOR\_8\_CHANNEL**
</dt> <dd>

Specifies a 64-bit generic eight-channel pixel value.

</dd> <dt>

<span id="COLOR_NAMED"></span><span id="color_named"></span>**COLOR\_NAMED**
</dt> <dd>

Specifies a 32-bit named color-indexed pixel value. Correlates to the ICM NAMEDCOLOR structure.

</dd> </dl>

## Remarks

In addition to managing the common two, three, and four channel color spaces, ICM 2.0 and WCS are able to perform color management with device profiles that contain five through eight color channels. ICM 2.0 and WCS are also able to use named color spaces. When five, six, seven, or eight color channels are used, the provider of the device profile is free to determine what the color channels represent. The same is true of named color spaces. ICM 2.0 and WCS are able to manage these color spaces as long as there is a mapping in the device profile that maps the channels or the name space to the Profile Connection Space (PCS). The device profile must also contain a mapping from the PCS into the five, six, seven, or eight channel spaces, or into the named color space.

The PCOLORTYPE and LPCOLORTYPE data types are defined as pointers to this enumeration:


```
typedef COLORTYPE *PCOLORTYPE, *LPCOLORTYPE;
```



## Requirements



|                    |                                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| Version<br/> | Included in Windows Vista and later.<br/>                                  |
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COLORTYPE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




