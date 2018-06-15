---
Description: Group-of-pictures (GOP) start time code, for an MPEG-1 or MPEG-2 video media type.
ms.assetid: 8313b83c-5a0a-4aaa-bdc8-58a987c329c7
title: MF\_MT\_MPEG\_START\_TIME\_CODE attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_MPEG\_START\_TIME\_CODE attribute

Group-of-pictures (GOP) start time code, for an MPEG-1 or MPEG-2 video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwStartTimeCode** member of the [**MPEG1VIDEOINFO**](https://msdn.microsoft.com/en-us/library/Dd390700(v=VS.85).aspx) and [**MPEG2VIDEOINFO**](https://msdn.microsoft.com/en-us/library/Dd390707(v=VS.85).aspx) structures.

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
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




