---
Description: Contains miscellaneous flags for an MPEG-2 video media type.
ms.assetid: 2e1bf3e3-c005-418b-b9fd-1d43c42dad6f
title: MF\_MT\_MPEG2\_FLAGS attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_MPEG2\_FLAGS attribute

Contains miscellaneous flags for an MPEG-2 video media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **dwFlags** member of the [**MPEG2VIDEOINFO**](https://msdn.microsoft.com/1a6ab686-99a1-40c2-addf-7fa215e2311a) structure. For a list of valid flags, see the documentation for **MPEG2VIDEOINFO**.

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

 

 




