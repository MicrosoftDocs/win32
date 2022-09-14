---
description: This topic describes how to use the Sequencer Source.
ms.assetid: 7ce8dc67-02b1-4fd4-9e4d-6614fdb40620
title: Using the Sequencer Source
ms.topic: article
ms.date: 05/31/2018
---

# Using the Sequencer Source

This topic describes how to use the [Sequencer Source](sequencer-source.md). It contains the following sections:

-   [Overview](#overview)
-   [Adding Topologies](#adding-topologies)
-   [Deleting Topologies](#deleting-topologies)
-   [Skipping to a Segment](#skipping-to-a-segment)
-   [Related topics](#related-topics)

For a general overview of the sequencer source, see [About the Sequencer Source](about-the-sequencer-source.md).

## Overview

The sequencer source exposes the following interfaces.



| Interface                                                                        | Description                                                                        |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)                                         | Exposes generic media source functionality.                                        |
| [**IMFSequencerSource**](/windows/desktop/api/mfidl/nn-mfidl-imfsequencersource)                                 | Enables the application to add or remove topologies.                               |
| [**IMFMediaSourceTopologyProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcetopologyprovider)         | Retrieves the next topology to queue on the Media Session.                         |
| [**IMFMediaSourcePresentationProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcepresentationprovider) | Used by the Media Session to end segments. Applications do not use this interface. |
| [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)                                           | Queries the sequencer source for [Service Interfaces](service-interfaces.md).     |



 

To play a sequence of media sources, perform the following steps:

1.  To create the sequencer source, call the [**MFCreateSequencerSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesequencersource) function.
2.  For each segment, create a playback topology, as described in [Creating Playback Topologies](creating-playback-topologies.md). To add the topology to the presentation, call [**IMFSequencerSource::AppendTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-appendtopology).
3.  Before starting playback, call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) on the sequencer source. This method returns a pointer to a presentation descriptor for the first segment. To get the topology associated with this segment, call **QueryInterface** on the sequencer source for the [**IMFMediaSourceTopologyProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcetopologyprovider) interface. Pass the presentation descriptor to the [**IMFMediaSourceTopologyProvider::GetMediaSourceTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourcetopologyprovider-getmediasourcetopology) method. This method returns a pointer to the topology.
4.  Pass the topology for the first segment to the Media Session, by calling the Media Session's [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) method.
5.  Start playback by calling [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start).
6.  When the sequencer source is ready to preroll the next segment, it sends an [MENewPresentation](menewpresentation.md) event whose event data is an [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) interface pointer. Again, get the topology for the segment by calling [**GetMediaSourceTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourcetopologyprovider-getmediasourcetopology) on the sequencer source, and set the topology on the Media Session by calling [**SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology). It is not necessary to re-start the media source; it will automatically play through to the next segment.
7.  Before the application quits, shut down the sequencer source by calling [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown).

The following code shows how to get the topology and set it on the Media Session:


```C++
// Queues the next topology on the session.

HRESULT CPlaylist::QueueNextSegment(IMFPresentationDescriptor *pPD)
{
    IMFMediaSourceTopologyProvider *pTopoProvider = NULL;
    IMFTopology *pTopology = NULL;

    //Get the topology for the presentation descriptor
    HRESULT hr = m_pSequencerSource->QueryInterface(IID_PPV_ARGS(&pTopoProvider));
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pTopoProvider->GetMediaSourceTopology(pPD, &pTopology);
    if (FAILED(hr))
    {
        goto done;
    }

    //Set the topology on the media session
    m_pSession->SetTopology(NULL, pTopology);

done:
    SafeRelease(&pTopoProvider);
    SafeRelease(&pTopology);
    return hr;
}
```



For a complete code example, see [Sequencer Source Example Code](sequencer-source-example-code.md).

## Adding Topologies

The sequencer source maintains two lists of topologies: the *input list* and the *preroll list*.

The input list is a collection of topologies corresponding to playlist segments, in the order that they were added by the application by calling [**IMFSequencerSource::AppendTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-appendtopology). This method assigns each topology a unique *segment identifier* of the type **MFSequencerElementId**. The segment identifier is set as an attribute for all source topology nodes. An application can get the segment identifier from a source node by using the [MF\_TOPONODE\_SEQUENCE\_ELEMENTID](mf-toponode-sequence-elementid-attribute.md) attribute. The input list can have duplicate topologies if the application called **AppendTopology** on the same topology more than once; however, they are identified by their unique segment identifiers.

The preroll list is a collection of input list topologies that have been initialized in preparation for playback. This enables the Media Session to transition to the next topology seamlessly when the active topology ends. The application cannot directly add or remove topologies from the preroll list; it is generated by the sequencer source when a topology from the input list is selected for playback. This causes the sequencer source to add the next topology from the input list to the preroll list. After doing so, the sequencer source asynchronously raises the [MENewPresentation](menewpresentation.md) event and passes the presentation descriptor for the preroll topology as event data. The application must listen for this event by using the Media Session's [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface and queue the preroll topology on the Media Session by calling [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology). This must be done before the Media Session completes playback of the active topology. **SetTopology** informs the Media Session about the next topology that it must play after playback of the active topology has ended. To ensure a seamless treansition, the application must call **SetTopology** before the Media Session completes playing the previous topology. Otherwise, there will be a gap between the segments.

The [MENewPresentation](menewpresentation.md) event is raised as long as there is a topology following the active topology. Consequently, if the input list contains only one topology, or if the active topology is the last one in the input list, this event is not raised.

The preroll list is synchronized with the input list and is refreshed each time a topology is added to or deleted from the input list.

## Deleting Topologies

To remove a topology from the sequencer source, an application must call the [**IMFSequencerSource::DeleteTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-deletetopology) method and specify the segment identifier.

Before calling [**DeleteTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-deletetopology), the application must make sure that Media Session is not using the topology that the application wants to delete. To do this, both of the following must occur before the application calls **DeleteTopology**:

-   [MESessionTopologyStatus](mesessiontopologystatus.md) event with MF\_TOPOSTATUS\_ENDED is received for the topology to ensure that Media Session has completed playback.

-   [MESessionTopologyStatus](mesessiontopologystatus.md) with MF\_TOPOSTATUS\_STARTED\_SOURCE is received for the next topology to ensure that the Media Session has started playing the next topology, [MESessionEnded](mesessionended.md) event is received to ensure that Media Session is done with the last topology in the sequencer source.

If the segment being deleted is the active topology, playback is stopped and the sequencer source raises the [MEEndOfPresentationSegment](meendofpresentationsegment.md) event. If the active topology is also the last topology, the [MEEndOfPresentation](meendofpresentation.md) event is raised.

## Skipping to a Segment

An application can skip to a particular segment in the sequence by starting the [Media Session](media-session.md) with a segment offset, as follows:

1.  Call the [**MFCreateSequencerSegmentOffset**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesequencersegmentoffset) function to create the segment offset. Specify the identifier of the segment in the *dwId* parameter. (The identifier was returned by the [**IMFSequencerSource::AppendTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-appendtopology) method when you first added the topology to the sequencer source.) The *hnsOffset* parameter specifies a time offset, relative to the start of the segment. Playback will start at this time. For the *pvarSegmentOffset* parameter, pass in the address of an empty **PROPVARIANT**. When the function returns, this **PROPVARIANT** contains the segment offset.

2.  Call the [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) method on the Media Session. For the *pguidTimeFormat* parameter, use the GUID value MF\_TIME\_FORMAT\_SEGMENT\_OFFSET. This value indicates seeking by segment offset. For the *pvarStartPosition* parameter, pass the address of the **PROPVARIANT** created in the previous step.

The following code example shows how to skip to the start of a specified segment in a sequence.


```C++
// Skips to the specified segment in the sequencer source

HRESULT CPlaylist::SkipTo(DWORD index)
{
    if (index >= m_count)
    {
        return E_INVALIDARG;
    }

    MFSequencerElementId ID = m_segments[index].SegmentID;

    PROPVARIANT var;

    HRESULT hr = MFCreateSequencerSegmentOffset(ID, NULL, &var);
    
    if (SUCCEEDED(hr))
    {
        hr = m_pSession->Start(&MF_TIME_FORMAT_SEGMENT_OFFSET, &var);
        PropVariantClear(&var);
    }
    return hr;
}
```



When the application seeks across segments, the application receives several events as the sequencer source ends the current segment and prepares to play the new segment. Because these events are received asynchronously, it is difficult to predict the exact sequence of events. These events are as follows:

-   The sequencer source sends an [MENewPresentation](menewpresentation.md) event for the new segment to which the Media Session is skipping.

-   When the sequencer source ends the active segment, it sends the [MEEndOfPresentationSegment](meendofpresentationsegment.md) event.
-   The sequencer source then cancels the preroll topology. This results in the following events for the canceled topology:

    -   [MESessionTopologyStatus](mesessiontopologystatus.md) event with the MF\_TOPOSTATUS\_READY flag.
    -   [MESessionTopologyStatus](mesessiontopologystatus.md) event with the MF\_TOPOSTATUS\_STARTED\_SOURCE flag.
    -   [MEEndOfPresentationSegment](meendofpresentationsegment.md) event with the [MF\_EVENT\_SOURCE\_TOPOLOGY\_CANCELED](mf-event-source-topology-canceled-attribute.md) attribute to indicate that the topology was canceled by the sequencer source.

-   Next, the sequencer source sends events for the new segment, including various [MESessionTopologyStatus](mesessiontopologystatus.md) events.
-   If the new segment is not the last on the list, the sequencer source refreshes the preroll list and raises another [MENewPresentation](menewpresentation.md) for the new preroll topology. For information about topologies in the preroll list, see [About the Sequencer Source](about-the-sequencer-source.md).

More details about the events sent by the sequencer source can be found in the topic [Sequencer Source Events](sequencer-source-events.md).

## Related topics

<dl> <dt>

[How to Create a Playlist](how-to-create-a-playlist.md)
</dt> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 



