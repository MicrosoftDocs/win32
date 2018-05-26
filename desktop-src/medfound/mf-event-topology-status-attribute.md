---
Description: Specifies the status of a topology during playback.
ms.assetid: f7c93bad-1a64-45b0-ab5c-6edea4a1c0d1
title: MF\_EVENT\_TOPOLOGY\_STATUS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_EVENT\_TOPOLOGY\_STATUS attribute

Specifies the status of a topology during playback.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MF\_TOPOSTATUS**](/windows/win32/mfapi/ne-mfapi-mf_topostatus?branch=master) enumeration.

This attribute is used with the [MESessionTopologyStatus](mesessiontopologystatus.md) event.

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
</dt> </dl>

 

 




