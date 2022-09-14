---
description: Raised by the Media Session when a new presentation starts. This event indicates when the presentation will start and the offset between the presentation time and the source time.
ms.assetid: 67c7d5f3-ffaf-4359-a59c-bb26b992b6cd
title: MESessionNotifyPresentationTime event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESessionNotifyPresentationTime event

Raised by the Media Session when a new presentation starts. This event indicates when the presentation will start and the offset between the presentation time and the source time.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                                                                   | Description                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_START\_PRESENTATION\_TIME**](mf-event-start-presentation-time-attribute.md)<br/>                       | Starting time for the presentation.<br/> <br/>                                                      |
| [**MF\_EVENT\_PRESENTATION\_TIME\_OFFSET**](mf-event-presentation-time-offset-attribute.md)<br/>                     | Offset between the presentation time and the media source's time stamps.<br/> <br/>                 |
| [**MF\_EVENT\_START\_PRESENTATION\_TIME\_AT\_OUTPUT**](mf-event-start-presentation-time-at-output-attribute.md)<br/> | Presentation time when the media sinks will render the first sample of the new topology.<br/> <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




