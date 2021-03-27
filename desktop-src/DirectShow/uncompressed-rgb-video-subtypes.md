---
description: The following subtypes define uncompressed RGB formats with no alpha channel.
ms.assetid: 49c91c8c-6889-48c6-8fa5-84929c03d951
title: Uncompressed RGB Video Subtypes (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Uncompressed RGB Video Subtypes

The following subtypes define uncompressed RGB formats with no alpha channel.



| Constant                                                                                                                                                                        | Description                                       |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|
| <span id="MEDIASUBTYPE_RGB1"></span><span id="mediasubtype_rgb1"></span><dl> <dt>**MEDIASUBTYPE\_RGB1**</dt> </dl>       | RGB, 1 bit per pixel (bpp), palettized<br/> |
| <span id="MEDIASUBTYPE_RGB4"></span><span id="mediasubtype_rgb4"></span><dl> <dt>**MEDIASUBTYPE\_RGB4**</dt> </dl>       | RGB, 4 bpp, palettized<br/>                 |
| <span id="MEDIASUBTYPE_RGB8"></span><span id="mediasubtype_rgb8"></span><dl> <dt>**MEDIASUBTYPE\_RGB8**</dt> </dl>       | RGB, 8 bpp, palettized<br/>                 |
| <span id="MEDIASUBTYPE_RGB555"></span><span id="mediasubtype_rgb555"></span><dl> <dt>**MEDIASUBTYPE\_RGB555**</dt> </dl> | RGB 555, 16 bpp<br/>                        |
| <span id="MEDIASUBTYPE_RGB565"></span><span id="mediasubtype_rgb565"></span><dl> <dt>**MEDIASUBTYPE\_RGB565**</dt> </dl> | RGB 565, 16 bpp<br/>                        |
| <span id="MEDIASUBTYPE_RGB24"></span><span id="mediasubtype_rgb24"></span><dl> <dt>**MEDIASUBTYPE\_RGB24**</dt> </dl>    | RGB, 24 bpp<br/>                            |
| <span id="MEDIASUBTYPE_RGB32"></span><span id="mediasubtype_rgb32"></span><dl> <dt>**MEDIASUBTYPE\_RGB32**</dt> </dl>    | RGB, 32 bpp<br/>                            |



The following subtypes define uncompressed RGB formats with alpha channel.



| Constant                                                                                                                                                                                       | Description                                                                              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| <span id="MEDIASUBTYPE_ARGB1555"></span><span id="mediasubtype_argb1555"></span><dl> <dt>**MEDIASUBTYPE\_ARGB1555**</dt> </dl>          | RGB 555 with alpha channel<br/>                                                    |
| <span id="MEDIASUBTYPE_ARGB32"></span><span id="mediasubtype_argb32"></span><dl> <dt>**MEDIASUBTYPE\_ARGB32**</dt> </dl>                | RGB 32 with alpha channel<br/>                                                     |
| <span id="MEDIASUBTYPE_ARGB4444"></span><span id="mediasubtype_argb4444"></span><dl> <dt>**MEDIASUBTYPE\_ARGB4444**</dt> </dl>          | 16-bit RGB with alpha channel; 4 bits per channel<br/>                             |
| <span id="MEDIASUBTYPE_A2R10G10B10"></span><span id="mediasubtype_a2r10g10b10"></span><dl> <dt>**MEDIASUBTYPE\_A2R10G10B10**</dt> </dl> | 32-bit RGB with alpha channel; 10 bits per RGB channel plus 2 bits for alpha.<br/> |
| <span id="MEDIASUBTYPE_A2B10G10R10"></span><span id="mediasubtype_a2b10g10r10"></span><dl> <dt>**MEDIASUBTYPE\_A2B10G10R10**</dt> </dl> | 32-bit BGR with alpha channel; 10 bits per BGR channel plus 2 bits for alpha.<br/> |



## Remarks

For palettized formats, the color of each pixel is specified as an index into a palette. The palette must be included in the format block, following the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure. For non-palettized formats, the color of each pixel is specified directly; the memory layout depends on the bit depth:

-   RGB 555 uses the following memory layout:
    ```C++
    High-order byte:    Low-order byte: 
    X R R R R R G G     G G G B B B B B 

    X = Don't care, R = Red, G = Green, B = Blue
    ```

    

-   RGB 565 uses the following memory layout:
    ```C++
    High-order byte:    Low-order byte: 
    R R R R R G G G     G G G B B B B B 
    ```

    

-   For RGB 24, every pixel is an [**RGBTRIPLE**](/windows/win32/api/wingdi/ns-wingdi-rgbtriple). Each color is one byte, with a value from 0 to 255, inclusive. The memory layout is: 

    |       |      |       |     |
    |-------|------|-------|-----|
    | Byte  | 0    | 1     | 2   |
    | Value | Blue | Green | Red |

    

     

-   For RGB 32, every pixel is an **RGBQUAD**. Each color is one byte, with a value from 0 to 255, inclusive. The memory layout is: 

    |       |      |       |     |                     |
    |-------|------|-------|-----|---------------------|
    | Byte  | 0    | 1     | 2   | 3                   |
    | Value | Blue | Green | Red | Alpha or Don't Care |

    

     

    If the subtype is MEDIASUBTYPE\_ARGB32, byte 3 contains a value for the alpha channel. If the subtype is MEDIASUBTYPE\_RGB32, byte 3 should be ignored.

-   A2R10G10B10 uses the following layout: 

    |       |       |         |         |         |
    |-------|-------|---------|---------|---------|
    | Bit   | 0 - 9 | 10 - 19 | 20 - 29 | 30 - 31 |
    | Value | Blue  | Green   | Red     | Alpha   |

    

     

-   A2B10G10R10 uses the following layout: 

    |       |       |         |         |         |
    |-------|-------|---------|---------|---------|
    | Bit   | 0 - 9 | 10 - 19 | 20 - 29 | 30 - 31 |
    | Value | Red   | Green   | Blue    | Alpha   |

    

     

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Video Subtypes](video-subtypes.md)
</dt> <dt>

[Working with Video Frames](working-with-video-frames.md)
</dt> </dl>

 

 
