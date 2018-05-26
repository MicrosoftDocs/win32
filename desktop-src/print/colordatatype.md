---
Description: The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content.
ms.assetid: ff7c9a81-3445-4a9e-aee3-2c63aafb0c82
title: COLORDATATYPE enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COLORDATATYPE enumeration

The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content.

## Syntax


```C++
typedef enum  { 
  COLOR_BYTE                = 1,
  COLOR_WORD                = 2,
  COLOR_FLOAT               = 3,
  COLOR_S2DOT13FIXED        = 4,
  COLOR_10b_R10G10B10A2     = 5,
  COLOR_10b_R10G10B10A2_XR  = 6,
  COLOR_FLOAT16             = 7
} COLORDATATYPE;
```



## Constants

<dl> <dt>

<span id="COLOR_BYTE"></span><span id="color_byte"></span>**COLOR\_BYTE**
</dt> <dd>

Color data is stored as 8 bits per channel, with a value from 0 to 255, inclusive.

</dd> <dt>

<span id="COLOR_WORD"></span><span id="color_word"></span>**COLOR\_WORD**
</dt> <dd>

Color data is stored as 16 bits per channel, with a value from 0 to 65535, inclusive.

</dd> <dt>

<span id="COLOR_FLOAT"></span><span id="color_float"></span>**COLOR\_FLOAT**
</dt> <dd>

Color data is stored as 32 bits value per channel, as defined by the IEEE 32-bit floating point standard.

</dd> <dt>

<span id="COLOR_S2DOT13FIXED"></span><span id="color_s2dot13fixed"></span>**COLOR\_S2DOT13FIXED**
</dt> <dd>

Color data is stored as 16 bits per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.

</dd> <dt>

<span id="COLOR_10b_R10G10B10A2"></span><span id="color_10b_r10g10b10a2"></span><span id="COLOR_10B_R10G10B10A2"></span>**COLOR\_10b\_R10G10B10A2**
</dt> <dd>

Packed WORD per channel. data range \[0, 1\]

</dd> <dt>

<span id="COLOR_10b_R10G10B10A2_XR"></span><span id="color_10b_r10g10b10a2_xr"></span><span id="COLOR_10B_R10G10B10A2_XR"></span>**COLOR\_10b\_R10G10B10A2\_XR**
</dt> <dd>

Packed extended range WORD per channel. data range \[-1, 3\]

</dd> <dt>

<span id="COLOR_FLOAT16"></span><span id="color_float16"></span>**COLOR\_FLOAT16**
</dt> <dd>

FLOAT16 per channel.

</dd> </dl>

## Remarks

The PCOLORDATATYPE and LPCOLORDATATYPE data types are defined as pointers to this enumeration:


```
typedef COLORDATATYPE *PCOLORDATATYPE, *LPCOLORDATATYPE;
```



## Requirements



|                    |                                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| Version<br/> | Included in Windows Vista and later.<br/>                                  |
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COLORDATATYPE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




