---
description: Filter Graph Manager
ms.assetid: 'b1a53193-27c6-4e86-a5b9-f3c1e4401690'
title: Filter Graph Manager
ms.topic: article
ms.date: 05/31/2018
---

# Filter Graph Manager

The Filter Graph Manager builds and controls filter graphs. This object is the central component in DirectShow. Applications use it to build and control filter graphs. The Filter Graph Manager also handles synchronization, event notification, and other aspects of the controlling the filter graph. Create this object by calling **CoCreateInstance**.

### CLSID

There are two CLSIDs for creating the Filter Graph Manager:



| CLSID                      | Description                                                 |
|----------------------------|-------------------------------------------------------------|
| CLSID\_FilterGraph         | Creates the Filter Graph Manager on a shared worker thread. |
| CLSID\_FilterGraphNoThread | Creates the Filter Graph Manager on the application thread. |



 

Generally, applications should use CLSID\_FilterGraph. Both CLSIDs create the same object, but they use different threading models:

-   CLSID\_FilterGraph creates the Filter Graph Manager on a worker thread, which is shared by all CLSID\_FilterGraph instances within the same process. The thread dispatches messages sent by filters, and controls the lifetime of any windows created by filters.
-   CLSID\_FilterGraphNoThread creates the Filter Graph Manager on the application's thread. If you use this CLSID, the thread that calls **CoCreateInstance** must have a message loop that dispatches messages; otherwise, deadlocks can occur. Also, before the application thread exits, it must release the Filter Graph Manager and all graph objects (such as filters, pins, reference clocks, and so forth).

### Interfaces

The Filter Graph Manager exposes the following interfaces:

-   [**IAMGraphStreams**](/windows/desktop/api/Strmif/nn-strmif-iamgraphstreams)
-   [**IAMStats**](/windows/desktop/api/Control/nn-control-iamstats)
-   [**IBasicAudio**](/windows/desktop/api/Control/nn-control-ibasicaudio)
-   [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo)
-   [**IBasicVideo2**](/windows/desktop/api/Control/nn-control-ibasicvideo2)
-   [**IFilterChain**](/windows/desktop/api/Strmif/nn-strmif-ifilterchain)
-   [**IFilterGraph**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph)
-   [**IFilterGraph2**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph2)
-   [**IFilterGraph3**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph3)
-   [**IFilterMapper2**](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2)
-   [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder)
-   [**IGraphConfig**](/windows/desktop/api/Strmif/nn-strmif-igraphconfig)
-   [**IGraphVersion**](/windows/desktop/api/Strmif/nn-strmif-igraphversion)
-   [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol)
-   [**IMediaEvent**](/windows/desktop/api/Control/nn-control-imediaevent)
-   [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex)
-   [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink)
-   [**IMediaFilter**](/windows/desktop/api/Strmif/nn-strmif-imediafilter)
-   [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition)
-   [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)
-   [**IQueueCommand**](/windows/desktop/api/Control/nn-control-iqueuecommand)
-   [**IRegisterServiceProvider**](/windows/desktop/api/Strmif/nn-strmif-iregisterserviceprovider)
-   [**IResourceManager**](/windows/desktop/api/Strmif/nn-strmif-iresourcemanager)
-   **IServiceProvider**
-   [**IVideoFrameStep**](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep)
-   [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow)

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



