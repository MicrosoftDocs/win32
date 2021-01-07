---
description: Specifies the color primaries for a video media type.
ms.assetid: 56f31c1a-b610-4da0-9df4-76e15add672c
title: MF_MT_VIDEO_PRIMARIES attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_VIDEO\_PRIMARIES attribute

Specifies the color primaries for a video media type.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideoPrimaries**](/windows/desktop/api/mfobjects/ne-mfobjects-mfvideoprimaries) enumeration.

The [**MFVideoPrimaries**](/windows/desktop/api/mfobjects/ne-mfobjects-mfvideoprimaries) enumeration identifies color primaries associated with certain common video standards. If the media type uses color primaries that are not identified in the **MFVideoPrimaries** enumeration, set the [**MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES**](mf-mt-custom-video-primaries-attribute.md) attribute instead of this attribute.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Extended Color Information](extended-color-information.md)
</dt> </dl>

 

 




