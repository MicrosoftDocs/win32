---
description: Media Source Events
ms.assetid: c7b6ea86-e919-45b8-a1f9-bd18c3aed163
title: Media Source Events
ms.topic: article
ms.date: 05/31/2018
---

# Media Source Events

This topic lists the events that are sent by media sources and media streams. Media sources can also send custom events not listed here.

## Media Source Events



| Event                                                                      | Description                                                                                      |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [MEEndOfPresentation Event](meendofpresentation.md)                       | The presentation ended. All streams in the presentation have reached the end of the stream.      |
| [MENewStream Event](menewstream.md)                                       | A new stream was created. The event contains a pointer to the stream.                            |
| [MESourceCharacteristicsChanged Event](mesourcecharacteristicschanged.md) | The characteristics of the source have changed. (Optional.)                                      |
| [MESourceMetadataChanged Event](mesourcemetadatachanged.md)               | The source's metadata has changed. (Optional.)                                                   |
| [MESourcePaused Event](mesourcepaused.md)                                 | The source was paused. Not all sources support pausing.                                          |
| [MESourceRateChanged Event](mesourceratechanged.md)                       | The source's playback rate has changed. (Optional; applies if the source supports rate control.) |
| [MESourceRateChangeRequested Event](mesourceratechangerequested.md)       | The source is requesting a new playback rate. (Optional.)                                        |
| [MESourceSeeked Event](mesourceseeked.md)                                 | The source was seeked. Not all sources support seeking.                                          |
| [MESourceStarted Event](mesourcestarted.md)                               | The source was started.                                                                          |
| [MESourceStopped Event](mesourcestopped.md)                               | The source was stopped.                                                                          |
| [MEUpdatedStream Event](meupdatedstream.md)                               | An existing stream was seeked or re-started. The event contains a pointer to the stream.         |



 

## Media Stream Events



| Event                                                    | Description                                                                                                                    |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [MEEndOfStream Event](meendofstream.md)                 | The stream ended.                                                                                                              |
| [MEError Event](meerror.md)                             | An error has occurred during streaming. Use this event for errors that are not related to any of the other events listed here. |
| [MEMediaSample Event](memediasample.md)                 | The stream has generated a new sample.                                                                                         |
| [MEStreamFormatChanged Event](mestreamformatchanged.md) | The media type has changed. (Optional.)                                                                                        |
| [MEStreamPaused Event](mestreampaused.md)               | The stream was paused.                                                                                                         |
| [MEStreamSeeked Event](mestreamseeked.md)               | The stream was seeked.                                                                                                         |
| [MEStreamStarted Event](mestreamstarted.md)             | The stream was started.                                                                                                        |
| [MEStreamStopped Event](mestreamstopped.md)             | The stream was stopped.                                                                                                        |
| [MEStreamThinMode Event](mestreamthinmode.md)           | Thinning mode has started or stopped. (Optional.)                                                                              |
| [MEStreamTick Event](mestreamtick.md)                   | There is a gap in the stream. (Optional.)                                                                                      |



 

## Related topics

<dl> <dt>

[Media Sources](media-sources.md)
</dt> </dl>

 

 



