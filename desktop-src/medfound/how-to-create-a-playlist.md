---
description: This topic describes how to use the Sequence Source to play a sequence of files.
ms.assetid: 5a760492-bd52-40b8-a652-8a62646db6ae
title: How to Create a Playlist
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Playlist

This topic describes how to use the Sequence Source to play a sequence of files.

## Overview

To play media files in a sequence, the application must add topologies in a sequence to create a playlist, and queue these topologies on the Media Session for playback.

The sequencer source ensures seamless playback by initializing and loading the next topology before the Media Session starts playing the current topology. This enables the application to start the next topology quickly whenever it is required.

The Media Session is responsible for feeding data to the sinks and playing the topologies in the sequence source. In addition, the Media Session manages the presentation time for the segments.

For more information about how the sequencer source manages topologies, see [About the Sequencer Source](about-the-sequencer-source.md).

This walk-through contains the following steps:

1.  [Prerequisites](#prerequisites)
2.  [Initializing Media Foundation](#initializing-media-foundation)
3.  [Creating Media Foundation Objects](#creating-media-foundation-objects)
4.  [Creating the Media Source](#creating-the-media-source)
5.  [Creating Partial Topologies](#creating-partial-topologies)
6.  [Adding Topologies to the Sequencer Source](#adding-topologies-to-the-sequencer-source)
7.  [Setting the First Topology on the Media Session](#setting-the-first-topology-on-the-media-session)
8.  [Queuing the Next Topology on the Media Session](#queuing-the-next-topology-on-the-media-session)
9.  [Releasing the Sequencer Source](#releasing-the-sequencer-source)

The code examples shown this topic are excerpts from the topic [Sequencer Source Example Code](sequencer-source-example-code.md), which contains the complete example code.

## Prerequisites

Before starting this walk-through, familiarize yourself with the following Media Foundation concepts:

-   [Media Session](media-session.md)
-   [Topologies](topologies.md)
-   [Media Event Generators](media-event-generators.md)
-   [Presentation Descriptors](presentation-descriptors.md)

Also read [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md), because the example code shwon here expands on the code in that topic.

## Initializing Media Foundation

Before you can use any Media Foundation interfaces or methods, initialize Media Foundation by calling the [**MFStartup**](/windows/desktop/api/mfapi/nf-mfapi-mfstartup) function. For more information, see [Initializing Media Foundation](initializing-media-foundation.md).


```C++
    hr = MFStartup(MF_VERSION);
```



## Creating Media Foundation Objects

Next, create the following Media Foundation objects:

-   Media session. This object exposes the [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) interface, which provides methods to play, pause, and stop the current topology.
-   Sequencer source. This object exposes the [**IMFSequencerSource**](/windows/desktop/api/mfidl/nn-mfidl-imfsequencersource) interface, which provides methods to add, update, and delete topologies in a sequence.

1.  Call the [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession) function to create the Media Session.
2.  Call [**IMFMediaEventQueue::BeginGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventqueue-begingetevent) to request the first event from the Media Session.
3.  Call the [**MFCreateSequencerSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesequencersource) function to create the sequencer source.

The following code creates the Media Session and requests the first event:


```C++
//  Create a new instance of the media session.
HRESULT CPlayer::CreateSession()
{
    // Close the old session, if any.
    HRESULT hr = CloseSession();
    if (FAILED(hr))
    {
        goto done;
    }

    assert(m_state == Closed);

    // Create the media session.
    hr = MFCreateMediaSession(NULL, &m_pSession);
    if (FAILED(hr))
    {
        goto done;
    }

    // Start pulling events from the media session
    hr = m_pSession->BeginGetEvent((IMFAsyncCallback*)this, NULL);
    if (FAILED(hr))
    {
        goto done;
    }

    m_state = Ready;

done:
    return hr;
}
```



## Creating the Media Source

Next, create a media source for the first playlist segment. Use the [Source Resolver](source-resolver.md) to create a media source from a URL. To do this, call the [**MFCreateSourceResolver**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatesourceresolver) function to create a source resolver and then call the [**IMFSourceResolver::CreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl) method to create the media source.

For information about media sources, see [Media Sources](media-sources.md).

## Creating Partial Topologies

Each segment in the sequencer source has its own partial topology. Next, create partial topologies for media sources. For a partial topology, the topology source nodes are connected directly to the output nodes, without specifying any intermediate transforms. The Media Session uses the topology loader object to resolve the topology. After a topology is resolved, the required decoders and other transform nodes are added. The sequencer source can also contain full topologies.

To create the topology object, use the [**MFCreateTopology**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopology) function and then use the [**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode) interface to create stream nodes.

For complete instructions on using these programming elements to create topologies, see [Creating Playback Topologies](creating-playback-topologies.md).

An application can play a selected portion of the native source by configuring the source node. To do this, set the [**MF\_TOPONODE\_MEDIASTART**](mf-toponode-mediastart-attribute.md) attribute and the [**MF\_TOPONODE\_MEDIASTOP**](mf-toponode-mediastop-attribute.md) attribute on **MF\_TOPOLOGY\_SOURCESTREAM\_NODE** topology nodes. Specify the media start time and the media stop time relative to the start of the native source as **UINT64** types.

## Adding Topologies to the Sequencer Source

Next, add to the sequencer source the partial topologies that you created. Each sequence element, called a *segment*, is assigned an **MFSequencerElementId** identifier. For more information about how the sequencer source manages topologies, see [About the Sequencer Source](about-the-sequencer-source.md).

After all of the topologies are added to the sequencer source, the application must flag the last segment in the sequence to end playback in the pipeline. Without this flag, the sequencer source expects more topologies to be added.

1.  Call the [**IMFSequencerSource::AppendTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-appendtopology) method to add a specific topology to the sequencer source.

    ```C++
        hr = m_pSequencerSource->AppendTopology(
            pTopology, 
            SequencerTopologyFlags_Last, 
            &SegmentId
            );
    ```

    

    [**AppendTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-appendtopology) adds the specified topology to the sequence. This method returns the segment identifier in the *pdwId* parameter.

    If the topology is the last one in the sequencer source, pass SequencerTopologyFlags\_Last in the *dwFlags* parameter. This value is defined in the [**MFSequencerTopologyFlags**](/windows/desktop/api/mfidl/ne-mfidl-mfsequencertopologyflags) enumeration.

2.  Call [**IMFSequencerSource::UpdateTopologyFlags**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-updatetopologyflags) to update the flags for the topology associated with the segment identifier in the input list. In this case, the call indicates that the specified segment is the last segment in the sequencer. (This call is optional if the last topology is specified in the [**AppendTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-appendtopology) call.)

    ```C++
        BOOL bFirstSegment = (NumSegments() == 0);

        if (!bFirstSegment)
        {
            // Remove the "last segment" flag from the last segment.
            hr = m_pSequencerSource->UpdateTopologyFlags(LastSegment(), 0);
            if (FAILED(hr))
            {
                goto done;
            }
        }
    ```

    

The application can replace a segment's topology with another topology by calling the [**IMFSequencerSource::UpdateTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfsequencersource-updatetopology) and passing the new topology in *pTopology*. If there are new native sources in the new topology, the sources are added to the source cache. The preroll list is also refreshed.

## Setting the First Topology on the Media Session

Next, queue the first topology in the sequence source on the Media Session. To get the first topology from the sequencer source, the application must call the [**IMFMediaSourceTopologyProvider::GetMediaSourceTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourcetopologyprovider-getmediasourcetopology) method. This method returns the partial topology, which is resolved by the Media Session.

For information about partial topologies, see [About Topologies](about-topologies.md).

1.  Retrieve the native media source for the first topology of the sequence source.
2.  Create a presentation descriptor for the media source by calling the [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) method.
3.  Retrieve the associated topology for the presentation by calling the [**IMFMediaSourceTopologyProvider::GetMediaSourceTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourcetopologyprovider-getmediasourcetopology) method.
4.  Set the first topology on the Media Session by Calling [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology).

    Call [**SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) with the *dwSetTopologyFlags* parameter set to **NULL**. This instructs the Media Session to start the specified topology when the current topology has been completed. Because in this case, the specified topology is the first topology and there is no current presentation, the Media Session starts the new presentation immediately.

    The **NULL** value also indicates that Media Session must resolve the topology because the topology returned by the topology provider is always a partial topology.


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



## Queuing the Next Topology on the Media Session

Next, the application needs to handle the [MENewPresentation](menewpresentation.md) event.

Sequencer source raises [MENewPresentation](menewpresentation.md) when the Media Session starts playing a segment that has another segment following it. This event informs the application about the next topology in the sequence source by providing the presentation descriptor for the next segment in the preroll list. The application must retrieve the associated topology, by using the topology provider, and queue it on the Media Session. The sequencer source then prerolls this topology, which ensures a seamless transition between presentations.

When the application seeks across segments, the application receives several [MENewPresentation](menewpresentation.md) events as the sequencer source refreshes the preroll list and sets up the correct topology. The application must handle each event and queue the topology returned in the event data, on the Media Session. For information about skipping segments, see [Using the Sequencer Source](using-the-sequencer-source.md).

For information about getting sequencer source notifications, see [Sequencer Source Events](sequencer-source-events.md).

1.  In the [MENewPresentation](menewpresentation.md) event handler, retrieve the presentation descriptor for the next segment from the event data.
2.  Get the associated topology for the presentation by calling the [**IMFMediaSourceTopologyProvider::GetMediaSourceTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourcetopologyprovider-getmediasourcetopology) method.
3.  Set the topology on the Media Session by calling the [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) method.

    The Media Session starts the new presentation when the current presentation has been completed.


```C++
HRESULT CPlaylist::OnNewPresentation(IMFMediaEvent *pEvent)
{
    IMFPresentationDescriptor *pPD = NULL;

    HRESULT hr = GetEventObject(pEvent, &pPD);

    if (SUCCEEDED(hr))
    {
        // Queue the next segment on the media session
        hr = QueueNextSegment(pPD);
    }

    SafeRelease(&pPD);
    return hr;
}
```



## Releasing the Sequencer Source

Finally, shut down the sequencer source. To do so, call the [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown) method on the sequencer source. This call shuts down all of the underlying native media sources in the sequencer source.

After releasing the sequencer source, the application should close and shut down the Media Session by calling [**IMFMediaSession::Close**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-close) and [**IMFMediaSession::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-shutdown), in that order.

To avoid memory leaks, the application must release pointers to Media Foundation interfaces when they are no longer needed.

## Next Steps

This walk-through illustrated how to create a basic playlist by using the sequencer source. After creating the playlist, you might want to add advanced features such as segment skipping, changing the playback state, and seeking within a segment. The following list provides links to the related topics:

-   [How to Control Presentation States](how-to-control-presentation-states.md): The sequencer source relies on the Media Session to provide transport control such as, Play, Pause, and Stop.
-   [How to Perform Scrubbing](how-to-perform-scrubbing.md) describes the steps required to seek to a specific position in a stream.

## Related topics

<dl> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 



