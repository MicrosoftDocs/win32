---
Description: Filter Graph Manager
ms.assetid: a227539a-7f9a-4f8d-99fe-f9ab67df9ef4
title: Filter Graph Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

-   [**IAMGraphStreams**](/windows/win32/Strmif/nn-strmif-iamgraphstreams?branch=master)
-   [**IAMStats**](/windows/win32/Control/nn-control-iamstats?branch=master)
-   [**IBasicAudio**](/windows/win32/Control/nn-control-ibasicaudio?branch=master)
-   [**IBasicVideo**](/windows/win32/Control/nn-control-ibasicvideo?branch=master)
-   [**IBasicVideo2**](/windows/win32/Control/nn-control-ibasicvideo2?branch=master)
-   [**IFilterChain**](/windows/win32/Strmif/nn-strmif-ifilterchain?branch=master)
-   [**IFilterGraph**](/windows/win32/Strmif/nn-strmif-ifiltergraph?branch=master)
-   [**IFilterGraph2**](/windows/win32/Strmif/nn-strmif-ifiltergraph2?branch=master)
-   [**IFilterGraph3**](/windows/win32/Strmif/nn-strmif-ifiltergraph3?branch=master)
-   [**IFilterMapper2**](/windows/win32/Strmif/nn-strmif-ifiltermapper2?branch=master)
-   [**IGraphBuilder**](/windows/win32/Strmif/nn-strmif-igraphbuilder?branch=master)
-   [**IGraphConfig**](/windows/win32/Strmif/nn-strmif-igraphconfig?branch=master)
-   [**IGraphVersion**](/windows/win32/Strmif/nn-strmif-igraphversion?branch=master)
-   [**IMediaControl**](/windows/win32/Control/nn-control-imediacontrol?branch=master)
-   [**IMediaEvent**](/windows/win32/Control/nn-control-imediaevent?branch=master)
-   [**IMediaEventEx**](/windows/win32/Control/nn-control-imediaeventex?branch=master)
-   [**IMediaEventSink**](/windows/win32/Strmif/nn-strmif-imediaeventsink?branch=master)
-   [**IMediaFilter**](/windows/win32/Strmif/nn-strmif-imediafilter?branch=master)
-   [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master)
-   [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master)
-   [**IQueueCommand**](/windows/win32/Control/nn-control-iqueuecommand?branch=master)
-   [**IRegisterServiceProvider**](/windows/win32/Strmif/nn-strmif-iregisterserviceprovider?branch=master)
-   [**IResourceManager**](/windows/win32/Strmif/nn-strmif-iresourcemanager?branch=master)
-   **IServiceProvider**
-   [**IVideoFrameStep**](/windows/win32/Strmif/nn-strmif-ivideoframestep?branch=master)
-   [**IVideoWindow**](/windows/win32/Control/nn-control-ivideowindow?branch=master)

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



