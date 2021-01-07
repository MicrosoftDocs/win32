---
description: This topic provides information about the native JPEG codec available through the Windows Imaging Component (WIC).
ms.assetid: 9DCBCE9B-965B-4C18-992C-EFFFF32FCE5E
title: JPEG Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# JPEG Format Overview

This topic provides information about the native JPEG codec available through the Windows Imaging Component (WIC).

## Codec Identity

The following table provides codec identification information.



|                        |                                         |
|------------------------|-----------------------------------------|
| Formal Name(s)         | Joint Photographic Experts Group (JPEG) |
| File Name Extension(s) | jpe, jpeg, jpg                          |
| MIME type              | image/jpeg, image/jpe, image/jpg        |
| Specification Support  | JFIF Specification 1.02                 |



 

The following table lists the GUIDs used to identify the native JPEG codec components.



| Component        | Friendly Name             | GUID                                |
|------------------|---------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatJpeg | 19e4a5aa-5662-4fc5-a0c01758028e1057 |
| Decoder          | CLSID\_WICJpegDecoder     | 9456a480-e88b-43ea-9e730b2d9b71b1ca |
| Encoder          | CLSID\_WICJpegEncoder     | 1a34f5c1-4a5a-46dc-b6441f4567e7a676 |



 

## Encoding

The WIC encoding API are designed to be codec-independent and image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

### Encoder Options

WIC-enabled codecs differ at the encoding option level. Encoder options reflect the capabilities of an image encoder and each native codec supports a set of these encoder options. Encoder options can be basic WIC supported options available to all WIC enabled codes (though not necessarily supported) or codec-specific options designed by the image format codec. To manage these encoding options during the encoding process, WIC uses the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) interface . For more information about using the **IPropertyBag2** interface for WIC encoding , see the [Encoding Overview](-wic-creating-encoder.md).

The JPEG codec uses basic WIC options. The following table lists the WIC encoder options supported by the native JPEG codec.



| Property Name                                        | VARTYPE           | Value Range                                                                       | Default Value                                                                  |
|------------------------------------------------------|-------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [ImageQuality](#imagequality-option)                 | VT\_R4            | 0 - 1.0                                                                           | 0.9                                                                            |
| [BitmapTransform](#bitmaptransform-option)           | VT\_UI1           | [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions)         | [**WICBitmapTransformRotate0**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions)      |
| [Luminance](#luminance-option)                       | VT\_UI4/VT\_ARRAY | 64 Entries (DCT)                                                                  | Default luminance table.                                                       |
| [Chrominance](#chrominance-option)                   | VT\_UI4/VT\_ARRAY | 64 Entries (DCT)                                                                  | Default chrominance table.                                                     |
| [JpegYCrCbSubsampling](#jpegycrcbsubsampling-option) | VT\_UI1           | [**WICJpegYCrCbSubsamplingOption**](/windows/desktop/api/Wincodec/ne-wincodec-wicjpegycrcbsubsamplingoption) | [**WICJpegYCrCbSubsampling420**](/windows/desktop/api/Wincodec/ne-wincodec-wicjpegycrcbsubsamplingoption) |
| [SuppressApp0](/windows)                       | VT\_BOOL          | **TRUE**/**FALSE**                                                                | **FALSE**                                                                      |



 

If an encoder option is present in the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) option list that the codec does not support, it is ignored.

### ImageQuality Option

Specifies the desired image fidelity. 0.0 indicates the lowest possible fidelity and 1.0 specifies the highest fidelity.

The default value is 0.9.

### BitmapTransform Option

Specifies how the image is to be transformed during image decoding. This option must be set to one of the [**WICBitmapTransformOptions**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions) enumeration values.

The default value is [**WICBitmapTransformRotate0**](/windows/desktop/api/Wincodec/ne-wincodec-wicbitmaptransformoptions).

### Luminance Option

Specifies the grayscale brightness level table to use for encoding.

### Chrominance Option

Specifies the chrominance table to use for encoding.

### JpegYCrCbSubsampling Option

Specifies the subsampling ratio to use for YCrCb encoding.

The default value is [**WICJpegYCrCbSubsampling420**](/windows/desktop/api/Wincodec/ne-wincodec-wicjpegycrcbsubsamplingoption).

### SuppressApp0 Option

Specifies whether to suppress the write of App0 metadata while encoding the image data.

The default value is **FALSE**.

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

The native JPEG codec also supports the [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) on frame decoding adding advaced options for decoding an image stream. For more information about these advanced options, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

 

 
