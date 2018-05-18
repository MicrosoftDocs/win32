---
Description: 'The approximate time when the Media Session raised an event.'
ms.assetid: '58083bc8-59cc-4503-8fae-36fcd864921a'
title: 'MF\_SESSION\_APPROX\_EVENT\_OCCURRENCE\_TIME attribute'
---

# MF\_SESSION\_APPROX\_EVENT\_OCCURRENCE\_TIME attribute

The approximate time when the Media Session raised an event.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

Some events from the Media Session have this attribute. The value gives the approximate presentation time when the event was raised.

This attribute is a signed value, although it is stored as a **UINT64**.

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

[**IMFAttributes::GetUINT64**](imfattributes-getuint64.md)
</dt> <dt>

[**IMFAttributes::SetUINT64**](imfattributes-setuint64.md)
</dt> </dl>

 

 




