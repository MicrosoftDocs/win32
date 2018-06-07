---
Description: The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.
ms.assetid: 1c29bf1e-e785-48ab-aa2c-3665fd5c0ab0
title: BMFORMAT enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# BMFORMAT enumeration

The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista.

## Syntax


```C++
typedef enum  { 
  BM_x555RGB              = 0x0000,
  BM_x555XYZ              = 0x0101,
  BM_x555Yxy              = 0x102,
  BM_x555Lab              = 0x103,
  BM_x555G3CH             = 0x104,
  BM_RGBTRIPLETS          = 0x0002,
  BM_BGRTRIPLETS          = 0x0004,
  BM_XYZTRIPLETS          = 0x0201,
  BM_YxyTRIPLETS          = 0x202,
  BM_LabTRIPLETS          = 0x203,
  BM_G3CHTRIPLETS         = 0x204,
  BM_5CHANNEL             = 0x205,
  BM_6CHANNEL             = 0x206,
  BM_7CHANNEL             = 0x207,
  BM_8CHANNEL             = 0x208,
  BM_GRAY                 = 0x209,
  BM_xRGBQUADS            = 0x0008,
  BM_xBGRQUADS            = 0x0010,
  BM_xG3CHQUADS           = 0x0304,
  BM_KYMCQUADS            = 0x305,
  BM_CMYKQUADS            = 0x0020,
  BM_10b_RGB              = 0x0009,
  BM_10b_XYZ              = 0x0401,
  BM_10b_Yxy              = 0x402,
  BM_10b_Lab              = 0x403,
  BM_10b_G3CH             = 0x404,
  BM_NAMED_INDEX          = 0x405,
  BM_16b_RGB              = 0x000A,
  BM_16b_XYZ              = 0x0501,
  BM_16b_Yxy              = 0x502,
  BM_16b_Lab              = 0x503,
  BM_16b_G3CH             = 0x504,
  BM_16b_GRAY             = 0x505,
  BM_565RGB               = 0x0001,
  BM_32b_scRGB            = 0x0601,
  BM_32b_scARGB           = 0x0602,
  BM_S2DOT13FIXED_scRGB   = 0x0603,
  BM_S2DOT13FIXED_scARGB  = 0x0604,
  BM_R10G10B10A2          = 0x0701,
  BM_R10G10B10A2_XR       = 0x0702,
  BM_R16G16B16A16_FLOAT   = 0x0703 
} BMFORMAT;
```



## Constants

<dl> <dt>

<span id="BM_x555RGB"></span><span id="bm_x555rgb"></span><span id="BM_X555RGB"></span>**BM\_x555RGB**
</dt> <dd>

16 bits per pixel. RGB color space. 5 bits per channel. The most significant bit is ignored.

</dd> <dt>

<span id="BM_x555XYZ"></span><span id="bm_x555xyz"></span><span id="BM_X555XYZ"></span>**BM\_x555XYZ**
</dt> <dd>

16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.

</dd> <dt>

<span id="BM_x555Yxy"></span><span id="bm_x555yxy"></span><span id="BM_X555YXY"></span>**BM\_x555Yxy**
</dt> <dd>

16 bits per pixel. Yxy color space. 5 bits per channel. The most significant bit is ignored.

</dd> <dt>

<span id="BM_x555Lab"></span><span id="bm_x555lab"></span><span id="BM_X555LAB"></span>**BM\_x555Lab**
</dt> <dd>

BM\_x555G3CH

</dd> <dt>

<span id="BM_x555G3CH"></span><span id="bm_x555g3ch"></span><span id="BM_X555G3CH"></span>**BM\_x555G3CH**
</dt> <dd>

16 bits per pixel. G3CH color space. 5 bits per channel. The most significant bit is ignored.

</dd> <dt>

<span id="BM_RGBTRIPLETS"></span><span id="bm_rgbtriplets"></span>**BM\_RGBTRIPLETS**
</dt> <dd>

24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.

</dd> <dt>

<span id="BM_BGRTRIPLETS"></span><span id="bm_bgrtriplets"></span>**BM\_BGRTRIPLETS**
</dt> <dd>

24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.

</dd> <dt>

<span id="BM_XYZTRIPLETS"></span><span id="bm_xyztriplets"></span>**BM\_XYZTRIPLETS**
</dt> <dd>

