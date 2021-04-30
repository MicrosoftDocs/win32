---
description: Specifies for a media type whether the media data is compressed.
ms.assetid: b44fb757-4390-4392-b1cb-37772b4ae3fb
title: MF_MT_COMPRESSED attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_COMPRESSED attribute

Specifies for a media type whether the media data is compressed.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

If this attribute is **TRUE**, the media type is a compressed format. Otherwise, either the media type is uncompressed or the compression type is not known.

This attribute is not guaranteed to be set to **TRUE** for all compressed formats, so applications should generally not rely this attribute. The most reliable way to determine whether a format is compressed is to maintain a list of known formats. If an application does not recognize a format, as specified in the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute, it should not assume anything about the compression of the format.

To determine whether a format uses temporal compression (meaning that some samples are computed as deltas from earlier samples), check the [**MF\_MT\_ALL\_SAMPLES\_INDEPENDENT**](mf-mt-all-samples-independent-attribute.md) attribute.

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
</dt> </dl>

 

 




