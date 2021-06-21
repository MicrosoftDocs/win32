---
description: This topic provides information about the native PNG codec available through the Windows Imaging Component (WIC).
ms.assetid: 703217EA-70C8-4F86-B8DF-95468C78C8DA
title: PNG Format Overview
ms.topic: article
ms.date: 05/31/2018
---

# PNG Format Overview

This topic provides information about the native PNG codec available through the Windows Imaging Component (WIC).

## Codec Identity

The following table provides codec identification information.



|     Component          | Description                     |
|------------------------|---------------------------------|
| Formal Name(s)         | Portable Network Graphics (PNG) |
| File Name Extension(s) | png                             |
| MIME type              | image/png                       |
| Specification Support  | PNG Specification 1.2           |



 

The following table lists the GUIDs used to identify the native PNG codec components.



| Component        | Friendly Name            | GUID                                |
|------------------|--------------------------|-------------------------------------|
| Container Format | GUID\_ContainerFormatPng | 1b7cfaf4-713f-473c-bbcd6137425faeaf |
| Decoder          | CLSID\_WICPngDecoder     | 389ea17b-5078-4cde-b6ef25c15175c751 |
| Encoder          | CLSID\_WICPngEncoder     | 27949969-876a-41d7-9447568f6a35a4dc |



 

### Windows 8 and later

Starting with Windows 8 WIC provides an additional PNG decoder

## Encoding

The WIC encoding API are designed to be codec-independent and image encoding for WIC-enabled codecs is essentially the same. For more information about image encoding using the WIC API, see the [Encoding Overview](-wic-creating-encoder.md).

### Encoder Options

WIC-enabled codecs differ at the encoding option level. Encoder options reflect the capabilities of an image encoder and each native codec supports a set of these encoder options. Encoder options can be basic WIC supported options available to all WIC enabled codes (though not necessarily supported) or codec-specific options designed by the image format codec. To manage these encoding options during the encoding process, WIC uses the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) interface . For more information about using the **IPropertyBag2** interface for WIC encoding , see the [Encoding Overview](-wic-creating-encoder.md).

The PNG codec uses basic WIC encoder options. The following table lists the WIC encoder options supported by the native PNG codec.



| Property Name   | VARTYPE  | Value Range                                                 | Default Value                                                    |
|-----------------|----------|-------------------------------------------------------------|------------------------------------------------------------------|
| InterlaceOption | VT\_BOOL | **TRUE**/**FALSE**                                          | **FALSE**                                                        |
| FilterOption    | VT\_UI1  | [**WICPngFilterOption**](/windows/desktop/api/Wincodec/ne-wincodec-wicpngfilteroption) | [**WICPngFilterUnspecified**](/windows/desktop/api/Wincodec/ne-wincodec-wicpngfilteroption) |



 

If an encoder option is present in the [**IPropertyBag2**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) option list that the codec does not support, it is ignored.

### InterlaceOption

Specifies whether to encode the image data as interlaced.

The default value is **FALSE**.

### FilterOption

Specifies the filter option to use for image compression.

The default value is [**WICPngFilterUnspecified**](/windows/desktop/api/Wincodec/ne-wincodec-wicpngfilteroption).

## Decoding

The WIC decoding API are designed to be codec-independent and image decoding for WIC-enabled codecs is essentially the same. For more information about image decoding, see the [Decoding Overview](-wic-creating-decoder.md). For more information about using decoded image data, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

The native PNG codec also supports the [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) on frame decoding adding advanced options for decoding an image stream. For more information about these advanced options, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

 

 
