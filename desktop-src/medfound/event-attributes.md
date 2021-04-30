---
description: Event Attributes
ms.assetid: 25e77ee1-cffc-4f8b-ac07-b5607a125fc7
title: Event Attributes (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Event Attributes (Microsoft Media Foundation)

The following attributes apply to events.



| Attribute                                                                                                        | Description                                                                                                           |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**MF\_EVENT\_DO\_THINNING**](mf-event-do-thinning-attribute.md)                                                | When a media source requests a new playback rate, specifies whether the source also requests thinning.                |
| [**MF\_EVENT\_OUTPUT\_NODE**](mf-event-output-node-attribute.md)                                                | Identifies the topology node for a stream sink.                                                                       |
| [**MF\_EVENT\_PRESENTATION\_TIME\_OFFSET**](mf-event-presentation-time-offset-attribute.md)                     | Offset between the presentation time and the media source's time stamps.                                              |
| [**MF\_EVENT\_SCRUBSAMPLE\_TIME**](mf-event-scrubsample-time-attribute.md)                                      | Presentation time for a sample that was rendered while scrubbing.                                                     |
| [**MF\_EVENT\_SESSIONCAPS**](mf-event-sessioncaps-attribute.md)                                                 | Contains flags that define the capabilities of the Media Session, based on the current presentation.                  |
| [**MF\_EVENT\_SESSIONCAPS\_DELTA**](mf-event-sessioncaps-delta-attribute.md)                                    | Contains flags that indicate which capabilities have changed in the Media Session, based on the current presentation. |
| [**MF\_EVENT\_SOURCE\_ACTUAL\_START**](mf-event-source-actual-start-attribute.md)                               | Contains the start time when a media source restarts from its current position.                                       |
| [**MF\_EVENT\_SOURCE\_CHARACTERISTICS**](mf-event-source-characteristics-attribute.md)                          | Specifies the current characteristics of the media source.                                                            |
| [**MF\_EVENT\_SOURCE\_CHARACTERISTICS\_OLD**](mf-event-source-characteristics-old-attribute.md)                 | Specifies the previous characteristics of the media source.                                                           |
| [**MF\_EVENT\_SOURCE\_FAKE\_START**](mf-event-source-fake-start-attribute.md)                                   | Specifies whether the current segment topology is empty.                                                              |
| [**MF\_EVENT\_SOURCE\_PROJECTSTART**](mf-event-source-projectstart-attribute.md)                                | Specifies the start time for a segment topology.                                                                      |
| [**MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED**](mf-event-source-topology-canceled-attribute.md)                     | Specifies whether the sequencer source canceled a topology.                                                           |
| [**MF\_EVENT\_START\_PRESENTATION\_TIME**](mf-event-start-presentation-time-attribute.md)                       | The starting time for the presentation, in 100-nanosecond units, as measured by the presentation clock.               |
| [**MF\_EVENT\_START\_PRESENTATION\_TIME\_AT\_OUTPUT**](mf-event-start-presentation-time-at-output-attribute.md) | The presentation time at which the media sinks will render the first sample of the new topology.                      |
| [**MF\_EVENT\_TOPOLOGY\_STATUS**](mf-event-topology-status-attribute.md)                                        | Specifies the status of a topology during playback.                                                                   |
| [**MF\_SESSION\_APPROX\_EVENT\_OCCURRENCE\_TIME**](mf-session-approx-event-occurrence-time-attribute.md)        | The approximate time when the Media Session raised an event.                                                          |



 

## Related topics

<dl> <dt>

[**IMFMediaEvent**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent)
</dt> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 



