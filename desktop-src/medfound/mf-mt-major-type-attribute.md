---
Description: 'Major type GUID for a media type.'
ms.assetid: 'b88b5fcf-8025-4638-930d-9fc5cf0ec8a3'
title: 'MF\_MT\_MAJOR\_TYPE attribute'
---

# MF\_MT\_MAJOR\_TYPE attribute

Major type GUID for a media type.

## Data type

**GUID**

## Remarks

The major type defines the overall category of the media data. Major types include video, audio, script, and so forth. For a list of possible values, see [Major Media Types](media-type-guids.md).

An alternate way to retrieve this attribute is to call [**IMFMediaType::GetMajorType**](imfmediatype-getmajortype.md).

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

 

 




