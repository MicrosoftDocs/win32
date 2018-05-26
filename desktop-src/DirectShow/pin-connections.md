---
Description: Pin Connections
ms.assetid: 1406ade4-77d8-49a7-8f36-cc49ff007a26
title: Pin Connections
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pin Connections

Filters connect at their pins, through the [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface. Output pins connect to input pins. Each pin connection has a media type, described by the [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure.

An application connects filters by calling methods on the Filter Graph Manager, never by calling methods on the filters or pins themselves. The application can directly specify which filters to connect, by calling the [**IFilterGraph::ConnectDirect**](/windows/win32/Strmif/nf-strmif-ifiltergraph-connectdirect?branch=master) or [**IGraphBuilder::Connect**](/windows/win32/Strmif/nf-strmif-igraphbuilder-connect?branch=master) method; or it can connect filters indirectly, using a graph-building method such as [**IGraphBuilder::RenderFile**](/windows/win32/Strmif/nf-strmif-igraphbuilder-renderfile?branch=master).

For the connection to succeed, both filters must be in the filter graph. The application can add a filter to the graph by calling the [**IFilterGraph::AddFilter**](/windows/win32/Strmif/nf-strmif-ifiltergraph-addfilter?branch=master) method. The Filter Graph Manager may add filters to the graph, as well. When a filter is added, the Filter Graph Manager calls the filter's [**IBaseFilter::JoinFilterGraph**](/windows/win32/Strmif/nf-strmif-ibasefilter-joinfiltergraph?branch=master) method to notify the filter.

The general outline of the connection process is the following:

1.  The Filter Graph Manager calls [**IPin::Connect**](/windows/win32/Strmif/nf-strmif-ipin-connect?branch=master) on the output pin, passing a pointer to the input pin.
2.  If the output pin accepts the connection, it calls [**IPin::ReceiveConnection**](/windows/win32/Strmif/nf-strmif-ipin-receiveconnection?branch=master) on the input pin.
3.  If the input pin also accepts the connection, the connection attempt succeeds and the pins are connected.

Some pins can be disconnected and reconnected while the filter is active. This type of reconnection is called a *dynamic* reconnection. For more information, see [Dynamic Graph Building](dynamic-graph-building.md). However, most filters do not support dynamic reconnection.

Filters are usually connected in downstream order—in other words, the filter's input pins are connected before its output pins. A filter should always support this order of connection. Some filters also support connections in the opposite order—output pins first, followed by input pins. For example, it might be possible to connect a MUX filter's output pin to the file-writer filter, before connecting the MUX filter's input pins.

When a pin's **Connect** or **ReceiveConnection** method is called, the pin must verify that it can support the connection. The details depend on the particular filter. The most common tasks include the following:

-   Check that the media type is acceptable
-   Negotiate an allocator
-   Query the other pin for required interfaces.

 

 



