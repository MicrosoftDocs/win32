---
description: Raised by a media source when it restarts or seeks a stream that is already active.
ms.assetid: 2d91a267-e109-45f5-886b-11b883cc5509
title: MEUpdatedStream event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MEUpdatedStream event

Raised by a media source when it restarts or seeks a stream that is already active.

When the [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method is called on a media source, the media source sends one event for each selected stream:

-   The source sends the [MENewStream](menewstream.md) event if the stream was not selected in the previous call to [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start), or this is the very first call to **Start** on this media source.

-   The source sends the MEUpdatedStream event if the stream was already selected in the previous call to [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start).

No events are sent for unselected streams.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE                | Description                                                                                        |
|------------------------|----------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Pointer to the stream's [**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream) interface.<br/> <br/> |



## Remarks

On the first call to [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) in which a stream becomes active, the media source sends an [MENewStream](menewstream.md) event for the stream. On subsequent calls to **Start**, the media source sends an MEUpdatedStream event, until the stream is deselected.

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

 

 




