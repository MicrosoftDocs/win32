---
title: COLORDATATYPE enumeration
description: Used by WCS functions to indicate the data type of vector content.
ms.assetid: '001001c2-9a34-4d70-937d-befa0fc2118c'
keywords: ["COLORDATATYPE enumeration Windows Color System", "PCOLORDATATYPE enumeration pointer Windows Color System", "LPCOLORDATATYPE enumeration pointer Windows Color System"]
topic_type:
- apiref
api_name:
- COLORDATATYPE
api_location:
- Icm.h
api_type:
- HeaderDef
---

# COLORDATATYPE enumeration

Used by WCS functions to indicate the data type of vector content.

## Syntax


```C++
typedef enum tagCOLORDATATYPE { 
  COLOR_BYTE                = 1,
  COLOR_WORD,
  COLOR_FLOAT,
  COLOR_S2DOT13FIXED,
  COLOR_10b_R10G10B10A2,
  COLOR_10b_R10G10B10A2_XR
} COLORDATATYPE, *PCOLORDATATYPE, *LPCOLORDATATYPE;
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

Color data is stored as 10 bits per channel. The two most significant bits are alpha.

</dd> <dt>

<span id="COLOR_10b_R10G10B10A2_XR"></span><span id="color_10b_r10g10b10a2_xr"></span><span id="COLOR_10B_R10G10B10A2_XR"></span>**COLOR\_10b\_R10G10B10A2\_XR**
</dt> <dd>

Color data is stored as 10 bits per channel, 32 bits per pixel. The 10 bits of each color channel are 2.8 fixed point with a -0.75 bias, giving a range of \[-0.76 .. 1.25\]. This range corresponds to \[-0.5 .. 1.5\] in a gamma = 1 space. The two most significant bits are preserved for alpha.

This uses an extended range (XR) sRGB color space. It has the same RGB primaries, white point, and gamma as sRGB.

</dd> </dl>

## Remarks

The PCOLORDATATYPE and LPCOLORDATATYPE data types are defined as pointers to the **COLORDATATYPE** enumeration:

`typedef COLORDATATYPE *PCOLORDATATYPE, *LPCOLORDATATYPE;`

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



 

 





