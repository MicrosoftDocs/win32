---
Description: 'Contains flags that define the capabilities of the Media Session, based on the current presentation.'
ms.assetid: 'a78a3f3f-4ba1-41f3-b808-43f1e4975bb9'
title: 'MF\_EVENT\_SESSIONCAPS attribute'
---

# MF\_EVENT\_SESSIONCAPS attribute

Contains flags that define the capabilities of the Media Session, based on the current presentation.

## Data type

**UINT32**

## Remarks

This attribute contains a bitwise **OR** of zero or more flags. For a list of possible flags, see [**IMFMediaSession::GetSessionCapabilities**](imfmediasession-getsessioncapabilities.md).

This attribute is used with the [MESessionCapabilitiesChanged](mesessioncapabilitieschanged.md) event.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> </dl>

 

 




