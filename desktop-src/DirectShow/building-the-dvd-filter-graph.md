---
description: Building the DVD Filter Graph
ms.assetid: 1d2f8284-2deb-4207-b067-24a54d6b286c
title: Building the DVD Filter Graph
ms.topic: article
ms.date: 05/31/2018
---

# Building the DVD Filter Graph

As with any DirectShow application, a DVD playback application starts by building a filter graph. DirectShow provides the following components for DVD playback:

-   [DVD Graph Builder](dvd-graph-builder.md). A helper object that constructs the filter graph. It exposes the [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder) interface.
-   [DVD Navigator](dvd-navigator-filter.md) filter. A DirectShow filter that handles DVD playback, navigation, and other commands.

DVD playback also requires an MPEG-2 decoder. Hardware and software MPEG-2 decoders are available from third parties. First, create an instance of the DVD Graph Builder object.


```C++
IDvdGraphBuilder *pBuild = NULL;
hr = CoCreateInstance(CLSID_DvdGraphBuilder, NULL, 
    CLSCTX_INPROC_SERVER, IID_IDvdGraphBuilder, (void **)&pBuild);
```



At this point, you can select and configure the video renderer before you build the rest of the graph. This step, which is optional, is described in more detail in the next section. If you omit this step, the DVD Graph Builder selects a default renderer. Next, build the graph by calling the [**IDvdGraphBuilder::RenderDvdVideoVolume**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-renderdvdvideovolume) method.


```C++
AM_DVD_RENDERSTATUS buildStatus;
hr = pBuild->RenderDvdVideoVolume(L"Z:\\video_ts", 0, &buildStatus);
```



The first parameter is the name of a directory that contains the DVD files. On a DVD disc, these files reside in a directory named VIDEO\_TS. If the first parameter is **NULL**, the DVD Graph Builder uses the first drive that contains a DVD volume.

The second parameter contains various optional flags for choosing the type of decoder (hardware or software) and other options.

