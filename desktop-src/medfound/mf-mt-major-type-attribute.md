---
description: Major type GUID for a media type.
ms.assetid: b88b5fcf-8025-4638-930d-9fc5cf0ec8a3
title: MF_MT_MAJOR_TYPE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_MAJOR\_TYPE attribute

Major type GUID for a media type.

## Data type

**GUID**

## Remarks

The major type defines the overall category of the media data. Major types include video, audio, script, and so forth. For a list of possible values, see [Major Media Types](media-type-guids.md).

An alternate way to retrieve this attribute is to call [**IMFMediaType::GetMajorType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediatype-getmajortype).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetGUID**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getguid)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setguid)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




