---
Description: 'Raised by a media source when it starts a new stream.'
ms.assetid: '1bc8b265-b7a1-4068-89f7-c0da03dfb874'
title: MENewStream event
---

# MENewStream event

Raised by a media source when it starts a new stream.

When the [**IMFMediaSource::Start**](imfmediasource-start.md) method is called on a media source, the media source sends one event for each selected stream:

-   The source sends the MENewStream event if the stream was not selected in the previous call to [**Start**](imfmediasource-start.md), or this is the very first call to **Start** on this media source.

-   The source sends the [MEUpdatedStream](meupdatedstream.md) event if the stream was already selected in the previous call to [**Start**](imfmediasource-start.md).

No events are sent for unselected streams.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------------------|
| VT\_UNKNOWN<br/> | Contains a pointer to the stream's [**IMFMediaStream**](imfmediastream.md) interface.<br/> <br/> |



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




