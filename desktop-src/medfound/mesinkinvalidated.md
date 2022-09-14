---
description: Raised when a media sink becomes invalid.
ms.assetid: fa75926e-7cef-44da-9efe-f2f86fd4fd45
title: MESinkInvalidated event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MESinkInvalidated event

Raised when a media sink becomes invalid.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE              | Description                           |
|----------------------|---------------------------------------|
| VT\_EMPTY<br/> | No event data.<br/> <br/> |



## Attributes

The following attributes are defined for this event.



| Attribute                                                                    | Description                                                              |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**MF\_EVENT\_OUTPUT\_NODE**](mf-event-output-node-attribute.md)<br/> | Identifies the topology node for this media sink.<br/> <br/> |



## Remarks

The Media Session raises this event if it receives any of the following events from the media sink:

-   [MEAudioSessionDeviceRemoved](meaudiosessiondeviceremoved.md)

-   [MEAudioSessionDisconnected](meaudiosessiondisconnected.md)

-   [MEAudioSessionExclusiveModeOverride](meaudiosessionexclusivemodeoverride.md)

-   [MEAudioSessionFormatChanged](meaudiosessionformatchanged.md)

-   [MEAudioSessionServerShutdown](meaudiosessionservershutdown.md)

A media sink can also raise this event, in which case the Media Session sets the [**MF\_EVENT\_OUTPUT\_NODE**](mf-event-output-node-attribute.md) attribute on the event and forwards the event to the application.

If the application receives this event, it needs to recreate the media sink and queue the topology again.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




