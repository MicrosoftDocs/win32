---
description: Pin Connections
ms.assetid: 1406ade4-77d8-49a7-8f36-cc49ff007a26
title: Pin Connections
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Pin Connections

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Filters connect at their pins, through the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface. Output pins connect to input pins. Each pin connection has a media type, described by the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

An application connects filters by calling methods on the Filter Graph Manager, never by calling methods on the filters or pins themselves. The application can directly specify which filters to connect, by calling the [**IFilterGraph::ConnectDirect**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-connectdirect) or [**IGraphBuilder::Connect**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-connect) method; or it can connect filters indirectly, using a graph-building method such as [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile).

For the connection to succeed, both filters must be in the filter graph. The application can add a filter to the graph by calling the [**IFilterGraph::AddFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-addfilter) method. The Filter Graph Manager may add filters to the graph, as well. When a filter is added, the Filter Graph Manager calls the filter's [**IBaseFilter::JoinFilterGraph**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-joinfiltergraph) method to notify the filter.

The general outline of the connection process is the following:

1.  The Filter Graph Manager calls [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) on the output pin, passing a pointer to the input pin.
2.  If the output pin accepts the connection, it calls [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) on the input pin.
3.  If the input pin also accepts the connection, the connection attempt succeeds and the pins are connected.

Some pins can be disconnected and reconnected while the filter is active. This type of reconnection is called a *dynamic* reconnection. For more information, see [Dynamic Graph Building](dynamic-graph-building.md). However, most filters do not support dynamic reconnection.

Filters are usually connected in downstream order—in other words, the filter's input pins are connected before its output pins. A filter should always support this order of connection. Some filters also support connections in the opposite order—output pins first, followed by input pins. For example, it might be possible to connect a MUX filter's output pin to the file-writer filter, before connecting the MUX filter's input pins.

When a pin's **Connect** or **ReceiveConnection** method is called, the pin must verify that it can support the connection. The details depend on the particular filter. The most common tasks include the following:

-   Check that the media type is acceptable
-   Negotiate an allocator
-   Query the other pin for required interfaces.

 

 



