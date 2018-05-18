---
Description: 'Subtype GUID for a media type.'
ms.assetid: '8e600943-92f1-4936-8c00-842fc7f4cb57'
title: 'MF\_MT\_SUBTYPE attribute'
---

# MF\_MT\_SUBTYPE attribute

Subtype GUID for a media type.

## Data type

**GUID**

## Remarks

The subtype GUID defines a specific media format type within a major type. For example, within video, the subtypes include RGB-24, RGB-32, UYVY, AYUV, and so forth. Within audio, the subtypes include PCM audio, Windows Media Audio 9, and so forth.

For possible values, see the following topics:

-   [Audio Subtype GUIDs](audio-subtype-guids.md)
-   [Video Subtype GUIDs](video-subtype-guids.md)

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

[**IMFAttributes::GetGUID**](imfattributes-getguid.md)
</dt> <dt>

[**IMFAttributes::SetGUID**](imfattributes-setguid.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




