---
Description: 'Contains additional format data for a media type.'
ms.assetid: '020832c4-40a1-4d8b-ada0-7a04ce097bce'
title: 'MF\_MT\_USER\_DATA attribute'
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
| Converted [**VIDEOINFOHEADER**](dshow.videoinfoheader) or [**VIDEOINFOHEADER2**](dshow.videoinfoheader2) structure.   | Extra data that appears after the [**BITMAPINFOHEADER**](dshow.bitmapinfoheader) structure, not including the color table or color masks. |
| Converted [**WAVEFORMATEX**](dshow.waveformatex) or [**WAVEFORMATEXTENSIBLE**](dshow.waveformatextensible) structure. | Extra data that appears after the audio format structure.                                                                                 |



 

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

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




