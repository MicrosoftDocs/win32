---
description: Sequencer Source Events
ms.assetid: 28654bae-9ce2-467b-b769-63279d69b173
title: Sequencer Source Events
ms.topic: article
ms.date: 05/31/2018
---

# Sequencer Source Events

When the [Sequencer Source](sequencer-source.md) plays a sequence of files, the Media Session generally sends all of the same events that are sent during normal playback, and which are listed in [Media Session Events](media-session-events.md). The application gets these events using the Media Session's [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface.

In addition, there are some events which are specific to playlist segments.



| Event                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MENewPresentation](menewpresentation.md)                                                              | Signals the application to preroll the next topology.<br/> To provide a seamless transition between two consecutive presentations, the sequencer source loads the next topology in advance. While the active topology is still playing, the sequencer source sends this event for the next topology, as long as there is a subsequent topology available in the source.<br/> This event data for this event is the presentation descriptor for the next topology. The application is responsible for setting the corresponding topology on the Media Session, as described in [Using the Sequencer Source](using-the-sequencer-source.md).<br/> |
| [MEEndOfPresentationSegment](meendofpresentationsegment.md)                                            | The sequencer source raises this event when the Media Session has completed playing the current segment, if that segment is followed by another segment. (If the current segment is the last one, the sequencer source raises the [MEEndOfPresentation](meendofpresentation.md) event instead.)<br/> The Media Session forwards this event to the application. Typically, the application receives [MEEndOfPresentationSegment](meendofpresentationsegment.md) after the Media Session has started processing the next segment, but while the media sinks are still delivering the samples for the previous segment.<br/>                            |
| [MESessionTopologyStatus](mesessiontopologystatus.md), with status **MF\_TOPOSTATUS\_SINK\_SWITCHED**. | The Media Session raises this event when it makes a transition to the next topology in the sequencer source and media sinks have completed playing the previous topology. This event contains a pointer to the next topology.                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Example 1: Playback without Skipping

When the sequencer source is involved, the number of events that you get from the Media Session can be confusing, especially because events associated with one segment are often interleaved with events for the next segment.

In the first example, the application queues three segments, S1, S2, and S3. The third segment has the **SequencerTopologyFlags\_Last** flag, to signal it is the last segment in the sequence. The segment to which each event corresponds is given in parentheses. The application's [**SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) calls are also listed, to make the order of operations clearer.

-   Application calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) (S1)
-   [MESessionTopologySet](mesessiontopologyset.md) (S1)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_READY** (S1)
-   [MENewPresentation](menewpresentation.md) (S2 preroll)
-   Application calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) (S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_STARTED\_SOURCE** (start of S1)
-   [MESessionTopologySet](mesessiontopologyset.md) (S2)
-   [MEEndOfPresentationSegment](meendofpresentationsegment.md) (end of S1)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_ENDED** (S1)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_SINK\_SWITCHED** (transition to S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_READY** (S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_STARTED\_SOURCE** (start of S2)
-   [MENewPresentation](menewpresentation.md) (S3 preroll)
-   Application calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) (S2)
-   [MESessionTopologySet](mesessiontopologyset.md) (S3)
-   [MEEndOfPresentationSegment](meendofpresentationsegment.md) (end of S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_ENDED** (S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_SINK\_SWITCHED** (transition to S3)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_READY** (S3)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_STARTED\_SOURCE** (start of S3)
-   [MEEndOfPresentation](meendofpresentation.md) (end of S3; last segment)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_ENDED**
-   [MESessionEnded](mesessionended.md)

This list does not include every event that you might receive. (For example, it omits the [MESessionCapabilitiesChanged](mesessioncapabilitieschanged.md) event, which is sent whenever the session capabilities change. An application typically receives multiple MESessionCapabilitiesChanged events throughout a presentation.) The events listed here are the ones that show the transition from one segment to the next. The most important events are [MENewPresentation](menewpresentation.md), which signals the application to preroll the next topology, and [MEEndOfPresentationSegment](meendofpresentationsegment.md), which signals the end of a segment (except for the last segment).

Because events in Media Foundation are asynchronous, and are not serialized with method calls, the exact order could vary. For example, you could receive **MF\_TOPOSTATUS\_STARTED\_SOURCE** for S1 before the application calls [**SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) for S2.

Also, you might not get every event listed here. The [MEEndOfPresentation](meendofpresentation.md) and [MESessionEnded](mesessionended.md) events, for example, are not sent unless the last segment has the **SequencerTopologyFlags\_Last** flag.

Finally, this list does not indicate the passage of time. The time from "start of S1" to "end of S1" is the entire duration of S1, which could be a few seconds or many hours, depending on the source.

## Example 2: Playback with Segment Skipping

In this example, the application queues the same segments, but skips to segment 3 while segment 1 is playing. In this case, the following events are sent:

-   Application calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) (S1)
-   [MESessionTopologySet](mesessiontopologyset.md) (S1)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_READY** (S1)
-   [MENewPresentation](menewpresentation.md) (S2 preroll)
-   Application calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) (S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_STARTED\_SOURCE** (start of S1)
-   [MESessionTopologySet](mesessiontopologyset.md) (S2)
-   Application calls [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) (skip to S3)
-   [MENewPresentation](menewpresentation.md) (S3 preroll)
-   Application calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) (S3)
-   [MESessionStarted](mesessionstarted.md)
-   [MEEndOfPresentationSegment](meendofpresentationsegment.md) (S1 canceled)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_ENDED** (S1)
-   [MESessionTopologySet](mesessiontopologyset.md) (S3)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_SINK\_SWITCHED** (transition to S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_READY** (S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_STARTED\_SOURCE** (S2)
-   [MEEndOfPresentationSegment](meendofpresentationsegment.md) (S2 canceled)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_ENDED** (S2)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_SINK\_SWITCHED** (transition to S3)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **TOPOSTATUS\_READY** (S3)
-   [MESessionTopologyStatus](mesessiontopologystatus.md): **MF\_TOPOSTATUS\_STARTED\_SOURCE** (S3)

When the application calls [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) to skip to segment 3, the sequencer source cancels segment 1, which is still playing. The [MEEndOfPresentationSegment](meendofpresentationsegment.md) event for this segment contains the [**MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED**](mf-event-source-topology-canceled-attribute.md) attribute, indicating that the segment ended because it was canceled. Then, because segment 2 is already pre-rolled, that segment is started but then immediately canceled. The MEEndOfPresentationSegment event for segment 2 also contains the **MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED** attribute. The session can then switch to segment 3 and play it normally.

## Related topics

<dl> <dt>

[About the Sequencer Source](about-the-sequencer-source.md)
</dt> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 




