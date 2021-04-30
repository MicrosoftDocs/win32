---
description: Signals an event from a media sink that renders media data.
ms.assetid: bb7db7c9-c39f-4bf4-9412-42525c4f2ea3
title: MERendererEvent event (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MERendererEvent event

Signals an event from a media sink that renders media data.

The [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR) sends this event when it receives a user event from the EVR presenter.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue) include the following.



| VARTYPE           | Description                        |
|-------------------|------------------------------------|
| VT\_I4<br/> | Event code.<br/> <br/> |



## Remarks

If the presenter calls the EVR's **IMediaEventSink::Notify** method with an event code in the range EC\_USER or higher, the EVR sends this event. The event data is the event code that was passed to the **Notify** method.

The original event parameters (*EventParam1* and *EventParam2* in the **IMediaEventSink::Notify** method) are ignored, so the presenter should set these values to **NULL**.

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

 

 




