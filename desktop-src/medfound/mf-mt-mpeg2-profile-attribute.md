---
Description: Specifies the MPEG-2 or H.264 profile in a video media type.
ms.assetid: 8c6a68cb-d976-4099-8934-064f0e8f6374
title: MF\_MT\_MPEG2\_PROFILE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_MPEG2\_PROFILE attribute

Specifies the MPEG-2 or H.264 profile in a video media type.

## Data type

**UINT32**

## Remarks

For MPEG-2 video, the value of this attribute is a member of the [**AM\_MPEG2Profile**](dshow.am_mpeg2profile) enumeration.

For H.264 video, the value is a member of the [**eAVEncH264VProfile**](/windows/win32/codecapi/ne-codecapi-eavench264vprofile?branch=master) enumeration.

This attribute corresponds to the **dwProfile** member of the [**MPEG2VIDEOINFO**](dshow.mpeg2videoinfo) structure.

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

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




