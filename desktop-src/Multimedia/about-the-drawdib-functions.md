---
title: About the DrawDib Functions
description: About the DrawDib Functions
ms.assetid: 0ae993df-8393-479e-aa11-14301384715d
keywords:
- Video for Windows (VFW),DrawDib
- VFW (Video for Windows),DrawDib
- DrawDib,about
- DrawDib,color tables
- DrawDib,transfer mode
- DrawDib,display adapters
- DrawDib,image stretching
- DrawDib,compressed images
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the DrawDib Functions

\[The feature associated with this page, [DrawDib](/windows/win32/multimedia/drawdib), is a legacy feature. It has been superseded by [MediaComposition class](/uwp/api/Windows.Media.Editing.MediaComposition). **MediaComposition class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaComposition class** instead of **DrawDib**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Collectively, the DrawDib functions are similar to the [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) function in that they provide image-stretching and dithering capabilities. However, the DrawDib functions support image decompression, data-streaming, and a greater number of display adapters.

You will find it beneficial to use the DrawDib functions in some circumstances. Still, [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) is more diverse than the DrawDib functions and should be used when the DrawDib functions cannot provide the desired functionality. The following list describes factors to consider when deciding whether to use the DrawDib functions or **StretchDIBits**.

-   Color table information format. DrawDib functions display images that use the **DIB\_RGB\_COLORS** format for their color table. If images in your application store color table information with the **DIB\_PAL\_COLORS** or **DIB\_PAL\_INDICES** format, you must use [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) to display them.
-   Transfer mode. DrawDib functions require that your application use the **SRCCOPY** transfer mode. If your application uses [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) with a transfer mode other than **SRCCOPY**, you should continue to use **StretchDIBits**. Similarly, if you need to use other raster operations in your application, such as an XOR, use **StretchDIBits**.
-   Quality of video and animation playback. You can use the DrawDib functions for data-streaming applications, such as those that play video clips and animated sequences. The DrawDib functions outperform [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) in that they provide higher-quality images and improve motion during playback.
-   Display adapters. DrawDib functions support a greater number of display adapters than [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits) supports. The DrawDib functions support VGA color adapters that provide 16-color palettes using 4-bit image depth, SVGA adapters that provide 256-color palettes using 8-bit image depth, and true-color display adapters that provide thousands of colors using 16-bit, 24-bit, and 32-bit image depths.

    The DrawDib functions also improve the speed and quality of displaying images on display adapters with more limited capabilities. For example, when using an 8-bit display adapter, the DrawDib functions efficiently dither true-color images to 256 colors. They also dither 8-bit images when using 4-bit display adapters.

-   Image-stretching. Like [**StretchDIBits**](/windows/desktop/api/wingdi/nf-wingdi-stretchdibits), the DrawDib functions use source and destination rectangles to control the portion of an image that is displayed. You can crop unwanted portions of an image or stretch an image by varying the position and size of the source and destination rectangles. If a display driver does not support image-stretching, the DrawDib functions provide more efficient stretching capabilities than **StretchDIBits**.
-   Compressed images. The DrawDib functions will draw any format for which you have a decompressor, including run-length encoding (RLE), Cinepak, and 411 YUV. Windows includes RLE and Cinepak decompressors that can be optionally installed.
-   The Indeo codec is no longer supported in Windows.

## Related topics

<dl> <dt>

[DrawDib](drawdib.md)
</dt> </dl>

 

 