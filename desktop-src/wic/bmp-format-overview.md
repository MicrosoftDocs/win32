---
description: This topic provides information about the native BMP codec available through the Windows Imaging Component (WIC).
ms.assetid: 85AC5A30-A915-439E-A10F-B2833DDA995C
title: BMP Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# BMP Format Overview

This topic provides information about the native BMP codec available through the Windows Imaging Component (WIC).

## Codec Identity

The following table provides codec identification information.



|                        |                       |
|------------------------|-----------------------|
| Formal Name(s)         | Windows Bitmap Format |
| File Name Extension(s) | bmp, dib              |
| MIME type              | image/bmp             |
| Specification Support  | BMP Specification v5  |



 

The following table lists the GUIDs used to identify the native BMP codec components.



| Component        | Friendly Name            | GUID                                |
|------------------|--------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatBmp | 0af1d87e-fcfe-4188-bdeba7906471cbe3 |
| Decoder          | CLSID\_WICBmpDecoder     | 6b462062-7cbf-400d-9fdb813dd10f2778 |
| Encoder          | CLSID\_WICBmpEncoder     | 69be8bb4-d66d-47c8-865aed1589433782 |



 

## Encoding

The WIC encoding API are designed to be codec-independent and therefore image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

### Encoder Options

WIC-enabled codecs differ at the encoding option level. Encoder options reflect the capabilities of an image encoder and each native codec supports a set of these encoder options. Encoder options can be basic WIC supported options available to all WIC enabled codes (though not necessarily supported) or codec-specific options designed by the image format codec. To manage these encoding options during the encoding process, WIC uses the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) interface . For more information about using the **IPropertyBag2** interface for WIC encoding see the [Encoding Overview](-wic-creating-encoder.md).

The following table lists the WIC encoder options supported by the native BMP codec.



| Property Name               | VARTYPE      | Value Range                      | Default Value      |
|-----------------------------|--------------|----------------------------------|--------------------|
| **EnableV5Header32bppBGRA** | **VT\_BOOL** | **VARIANT\_TRUE/VARIANT\_FALSE** | **VARIANT\_FALSE** |



 

### EnableV5Header32bppBGRA

Specifies whether to allow encoding data in the GUID\_WICPixelFormat32bppBGRA pixel format. If this option is set to **VARIANT\_TRUE**, the BMP will be written out with a BITMAPV5HEADER header.

The default value is **VARIANT\_FALSE**.

If an encoder option is present in the IPropertyBag2 option list that the codec does not support, it is ignored.

Note for 16-bit and 32-bit Windows BMP files, the BMP codec ignores any alpha channel, as many legacy image files contain invalid data in this extra channel. Starting with Windows 8, 32-bit Windows BMP files written using the **BITMAPV5HEADER** with valid alpha channel content are read as WICPixelFormat32bppBGRA

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

 

 