The third parameter is an [**AM\_DVD\_RENDERSTATUS**](/windows/win32/api/strmif/ns-strmif-am_dvd_renderstatus) structure that receives status information. If the [**RenderDvdVideoVolume**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-renderdvdvideovolume) method returns S\_FALSE, it means the call partially succeeded (or partially failed, if you're a pessimist). For example, the method might fail to render the subpicture stream, even though the other streams rendered successfully. If the **RenderDvdVideoVolume** method returns an error code or the value S\_FALSE, you can examine the **AM\_DVD\_RENDERSTATUS** structure for details about the error.

Next, get a pointer to the Filter Graph Manager by calling [**IDvdGraphBuilder::GetFiltergraph**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-getfiltergraph). This method returns a pointer to the Filter Graph Manager's [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) interface.


```C++
IGraphBuilder *pGraph = NULL;
hr =  pBuild->GetFiltergraph(&m_pGraph);
```



Use the [**IDvdGraphBuilder::GetDvdInterface**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-getdvdinterface) method to retrieve DVD-related interfaces, including the following:

-   [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2). Controls playback and DVD commands
-   [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2). Returns information about the DVD Navigator's current state.
-   [**IAMLine21Decoder**](/previous-versions/windows/desktop/api/il21dec/nn-il21dec-iamline21decoder). Controls closed caption display. Closed caption display is enabled by default. To disable it, call [**IAMLine21Decoder::SetServiceState**](/previous-versions/windows/desktop/api/il21dec/nf-il21dec-iamline21decoder-setservicestate) with the AM\_L21\_CCSTATE\_Off flag.
-   [**IBasicAudio**](/windows/desktop/api/Control/nn-control-ibasicaudio). Controls audio volume and balance.

For example, the following code returns the [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2) interface.


```C++
IDvdControl2 *pDvdControl = NULL;
hr = pBuild->GetDvdInterface(IID_IDvdControl2, (void**)&pDvdControl);
```



The recommended way to build the DVD playback filter graph is to have a [DVD Graph Builder](dvd-graph-builder.md) object do it for you automatically. This approach is demonstrated below and in the DVD sample application. If you need to build your DVD filter graph manually, you can do so by following the basic rules of graph building discussed elsewhere in the DirectShow documentation. Generally, you should not manually add, remove, connect, or disconnect individual filters in the graph created by the DVD Graph Builder, because doing so might confuse the cleanup code.

Configuring the Video Renderer

DirectShow provides several video renderer filters. Before you build the graph, you can chose which video renderer you prefer. Select the renderer by calling [**IDvdGraphBuilder::GetDvdInterface**](/windows/desktop/api/Strmif/nf-strmif-idvdgraphbuilder-getdvdinterface) and requesting an interface that is specific to that renderer:

-   Overlay Mixer Filter: [**IDDrawExclModeVideo**](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideo).
-   Video Mixing Renderer 7 (VMR-7): [**IVMRFilterConfig**](/windows/desktop/api/Strmif/nn-strmif-ivmrfilterconfig).
-   Video Mixing Renderer 9 (VMR-9): [**IVMRFilterConfig9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrfilterconfig9).
-   Enhanced Video Renderer (EVR): [**IEVRFilterConfig**](/windows/desktop/api/evr/nn-evr-ievrfilterconfig).

If you request any of these interfaces before building the filter graph, the DVD Graph Builder creates the corresponding video renderer. Later, when you build the graph, the DVD Graph Builder will try to use that renderer. But if it cannot build the graph using the renderer you selected, it may switch to another renderer. For example, your MPEG-2 decoder might not be compatible with the VMR filter, in which case the DVD Graph Builder would default to the Overlay Mixer.

These interfaces also give you a chance to configure the renderer before it is connected to the decoder. For example, you can set the VMR to use windowless mode instead of the default windowed mode. For more information about video renderers, see the topic [About Video Rendering in DirectShow](about-video-rendering-in-directshow.md).

On Windows XP and later, the DVD Graph Builder always uses the [Video Mixing Renderer 7](video-mixing-renderer-filter-7.md) (VMR-7), unless:

-   The caller queries interfaces found only the [Overlay Mixer](overlay-mixer-filter.md), such as [**IMixerPinConfig2**](/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig2). This sends a hint to the DVD Graph Builder that the application wants to use the Overlay Mixer and not the VMR. Windows Media Player also has a dialog box option to force the use of the Overlay Mixer.
-   The installed decoder is not VMR-compatible. During graph building, the new [**IAMDecoderCaps**](/windows/desktop/api/Strmif/nn-strmif-iamdecodercaps) interface is used to check for the decoder's VMR support. If that is not present, the DVD Graph Builder will use the Overlay Mixer.
-   While using a hardware decoder, the decoder cannot connect to the [Video Port Manager](video-port-manager.md) (VPM). If a hardware decoder cannot use the VPM, then it cannot use the VMR, and so the DVD Graph Builder then tries to build a graph using the Overlay Mixer.
-   The display card is known to have insufficient resources and/or capabilities to support the VMR but does not correctly report this in the driver. (Some known cases are specifically excluded by the DVD Graph Builder.)
-   The connection between the decoder and the VMR fails for any reason, usually due to a lack of VRAM to create the necessary surfaces. In these cases, the DVD Graph Builder switches off VMR use and tries to use the Overlay Mixer to build a graph.

Windowed Mode

In windowed mode (Overlay Mixer or VMR), the renderer creates its own video window. To make this window a child of the application window, call [**IVideoWindow::put\_Owner**](/windows/desktop/api/Control/nf-control-ivideowindow-put_owner) with a handle to the application. Also call [**IVideoWindow::put\_WindowStyle**](/windows/desktop/api/Control/nf-control-ivideowindow-put_windowstyle) to set the WS\_CHILD and WS\_CLIPSIBLINGS styles on the renderer's video window. To get mouse messages from the renderer's video window, call [**IVideoWindow::put\_MessageDrain**](/windows/desktop/api/Control/nf-control-ivideowindow-put_messagedrain) with a handle to the application window. This method sets up a "message drain" — the video window forwards any mouse messages it receives to the message drain window.


```C++
pVideoWindow->put_Owner((OAHWND)hwnd);
pVideoWindow->put_WindowStyle(WS_CHILD | WS_CLIPSIBLINGS);
pVideoWindow->put_MessageDrain((OAHWND)hwnd) ;
```



The message drain makes selecting DVD menu buttons somewhat complicated. Assuming the video window does not fill the application's entire client area, some mouse events will fall outside the video window. When you get a mouse event from *inside* the video window, you should process it for DVD menu navigation. Mouse events from *outside* the video window should not be processed. With the message drain, there is no way to distinguish between the two. Furthermore, the coordinates for mouse events from the video window are relative to the video window's client area; but mouse events from outside the video window are relative to the application's client area.

Windowless Mode

Windowless mode avoids the problems with mouse messages altogether. You do not need a message drain, because the VMR (or EVR) does not create its own window in windowless mode. Instead, it draws directly onto your application window. If the destination rectangle is smaller than the application client area, the DVD Navigator takes this into account when it calculates the DVD button positions. Therefore, when you get a mouse message, you can pass the coordinates directly to the DVD Navigator, as described in the section Menu Navigation.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 
