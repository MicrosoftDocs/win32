---
Description: Specifies the MPEG-2 or H.264 level in a video media type.
ms.assetid: 8dd8e8c4-5a6f-4a87-a643-73af35c362a9
title: MF_MT_MPEG2_LEVEL attribute
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_MPEG2\_LEVEL attribute

Specifies the MPEG-2 or H.264 level in a video media type.

## Data type

**UINT32**

## Remarks

For MPEG-2 video, the value of this attribute is a member of the [**AM\_MPEG2Level**](https://msdn.microsoft.com/en-us/library/Dd373478(v=VS.85).aspx) enumeration.

For H.264 video, the value is a member of the [**eAVEncH264VLevel**](/windows/desktop/api/codecapi/ne-codecapi-eavench264vlevel) enumeration.

This attribute corresponds to the **dwLevel** member of the [**MPEG2VIDEOINFO**](https://msdn.microsoft.com/en-us/library/Dd390707(v=VS.85).aspx) structure.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




