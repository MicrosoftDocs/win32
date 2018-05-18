---
Description: 'Describes how chroma was sampled for a Y''Cb''Cr'' video media type.'
ms.assetid: '0c930348-8669-42cc-9d74-df9ef475bdc8'
title: 'MF\_MT\_VIDEO\_CHROMA\_SITING attribute'
---

# MF\_MT\_VIDEO\_CHROMA\_SITING attribute

Describes how chroma was sampled for a Y'Cb'Cr' video media type.

## Data type

**UINT32**

## Remarks

The value of this attribute is a bitwise **OR** of flags from the [**MFVideoChromaSubsampling**](mfvideochromasubsampling.md) enumeration.

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

 

 