24 bits per pixel maximum. For three channel colors, such as red, green, and blue, the total size is 24 bits per pixel. For single channel colors, such as gray, the total size is 8 bits per pixel.

</dd> <dt>

<span id="BM_YxyTRIPLETS"></span><span id="bm_yxytriplets"></span><span id="BM_YXYTRIPLETS"></span>**BM\_YxyTRIPLETS**
</dt> <dd>

24 bits per pixel maximum. For three channel, Y, x, and y values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.

</dd> <dt>

<span id="BM_LabTRIPLETS"></span><span id="bm_labtriplets"></span><span id="BM_LABTRIPLETS"></span>**BM\_LabTRIPLETS**
</dt> <dd>

24 bits per pixel maximum. For three channel, L, a, and b values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.

</dd> <dt>

<span id="BM_G3CHTRIPLETS"></span><span id="bm_g3chtriplets"></span>**BM\_G3CHTRIPLETS**
</dt> <dd>

24 bits per pixel maximum. For three channel values, the total size is 24 bits per pixel. For single channel gray scale, the total size is 8 bits per pixel.

</dd> <dt>

<span id="BM_5CHANNEL"></span><span id="bm_5channel"></span>**BM\_5CHANNEL**
</dt> <dd>

40 bits per pixel. 8 bits apiece are used for each channel.

</dd> <dt>

<span id="BM_6CHANNEL"></span><span id="bm_6channel"></span>**BM\_6CHANNEL**
</dt> <dd></dd> <dt>

<span id="BM_7CHANNEL"></span><span id="bm_7channel"></span>**BM\_7CHANNEL**
</dt> <dd>

56 bits per pixel. 8 bits apiece are used for each channel.

</dd> <dt>

<span id="BM_8CHANNEL"></span><span id="bm_8channel"></span>**BM\_8CHANNEL**
</dt> <dd>

64 bits per pixel. 8 bits apiece are used for each channel.

</dd> <dt>

<span id="BM_GRAY"></span><span id="bm_gray"></span>**BM\_GRAY**
</dt> <dd>

32 bits per pixel. Only the 8 bit gray-scale value is used.

</dd> <dt>

<span id="BM_xRGBQUADS"></span><span id="bm_xrgbquads"></span><span id="BM_XRGBQUADS"></span>**BM\_xRGBQUADS**
</dt> <dd>

32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.

</dd> <dt>

<span id="BM_xBGRQUADS"></span><span id="bm_xbgrquads"></span><span id="BM_XBGRQUADS"></span>**BM\_xBGRQUADS**
</dt> <dd>

32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.

</dd> <dt>

<span id="BM_xG3CHQUADS"></span><span id="bm_xg3chquads"></span><span id="BM_XG3CHQUADS"></span>**BM\_xG3CHQUADS**
</dt> <dd>

32 bits per pixel. 8 bits are used for each color channel. The most significant byte is ignored.

</dd> <dt>

<span id="BM_KYMCQUADS"></span><span id="bm_kymcquads"></span>**BM\_KYMCQUADS**
</dt> <dd>

32 bits per pixel. 8 bits are used for each color channel.

</dd> <dt>

<span id="BM_CMYKQUADS"></span><span id="bm_cmykquads"></span>**BM\_CMYKQUADS**
</dt> <dd>

32 bits per pixel. 8 bits are used for each color channel.

</dd> <dt>

<span id="BM_10b_RGB"></span><span id="bm_10b_rgb"></span><span id="BM_10B_RGB"></span>**BM\_10b\_RGB**
</dt> <dd>

32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.

</dd> <dt>

<span id="BM_10b_XYZ"></span><span id="bm_10b_xyz"></span><span id="BM_10B_XYZ"></span>**BM\_10b\_XYZ**
</dt> <dd>

32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.

</dd> <dt>

<span id="BM_10b_Yxy"></span><span id="bm_10b_yxy"></span><span id="BM_10B_YXY"></span>**BM\_10b\_Yxy**
</dt> <dd>

32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.

</dd> <dt>

<span id="BM_10b_Lab"></span><span id="bm_10b_lab"></span><span id="BM_10B_LAB"></span>**BM\_10b\_Lab**
</dt> <dd>

32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.

</dd> <dt>

<span id="BM_10b_G3CH"></span><span id="bm_10b_g3ch"></span><span id="BM_10B_G3CH"></span>**BM\_10b\_G3CH**
</dt> <dd>

