---
Description: Specifies the previous characteristics of the media source.
ms.assetid: 9779f350-60d5-4129-bada-0c4a58f93e6a
title: MF\_EVENT\_SOURCE\_CHARACTERISTICS\_OLD attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_EVENT\_SOURCE\_CHARACTERISTICS\_OLD attribute

Specifies the previous characteristics of the media source. The attribute data is a bitwise **OR** of flags from the [**MFMEDIASOURCE\_CHARACTERISTICS**](/windows/win32/mfidl/ne-mfidl-_mfmediasource_characteristics?branch=master) enumeration.

## Data type

**UINT32**

## Remarks

This attribute is used with the [MESourceCharacteristicsChanged](mesourcecharacteristicschanged.md) event.

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

[Event Attributes](event-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master)
</dt> </dl>

 

 




