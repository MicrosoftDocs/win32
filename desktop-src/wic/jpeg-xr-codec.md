---
description: The native JPEG XR codec is available through the Windows Imaging Component (WIC). The JPEG XR format, which the codec supports, is designed for consumer and professional digital photography.
ms.assetid: CB8D1A5F-B544-462E-8927-F45512CED873
title: JPEG XR Codec Overview
ms.topic: article
ms.date: 05/31/2018
---

# JPEG XR Codec Overview

The native JPEG XR codec is available through the Windows Imaging Component (WIC). The JPEG XR format, which the codec supports, is designed for consumer and professional digital photography.

The JPEG XR format can achieve up to twice the compression efficiency of the original JPEG format, with less noticeable compression artifacts. Features of JPEG XR include:

-   Support for monochrome, RGB, CMYK, and n-channel images
-   8-, 16-, and 32-bit integer formats
-   High dynamic range, wide-gamut formats, using fixed point or floating point color values
-   Progressive decoding
-   Lossy or lossless encoding using the same compression algorithm
-   Support for decoding of regions of interest in large images

The JPEG XR format is defined in the following standards documents:

-   ITU-T T.832: *Information technology – JPEG XR image coding system – Image coding specification*
-   ISO/IEC 29199-2:2010: *Information technology — JPEG XR image coding system — Part 2: Image coding specification*

The JPEG XR standard is largely based on the [HD Photo](hdphoto-format-overview.md) format, but there are some differences between the two formats. In Windows 8, the HD Photo codec has been updated to support JPEG XR. The encoder now always outputs a JPEG XR–compliant bit stream. The decoder can decode both JPEG XR and HD Photo images.

Substantial performance improvements, in relation to the HD Photo codec, have been made to the JPEG XR codec. For example, sub-resolution image decoding, such as thumbnail generation, has been improved, as well as low-resolution image decoding. It is recommended that you use the JPEG XR format instead of the HD Photo format.

## Codec Information



|      Component      |    Description                                                          |
|---------------------|-------------------------------------------------------------------------|
| File name extension | "jxr" and "wdp"                                                         |
| Container GUID      | **GUID\_ContainerFormatWmp**                                            |
| Decoder GUID        | **CLSID\_WICWmpDecoder**                                                |
| Encoder GUID        | **CLSID\_WICWmpEncoder**                                                |
| Profile Support     | The encoder and decoder support up to Main Profile and up to level 128. |



 

## Codec Features

### High Dynamic Range

JPEG XR supports high-dynamic range images, using floating-point or fixed-point colors. In these color formats, the numerical range of a pixel is larger than the visible range, so you can adjust colors above or below the visible range during intermediate processing stages.

-   Fixed-point: In a fixed-point representation, 0 represents black and 1.0 represents maximum saturation. The JPEG XR codec supports both 16-bit and 32-bit fixed-point formats. For 16-bit, 1.0 = 0x2000h, which gives 13 bits for the visible range \[0...1\]. The total range is –4.0 to +3.999, and is mapped linearly. For 32-bit, 1.0 = 0x01000000h, the visible range is 24 bits, and the total range is –128 to +127.999.
-   Floating-point: In a floating-point representation, 0 represents black and 1.0 represents maximum saturation. The JPEG XR codec supports both 16-bit and 32-bit floating-point formats.

### Tiles

A frame can be partitioned into rectangular subregions called *tiles*. A tile is an area of a image that contains rectangular arrays of macroblocks. Tiles enable regions of the image to be decoded without processing the entire image.

During encoding, select the number of tiles by setting the **HorizontalTileSlices** and **VerticalTileSlices** properties. The minimum tile size is 16 × 16 pixels. The encoder adjusts the number of tiles to maintain this restriction. There is storage and processing overhead associated with each tile, so you should consider the number of tiles that are needed for particular scenarios.

### Image Stream Output

The JPEG-XR standard defines two parts of a JPEG-XR file:

-   The image bit stream, defined in the body of the standard.
-   The image container. The file contains Exif and XMP metadata, and is defined in Annex A of the standard.

It is possible, and allowed by the standard, to embed the image stream inside another type of file container. The encoder supports a stream-only mode, which outputs the raw image bit stream with no image container. An application can store the bit stream in some other container format.

