---
Description: Filter Graph Manager
ms.assetid: 'a227539a-7f9a-4f8d-99fe-f9ab67df9ef4'
title: Filter Graph Manager
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

-   [**IAMGraphStreams**](iamgraphstreams.md)
-   [**IAMStats**](iamstats.md)
-   [**IBasicAudio**](ibasicaudio.md)
-   [**IBasicVideo**](ibasicvideo.md)
-   [**IBasicVideo2**](ibasicvideo2.md)
-   [**IFilterChain**](ifilterchain.md)
-   [**IFilterGraph**](ifiltergraph.md)
-   [**IFilterGraph2**](ifiltergraph2.md)
-   [**IFilterGraph3**](ifiltergraph3.md)
-   [**IFilterMapper2**](ifiltermapper2.md)
-   [**IGraphBuilder**](igraphbuilder.md)
-   [**IGraphConfig**](igraphconfig.md)
-   [**IGraphVersion**](igraphversion.md)
-   [**IMediaControl**](imediacontrol.md)
-   [**IMediaEvent**](imediaevent.md)
-   [**IMediaEventEx**](imediaeventex.md)
-   [**IMediaEventSink**](imediaeventsink.md)
-   [**IMediaFilter**](imediafilter.md)
-   [**IMediaPosition**](imediaposition.md)
-   [**IMediaSeeking**](imediaseeking.md)
-   [**IQueueCommand**](iqueuecommand.md)
-   [**IRegisterServiceProvider**](iregisterserviceprovider.md)
-   [**IResourceManager**](iresourcemanager.md)
-   **IServiceProvider**
-   [**IVideoFrameStep**](ivideoframestep.md)
-   [**IVideoWindow**](ivideowindow.md)

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



