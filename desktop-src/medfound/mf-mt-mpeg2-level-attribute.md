---
Description: 'Specifies the MPEG-2 or H.264 level in a video media type.'
ms.assetid: '8dd8e8c4-5a6f-4a87-a643-73af35c362a9'
title: 'MF\_MT\_MPEG2\_LEVEL attribute'
---

# MF\_MT\_MPEG2\_LEVEL attribute

Specifies the MPEG-2 or H.264 level in a video media type.

## Data type

**UINT32**

## Remarks

For MPEG-2 video, the value of this attribute is a member of the [**AM\_MPEG2Level**](dshow.am_mpeg2level) enumeration.

For H.264 video, the value is a member of the [**eAVEncH264VLevel**](eavench264vlevel.md) enumeration.

This attribute corresponds to the **dwLevel** member of the [**MPEG2VIDEOINFO**](dshow.mpeg2videoinfo) structure.

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

 

 




