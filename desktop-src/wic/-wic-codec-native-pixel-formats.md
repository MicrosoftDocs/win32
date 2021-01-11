---
description: This topic introduces the pixel formats provided by the Windows Imaging Component (WIC).
ms.assetid: 348b6d15-e339-4dce-99f3-4d639ee9bf7d
title: Native Pixel Formats Overview
ms.topic: article
ms.date: 05/31/2018
---

# Native Pixel Formats Overview

This topic introduces the pixel formats provided by the Windows Imaging Component (WIC).

A pixel format describes the memory layout of each pixel in a bitmap. This memory layout describes how the image data of a bitmap is encoded by specifying the numerical format and color-channel organization. WIC supports several numerical formats for multiple color-channel organization schemes, providing a wide range of pixel formats.

-   [Bit Depth](#bit-depth)
-   [Numerical Encoding](#numerical-encoding)
-   [Color Channels](#color-channels)
    -   [RGB/BGR Color Model](#rgbbgr-color-model)
    -   [CMYK Color Model](#cmyk-color-model)
    -   [n-channel Color Model](#n-channel-color-model)
    -   [Indexed and Grayscale Color Models](#indexed-and-grayscale-color-models)
    -   [Y’CbCr Color Model](#ycbcr-color-model)
-   [WIC Pixel Format](#wic-pixel-format)
    -   [Undefined Pixel Formats](#undefined-pixel-formats)
    -   [Indexed Pixel Formats](#indexed-pixel-formats)
    -   [Packed Bit Pixel Formats](#packed-bit-pixel-formats)
    -   [Grayscale Pixel Formats](#grayscale-pixel-formats)
    -   [RGB/BGR Pixel formats](#rgbbgr-pixel-formats)
    -   [CMYK Pixel Formats](#cmyk-pixel-formats)
    -   [n-channel Pixel Formats](#n-channel-pixel-formats)
    -   [Alpha Only Pixel Formats](#alpha-only-pixel-formats)
    -   [Y’CbCr Pixel Formats](#ycbcr-pixel-formats)
-   [Color Space](#color-space)
-   [Native Image Formats](#native-image-formats)
    -   [BMP Native Codec](#bmp-native-codec)
    -   [GIF Native Codec](#gif-native-codec)
    -   [ICO Native Codec](#ico-native-codec)
    -   [JPEG Native Codec](#jpeg-native-codec)
    -   [PNG Native Codec](#png-native-codec)
    -   [TIFF Native Codec](#tiff-native-codec)
    -   [JPEG-XR Native Codec](#jpeg-xr-native-codec)
-   [DDS Native Codec](#dds-native-codec)
-   [Pixel Format Extensibility](#pixel-format-extensibility)
-   [Related topics](#related-topics)

## Bit Depth

The *bit depth* is the number of bits used to encode each color channel. Today, most digital images use a bit depth of 8, meaning that each color channel in a pixel is represented by 8 bits, providing 2⁸ (256) unique values per channel. An image that has a bit depth of 8 and three color channels (such as red, green, and blue) uses 24 bits per pixel (bpp), which provides 2²⁴ (16,777,216) different colors per pixel.

For better color resolution, a bit depth of 16 or 32 can be used. This provides each color channel with 2¹⁶ (65,536) or 2³² unique values, at a cost of more memory per pixel.

In some formats, the bit depth is not a multiple of 8. These formats are called *packed* formats, because the color channels in a pixel are not aligned to byte boundaries. For example, if the bit depths of 5, three color channels can be stored in 16 bits (including 1 bit of padding, to make pixels byte-aligned). Packed formats are useful when memory or processing power are limited.

## Numerical Encoding

For the majority of today's digital images, unsigned bytes and unsigned short integers are used to describe the numerical range of each color channel. The minimum value (0) represents zero intensity in a single color channel, and black is achieved when all color channels are zero. Similarly, the maximum value represents full intensity, and white is achieved when all color channels are at full intensity. At a bit depth of 8, a UINT provides 256 unique values per color channel (0 - 255). A 16-bit UINT provides 65,536 unique values per color channel (0 - 65,535).

In addition, WIC supports fixed-point and floating-point formats. These formats support larger dynamic ranges, because the entire numerical range of each color channel is larger than the visible range. As a result, colors can be adjusted above or below the visible range, during the intermediate steps of image processing, without loss of image information.

### Fixed-Point Numerical Encoding

16-bit fixed-point values are interpreted as s2.13: sign bit, two integer bits, and thirteen fractional bits. Using this interpretation, a numerical range of −4.0 to +3.999... can be represented, with the value of 1.0 represented by the signed integer value 8192 (0x2000).

32-bit fixed-point values are interpreted as s7.24: sign bit, seven integer bits, and twenty-four fractional bits. Using this interpretation, a numerical range of −128.0 to +127.999... can be represented, with the value of 1.0 represented by the signed integer value 16777216 (0x01000000).

## Color Channels

The color channels of a pixel format define the memory layout of each color within the image data of a bitmap. There are a variety of different color-channel structures common in today's digital images, and WIC provides support for many of these.

### RGB/BGR Color Model

RGB and BGR formats describe colors in an additive color model. The most common method of describing an image is with three separate color channels representing the colors red (R), green (G), and blue (B). WIC provides support for these three channels in either the red-green-blue (RGB) or blue-green-red (BGR) order. This is the order in which each color channel appears within the sequential bit stream. For example, in the GUID\_WICPixelFormat32bppRGB format, each pixel is 32 bits wide. The red channel is the first (least significant) byte in memory, followed by green, and then blue. Conversely, in the GUID\_WICPixelFormat32bppBGR format, the color channels are in the opposite order. WIC supports a number of RGB/BGR formats, including special packed bit formats such as GUID\_WICPixelFormat16bppBGR555.

> [!Note]  
> The color channels of the special BGR packed bit formats are not in multiples of 8 like the color channels in typical pixel formats. This means that the channel values are not byte aligned. Care must be taken when reading packed bit color channels.

 

In addition to the RGB and BGR formats, WIC also provides RGB and BGR pixel formats that support an alpha (A) channel. The alpha channel provides opacity data for the pixel. For formats with an added alpha channel, the alpha channel usually comes last in the color-channel order. For example, in the pixel format GUID\_WICPixelFormat32bppBGRA, the byte order is blue, green, and red, followed by the alpha channel.

WIC also supports pre-multiplied (P) alpha RGB pixel formats. In a typical RGBA pixel format, the red, green, and blue color values are the actual color values for the image. To make a composite image in the standard RGBA format, the alpha value of the foreground image must be multiplied by each of the red, green, and blue channels before adding it to the color of the background image. In a pre-multiplied alpha RGB pixel format, each color channel has already been multiplied by the alpha value. This provides a more efficient method of image composition with alpha-channel data. To retrieve the true color values of each channel in a PRGBA/PBGRA pixel format, the alpha-channel multiplication must be reversed by dividing color values by the alpha value.

### CMYK Color Model

CMYK is a subtractive color model that is used in printing. The colors produced by a CMYK model are generated by the light that is not absorbed, but reflected. CMYK is a four channel model of cyan (C), magenta (M), yellow (Y), and black (K). When all four color channels are at maximum value, the result is black. Like the RGB/BGR color models, the byte order within the sequential bit stream is given by the pixel format's name. For instance, in the pixel format GUID\_WICPixelFormat32bppCMYK, each pixel is made up of 32 bits. The first byte contains the cyan value, followed in turn by magenta, yellow, and black. WIC provides pixel formats for CMYK at 32 and 64 bits per pixel (bpp).

In addition to the standard CMYK color model, WIC also provides CMYK with alpha. This allows CMYK images to have alpha blending data similar to the RGB/BGR color model. The alpha channel is located immediately after black in the sequential bit stream of a bitmap.

### n-channel Color Model

For flexibility, WIC also provides pixel formats that do not have a predefined channel order. WIC provides pixel formats that support from three to eight channels of continuous image data at bit depths of both 8 and 16. Unlike the RGB/BGR and CMYK pixel formats, n-channel formats do not specify the channel order but rather the number of color channels available. For instance, in the pixel format GUID\_WICPixelFormat32bpp4Channels, each pixel is made up of 32 bits with each of the 4 channels occupying a single byte.

WIC also provides pixel formats for n-channel with alpha. This allows n-channel images to have alpha blending data similar to the RGB/BGR and CMYK color models. The alpha channel is located immediately after last color channel in the sequential bit stream of a bitmap.

### Indexed and Grayscale Color Models

*Indexed* formats use a table of colors, called a *palette*. The palette is stored externally to the pixel data or else defined implicitly. The value of each pixel in the image is an index into the palette. With an indexed format, the number of bits per pixel is directly related to the number of entries in the palette. This significantly reduces the amount of data required to represent the image, but also restricts the number of colors available to the image. WIC supports indexed formats with 1, 2, 4, or 8 bpp.

For monochrome (grayscale) formats, WIC supports 1, 2, 4, 8, 16, and 32 bits per pixel. For bit depths of 1, 8, 16, and 32, the color data is stored in a single channel. For bit depths of 2 or 4, pixels are indexes into a grayscale palette.

### Y’CbCr Color Model

WIC adds support for the JPEG JFIF Y’CbCr color model. Y’CbCr separate colors into a luma component (Y’) and two chroma components (Cb and Cr). Many JPEG files natively store image data using the Y’CbCr color model.

The human visual system is less sensitive to changes in chroma than to luma, and Y’CbCr formats can take advantage of this reduced sensitivity by reducing the amount of chroma data that is stored relative to luma. They accomplish this by storing chroma and luma into separate planes and scaling each component plane to a different resolution. This practice is known as chroma subsampling.

Because chroma and luma data are stored separately and may be different resolutions, WIC defines separate luma and chroma pixel formats. WIC supports data that is 8 bits per channel.

## WIC Pixel Format

The pixel formats in WIC are defined using GUIDs to avoid clashes with IHVs. WIC provides a friendly name to reference the GUID of a native pixel format. The naming convention for the WIC pixel formats is as follows:

**\[GUID\_WICPixelFormat\]\[Bits Per Pixel\]\[Channel Order\]\[Storage Type\]**

| Format component         | Description                                                                                                                                                                                                                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GUID\_WICPixelFormat** | The descriptive identification for all WIC pixel formats. The friendly name for all WIC pixels begin with this string.                                                                                                                                                                                       |
| **Bits Per Pixel**       | The number of bits per pixel (bpp) used for the pixel format.                                                                                                                                                                                                                                                |
| **Channel Order**        | The color-channel model and order of each channel for the format.                                                                                                                                                                                                                                            |
| **Storage Type**         | The numerical encoding used for the pixel format. The default encoding is an unsigned integer. If nothing follows the color model information, an unsigned integer (UINT) is implied. FixedPoint and Float are used to identify pixel formats that use fixed-point and floating-point encoding respectively. |



 

> [!Note]  
> For n-channel formats, \[Channel Order\] does not specify color order but rather the number of channels available. For example, GUID\_WICPixelFormat24bpp3Channels provides 3 color channels where "3Channels" is the \[Channel Order\] entry, but indicates only the number of channels and not the order.

 

For example, the friendly name GUID\_WICPixelFormat24bppRGB means that the pixel format uses 24 bits per pixel and the RGB color model. Because the name does not explicitly identify a storage type, an unsigned integer is implied.

WIC supports a several pixel formats. The following tables group similar pixel formats by color structure while providing additional information such as bit depth, bits per pixel, and numerical encoding. Each table contains the following information:

-   **Friendly Name**. The friendly name of the pixel format.
-   **Channel Count**. The number of color channels.
-   **Bits Per Channel**. The number of bits per channel (bit depth).
-   **Bits Per Pixel**. The number of bits per pixel, including any padding bits.
-   **Storage Type**. The numerical encoding of the image data. This value can be an unsigned integer (UINT), a fixed-point number (FixedPoint), or a floating-point number (Float).

> [!Note]  
> For clarity, this document refers to pixel formats only by their friendly names. The actual hexadecimal value for the pixel formats can be found in the wincodec.h/idl files.

 

### Undefined Pixel Formats

The following list shows generic pixel formats that are used when the pixel format is undefined or is unimportant to an image operation.

-   GUID\_WICPixelFormatUndefined
-   GUID\_WICPixelFormatDontCare

### Indexed Pixel Formats

The following table lists the indexed pixel formats provided by WIC. In these formats, the value for each pixel is an index into a color palette.



| Friendly Name                   | Channel Count | Bits Per Pixel | Storage Type |
|---------------------------------|---------------|----------------|--------------|
| GUID\_WICPixelFormat1bppIndexed | 1             | 1              | UINT         |
| GUID\_WICPixelFormat2bppIndexed | 1             | 2              | UINT         |
| GUID\_WICPixelFormat4bppIndexed | 1             | 4              | UINT         |
| GUID\_WICPixelFormat8bppIndexed | 1             | 8              | UINT         |



 

### Packed Bit Pixel Formats

The following table lists the packed bit formats provided by WIC. In these formats, color-channel data is not byte-aligned.



| Friendly Name                          | Channel Count | Bits Per Channel       | Bits Per Pixel | Storage Type |
|-------------------------------------------|---------------|------------------------|----------------|--------------|
| GUID\_WICPixelFormat16bppBGR555           | 3             | 5                      | 16             | UINT         |
| GUID\_WICPixelFormat16bppBGR565           | 3             | 5(B)/6(G)/5(R)         | 16             | UINT         |
| GUID\_WICPixelFormat16bppBGRA555          | 4             | 5(B)/5(G)/5(R)/1(A)    | 16             | UINT         |
| GUID\_WICPixelFormat32bppBGR101010        | 3             | 10                     | 32             | UINT         |
| GUID\_WICPixelFormat32bppRGBA1010102      | 4             | 10(R)/10(G)/10(B)/2(A) | 32             | UINT         |
| GUID\_WICPixelFormat32bppRGBA1010102XR    | 4             | 10(R)/10(G)/10(B)/2(A) | 32             | UINT         |
| GUID\_WICPixelFormat32bppR10G10B10A2      | 4             | 10(R)/10(G)/10(B)/2(A) | 32             | UINT         |
| GUID\_WICPixelFormat32bppR10G10B10A2HDR10 | 4             | 10(R)/10(G)/10(B)/2(A) | 32             | UINT         |

For the GUID\_WICPixelFormat32bppBGR101010 and GUID\_WICPixelFormat32bppRGBA1010102 formats, the red channel is stored in the least significant bits. For the GUID\_WICPixelFormat32bppR10G10B10A2 and GUID\_WICPixelFormat32bppR10G10B10A2HDR10 formats, the red channel is defined in the most significant bits, the same layout as [DXGI_FORMAT_R10G10B10A2_UNORM](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

The GUID\_WICPixelFormat32bppR10G10B10A2HDR10 format is the 10 bit pixel format for HDR10 (BT.2020 color space and SMPTE ST.2084 EOTF).

### Grayscale Pixel Formats

The following table lists the grayscale formats provided by WIC. In these formats, color data represents shades of gray.



| Friendly Name                           | Channel Count | Bits Per Channel | Bits Per Pixel | Storage Type |
|-----------------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormatBlackWhite          | 1             | 1                | 1              | UINT         |
| GUID\_WICPixelFormat2bppGray            | 1             | 2                | 2              | UINT         |
| GUID\_WICPixelFormat4bppGray            | 1             | 4                | 4              | UINT         |
| GUID\_WICPixelFormat8bppGray            | 1             | 8                | 8              | UINT         |
| GUID\_WICPixelFormat16bppGray           | 1             | 16               | 16             | UINT         |
| GUID\_WICPixelFormat16bppGrayFixedPoint | 1             | 16               | 16             | FixedPoint   |
| GUID\_WICPixelFormat16bppGrayHalf       | 1             | 16               | 16             | Float        |
| GUID\_WICPixelFormat32bppGrayFloat      | 1             | 32               | 32             | Float        |
| GUID\_WICPixelFormat32bppGrayFixedPoint | 1             | 32               | 32             | FixedPoint   |



 

### RGB/BGR Pixel formats

The following table lists the RGB/BGR formats provided by WIC. These formats separate the primary color data into red (R), green (G), and blue (B) channels. An additional alpha (A) channel is provided for opacity information in some formats.



| Friendly Name                            | Channel Count | Bits Per Channel | Bits Per Pixel | Storage Type |
|------------------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormat24bppRGB             | 3             | 8                | 24             | UINT         |
| GUID\_WICPixelFormat24bppBGR             | 3             | 8                | 24             | UINT         |
| GUID\_WICPixelFormat32bppBGR             | 3             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat32bppRGBA            | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat32bppBGRA            | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat32bppRGBE\*          | 4             | 8                | 32             | Float        |
| GUID\_WICPixelFormat32bppPRGBA           | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat32bppPBGRA           | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat48bppRGB             | 3             | 16               | 48             | UINT         |
| GUID\_WICPixelFormat48bppBGR             | 3             | 16               | 48             | UINT         |
| GUID\_WICPixelFormat48bppRGBFixedPoint   | 3             | 16               | 48             | Fixed        |
| GUID\_WICPixelFormat48bppBGRFixedPoint   | 3             | 16               | 48             | Fixed        |
| GUID\_WICPixelFormat48bppRGBHalf         | 3             | 16               | 48             | Float        |
| GUID\_WICPixelFormat64bppRGBA            | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat64bppBGRA            | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat64bppPRGBA           | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat64bppPBGRA           | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat64bppRGBFixedPoint   | 3             | 16               | 64             | Fixed        |
| GUID\_WICPixelFormat64bppRGBAFixedPoint  | 4             | 16               | 64             | Fixed        |
| GUID\_WICPixelFormat64bppBGRAFixedPoint  | 4             | 16               | 64             | Fixed        |
| GUID\_WICPixelFormat64bppRGBHalf         | 3             | 16               | 64             | Float        |
| GUID\_WICPixelFormat64bppRGBAHalf        | 4             | 16               | 64             | Float        |
| GUID\_WICPixelFormat96bppRGBFixedPoint   | 3             | 32               | 96             | Fixed        |
| GUID\_WICPixelFormat128bppRGBFloat       | 3             | 32               | 128            | Float        |
| GUID\_WICPixelFormat128bppRGBAFloat      | 4             | 32               | 128            | Float        |
| GUID\_WICPixelFormat128bppPRGBAFloat     | 4             | 32               | 128            | Float        |
| GUID\_WICPixelFormat128bppRGBFixedPoint  | 3             | 32               | 128            | Fixed        |
| GUID\_WICPixelFormat128bppRGBAFixedPoint | 4             | 32               | 128            | Fixed        |



 

> [!Note]  
> \*The GUID\_WICPixelFormat32bppRGBE format encodes three 16-bit floating-point values in 4 bytes, as follows: Three unsigned 8-bit mantissas for the R, G, and B channels, plus a shared 8-bit exponent. This format provides 16-bit floating-point precision in a smaller pixel representation.

 

Starting with Windows 8 and the [Platform Update for Windows 7](/windows/desktop/direct3darticles/platform-update-for-windows-7), WIC provides additional formats, shown in the table here.



| Friendly Name                      | Channel Count | Bits Per Channel | Bits Per Pixel | Storage Type |
|------------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormat32bppRGB       | 3             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat64bppRGB       | 3             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat96bppRGBFloat  | 3             | 32               | 96             | FLOAT        |
| GUID\_WICPixelFormat64bppPRGBAHalf | 4             | 16               | 64             | FLOAT        |



 

### CMYK Pixel Formats

The following table lists the CMYK formats provided by WIC. These formats separate the primary color data into cyan (C), magenta (M), yellow (Y), and black (K) channels.



| Friendly Name                      | Channel Count | Bits Per Channel | Bits Per Pixel | Storage Type |
|------------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormat32bppCMYK      | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat64bppCMYK      | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat40bppCMYKAlpha | 5             | 8                | 40             | UINT         |
| GUID\_WICPixelFormat80bppCMYKAlpha | 5             | 16               | 80             | UINT         |



 

### n-channel Pixel Formats

The following table lists the n-channel formats provided by WIC. These formats provide a number of undefined color channels to store image data.



| Friendly Name                            | Channel Count | Bits Per Channel | Bits Per Pixel | Storage Type |
|------------------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormat24bpp3Channels       | 3             | 8                | 24             | UINT         |
| GUID\_WICPixelFormat48bpp3Channels       | 3             | 16               | 48             | UINT         |
| GUID\_WICPixelFormat32bpp3ChannelsAlpha  | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat64bpp3ChannelsAlpha  | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat32bpp4Channels       | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat64bpp4Channels       | 4             | 16               | 64             | UINT         |
| GUID\_WICPixelFormat40bpp4ChannelsAlpha  | 5             | 8                | 40             | UINT         |
| GUID\_WICPixelFormat80bpp4ChannelsAlpha  | 5             | 16               | 80             | UINT         |
| GUID\_WICPixelFormat40bpp5Channels       | 5             | 8                | 40             | UINT         |
| GUID\_WICPixelFormat80bpp5Channels       | 5             | 16               | 80             | UINT         |
| GUID\_WICPixelFormat48bpp5ChannelsAlpha  | 6             | 8                | 48             | UINT         |
| GUID\_WICPixelFormat96bpp5ChannelsAlpha  | 6             | 16               | 96             | UINT         |
| GUID\_WICPixelFormat48bpp6Channels       | 6             | 8                | 48             | UINT         |
| GUID\_WICPixelFormat96bpp6Channels       | 6             | 16               | 96             | UINT         |
| GUID\_WICPixelFormat56bpp6ChannelsAlpha  | 7             | 8                | 56             | UINT         |
| GUID\_WICPixelFormat112bpp6ChannelsAlpha | 7             | 16               | 112            | UINT         |
| GUID\_WICPixelFormat56bpp7Channels       | 7             | 8                | 56             | UINT         |
| GUID\_WICPixelFormat112bpp7Channels      | 7             | 16               | 112            | UINT         |
| GUID\_WICPixelFormat64bpp7ChannelsAlpha  | 8             | 8                | 64             | UINT         |
| GUID\_WICPixelFormat128bpp7ChannelsAlpha | 8             | 16               | 128            | UINT         |
| GUID\_WICPixelFormat64bpp8Channels       | 8             | 8                | 64             | UINT         |
| GUID\_WICPixelFormat128bpp8Channels      | 8             | 16               | 128            | UINT         |
| GUID\_WICPixelFormat72bpp8ChannelsAlpha  | 9             | 8                | 72             | UINT         |
| GUID\_WICPixelFormat144bpp8ChannelsAlpha | 9             | 16               | 144            | UINT         |



 

### Alpha Only Pixel Formats

The following table lists the Alpha Only formats provided by WIC. This format contains only alpha information.



| Friendly Name                 | Channel Count | Bits Per Channel | Bits Per Pixel | Storage Type |
|-------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormat8bppAlpha | 1             | 8                | 32             | UINT         |



 

### Y’CbCr Pixel Formats

The following table lists the Y’CbCr formats provided by WIC. These formats separate the primary color data into luma (Y), blue chroma difference (Cb), and red choma difference (Cr). Note that these formats are designed to store JPEG JFIF Y’CbCr pixel data.



| Friendly Name                 | Channel Count | Bits Per Pixel | Storage Type |
|-------------------------------|---------------|----------------|--------------|
| GUID\_WICPixelFormat8bppY     | 1             | 8              | UINT         |
| GUID\_WICPixelFormat8bppCb    | 1             | 8              | UINT         |
| GUID\_WICPixelFormat8bppCr    | 1             | 8              | UINT         |
| GUID\_WICPixelFormat16bppCbCr | 2             | 16             | UINT         |



 

## Color Space

Pixel formats in themselves do not have a color space. Generally, color space is a semantic interpretation of the pixel values that depends on the context of the bitmap. Some images identify a color context that defines the color space of the image. Only in the absence of a color context should the color space be inferred.

Color context information is defined by the [**IWICColorContext**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccolorcontext) interface for WIC. To retrieve the color context information for an image frame, use the **GetColorContext** method.

In the absence of color space information for an image, the general rule for color space inference is that UINT RGB and grayscale formats use the standard RGB color space (sRGB), while fixed-point and floating-point RGB and grayscale formats use the extended RGB color space (scRGB). The CMYK color model uses an RWOP color space.

## Native Image Formats

Each of the Windows provided WIC codecs supports a subset of the WIC pixel formats. For each codec, the supported decode formats may be different than the supported encode formats.

When decoding an image, if data is natively stored in a pixel format that is not supported by the decoder then it will be converted a supported format. To determine the output pixel format, call [**IWICBitmapFrameDecode::GetPixelFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-getpixelformat).

When encoding an image, use [**IWICBitmapFrameEncode::SetPixelFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapframeencode-setpixelformat) to request that the encoder use a specific pixel format. The encoder will return the closest supported pixel format, which may be different from what was requested.

The following tables show the pixel formats supported by each of the Windows provided WIC codecs.

### BMP Native Codec



| Decoder Pixel Formats                   | Encoder Pixel Formats                   |
|-----------------------------------------|-----------------------------------------|
| GUID\_WICPixelFormat1bppIndexed         | GUID\_WICPixelFormat1bppIndexed         |
| GUID\_WICPixelFormat4bppIndexed         | GUID\_WICPixelFormat4bppIndexed         |
| GUID\_WICPixelFormat8bppIndexed         | GUID\_WICPixelFormat8bppIndexed         |
| GUID\_WICPixelFormat16bppBGR555         | GUID\_WICPixelFormat16bppBGR555         |
| GUID\_WICPixelFormat16bppBGR565         | GUID\_WICPixelFormat16bppBGR565         |
| GUID\_WICPixelFormat24bppBGR            | GUID\_WICPixelFormat24bppBGR            |
| GUID\_WICPixelFormat32bppBGR            | GUID\_WICPixelFormat32bppBGR            |
| GUID\_WICPixelFormat32bppBGRA\*         | GUID\_WICPixelFormat32bppBGRA\*         |
| GUID\_WICPixelFormat64bppRGBAFixedPoint | GUID\_WICPixelFormat32bppPBGRA          |
|                                         | GUID\_WICPixelFormat64bppRGBAFixedPoint |
|                                         | GUID\_WICPixelFormat64bppBGRAFixedPoint |



 

> [!Note]  
> GUID\_WICPixelFormat32bppBGRA is only supported in Windows 8, the [Platform Update for Windows 7](/windows/desktop/direct3darticles/platform-update-for-windows-7), and above.
>
> -   To encode to this format, use the **EnableV5Header32bppBGRA** encoder option. The BMP will be written with a BITMAPV5HEADER header.
> -   If a file has a BITMAPV5HEADER, it decodes as GUID\_WICPixelFormat32bppBGRA.

 

### GIF Native Codec



| Decoder Pixel Formats           | Encoder Pixel Formats           |
|---------------------------------|---------------------------------|
| GUID\_WICPixelFormat8bppIndexed | GUID\_WICPixelFormat8bppIndexed |



 

### ICO Native Codec



| Decoder Pixel Formats         | Encoder Pixel Formats |
|-------------------------------|-----------------------|
| GUID\_WICPixelFormat32bppBGRA |                       |



 

### JPEG Native Codec



| Decoder Pixel Formats         | Encoder Pixel Formats         |
|-------------------------------|-------------------------------|
| GUID\_WICPixelFormat8bppGray  | GUID\_WICPixelFormat8bppGray  |
| GUID\_WICPixelFormat24bppBGR  | GUID\_WICPixelFormat24bppBGR  |
| GUID\_WICPixelFormat32bppCMYK | GUID\_WICPixelFormat32bppCMYK |



 

### PNG Native Codec



| Decoder Pixel Formats           | Encoder Pixel Formats           |
|---------------------------------|---------------------------------|
| GUID\_WICPixelFormat1bppIndexed | GUID\_WICPixelFormat1bppIndexed |
| GUID\_WICPixelFormat2bppIndexed | GUID\_WICPixelFormat2bppIndexed |
| GUID\_WICPixelFormat4bppIndexed | GUID\_WICPixelFormat4bppIndexed |
| GUID\_WICPixelFormat8bppIndexed | GUID\_WICPixelFormat8bppIndexed |
| GUID\_WICPixelFormatBlackWhite  | GUID\_WICPixelFormatBlackWhite  |
| GUID\_WICPixelFormat2bppGray    | GUID\_WICPixelFormat2bppGray    |
| GUID\_WICPixelFormat4bppGray    | GUID\_WICPixelFormat4bppGray    |
| GUID\_WICPixelFormat8bppGray    | GUID\_WICPixelFormat8bppGray    |
| GUID\_WICPixelFormat16bppGray   | GUID\_WICPixelFormat16bppGray   |
| GUID\_WICPixelFormat24bppBGR    | GUID\_WICPixelFormat24bppBGR    |
| GUID\_WICPixelFormat32bppBGRA   | GUID\_WICPixelFormat32bppBGRA   |
| GUID\_WICPixelFormat48bppRGB    | GUID\_WICPixelFormat48bppRGB    |
| GUID\_WICPixelFormat64bppRGBA   | GUID\_WICPixelFormat48bppBGR    |
|                                 | GUID\_WICPixelFormat64bppRGBA   |
|                                 | GUID\_WICPixelFormat64bppBGRA   |



 

### TIFF Native Codec



| Decoder Pixel Formats                | Encoder Pixel Formats           |
|--------------------------------------|---------------------------------|
| GUID\_WICPixelFormat1bppIndexed      | GUID\_WICPixelFormat1bppIndexed |
| GUID\_WICPixelFormat4bppIndexed      | GUID\_WICPixelFormat4bppIndexed |
| GUID\_WICPixelFormat8bppIndexed      | GUID\_WICPixelFormat8bppIndexed |
| GUID\_WICPixelFormatBlackWhite       | GUID\_WICPixelFormatBlackWhite  |
| GUID\_WICPixelFormat4bppGray         | GUID\_WICPixelFormat4bppGray    |
| GUID\_WICPixelFormat8bppGray         | GUID\_WICPixelFormat8bppGray    |
| GUID\_WICPixelFormat16bppGray        | GUID\_WICPixelFormat16bppGray   |
| GUID\_WICPixelFormat32bppGrayFloat   | GUID\_WICPixelFormat24bppBGR    |
| GUID\_WICPixelFormat24bppBGR         | GUID\_WICPixelFormat32bppBGRA   |
| GUID\_WICPixelFormat32bppBGRA        | GUID\_WICPixelFormat32bppCMYK   |
| GUID\_WICPixelFormat32bppPBGRA       | GUID\_WICPixelFormat48bppRGB    |
| GUID\_WICPixelFormat48bppRGB         | GUID\_WICPixelFormat64bppRGBA   |
| GUID\_WICPixelFormat32bppCMYK        |                                 |
| GUID\_WICPixelFormat40bppCMYKAlpha   |                                 |
| GUID\_WICPixelFormat64bppRGBA        |                                 |
| GUID\_WICPixelFormat64bppPRGBA       |                                 |
| GUID\_WICPixelFormat64bppCMYK        |                                 |
| GUID\_WICPixelFormat80bppCMYKAlpha   |                                 |
| GUID\_WICPixelFormat96bppRGBFloat\*  |                                 |
| GUID\_WICPixelFormat128bppRGBAFloat  |                                 |
| GUID\_WICPixelFormat128bppPRGBAFloat |                                 |



 

> [!Note]  
> GUID\_ WICPixelFormat96bppRGBFloat is only supported in Windows 8, the [Platform Update for Windows 7](/windows/desktop/direct3darticles/platform-update-for-windows-7), and above.

 

### JPEG-XR Native Codec



| Decoder Pixel Formats                    | Encoder Pixel Formats                    |
|------------------------------------------|------------------------------------------|
| GUID\_WICPixelFormatBlackWhite           | GUID\_WICPixelFormatBlackWhite           |
| GUID\_WICPixelFormat8bppGray             | GUID\_WICPixelFormat8bppGray             |
| GUID\_WICPixelFormat16bppBGR555          | GUID\_WICPixelFormat16bppBGR555          |
| GUID\_WICPixelFormat16bppGray            | GUID\_WICPixelFormat16bppGray            |
| GUID\_WICPixelFormat24bppBGR             | GUID\_WICPixelFormat24bppBGR             |
| GUID\_WICPixelFormat24bppRGB             | GUID\_WICPixelFormat24bppRGB             |
| GUID\_WICPixelFormat32bppBGR             | GUID\_WICPixelFormat32bppBGR             |
| GUID\_WICPixelFormat32bppBGRA            | GUID\_WICPixelFormat32bppBGRA            |
| GUID\_WICPixelFormat48bppRGBFixedPoint   | GUID\_WICPixelFormat48bppRGBFixedPoint   |
| GUID\_WICPixelFormat16bppGrayFixedPoint  | GUID\_WICPixelFormat16bppGrayFixedPoint  |
| GUID\_WICPixelFormat32bppBGR101010       | GUID\_WICPixelFormat32bppBGR101010       |
| GUID\_WICPixelFormat48bppRGB             | GUID\_WICPixelFormat48bppRGB             |
| GUID\_WICPixelFormat64bppRGBA            | GUID\_WICPixelFormat64bppRGBA            |
| GUID\_WICPixelFormat96bppRGBFixedPoint   | GUID\_WICPixelFormat96bppRGBFixedPoint   |
| GUID\_WICPixelFormat96bppRGBFixedPoint   | GUID\_WICPixelFormat128bppRGBAFloat      |
| GUID\_WICPixelFormat128bppRGBFloat       | GUID\_WICPixelFormat128bppRGBFloat       |
| GUID\_WICPixelFormat32bppCMYK            | GUID\_WICPixelFormat32bppCMYK            |
| GUID\_WICPixelFormat64bppRGBAFixedPoint  | GUID\_WICPixelFormat64bppRGBAFixedPoint  |
| GUID\_WICPixelFormat128bppRGBAFixedPoint | GUID\_WICPixelFormat128bppRGBAFixedPoint |
| GUID\_WICPixelFormat64bppCMYK            | GUID\_WICPixelFormat64bppCMYK            |
| GUID\_WICPixelFormat24bpp3Channels       | GUID\_WICPixelFormat24bpp3Channels       |
| GUID\_WICPixelFormat32bpp4Channels       | GUID\_WICPixelFormat32bpp4Channels       |
| GUID\_WICPixelFormat40bpp5Channels       | GUID\_WICPixelFormat40bpp5Channels       |
| GUID\_WICPixelFormat48bpp6Channels       | GUID\_WICPixelFormat48bpp6Channels       |
| GUID\_WICPixelFormat56bpp7Channels       | GUID\_WICPixelFormat56bpp7Channels       |
| GUID\_WICPixelFormat64bpp8Channels       | GUID\_WICPixelFormat64bpp8Channels       |
| GUID\_WICPixelFormat48bpp3Channels       | GUID\_WICPixelFormat48bpp3Channels       |
| GUID\_WICPixelFormat64bpp4Channels       | GUID\_WICPixelFormat64bpp4Channels       |
| GUID\_WICPixelFormat80bpp5Channels       | GUID\_WICPixelFormat80bpp5Channels       |
| GUID\_WICPixelFormat96bpp6Channels       | GUID\_WICPixelFormat96bpp6Channels       |
| GUID\_WICPixelFormat112bpp7Channels      | GUID\_WICPixelFormat112bpp7Channels      |
| GUID\_WICPixelFormat128bpp8Channels      | GUID\_WICPixelFormat128bpp8Channels      |
| GUID\_WICPixelFormat40bppCMYKAlpha       | GUID\_WICPixelFormat40bppCMYKAlpha       |
| GUID\_WICPixelFormat80bppCMYKAlpha       | GUID\_WICPixelFormat80bppCMYKAlpha       |
| GUID\_WICPixelFormat32bpp3ChannelsAlpha  | GUID\_WICPixelFormat32bpp3ChannelsAlpha  |
| GUID\_WICPixelFormat64bpp7ChannelsAlpha  | GUID\_WICPixelFormat40bpp4ChannelsAlpha  |
| GUID\_WICPixelFormat72bpp8ChannelsAlpha  | GUID\_WICPixelFormat48bpp5ChannelsAlpha  |
| GUID\_WICPixelFormat64bpp3ChannelsAlpha  | GUID\_WICPixelFormat56bpp6ChannelsAlpha  |
| GUID\_WICPixelFormat80bpp4ChannelsAlpha  | GUID\_WICPixelFormat64bpp7ChannelsAlpha  |
| GUID\_WICPixelFormat96bpp5ChannelsAlpha  | GUID\_WICPixelFormat72bpp8ChannelsAlpha  |
| GUID\_WICPixelFormat112bpp6ChannelsAlpha | GUID\_WICPixelFormat64bpp3ChannelsAlpha  |
| GUID\_WICPixelFormat128bpp7ChannelsAlpha | GUID\_WICPixelFormat80bpp4ChannelsAlpha  |
| GUID\_WICPixelFormat144bpp8ChannelsAlpha | GUID\_WICPixelFormat96bpp5ChannelsAlpha  |
| GUID\_WICPixelFormat64bppRGBAHalf        | GUID\_WICPixelFormat112bpp6ChannelsAlpha |
| GUID\_WICPixelFormat48bppRGBHalf         | GUID\_WICPixelFormat128bpp7ChannelsAlpha |
| GUID\_WICPixelFormat32bppRGBE            | GUID\_WICPixelFormat144bpp8ChannelsAlpha |
| GUID\_WICPixelFormat16bppGrayHalf        | GUID\_WICPixelFormat64bppRGBAHalf        |
| GUID\_WICPixelFormat32bppGrayFixedPoint  | GUID\_WICPixelFormat48bppRGBHalf         |
| GUID\_WICPixelFormat64bppRGBFixedPoint   | GUID\_WICPixelFormat32bppRGBE            |
| GUID\_WICPixelFormat128bppRGBFixedPoint  | GUID\_WICPixelFormat16bppGrayHalf        |
| GUID\_WICPixelFormat64bppRGBHalf         | GUID\_WICPixelFormatBlackWhite           |



 

## DDS Native Codec



| Decoder Pixel Formats          | Encoder Pixel Formats          |
|--------------------------------|--------------------------------|
| GUID\_WICPixelFormat32bppBGRA  | GUID\_WICPixelFormat32bppBGRA  |
| GUID\_WICPixelFormat32bppPBGRA | GUID\_WICPixelFormat32bppPBGRA |



 

> [!Note]  
> The DDS Windows provided codec supports DDS files encoded using the following DXGI\_FORMAT values:

 

-   DXGI\_FORMAT\_BC1\_UNORM
-   DXGI\_FORMAT\_BC2\_UNORM
-   DXGI\_FORMAT\_BC3\_UNORM

These are decoded and encoded as GUID\_WICPixelFormat32bppBGRA or GUID\_WICPixelFormat32bppPBGRA. For more information, see the [DDS Format Overview](dds-format-overview.md).

## Pixel Format Extensibility

Custom image formats can use pixel formats that are not natively provided by WIC such as YCbCr (YUV) and YCCK (Y/Cb/Cr/K). WIC provides an extensibility model that permits both built-in and add-in pixel formats to work within the same imaging pipeline. To integrate these pixel formats with the WIC imaging pipeline, you must create pixel format converters to convert add-in pixel formats to one or more of the native pixel formats. The main interface for building format converters is [**IWICFormatConverter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicformatconverter).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC GUIDs and CLSIDs](-wic-guids-clsids.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[HD Photo Specification 1.0](https://www.microsoft.com/whdc/xps/wmphoto.mspx)
</dt> </dl>

 

 
