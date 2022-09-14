---
description: This topic describes how to create a topology for audio or video playback.
ms.assetid: 9c536c4e-fbf8-4c16-932f-e5863b7652fe
title: Creating Playback Topologies
ms.topic: article
ms.date: 05/31/2018
---

# Creating Playback Topologies

This topic describes how to create a topology for audio or video playback. For basic playback, you can create a partial topology, in which the source nodes are connected directly to the output nodes. You do not need to insert any nodes for the intermediate transforms, such as decoders or color converters. The Media Session will use the topology loader to resolve the topology, and the topology loader will insert the transforms that are required.

-   [Creating the Topology](#creating-the-topology)
-   [Connecting Streams to Media Sinks](#connecting-streams-to-media-sinks)
-   [Creating the Media Sink](#creating-the-media-sink)
-   [Next Steps](#next-steps)
-   [Related topics](#related-topics)

## Creating the Topology

Here are the overall steps for creating a partial playback topology from a media source:

1.  Create the media source. In most cases, you will use the source resolver to create the media source. For more information, see [Source Resolver](source-resolver.md).
2.  Get the media source's presentation descriptor.
3.  Create an empty topology.
4.  Use the presentation descriptor to enumerate the stream descriptors. For each stream descriptor:
    1.  Get the stream's major media type, such as audio or video.
    2.  Check if the stream is currently selected. (Optionally, you can select or deselect a stream, based on the media type.)
    3.  If the stream is selected, create an activation object for the media sink, based on the stream's media type.
    4.  Add a source node for the stream and an output node for the media sink.
    5.  Connect the source node to the output node.

To make this process easier to follow, the example code in this topic is organized into several functions. The top-level function is named `CreatePlaybackTopology`. It takes three parameters:

-   A pointer to a [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface of the media source.
-   A pointer to the [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) interface of the presentation descriptor. Get this pointer by calling [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor). For sources with multiple presentations, the presentation descriptors for subsequent presentations are delivered in the [MENewPresentation](menewpresentation.md) event.
-   A handle to an application window. If the source has a video stream, the video will be displayed in this window.

The function returns a pointer to a partial playback topology in the *ppTopology* parameter.


```C++
//  Create a playback topology from a media source.
HRESULT CreatePlaybackTopology(
    IMFMediaSource *pSource,          // Media source.
    IMFPresentationDescriptor *pPD,   // Presentation descriptor.
    HWND hVideoWnd,                   // Video window.
    IMFTopology **ppTopology)         // Receives a pointer to the topology.
{
    IMFTopology *pTopology = NULL;
    DWORD cSourceStreams = 0;

    // Create a new topology.
    HRESULT hr = MFCreateTopology(&pTopology);
    if (FAILED(hr))
    {
        goto done;
    }




    // Get the number of streams in the media source.
    hr = pPD->GetStreamDescriptorCount(&cSourceStreams);
    if (FAILED(hr))
    {
        goto done;
    }

    // For each stream, create the topology nodes and add them to the topology.
    for (DWORD i = 0; i < cSourceStreams; i++)
    {
        hr = AddBranchToPartialTopology(pTopology, pSource, pPD, i, hVideoWnd);
        if (FAILED(hr))
        {
            goto done;
        }
    }

    // Return the IMFTopology pointer to the caller.
    *ppTopology = pTopology;
    (*ppTopology)->AddRef();

done:
    SafeRelease(&pTopology);
    return hr;
}
```



This function performs the following steps:

1.  Call [**MFCreateTopology**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopology) to create the topology. Initially, the topology does not contain any nodes.
2.  Call [**IMFPresentationDescriptor::GetStreamDescriptorCount**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorcount) to get the number of streams in the presentation.
3.  For each stream, call the application-defined `AddBranchToPartialTopology` function to a branch in the topology. This function is shown in the next section.

## Connecting Streams to Media Sinks

For each selected stream, add a source node and an output node, then connect the two nodes. The source node represents the stream. The output node represents either the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR) or the [Streaming Audio Renderer](streaming-audio-renderer.md) (SAR).

The `AddBranchToPartialTopology` function, shown in the next example, takes the following parameters:

-   A pointer to the [**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology) interface of the topology.
-   A pointer to the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface of the media source.
-   A pointer to the [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) interface of the presentation descriptor.
-   The zero-based index of the stream.
-   A handle to the video window. This handle is used only for the video stream.


```C++
//  Add a topology branch for one stream.
//
//  For each stream, this function does the following:
//
//    1. Creates a source node associated with the stream. 
//    2. Creates an output node for the renderer. 
//    3. Connects the two nodes.
//
//  The media session will add any decoders that are needed.

HRESULT AddBranchToPartialTopology(
    IMFTopology *pTopology,         // Topology.
    IMFMediaSource *pSource,        // Media source.
    IMFPresentationDescriptor *pPD, // Presentation descriptor.
    DWORD iStream,                  // Stream index.
    HWND hVideoWnd)                 // Window for video playback.
{
    IMFStreamDescriptor *pSD = NULL;
    IMFActivate         *pSinkActivate = NULL;
    IMFTopologyNode     *pSourceNode = NULL;
    IMFTopologyNode     *pOutputNode = NULL;

    BOOL fSelected = FALSE;

    HRESULT hr = pPD->GetStreamDescriptorByIndex(iStream, &fSelected, &pSD);
    if (FAILED(hr))
    {
        goto done;
    }

    if (fSelected)
    {
        // Create the media sink activation object.
        hr = CreateMediaSinkActivate(pSD, hVideoWnd, &pSinkActivate);
        if (FAILED(hr))
        {
            goto done;
        }

        // Add a source node for this stream.
        hr = AddSourceNode(pTopology, pSource, pPD, pSD, &pSourceNode);
        if (FAILED(hr))
        {
            goto done;
        }

        // Create the output node for the renderer.
        hr = AddOutputNode(pTopology, pSinkActivate, 0, &pOutputNode);
        if (FAILED(hr))
        {
            goto done;
        }

        // Connect the source node to the output node.
        hr = pSourceNode->ConnectOutput(0, pOutputNode, 0);
    }
    // else: If not selected, don't add the branch. 

done:
    SafeRelease(&pSD);
    SafeRelease(&pSinkActivate);
    SafeRelease(&pSourceNode);
    SafeRelease(&pOutputNode);
    return hr;
}
```



The function does the following:

1.  Calls [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex) and passes in the stream index. This method returns a pointer to the stream descriptor for that stream, along with a Boolean value indicating whether the stream is selected.
2.  If the stream is not selected, the function exits and returns S\_OK, because the application does not need to create a topology branch for a stream unless it is selected.
3.  If the stream is selected, the function completes the topology branch as follows:
    1.  Creates an activation object for the sink, by calling the application-defined CreateMediaSinkActivate function. This function is shown in the next section.
    2.  Adds a source node to the topology. Code for this step is shown in the topic [Creating Source Nodes](creating-source-nodes.md).
    3.  Adds an output node to the topology. Code for this step is shown in the topic [Creating Output Nodes](creating-output-nodes.md).
    4.  Connects the two nodes by calling [**IMFTopologyNode::ConnectOutput**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-connectoutput) on the source node. By connecting the nodes, the application indicates that the upstream node should deliver data to the downstream node. A source node has one output, and an output node has one input, so both stream indexes are zero.

More advanced applications can select or deselect streams, instead of using the source's default configuration. A source could have multiple streams, and any of them might be selected by default. The media source's presentation descriptor has a default set of stream selections. In a simple video file with a single audio stream and video stream, the media source will usually select both streams by default. However, a file might have multiple audio streams for different languages, or multiple video streams encoded at different bit rates. In that case, some of the streams will be unselected by default. The application can change the selection by calling [**IMFPresentationDescriptor::SelectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-selectstream) and [**IMFPresentationDescriptor::DeselectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-deselectstream) on the presentation descriptor.

## Creating the Media Sink

The next function creates an activation object for the EVR or SAR media sink.


```C++
//  Create an activation object for a renderer, based on the stream media type.

HRESULT CreateMediaSinkActivate(
    IMFStreamDescriptor *pSourceSD,     // Pointer to the stream descriptor.
    HWND hVideoWindow,                  // Handle to the video clipping window.
    IMFActivate **ppActivate
)
{
    IMFMediaTypeHandler *pHandler = NULL;
    IMFActivate *pActivate = NULL;

    // Get the media type handler for the stream.
    HRESULT hr = pSourceSD->GetMediaTypeHandler(&pHandler);
    if (FAILED(hr))
    {
        goto done;
    }

    // Get the major media type.
    GUID guidMajorType;
    hr = pHandler->GetMajorType(&guidMajorType);
    if (FAILED(hr))
    {
        goto done;
    }
 
    // Create an IMFActivate object for the renderer, based on the media type.
    if (MFMediaType_Audio == guidMajorType)
    {
        // Create the audio renderer.
        hr = MFCreateAudioRendererActivate(&pActivate);
    }
    else if (MFMediaType_Video == guidMajorType)
    {
        // Create the video renderer.
        hr = MFCreateVideoRendererActivate(hVideoWindow, &pActivate);
    }
    else
    {
        // Unknown stream type. 
        hr = E_FAIL;
        // Optionally, you could deselect this stream instead of failing.
    }
    if (FAILED(hr))
    {
        goto done;
    }
 
    // Return IMFActivate pointer to caller.
    *ppActivate = pActivate;
    (*ppActivate)->AddRef();

done:
    SafeRelease(&pHandler);
    SafeRelease(&pActivate);
    return hr;
}
```



This function performs the following steps:

1.  Calls [**IMFStreamDescriptor::GetMediaTypeHandler**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamdescriptor-getmediatypehandler) on the stream descriptor. This method returns an [**IMFMediaTypeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfmediatypehandler) interface pointer.

2.  Calls [**IMFMediaTypeHandler::GetMajorType**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-getmajortype). This method returns the major type GUID for the stream.

3.  If the stream type is audio, the function calls [**MFCreateAudioRendererActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateaudiorendereractivate) to create the audio renderer activation object. If the stream type is video, the function calls [**MFCreateVideoRendererActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatevideorendereractivate) to create the video renderer activation object. Both of these functions return a pointer to the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface. This pointer is used to initialize the output node for the sink, as shown previously.

For any other stream type, this example returns an error code. Alternatively, you could simply deselect the stream.

## Next Steps

To play one media file at a time, queue the topology on the Media Session by calling [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology). The Media Session will use the topology loader to resolve the topology. For a complete example, see [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md).

## Related topics

<dl> <dt>

[How to Play Unprotected Media Files](how-to-play-unprotected-media-files.md)
</dt> <dt>

[Media Session](media-session.md)
</dt> <dt>

[Topologies](topologies.md)
</dt> </dl>

 

 



