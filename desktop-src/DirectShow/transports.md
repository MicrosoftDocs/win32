---
description: Transports
ms.assetid: 63c5ff5b-293d-4a80-92e8-3ece41321095
title: Transports
ms.topic: article
ms.date: 05/31/2018
---

# Transports

In order to move media data through the filter graph, a DirectShow filter must support one of several possible protocols. These protocols are called transports. When two filters connect, they must support the same transport; otherwise they cannot exchange media data. Typically, a transport requires that one of the pins support a particular interface. When the filters connect, one pin queries the other for the interface.

Most DirectShow filters hold media data in main memory, and deliver it to other filters across pin connections. This type of transport is called local memory transport. Although local memory transport is the most common transport in DirectShow, not all filters use it. For example, some filters send media data along a hardware path, and use pins only to deliver control information. For example, see the [**IOverlay**](/windows/desktop/api/Strmif/nn-strmif-ioverlay) interface.

DirectShow defines two mechanisms for local memory transport, the push model and the pull model. In the push model, a source filter generates data and delivers it to the next filter downstream. That filter passively receives the data, processes it, and sends it further downstream. In the pull model, the source filter is connected to a parser filter. The parser filter requests data from the source filter. The source filter responds to the requests by delivering data. The push model uses the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface, and the pull model uses the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface.

The push model is more common than the pull model. Therefore, the articles that follow assume a push model. The last article in this section, [Pull Model](pull-model.md), describes how the **IAsyncReader** interface differs from **IMemInputPin**.

## Related topics

<dl> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> </dl>

 

 



