---
Description: 'Offset between the presentation time and the media source's time stamps.'
ms.assetid: '450f3c39-063e-4bf3-838a-0f7c240d6647'
title: 'MF\_EVENT\_PRESENTATION\_TIME\_OFFSET attribute'
---

# MF\_EVENT\_PRESENTATION\_TIME\_OFFSET attribute

Offset between the presentation time and the media source's time stamps.

## Data type

**UINT64**

## Remarks

The offset is calculated as follows: offset = presentation time − source time. This attribute is used with the following events:

-   [MESessionNotifyPresentationTime](mesessionnotifypresentationtime.md)
-   [MESessionStarted](mesessionstarted.md)

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

 

 




