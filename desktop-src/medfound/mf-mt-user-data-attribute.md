---
Description: Contains additional format data for a media type.
ms.assetid: 020832c4-40a1-4d8b-ada0-7a04ce097bce
title: MF\_MT\_USER\_DATA attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_USER\_DATA attribute

Contains additional format data for a media type.

## Data type

Byte array

## Remarks

The meaning of the data in this attribute depends on the format that is described by the media type.



| Format Type                                                                                                           | Additional Format Data                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Media codec.                                                                                                  | Codec private data.                                                                                                                       |
| Converted [**VIDEOINFOHEADER**](https://msdn.microsoft.com/a175592b-0dc1-4001-b52f-785407965932) or [**VIDEOINFOHEADER2**](https://msdn.microsoft.com/5e3d5bf0-435f-45da-8409-a1463b56a7ae) structure.   | Extra data that appears after the [**BITMAPINFOHEADER**](https://msdn.microsoft.com/153c08a8-d32c-4e9d-9da9-b915eb172327) structure, not including the color table or color masks. |
| Converted [**WAVEFORMATEX**](https://www.bing.com/search?q=**WAVEFORMATEX**) or [**WAVEFORMATEXTENSIBLE**](https://www.bing.com/search?q=**WAVEFORMATEXTENSIBLE**) structure. | Extra data that appears after the audio format structure.                                                                                 |



 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