32 bits per pixel. 10 bits are used for each color channel. The 2 most significant bits are ignored.

</dd> <dt>

<span id="BM_NAMED_INDEX"></span><span id="bm_named_index"></span>**BM\_NAMED\_INDEX**
</dt> <dd>

32 bits per pixel. Named color indices. Index numbering begins at one.

</dd> <dt>

<span id="BM_16b_RGB"></span><span id="bm_16b_rgb"></span><span id="BM_16B_RGB"></span>**BM\_16b\_RGB**
</dt> <dd>

64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.

</dd> <dt>

<span id="BM_16b_XYZ"></span><span id="bm_16b_xyz"></span><span id="BM_16B_XYZ"></span>**BM\_16b\_XYZ**
</dt> <dd>

64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.

</dd> <dt>

<span id="BM_16b_Yxy"></span><span id="bm_16b_yxy"></span><span id="BM_16B_YXY"></span>**BM\_16b\_Yxy**
</dt> <dd>

64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.

</dd> <dt>

<span id="BM_16b_Lab"></span><span id="bm_16b_lab"></span><span id="BM_16B_LAB"></span>**BM\_16b\_Lab**
</dt> <dd>

64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.

</dd> <dt>

<span id="BM_16b_G3CH"></span><span id="bm_16b_g3ch"></span><span id="BM_16B_G3CH"></span>**BM\_16b\_G3CH**
</dt> <dd>

64 bits per pixel. 16 bits are used for the gray-scale value. Each of the three color channels uses 16 bits.

</dd> <dt>

<span id="BM_16b_GRAY"></span><span id="bm_16b_gray"></span><span id="BM_16B_GRAY"></span>**BM\_16b\_GRAY**
</dt> <dd>

64 bits per pixel. 16 bits are used for the gray-scale value. All other bits are ignored.

</dd> <dt>

<span id="BM_565RGB"></span><span id="bm_565rgb"></span>**BM\_565RGB**
</dt> <dd>

16 bits per pixel. 5 bits are used for red, 6 for green, and 5 for blue.

</dd> <dt>

<span id="BM_32b_scRGB"></span><span id="bm_32b_scrgb"></span><span id="BM_32B_SCRGB"></span>**BM\_32b\_scRGB**
</dt> <dd>

96 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.

</dd> <dt>

<span id="BM_32b_scARGB"></span><span id="bm_32b_scargb"></span><span id="BM_32B_SCARGB"></span>**BM\_32b\_scARGB**
</dt> <dd>

128 bits per pixel. 32 bits are used for each color channel, as defined by the IEEE 32-bit floating point standard.

</dd> <dt>

<span id="BM_S2DOT13FIXED_scRGB"></span><span id="bm_s2dot13fixed_scrgb"></span><span id="BM_S2DOT13FIXED_SCRGB"></span>**BM\_S2DOT13FIXED\_scRGB**
</dt> <dd>

48 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.

</dd> <dt>

<span id="BM_S2DOT13FIXED_scARGB"></span><span id="bm_s2dot13fixed_scargb"></span><span id="BM_S2DOT13FIXED_SCARGB"></span>**BM\_S2DOT13FIXED\_scARGB**
</dt> <dd>

64 bits per pixel. Color data is stored as one 16-bit word per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.

</dd> <dt>

<span id="BM_R10G10B10A2"></span><span id="bm_r10g10b10a2"></span>**BM\_R10G10B10A2**
</dt> <dd></dd> <dt>

<span id="BM_R10G10B10A2_XR"></span><span id="bm_r10g10b10a2_xr"></span>**BM\_R10G10B10A2\_XR**
</dt> <dd></dd> <dt>

<span id="BM_R16G16B16A16_FLOAT"></span><span id="bm_r16g16b16a16_float"></span>**BM\_R16G16B16A16\_FLOAT**
</dt> <dd>

\#endif // NTDDI\_VERSION &gt;= NTDDI\_WIN7

</dd> </dl>

## Remarks

The last four values were added to the BMFORMAT enumeration beginning with Windows Vista.

The PBMFORMAT and LPBMFORMAT data types are defined as pointers to this enumeration:


```
typedef BMFORMAT *PBMFORMAT, *LPBMFORMAT;
```



## Requirements



|                    |                                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| Version<br/> | Included in Windows Vista and later.<br/>                                  |
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BMFORMAT%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




