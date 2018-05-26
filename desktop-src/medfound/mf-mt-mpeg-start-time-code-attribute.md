---
Description: Group-of-pictures (GOP) start time code, for an MPEG-1 or MPEG-2 video media type.
ms.assetid: 8313b83c-5a0a-4aaa-bdc8-58a987c329c7
title: MF\_MT\_MPEG\_START\_TIME\_CODE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_MPEG\_START\_TIME\_CODE attribute

Group-of-pictures (GOP) start time code, for an MPEG-1 or MPEG-2 video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwStartTimeCode** member of the [**MPEG1VIDEOINFO**](dshow.mpeg1videoinfo) and [**MPEG2VIDEOINFO**](dshow.mpeg2videoinfo) structures.

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
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




