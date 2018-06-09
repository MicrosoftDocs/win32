---
Description: This topic provides information about the native TIFF codec available through Windows Imaging Component (WIC).
ms.assetid: 021AAF33-A89E-4336-AEB1-1A0D79A14C75
title: TIFF Format Overview
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TIFF Format Overview

This topic provides information about the native TIFF codec available through Windows Imaging Component (WIC).

-   [Codec Identity](#codec-identity)
-   [Encoding](#encoding)
    -   [Encoder Options](#encoder-options)
-   [Decoding](#decoding)

## Codec Identity

The following table provides codec identification information.



|                        |                                 |
|------------------------|---------------------------------|
| Formal Name(s)         | Tagged Image File Format (TIFF) |
| File Name Extension(s) | tiff, tif                       |
| MIME type(s)           | image/tiff, image/tif           |
| Specification Support  | TIFF Specification 6.0          |



 

The following table lists the GUIDs used to identify the native TIFF codec components.



| Component        | Friendly Name             | GUID                                 |
|------------------|---------------------------|--------------------------------------|
| Container Format | GUID\_ContainerFormatTiff | 163bcc30-e2e9-4f0b-961da3e9fdb788a3  |
| Decoder          | CLSID\_WICTiffDecoder     | b54e85d9-fe23-499f-8b886acea7137502b |
| Encoder          | CLSID\_WICTiffEncoder     | 0131be10-2001-4c5f-a9b0cc88fab64ce8  |



 

## Encoding

The WIC encoding API are designed to be codec-independent and image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

### Encoder Options

WIC-enabled codecs differ at the encoding option level. Encoder options reflect the capabilities of an image encoder and each native codec supports a set of these encoder options. Encoder options can be basic WIC supported options available to all WIC enabled codes (though not necessarily supported) or codec-specific options designed by the image format codec. To manage these encoding options during the encoding process, WIC uses the [**IPropertyBag2**](c74297d0-919d-4cf5-b8f9-5bdbe5111df9) interface . For more information about using the **IPropertyBag2** interface for WIC encoding , see the [Encoding Overview](-wic-creating-encoder.md).

The TIFF codec uses basic WIC options. The following table lists the WIC encoder options supported by the native TIFF codec.



Basic WIC Encoder Options

Property Name

VARTYPE

Value Range

Default Value

CompressionQuality

VT\_R4

0 - 1.0

TIFFCompressionMethod

VT\_UI1

[**WICTiffCompressionOption**](/windows/desktop/api/Wincodec/ne-wincodec-wictiffcompressionoption)

[**WICTiffCompressionDontCare**](/windows/desktop/api/Wincodec/ne-wincodec-wictiffcompressionoption)



 

If an encoder option is present in the [**IPropertyBag2**](c74297d0-919d-4cf5-b8f9-5bdbe5111df9) option list that the codec does not support, it is ignored.

### CompressionQuality Option

Specifies the desired compression quality. 0.0 indicates the efficient compression schema available. Typically, this schema results in a faster encode but larger output. A value of 1.0 specifies the most efficient compression schema available. Typically, this schema results in a longer encode but producing smaller output.

The default value is .

### TIFFCompressionMethod Option

Specifies the TIFF compression method.

The default value is [**WICTiffCompressionDontCare**](/windows/desktop/api/Wincodec/ne-wincodec-wictiffcompressionoption).

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

 

 



