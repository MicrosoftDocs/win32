---
description: Specifies whether an ASF image stream is a degradable JPEG type.
ms.assetid: e29d0893-8561-4a8c-99e2-168186becd82
title: MF_MT_IMAGE_LOSS_TOLERANT attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_IMAGE\_LOSS\_TOLERANT attribute

Specifies whether an ASF image stream is a degradable JPEG type.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)

## Remarks

This attribute applies to the media type for image streams in ASF. If the value is **TRUE**, the stream is a degradable JPEG image type. Otherwise, the stream is a JFIF image type. For more information about these stream types, see the ASF specification.

In addition to the MF\_MT\_IMAGE\_LOSS\_TOLERANT attribute, the media type for an ASF image stream contains the following attributes:



| Attribute                                                 | Description                                |
|-----------------------------------------------------------|--------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md) | Contains the value **MFMediaType\_Image**. |
| [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md) | Gives the image size in pixels.            |



 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




