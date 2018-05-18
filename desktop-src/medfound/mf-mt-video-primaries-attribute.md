---
Description: 'Specifies the color primaries for a video media type.'
ms.assetid: '56f31c1a-b610-4da0-9df4-76e15add672c'
title: 'MF\_MT\_VIDEO\_PRIMARIES attribute'
---

# MF\_MT\_VIDEO\_PRIMARIES attribute

Specifies the color primaries for a video media type.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideoPrimaries**](mfvideoprimaries.md) enumeration.

The [**MFVideoPrimaries**](mfvideoprimaries.md) enumeration identifies color primaries associated with certain common video standards. If the media type uses color primaries that are not identified in the **MFVideoPrimaries** enumeration, set the [**MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES**](mf-mt-custom-video-primaries-attribute.md) attribute instead of this attribute.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Extended Color Information](extended-color-information.md)
</dt> </dl>

 

 