To enable stream-only mode, set the **StreamOnly** property.

### Image Quality Settings

Several codec properties control the quality of the output image from the encoder.

-   [ImageQuality](#imagequality) is a property common across WIC codecs. It specifies image quality as a single floating-point value from 0.0–1.0,
-   The [Quality](#image-quality-settings), [Overlap](#overlap), and [Subsampling](#subsampling) properties give more control over the quality settings.

To use the [Quality](#image-quality-settings), [Overlap](#overlap), and [Subsampling](#subsampling) properties, set the [UseCodecOptions](#usecodecoptions) property to **VARIANT\_TRUE**.

If [UseCodecOptions](#usecodecoptions) is **VARIANT\_FALSE** (**VARIANT\_FALSE** is the default) the encoder uses the [ImageQuality](#imagequality) property. The encoder maps the value of ImageQuality to [Quality](#image-quality-settings), [Overlap](#overlap), and [Subsampling](#subsampling) through a lookup table.

The encoder does not support the **CompressionQuality** property.

### Compressed Domain Transcode

The JPEG XR codec can perform certain image transformations without actually decoding the compressed data and re-encoding it. Compressed domain operations are very efficient and avoid any additional quality loss that is typical when you decode and re-encode a lossy-compressed image.

The following compressed domain operations are supported:

-   Crop a region of the image.
-   Rotate or flip the image.
-   Discard frequency data to create a smaller image file.
-   Reorganize the image between spatial and frequency order.

The JPEG XR encoder uses compressed domain transcoding, if possible, when the source image is a JPEG XR image. When the encoder performs a compressed domain operation, it ignores the following codec properties: [AlphaQuality](#alphaquality), [ImageQuality](#imagequality), [InterleavedAlpha](#interleavedalpha), [Lossless](#lossless)[Overlap](#overlap), and [Quality](#image-quality-settings). If the [HorizontalTileSlices](/windows) and [VerticalTileSlices](/windows) properties are present, you must set them to zero. You cannot change the tile size of an image as part of a compressed domain transcode.

The follow list describes how to perform the image transformations.

-   To crop the image, set the desired region in the [**WICRect**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapframeencode-writesource) parameter of the **WriteSource** method.
-   To rotate or flip the image, set the [BitmapTransform](#bitmaptransform) property.
-   To discard frequency data in the image, set the [ImageDataDiscard](#imagedatadiscard) property. To discard frequency data in the alpha channel, set the [AlphaDataDiscard](#alphadatadiscard) property. Discarding frequency data reduces the encoded file size and can reduce the resolution.
-   To change the image organization between frequency and spatial ordering, set the [FrequencyOrdering](/windows) property.

To disable compressed domain transcode and force the encoder to re-encode the image, set the [UseCodecOptions](#usecodecoptions) to **VARIANT\_TRUE** and set [CompressedDomainTranscode](#compresseddomaintranscode) to **VARIANT\_FALSE**.

## Encoder Options

To set encoding properties, use the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) interface. For more information, see the [Encoding Overview](-wic-creating-encoder.md).

The following list specifies the encoder options.

-   [AlphaDataDiscard](#alphadatadiscard)
-   [AlphaQuality](#alphaquality)
-   [BitmapTransform](#bitmaptransform)
-   [CompressedDomainTranscode](#compresseddomaintranscode)
-   [FrequencyOrder](#frequencyorder)
-   [HorizontalTileSlices](#horizontaltileslices)
-   [IgnoreOverlap](#ignoreoverlap)
-   [ImageDataDiscard](#imagedatadiscard)
-   [ImageQuality](#imagequality)
-   [InterleavedAlpha](#interleavedalpha)
-   [Lossless](#lossless)
-   [Overlap](#overlap)
-   [ProgressiveMode](#progressivemode)
-   [Quality](#image-quality-settings)
-   [StreamOnly](#streamonly)
-   [Subsampling](#subsampling)
-   [UseCodecOptions](#usecodecoptions)
-   [VerticalTileSlices](#verticaltileslices)

### AlphaDataDiscard

Sets the amount of alpha frequency data to discard during a compressed domain transcode.



| Data type | VARTYPE     | Range | Default |
|-----------|-------------|-------|---------|
| **UCHAR** | **VT\_UI1** | 0–4   | None    |



 

This property applies only if the [CompressedDomainTranscode](#compresseddomaintranscode) property is set to **VARIANT\_TRUE** and the image contains either a planar alpha channel or interleaved alpha channel; otherwise it is ignored.

For images that contain a planar alpha channel, the following values are valid.



| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | No image frequency data is discarded.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 1     | The flexbits are discarded. This arbitrarily reduces the quality of the planar alpha channel for the transcoded image. , without a change in the effective resolution. The exact reduction in file size and quality depends on numerous factors and cannot be exactly specified.                                                                                                                                                                                           |
| 2     | The high-pass frequency data band is discarded, including the flexbits. This effectively reduces the resolution of the planar alpha channel by a factor of 4 in both dimensions. The actual dimensions of the transcoded image remain the same, but the image loses all detail in each 4x4 block of alpha-channel pixels. Typically, you should set this value only when the [ImageDataDiscard](#imagedatadiscard) property has the same value.                            |
| 3     | Both the high-pass and low-pass frequency data bands are discarded, including the flexbits. This ffectively reduces the resolution of the planar alpha channel by a factor of 16 in both dimensions. The actual dimensions of the transcoded image remain the same, but the image loses all detail in each 16x16 macroblock of alpha-channel pixels. Typically, you should set this value only when the [ImageDataDiscard](#imagedatadiscard) property has the same value. |
| 4     | The alpha channel is completely discarded. The pixel format of the transcoded image is changed to reflect the removal of the alpha channel.                                                                                                                                                                                                                                                                                                                                |



 

For images that contain an interleaved alpha channel, the following value is valid.



| Value | Description                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 4     | The alpha channel is completely discarded. The pixel format of the transcoded image is changed to reflect the removal of the alpha channel. |



 

For interleaved alpha, unless this property is set to 4, the alpha channel is processed the same as the image data, according to the value of the [ImageDataDiscard](#imagedatadiscard) property.

### AlphaQuality

Sets the compression quality for the planar alpha channel image.



| Data type | VARTYPE     | Range | Default |
|-----------|-------------|-------|---------|
| **UCHAR** | **VT\_UI1** | 1–255 | 1       |



 

This property applies when the image has an alpha channel and the [InterleavedAlpha](#interleavedalpha) property is **VARIANT\_FALSE**. The value 1 indicates lossless mode. Increasing values result in higher compression ratios and lower image quality.

### BitmapTransform

Specifies whether the image is rotated or flipped when decoded.



| Data type | VARTYPE     | Range                                                                     | Default                       |
|-----------|-------------|---------------------------------------------------------------------------|-------------------------------|
| **UCHAR** | **VT\_UI1** | [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) | **WICBitmapTransformRotate0** |



 

### CompressedDomainTranscode

Enables or disables compressed domain transcoding.



| Data type         | VARTYPE      | Default           |
|-------------------|--------------|-------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_TRUE** |



 

To disable compressed domain operations, set this property to **VARIANT\_FALSE**.

### FrequencyOrder

Enables encoding in frequency order. Device implementations of JPEG XR encoders can organize a file in spatial order to reduce the memory required during encoding.



| Data type         | VARTYPE      | Default           |
|-------------------|--------------|-------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_TRUE** |



 

-   **VARIANT\_TRUE**: Frequency order. The lowest frequency data appears first in the file, and image content is grouped by its frequency rather than its spatial orientation. Organizing a file by frequency order provides the best performance for any frequency-based decoding.
-   **VARIANT\_FALSE**: Spatial order. Spatial order reduces the memory required during encoding

Frequency order is recommended unless you have performance or application-specific reasons to use spatial order.

### HorizontalTileSlices

Sets the number of horizontal tiles.



| Data type  | VARTYPE     | Range  | Default                      |
|------------|-------------|--------|------------------------------|
| **USHORT** | **VT\_UI2** | 0–4095 | (image width – 1) >> 8 |



 

The value is the number of horizontal subdivisions; that is, the number of horizontal tiles – 1.

### IgnoreOverlap

Specifies how the encoder handles tile boundaries during a compressed domain transcode.



| Data type         | VARTYPE      | Default            |
|-------------------|--------------|--------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_FALSE** |



 

This property is applied only if the [CompressedDomainTranscode](#compresseddomaintranscode) property is set to **VARIANT\_TRUE** and a sub-region transcode of exactly one or more tiles is performed.

The default operation for a region transcode is to expand the requested region to include the surrounding pixels that are required for overlap decoding of the region edges. If this property is set to **VARIANT\_TRUE**, the codec ignores the surrounding pixels, and only the selected tile or tiles are extracted. If the source image is not tiled or if the requested region includes partial tiles, this parameter is ignored.

### ImageDataDiscard

Sets the amount of image frequency data to discard during a compressed domain transcode.



| Data type | VARTYPE     | Range | Default |
|-----------|-------------|-------|---------|
| **UCHAR** | **VT\_UI1** | 0–3   | 0       |



 

This property applies only if the [CompressedDomainTranscode](#compresseddomaintranscode) property is set to **VARIANT\_TRUE**; otherwise it is ignored.



| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | No image frequency data is discarded.                                                                                                                                                                                                                                                                                                                                                                             |
| 1     | The flexbits are discarded. This arbitrarily reduces the quality of the transcoded image without changing the effective resolution of the image. The exact reduction in file size and quality depends on numerous factors and cannot be exactly specified. This value returns an error specified for an interleaved alpha channel.                                                                                |
| 2     | The high-pass frequency data band is discarded, including the flexbits. This reduces the resolution of the transcoded image by a factor of 4 in both dimensions. The actual dimensions of the transcoded image remain the same, but the image loses all detail in each 4x4 block of pixels. Therefore, the transcoded image should be downsampled accordingly whenever it is decoded.                             |
| 3     | Both the high-pass and low-pass frequency data bands are discarded, including the flexbits. This reduces the resolution of the transcoded image by a factor of 16 in both dimensions. The actual dimensions of the transcoded image remain the same, but the image loses all detail in each 16x16 macroblock of pixels. Therefore, the transcoded image should be downsampled accordingly whenever it is decoded. |



 

If the image contains an interleaved alpha channel, the value of [ImageDataDiscard](#imagedatadiscard) is applied to the alpha channel unless the [AlphaDataDiscard](#alphadatadiscard) property is set to 4, in which case the alpha channel is discarded.

For planar alpha, the frequency data that is discarded is controlled by the [AlphaDataDiscard](#alphadatadiscard) property.

### ImageQuality

Sets the image quality.



| Data type | VARTYPE    | Range | Default |
|-----------|------------|-------|---------|
| **FLOAT** | **VT\_R4** | 0–1.0 | 0.9     |



 

Level 1.0 gives mathematically lossless compression.

Level 0.0 is the lowest quality setting.

### InterleavedAlpha

Specifies whether to encode interleaved alpha or planar alpha.



| Data type         | VARTYPE      | Default            |
|-------------------|--------------|--------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_FALSE** |



 

-   **VARIANT\_TRUE**: Interleaved alpha. Alpha channel information is encoded as an additional interleaved channel, with no correlation to the image content channels. This mode is useful for decoding alpha simultaneously with the image when the image is streaming.
-   VARIANT\_FALSE: Planar alpha. A planar alpha channel is encoded as a separate image. The image data and the alpha channel are decoded independently. Optionally, you can set the quality level of the alpha channel by setting the [AlphaQuality](#alphaquality) property.

Interleaved alpha is supported only for certain RGB pixel formats. Planar alpha is supported for any image format that defines an alpha channel.

### Lossless

Enables losses compression.



| Data type         | VARTYPE      | Default        |
|-------------------|--------------|----------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | VARIANT\_FALSE |



 

If the value is **VARIANT\_TRUE**, the encoder uses lossless compression. When set to **VARIANT\_TRUE**, this property overrides the [ImageQuality](#imagequality) property.

### Overlap

Sets the level of overlap filtering. With overlap filtering, transform coefficients are applied across block and macroblock boundaries. This can reduce blocking artifacts.



| Data type | VARTYPE     | Range | Default |
|-----------|-------------|-------|---------|
| **UCHAR** | **VT\_UI1** | 0–4   | 1       |



 



| Value | Description                                   |
|-------|-----------------------------------------------|
| 0     | No overlap.                                   |
| 1     | One level of overlap, soft tiling. (Default.) |
| 2     | Two levels of overlap, soft tiling.           |
| 3     | One level of overlap, hard tiling             |
| 4     | Two levels of overlap, hard tiling.           |



 

Definitions:

-   One level of overlap: The encoded values of 4x4 blocks are modified based on neighboring blocks.
-   Two levels of overlap: The first level of overlap is applied. In addition, the encoded values of 16x16 macroblocks are modified based on the neighboring macroblocks.
-   Soft tiling: Overlap filtering is applied across tile boundaries.
-   Hard tiling: Overlap filtering is not applied across tile boundaries. Hard tiles can introduce some visual artifacts along tile boundaries.

If you set this property, also set [UseCodecOptions](#usecodecoptions) to **VARIANT\_TRUE**.

### ProgressiveMode

Enables or disables progressive encoding.



| Data type         | VARTYPE      | Default            |
|-------------------|--------------|--------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_FALSE** |



 



| Value              | Description                |
|--------------------|----------------------------|
| **VARIANT\_TRUE**  | Sequential mode (default). |
| **VARIANT\_FALSE** | Progressive mode.          |



 

### Quality

Sets the compression quality.



| Data type | VARTYPE     | Range | Default |
|-----------|-------------|-------|---------|
| **UCHAR** | **VT\_UI1** | 1–255 | 1       |



 

The value 1 indicates lossless mode. Increasing values result in higher compression ratios and lower image quality.

If you set this property, also set [UseCodecOptions](#usecodecoptions) to **VARIANT\_TRUE**.

### StreamOnly

Enables or disables stream-only mode.



| Data type         | VARTYPE      | Default            |
|-------------------|--------------|--------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_FALSE** |



 



| Value              | Description                                                            |
|--------------------|------------------------------------------------------------------------|
| **VARIANT\_TRUE**  | The encoder outputs the raw image stream without metadata.             |
| **VARIANT\_FALSE** | The encoder outputs the container format (image stream plus metadata). |



 

### Subsampling

Sets the chroma subsampling. This property applies only to RGB images.



| Data type | VARTYPE     | Range | Default                                                  |
|-----------|-------------|-------|----------------------------------------------------------|
| **UCHAR** | **VT\_UI1** | 0–3   | 3 if [ImageQuality](#imagequality) > 0.8; otherwise 1 |



 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td>4:4:4 encoding. Preserves full chroma resolution.</td>
</tr>
<tr class="even">
<td>2</td>
<td>4:2:2 encoding. Chroma resolution is ½ of luminance resolution.</td>
</tr>
<tr class="odd">
<td>1</td>
<td>4:2:0 encoding. Chroma resolution is ¼ of luminance resolution.</td>
</tr>
<tr class="even">
<td>0</td>
<td>4:0:0 encoding. Discards all chroma values and preserves luminance only.
<blockquote>
[!Note]<br />
This mode is not recommended, because the codec uses a slightly modified definition of luminance to improve performance. Instead, it is better to convert the image to monochrome before encoding.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

4:2:2 and 4:2:0 preserve luminance detail at the expense of color detail.

If you set this property, also set [UseCodecOptions](#usecodecoptions) to **VARIANT\_TRUE**.

### UseCodecOptions

Specifies whether to use the [Quality](#image-quality-settings), [Overlap](#overlap), and [Subsampling](#subsampling) properties instead of the generic [ImageQuality](#imagequality) property.



| Data type         | VARTYPE      | Default            |
|-------------------|--------------|--------------------|
| **VARIANT\_BOOL** | **VT\_BOOL** | **VARIANT\_FALSE** |



 

### VerticalTileSlices

Sets the number of horizontal tiles.



| Data type  | VARTYPE     | Range  | Default                       |
|------------|-------------|--------|-------------------------------|
| **USHORT** | **VT\_UI2** | 0–4095 | (image height – 1) >> 8 |



 

The value is the number of vertical subdivisions; that is, the number of vertical tiles – 1.

## Supported Color Formats

For more information about these formats, see [Native Pixel Formats](-wic-codec-native-pixel-formats.md).

-   **Integer RGB formats**
    -   GUID\_WICPixelFormat24bppRGB
    -   GUID\_WICPixelFormat24bppBGR
    -   GUID\_WICPixelFormat32bppBGR
    -   GUID\_WICPixelFormat48bppRGB
    -   GUID\_WICPixelFormat32bppBGRA
    -   GUID\_WICPixelFormat64bppRGBA
    -   GUID\_WICPixelFormat32bppPBGRA
    -   GUID\_WICPixelFormat64bppPRGBA
-   **Fixed-point RGB formats**
    -   GUID\_WICPixelFormat48bppRGBFixedPoint
    -   GUID\_WICPixelFormat64bppRGBFixedPoint
    -   GUID\_WICPixelFormat96bppRGBFixedPoint
    -   GUID\_WICPixelFormat128bppRGBFixedPoint
    -   GUID\_WICPixelFormat128bppRGBAFixedPoint
-   **Floating-point RGB formats**
    -   GUID\_WICPixelFormat48bppRGBHalf
    -   GUID\_WICPixelFormat64bppRGBHalf
    -   GUID\_WICPixelFormat128bppRGBFloat
    -   GUID\_WICPixelFormat64bppRGBAFixedPoint
    -   GUID\_WICPixelFormat64bppRGBAHalf
    -   GUID\_WICPixelFormat128bppRGBAFloat
    -   GUID\_WICPixelFormat128bppPRGBAFloat
-   **Grayscale formats**
    -   GUID\_WICPixelFormat8bppGray
    -   GUID\_WICPixelFormat16bppGray
    -   GUID\_WICPixelFormat16bppGrayFixedPoint
    -   GUID\_WICPixelFormat16bppGrayHalf
    -   GUID\_WICPixelFormat32bppGrayFixedPoint
    -   GUID\_WICPixelFormat32bppGrayFloat
-   **Packed formats**
    -   GUID\_WICPixelFormat16bppBGR555
    -   GUID\_WICPixelFormat16bppBGR565
    -   GUID\_WICPixelFormat32bppBGR101010
    -   GUID\_WICPixelFormat32bppRGBE
-   **CMYK formats**
    -   GUID\_WICPixelFormat40bppCMYKAlpha
    -   GUID\_WICPixelFormat64bppCMYK
    -   GUID\_WICPixelFormat80bppCMYKAlpha
-   **N-channel formats**
    -   GUID\_WICPixelFormat32bpp4Channels
    -   GUID\_WICPixelFormat40bpp5Channels
    -   GUID\_WICPixelFormat48bpp6Channels
    -   GUID\_WICPixelFormat56bpp7Channels
    -   GUID\_WICPixelFormat64bpp8Channels
    -   GUID\_WICPixelFormat32bpp3ChannelsAlpha
    -   GUID\_WICPixelFormat40bpp4ChannelsAlpha
    -   GUID\_WICPixelFormat48bpp5ChannelsAlpha
    -   GUID\_WICPixelFormat56bpp6ChannelsAlpha
    -   GUID\_WICPixelFormat64bpp7ChannelsAlpha
    -   GUID\_WICPixelFormat72bpp8ChannelsAlpha
    -   GUID\_WICPixelFormat48bpp3Channels
    -   GUID\_WICPixelFormat64bpp4Channels
    -   GUID\_WICPixelFormat80bpp5Channels
    -   GUID\_WICPixelFormat96bpp6Channels
    -   GUID\_WICPixelFormat128bpp8Channels
    -   GUID\_WICPixelFormat64bpp3ChannelsAlpha
    -   GUID\_WICPixelFormat80bpp4ChannelsAlpha
    -   GUID\_WICPixelFormat96bpp5ChannelsAlpha
    -   GUID\_WICPixelFormat112bpp6ChannelsAlpha
    -   GUID\_WICPixelFormat128bpp7ChannelsAlpha
    -   GUID\_WICPixelFormat144bpp8ChannelsAlpha

 

 
