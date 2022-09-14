---
description: Contains flags that indicate which capabilities have changed in the Media Session, based on the current presentation.
ms.assetid: aa01d17f-f2ac-4504-b278-3edd90ab8a23
title: MF_EVENT_SESSIONCAPS_DELTA attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_EVENT\_SESSIONCAPS\_DELTA attribute

Contains flags that indicate which capabilities have changed in the Media Session, based on the current presentation.

## Data type

**UINT32**

## Remarks

This attribute contains a bitmask indicating which capabilities flags have changed. For a list of possible flags, see [**IMFMediaSession::GetSessionCapabilities**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-getsessioncapabilities). Bits are set to 1 in the bitmask for any of the following reasons:

-   The corresponding capabilities bit changed from 0 to 1.
-   The corresponding capabilities bit changed from 1 to 0.
-   The corresponding capabilities bit remained 1, but the details of the capability changed. For example, the maximum playback rate changed.

This attribute is used with the [MESessionCapabilitiesChanged](mesessioncapabilitieschanged.md) event.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> </dl>

 

 




