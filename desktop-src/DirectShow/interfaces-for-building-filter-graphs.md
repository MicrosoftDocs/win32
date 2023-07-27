---
description: Interfaces for Building Filter Graphs
ms.assetid: 18d5217a-7f4e-49e9-ac14-2f4ba229e065
title: Interfaces for Building Filter Graphs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Interfaces for Building Filter Graphs

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Applications use these interfaces to build various types of filter graphs.



| Interface                                                  | Description                                                 |
|------------------------------------------------------------|-------------------------------------------------------------|
| [**IAMFilterGraphCallback**](/windows/desktop/api/Strmif/nn-strmif-iamfiltergraphcallback)   | Receive callback notifications if a pin cannot be rendered. |
| [**IAMGraphBuilderCallback**](/windows/desktop/api/Strmif/nn-strmif-iamgraphbuildercallback) | Provides a callback mechanism during graph building.        |
| [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2)     | Build filter graphs for video capture.                      |
| [**ICreateDevEnum**](/windows/desktop/api/Strmif/nn-strmif-icreatedevenum)                   | Enumerate system devices, such as capture devices.          |
| [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder)               | Build filter graphs for DVD navigation and playback.        |
| [**IEnumFilters**](/windows/desktop/api/Strmif/nn-strmif-ienumfilters)                       | Enumerate the filters in the graph.                         |
| [**IFilterGraph2**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph2)                     | Add, remove, or connect filters.                            |
| [**IFilterMapper2**](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2)                   | Enumerate the filters registered on the user's system.      |
| [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder)                     | Build filter graphs for file playback or for custom uses.   |
| [**IGraphConfig**](/windows/desktop/api/Strmif/nn-strmif-igraphconfig)                       | Dynamically reconfigure a filter graph.                     |
| [**IGraphVersion**](/windows/desktop/api/Strmif/nn-strmif-igraphversion)                     | Determine when the graph changes.                           |



 

 

 



