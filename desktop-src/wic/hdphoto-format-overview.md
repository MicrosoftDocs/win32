---
description: This topic provides information about the native HD Photo codec available through the Windows Imaging Component (WIC).
ms.assetid: C73752AB-3D6E-4D92-9FDE-CB68B6A9743C
title: HD Photo Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# HD Photo Format Overview

This topic provides information about the native HD Photo codec available through the Windows Imaging Component (WIC).

> [!IMPORTANT]
>
> The HD Photo format is a pre-standard implementation of the JPEG XR format. The JPEG XR format has been fully implemented in Windows 8. See the [JPEG XR Codec Overview](jpeg-xr-codec.md) for more information.

 

This topic contains the following sections.

-   [Codec Identity](#codec-identity)
-   [Encoding](#encoding)
    -   [Encoder Options](#encoder-options)
-   [Decoding](#decoding)
    -   [IWICBitmapSourceTransform Support](#iwicbitmapsourcetransform-support)

## Codec Identity

The following table provides codec identification information.



|   Component            | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| Formal Name(s)         | HD Photo, Windows Media Photo                                                   |
| File Name Extension(s) | wdp                                                                             |
| MIME type              | image/vnd.ms-photo                                                              |
| File Signature(s)      | First four bytes: 0x4949bc00 (Version 0; pre-release), 0x4949bc01 (Version 1.0) |



 

The following table lists the GUIDs used to identify the native HD Photo codec components.



| Component        | Friendly Name            | GUID                                |
|------------------|--------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatWmp | 57a37caa-367a-4540-916bf183c5093a4b |
| Decoder          | CLSID\_WICWmpDecoder     | a26cec36-234c-4950-ae16e34aace71d0d |
| Encoder          | CLSID\_WICWmpEncoder     | ac4ce3cb-e1c1-44cd-82155a1665509ec2 |



 

## Encoding

The WIC encoding API are designed to be codec-independent and image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

### Encoder Options

WIC-enabled codecs differ at the encoding option level. Encoder options reflect the capabilities of an image encoder and each native codec supports a set of these encoder options. Encoder options can be basic WIC supported options available to all WIC enabled codes (though not necessarily supported) or codec-specific options designed by the image format codec. To manage these encoding options during the encoding process, WIC uses the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) interface . For more information about using the **IPropertyBag2** interface for WIC encoding, see the [Encoding Overview](-wic-creating-encoder.md).

The HD Photo codec uses both basic WIC options and provides several HD Photo specific encoding options. The following table lists the encoder options supported by the native HD Photo codec.

Basic WIC Encoder Options

| Property Name | VARTYPE | Value Range | Default Value |
|---------------|---------|-------------|---------------|
| [ImageQuality](#imagequality-option) | VT\_R4 | 0 - 1.0 | 0.9 |
| [Lossless](#lossless-option) | VT\_BOOL | **TRUE**, **FALSE** | **FALSE** |
| [BitmapTransform](#bitmaptransform-option) | VT\_UI1 | [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) |   [**WICBitmapTransformRotate0**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) |

HD Photo Specific Encoder Options

| Property Name | VARTYPE | Value Range | Default Value |
|---------------|---------|-------------|---------------|
| [UseCodecOptions](#usecodecoptions-option) | VT\_BOOL | **TRUE**, **FALSE** | **FALSE** |
| [Quality](#quality-option) | VT\_UI1 | 1 - 255 | 10 |
| [Overlap](#overlap-option) | VT\_UI1 | 0 - 2 | 1 |
| [Subsampling](#subsampling-option) | VT\_UI1 | 0 - 3 | 3 if ImageQuality > 0.8; otherwise 1; |
| [HorizontalTileSlices](#horizontaltileslices-verticaltileslices-options) | VT\_UI2 | 0 - 4095 | (image width – 1) >> 8 |
| [VerticalTileSlices](#horizontaltileslices-verticaltileslices-options) | VT\_UI2 | 0 - 4095 | (image height – 1) >> 8 |
| [FrequencyOrder](#frequencyorder-option) | VT\_BOOL | **TRUE**, **FALSE** | **TRUE** |
| [InterleavedAlpha](#interleavedalpha-option) | VT\_BOOL | **TRUE**, **FALSE** | **FALSE** |
| [AlphaQuality](#alphaquality-option) | VT\_UI1 | 1 - 255 | 1 |
| [CompressedDomainTranscode](#compresseddomaintranscode-option) | VT\_BOOL | **TRUE**, **FALSE** | **TRUE** |
| [ImageDataDiscard](#imagedatadiscard-option) | VT\_UI1 | 0 - 3 | 0 |
| [AlphaDataDiscard](#alphadatadiscard-option) | VT\_UI1 | 0 - 4 | Not Used. |
| [IgnoreOverlap](#ignoreoverlap-option) | VT\_BOOL | **TRUE**, **FALSE** | **FALSE** |


If an encoder option is present in the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) option list that the codec does not support, it is ignored.

### ImageQuality Option

Specifies the desired image fidelity. 0.0 indicates the lowest possible fidelity and 1.0 specifies the highest fidelity. For the HD Photo image format, a 1.0 value results in a mathematically lossless compression.

The default value is 0.9.

### CompressionQuality Option

Specifies the desired compression quality. 0.0 indicates the efficient compression schema available. Typically, this schema produces a faster encode but larger output. A value of 1.0 specifies the most efficient compression schema available, which typically produces a longer encode but a smaller output.

HD Photo does not support this encoder option. This value is ignored if present in the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) parameter list.

### Lossless Option

Specifies whether to use losses compression mode. For the HD Photo image format, this value overrides the [ImageQuality](#imagequality-option) option value.

The default value is **FALSE**.

### BitmapTransform Option

Specifies how the image is transformed during image decoding. You must set this option to one of the [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) enumeration values.

The default value is [**WICBitmapTransformOptions::WICBitmapTransformRotate0**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions).

### UseCodecOptions Option

If the value is VARIANT\_TRUE the [Quality](#quality-option), [Overlap](#overlap-option), and [Subsampling](#subsampling-option) options instead of the option value.

The default value is **FALSE**.

### Quality Option

Specifies the compression quality for the image. A value of 1 indicates lossless mode. Increasing values result in higher compression ratios and lower image quality.

The default value is 10.

### Overlap Option

Specifies the level of overlap processing.

The following table lists the available overlap processing levels.



| Value | Description                                                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | No overlap processing is enabled.                                                                                                                                                           |
| 1     | One level of overlap processing is enabled, modifying 4x4 block encoded values based on values of neighboring blocks.                                                                       |
| 2     | Two levels of overlap processing are enabled. In addition to the first level processing, encoded values of 16x16 macro blocks are modified based on the values of neighboring macro blocks. |



 

The default value is 1.

### Subsampling Option

Specifies additional compression in the chroma space. In this way, you can preserve luminance detail at the expense of color detail . This option applies only to RGB images.

The following table lists the available subsampling options.



| Value | Description                                                                                                                                                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3     | 4:4:4 encoding preserves full chroma resolution.                                                                                                                                                                                                                                            |
| 2     | 4:2:2 encoding reduces chroma resolution to ½ of luminance resolution.                                                                                                                                                                                                                      |
| 1     | 4:2:0 encoding reduces chroma resolution to ¼ of luminance resolution.                                                                                                                                                                                                                      |
| 0     | 4:0:0 encoding discards all chroma content, and preserves luminance only. Because the codec uses a slightly modified definition of luminance to improve performance, we recommend that you convert an RGB image to monochrome before encoding rather than use this chroma subsampling mode. |



 

The default value is 3 if [ImageQuality](#imagequality-option) > 0.8; otherwise 1.

### HorizontalTileSlices, VerticalTileSlices Options

Specify the horizontal and vertical tiling of the image before you perform compression encoding for the optimal performance of region decode . By dividing the image into rectangular tiles during encoding you can decode regions of the image without processing the entire compressed data stream. The default value of 0 specifies no subdivision, so the entire image is treated as a single tile. A value of 1 for each parameter creates a single horizontal and a single vertical division, effectively dividing the image into four equally sized tiles. The maximum value of 4095 for each parameter divides the image into 4096 tile rows with 4096 tiles per row. In other words, the parameter values equal the number of horizontal and vertical tiles (respectively) minus 1. A tile can never be smaller than 16 pixels in width or height, so the HD Photo encoder might adjust this parameter to maintain the required minimum tile size. Because there is storage and processing overhead associated with each tile, you should choose these values carefully to meet the specific scenario.

[HorizontalTileSlices](/windows): The default value is (Image Width – 1) >> 8.

[VerticalTileSlices](/windows): The default value is (Image Height – 1) >> 8.

### FrequencyOrder Option

Specifies that the image must be encoded in frequency order. The lowest frequency data appears first in the file, and image content is grouped by its frequency rather than its spatial orientation. Organizing a file by frequency order provides the best performance for any frequency-based decoding, and therefore we recommend it. Device implementations of HD Photo encoders can organize a file in spatial order to reduce the memory footprint required during encoding.

The default value is **TRUE** and we recommend that applications and devices always use frequency order unless you have performance or application-specific reasons to use spatial order.

### InterleavedAlpha Option

Setting this option to **TRUE** instructs the codec to encode the alpha channel information as an additional interleaved channel, with no correlation to the image content channels. This mode is useful when you need to decode alpha simultaneously with the image in a streaming scenario.

Setting this parameter to **FALSE** results in a planar alpha channel, encoded as a separate image with its own optional Quality value. By using a Planar alpha channel you can decode the image data and the alpha channel independently. Interleaved alpha channels are supported only for certain RGB pixel formats. You can associate a Planar alpha channel with any image format that defines an alpha channel.

The default value is **FALSE**.

### AlphaQuality Option

Specifies the compression quality for the planar alpha channel image. A value of 1 sets lossless mode. Increasing values result in higher compression ratios and lower image quality.

The default value is 1.

### CompressedDomainTranscode Option

By using HD Photo you can perform a number of file transformation operations without actually decoding the compressed data and re-encoding it to the destination file. Compressed domain operations are very efficient and avoid any additional quality loss that is typical when you decode and re-encode a lossy-compressed image.

The following compressed domain operations are supported:

-   Crop a region of the image.
-   Perform a rotation/flip transformation.
-   Discard frequency data (making it possible to create a smaller image file.)
-   Reorganize the image between spatial and frequency sequential order.

The HD Photo encoder performs a compressed domain transcode operation when it encodes an HD Photo image by using an HD Photo decoder as the image source. Depending on the encoding options you selected, the codec uses a compressed domain operation if possible. If an application chooses to explicitly inhibit any compressed domain transcode operations, you should set the *UseCodecOptions* option to **TRUE** and the *CompressedDomainTranscode* option to **FALSE**.

When the codec performs a compressed domain operation, only certain encoder parameter and property settings are allowed.

-   The basic encoder options [ImageQuality](#imagequality-option), [CompressionQuality](/windows) and [Lossless](#lossless-option) are ignored.
-   The HD Photo-specific encoder options [Quality](#quality-option), [Overlap](#overlap-option), [InterleavedAlpha](#interleavedalpha-option) and [AlphaQuality](#alphaquality-option) are ignored.
-   If present, the [HorizontalTileSlices](/windows) and [VerticalTileSlices](/windows) options must be set to zero. The tile size of an image cannot be changed as part of a compressed domain transcode.
-   You can change the image organization between frequency and spatial ordering by specifying the appropriate value of the [FrequencyOrdering](/windows) options.
-   A cardinal rotation and/or horizontal/vertical flip operation can be performed based on the value specified in the [BitmapTransform](#bitmaptransform-option) encoder option.
-   The image can be cropped by specifying the desired region using the [**WICRect**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapframeencode-writesource) parameter of the **WriteSource** encoder method.
-   Image and/or alpha data can be discarded by specifying the appropriate values in the [ImageDataDiscard](#imagedatadiscard-option) and/or [AlphaDataDiscard](#alphadatadiscard-option) options, reducing the encoded file size and effectively reducing the resolution of the new image.

The default value is **TRUE** and we recommend that applications and devices always use the frequency order unless you have specific performance or application reasons to use the spatial order.

### ImageDataDiscard Option

This parameter is valid only if the [CompressedDomainTranscode](#compresseddomaintranscode-option) option is **TRUE**; otherwise it is ignored. [ImageDataDiscard](#imagedatadiscard-option) specifies the amount of image data to discard during a compressed domain transcode. If the image contains an interleaved alpha channel, this data discard applies also to the alpha channel, with the exceptions as described later in this section.

The following values are allowed.



| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | No image frequency data is discarded.                                                                                                                                                                                                                                                                                                                                                                                        |
| 1     | The FlexBits are discarded, making an arbitrary reduction of the quality of the transcoded image without changing the effective resolution of the image. The exact file size reduction or the specific quality reduction depends on numerous factors and cannot be specified or predicted. This valuereturns an error if you specify it for an interleaved alpha channel.                                                    |
| 2     | The HighPass frequency data band is discarded (which also includes the FlexBits), effectively reducing the resolution of the transcoded image by a factor of 4 in both dimensions. The actual dimensions of the transcoded image remain the same, but it loses all detail in each 4x4 block of pixels. Therefore, you should down-sample the transcoded image accordingly whenever you decode it.                            |
| 3     | Both the HighPass and LowPass frequency data bands are discarded (which also includes the FlexBits), effectively reducing the resolution of the transcoded image by a factor of 16 in both dimensions. The actual dimensions of the transcoded image remain the same, but it loses all detail in each 16x16 macroblock of pixels. Therefore, you should down-sample the transcoded image accordingly whenever you decode it. |



 

The default value is 0.

### AlphaDataDiscard Option

This option is valid only if the [CompressedDomainTranscode](#compresseddomaintranscode-option) property is **TRUE** and the image contains either a planar or interleaved alpha channel; otherwise it is ignored. It specifies the amount of alpha frequency data to discard during a compressed domain transcode. The following values are allowed for a planar alpha channel.



| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | No image frequency data is discarded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1     | The FlexBits are discarded, making an arbitrary reduction of the quality of the planar alpha channel for the transcoded image without changing the effective resolution. The exact file size reduction or the specific quality reduction depends on numerous factors and cannot be specified or predicted.                                                                                                                                                                                                                                                |
| 2     | The HighPass frequency data band is discarded (which also includes the FlexBits), effectively reducing the resolution of the transcoded image planar alpha channel by a factor of 4 in both dimensions. The actual dimensions of the transcoded image remain the same, but the image loses all planar alpha channel detail in each 4x4 block of pixels. Therefore, the transcoded image should be down-sampled accordingly whenever it is decoded. Typically, you should set this value only when you set the ImageDataDiscard propertyto the same value. |
| 3     | Both the HighPass and LowPass frequency data bands are discarded (which also includes the FlexBits), effectively reducing the resolution of the transcoded image by a factor of 16 in both dimensions. The actual dimensions of the transcoded image remain the same, but the image loses all detail in each 16x16 macroblock of pixels. Therefore, the transcoded image should be down-sampled accordingly whenever it is decoded. Typically, you should set this value only when you set the ImageDataDiscard property to the same value.               |
| 4     | The Alpha channel is completely discarded. The pixel format of the transcoded image is changed to reflect the removal of the alpha channel.                                                                                                                                                                                                                                                                                                                                                                                                               |



 

For images that contain interleaved alpha channels, unless this property is set to 4, the alpha channel is processed the same as the image data, according to the value of the ImageDataDiscard property. If this property is set to 4, the interleaved alpha channel is completely discarded and the pixel format of the transcoded image is changed accordingly.

No default value.

### IgnoreOverlap Option

This option is valid only if the [CompressedDomainTranscode](#compresseddomaintranscode-option) property is **TRUE** and a sub-region transcode of exactly one or more tiles is requested. The default operation for a region transcode (or decode) is to expand the requested region to include the surrounding pixels that are required for overlap decoding of the region edges. When this parameter is set to **TRUE**, the surrounding pixels are ignored and only the selected tile or tiles are extracted. Again, this requires that the requested region exactly match the coordinates of one or more tiles. If the source image is not tiled or if the requested region specifies any partial tiles, this parameter is ignored.

The default value is **FALSE**.

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

### IWICBitmapSourceTransform Support

In addition to the interfaces required to be a WIC-enabled codec, the native HD Photo decoder also supports the [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform). The **IWICBitmapSourceTransform** interface provides an advanced option for decoding an image bit stream. Rather than just return a complete image using [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode), **IWICBitmapSourceTransform** interface enables the following decoder options.

-   Decode a rectangular sub-region of the image.
-   Decode to a lower resolution
-   Decode to a different pixel format
-   Perform a transformation (rotation/flip) while decoding

The native HD Photo codec provides the following level of support for the [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) interface.

### DoesSupportTransform

Native implementation supports all [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) transforms.

### GetClosestSize

For requests that are less than ½ the dimension of the source image in both dimensions, HD Photo returns the next largest integer image size that is evenly divisible by a factor of two. For all other requested sizes, HD Photo returns the original image dimensions.

### GetClosestPixelFormat

HD Photo returns the pixel format of the encoded image.

### CopyPixels

HD Photo accepts any requested region specified by the [**WICRect**](/windows/desktop/api/Wincodec/ns-wincodec-wicrect) parameter and returns that portion of the image.

The *uiWidth* and *uiHeight* parameters must specify dimensions as returned by the [**GetClosestSize**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestsize) function. Any other values return an error.

The *pguidDstFormat* parameter must specify the pixel format returned by the [**GetClosestPixelFormat**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestpixelformat) function. Any other value returns an error.

HD Photo accepts any allowable value for the *dstTransform* parameter. Note that the values allowed by WIC for this parameter are different from the values used by HD Photo for the Transformation metadata tag.

 

 
