---
Description: Specifies whether a video media type requires the enforcement of copy protection.
ms.assetid: fb12ba38-a4f4-44fe-bf31-e731c56bb145
title: MF\_MT\_DRM\_FLAGS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_DRM\_FLAGS attribute

Specifies whether a video media type requires the enforcement of copy protection.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideoDRMFlags**](/windows/win32/mfapi/ne-mfapi-_mfvideodrmflags?branch=master) enumeration.

This attribute provides a hint to the application. It is not used to enforce copy protection or to specify the copy protection mechanism.

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

[MF\_SD\_PROTECTED](mf-sd-protected-attribute.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




