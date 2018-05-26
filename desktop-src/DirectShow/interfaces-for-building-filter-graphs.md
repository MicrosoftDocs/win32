---
Description: Interfaces for Building Filter Graphs
ms.assetid: 18d5217a-7f4e-49e9-ac14-2f4ba229e065
title: Interfaces for Building Filter Graphs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces for Building Filter Graphs

Applications use these interfaces to build various types of filter graphs.



| Interface                                                  | Description                                                 |
|------------------------------------------------------------|-------------------------------------------------------------|
| [**IAMFilterGraphCallback**](/windows/win32/Strmif/nn-strmif-iamfiltergraphcallback?branch=master)   | Receive callback notifications if a pin cannot be rendered. |
| [**IAMGraphBuilderCallback**](/windows/win32/Strmif/nn-strmif-iamgraphbuildercallback?branch=master) | Provides a callback mechanism during graph building.        |
| [**ICaptureGraphBuilder2**](/windows/win32/Strmif/nn-strmif-icapturegraphbuilder2?branch=master)     | Build filter graphs for video capture.                      |
| [**ICreateDevEnum**](/windows/win32/Strmif/nn-strmif-icreatedevenum?branch=master)                   | Enumerate system devices, such as capture devices.          |
| [**IDvdGraphBuilder**](/windows/win32/Strmif/nn-strmif-idvdgraphbuilder?branch=master)               | Build filter graphs for DVD navigation and playback.        |
| [**IEnumFilters**](/windows/win32/Strmif/nn-strmif-ienumfilters?branch=master)                       | Enumerate the filters in the graph.                         |
| [**IFilterGraph2**](/windows/win32/Strmif/nn-strmif-ifiltergraph2?branch=master)                     | Add, remove, or connect filters.                            |
| [**IFilterMapper2**](/windows/win32/Strmif/nn-strmif-ifiltermapper2?branch=master)                   | Enumerate the filters registered on the user's system.      |
| [**IGraphBuilder**](/windows/win32/Strmif/nn-strmif-igraphbuilder?branch=master)                     | Build filter graphs for file playback or for custom uses.   |
| [**IGraphConfig**](/windows/win32/Strmif/nn-strmif-igraphconfig?branch=master)                       | Dynamically reconfigure a filter graph.                     |
| [**IGraphVersion**](/windows/win32/Strmif/nn-strmif-igraphversion?branch=master)                     | Determine when the graph changes.                           |



 

 

 



