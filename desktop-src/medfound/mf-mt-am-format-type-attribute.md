---
Description: 'Contains a DirectShow format GUID for a media type.'
ms.assetid: 'dc532791-39e1-4acb-9e62-21d8f25be870'
title: 'MF\_MT\_AM\_FORMAT\_TYPE attribute'
---

# MF\_MT\_AM\_FORMAT\_TYPE attribute

Contains a DirectShow format GUID for a media type.

## Data type

**GUID**

## Remarks

This attribute might be set when a DirectShow media type is converted into a Media Foundation media type. The attribute indicates the original DirectShow format type. The value corresponds to the formattype member of the [**AM\_MEDIA\_TYPE**](dshow.am_media_type) structure.

For an audio format, the [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md) attribute might contain the original format block, if the DirectShow format type was not recognized.

Do not set this attribute on a media type unless you are converting a DirectShow format structure.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Media Type Conversions](media-type-conversions.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> <dt>

[**IMFAttributes::GetGUID**](imfattributes-getguid.md)
</dt> <dt>

[**IMFAttributes::SetGUID**](imfattributes-setguid.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[**MFCreateMediaTypeFromRepresentation**](mfcreatemediatypefromrepresentation.md)
</dt> </dl>

 

 




