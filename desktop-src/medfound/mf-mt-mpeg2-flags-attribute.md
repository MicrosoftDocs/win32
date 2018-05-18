---
Description: 'Contains miscellaneous flags for an MPEG-2 video media type.'
ms.assetid: '2e1bf3e3-c005-418b-b9fd-1d43c42dad6f'
title: 'MF\_MT\_MPEG2\_FLAGS attribute'
---

# MF\_MT\_MPEG2\_FLAGS attribute

Contains miscellaneous flags for an MPEG-2 video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwFlags** member of the [**MPEG2VIDEOINFO**](dshow.mpeg2videoinfo) structure. For a list of valid flags, see the documentation for **MPEG2VIDEOINFO**.

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
</dt> </dl>

 

 




