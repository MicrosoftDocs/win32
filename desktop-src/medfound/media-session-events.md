---
description: Media Session Events
ms.assetid: 882a01f2-8f5c-4640-a8ac-f4f5860d7ed1
title: Media Session Events
ms.topic: article
ms.date: 05/31/2018
---

# Media Session Events

Most of the Media Session's operations are performed asynchronously, so the application must listen for events by using the Media Session's [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. (The [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) interface inherits **IMFMediaEventGenerator**.) The exact sequence of events will depend on your application, but the following events are raised by the Media Session in almost any situation.



| Event                                                                  | Description                                                                                                                                                                                                                    |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MEEndOfPresentation](meendofpresentation.md)                         | Raised when the media source has completed the presentation. Data might still be moving through the pipeline at this time.                                                                                                     |
| [MEError](meerror.md)                                                 | Raised if an error occurs during streaming.                                                                                                                                                                                    |
| [MESessionClosed](mesessionclosed.md)                                 | Raised when the [**Close**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-close) method completes. This event is the last event that the Media Session queues. After you receive this event, it is safe to shut down any media sources that you created. |
| [MESessionEnded](mesessionended.md)                                   | Raised when the Media Session is done with the last presentation.                                                                                                                                                              |
| [MESessionNotifyPresentationTime](mesessionnotifypresentationtime.md) | Notifies the application of the presentation time when the new presentation will start.                                                                                                                                        |
| [MESessionStarted](mesessionstarted.md)                               | Raised when the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) method completes. Unless an error occurred, data is moving through the pipeline at this point.                                                                          |
| [MESessionTopologySet](mesessiontopologyset.md)                       | Raised when the [**SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) method completes. Unless an error occurs, the application does not need to take any action.                                                                 |
| [MESessionTopologyStatus](mesessiontopologystatus.md)                 | Raised at various times when the status of a topology changes.                                                                                                                                                                 |



 

The [**IMFMediaSession::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-shutdown) method does not raise an event. The **Shutdown** method is synchronous. After this method returns, it is safe to release your event callback pointer.

In addition to events from the Media Session, the application might receive events from the media sinks in the topology. These can be custom events defined by the media sink, which might contain arbitrary data. For example, the sink might derive the event data from the source data, which can be from an untrusted external source. An application should ignore any events that it does not recognize, and exercise caution when parsing event data.

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> </dl>

 

 



