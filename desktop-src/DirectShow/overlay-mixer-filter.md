---
description: Overlay Mixer Filter
ms.assetid: e80938b7-31f0-467b-a3fa-c4511d14758d
title: Overlay Mixer Filter
ms.topic: article
ms.date: 05/31/2018
---

# Overlay Mixer Filter

The Overlay Mixer filter is a video renderer designed specifically for DVD playback and broadcast video streams with line-21 closed captioning. The Overlay Mixer also supports Video Port Extensions (VPEs), enabling it to work with hardware MPEG-2 decoders or analog TV tuners that send video directly to the graphics card, rather than over the PCI bus.

> [!Note]  
> The [Video Mixing Renderer 9](video-mixing-renderer-filter-9.md) is now preferred over the Overlay Mixer filter, except in VPE scenarios.

 

The Overlay Mixer uses DirectDraw for rendering. It requires an overlay surface on the graphics card. The primary video stream should be connected to pin 0. Secondary streams (closed caption graphics or DVD subpictures) are connected to pins 1 and higher. The Overlay Mixer blits the secondary streams directly onto the primary suface; it does not mix or alpha blend them.

The Overlay Mixer uses the Video Renderer for window management. The Video Renderer connects to the Overlay Mixer's output pin.

This filter is added to the filter graph automatically when applications use the [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder) and [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interfaces to create the graph. The Filter Graph Manager will not automatically add the Overlay Mixer to the graph.

> [!Note]  
> In the following table, the media subtypes accepted on input pin 0 are hardware dependent. The Overlay Mixer cannot determine whether a particular subtype is supported until it creates the DirectDraw surface. Therefore, the only way for an upstream filter to determine whether a subtype is supported is to attempt a connection with that subtype.

 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td><a href="/windows/desktop/api/Strmif/nn-strmif-iamoverlayfx"><strong>IAMOverlayFX</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iamvideodecimationproperties"><strong>IAMVideoDecimationProperties</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideo"><strong>IDDrawExclModeVideo</strong></a>, <a href="ikspropertyset.md"><strong>IKsPropertySet</strong></a>, <a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/previous-versions/windows/desktop/api/Mixerocx/nn-mixerocx-imixerocx"><strong>IMixerOCX</strong></a>, <a href="/previous-versions/windows/desktop/api/Amvideo/nn-amvideo-iqualprop"><strong>IQualProp</strong></a>, <a href="/previous-versions/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify"><strong>IVPNotify</strong></a>, <a href="/previous-versions/windows/desktop/api/vpnotify/nn-vpnotify-ivpnotify2"><strong>IVPNotify2</strong></a></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major Type: MEDIATYPE_Video<br/> Subtypes:<br/>
<ul>
<li>MEDIASUBTYPE_Overlay (pin 0 only)</li>
<li>DirectDraw YUV formats (pin 0 only)</li>
<li>DirectDraw Video Acceleration formats (pin 0 only)</li>
<li>DirectDraw RGB formats (all input pins)</li>
</ul>
Format Types:<br/>
<ul>
<li>Format_VIDEOINFO</li>
<li>Format_VIDEOINFO2</li>
</ul></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><a href="/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator"><strong>IAMVideoAccelerator</strong></a>, <a href="ikspin.md"><strong>IKsPin</strong></a>, <a href="ikspropertyset.md"><strong>IKsPropertySet</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig"><strong>IMixerPinConfig</strong></a>, <a href="/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig2"><strong>IMixerPinConfig2</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ioverlay"><strong>IOverlay</strong></a> (pin 0 only), <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipinconnection"><strong>IPinConnection</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a>, <a href="/previous-versions/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify"><strong>IVPNotify</strong></a>, <a href="/previous-versions/windows/desktop/api/vpnotify/nn-vpnotify-ivpnotify2"><strong>IVPNotify2</strong></a></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>MEDIATYPE_Video, MEDIASUBTYPE_Overlay</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td><a href="/windows/desktop/api/Control/nn-control-imediaposition"><strong>IMediaPosition</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_OverlayMixer</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>No property page.</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>qdvd.dll</td>
</tr>
<tr class="odd">
<td><a href="merit.md">Merit</a></td>
<td>MERIT_DO_NOT_USE</td>
</tr>
<tr class="even">
<td><a href="filter-categories.md">Filter Category</a></td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

### Remarks

The Overlay Mixer uses destination color keying to mix video surfaces with overlays. It blits the color key and the secondary video to the primary surface, and sends the primary video to the overlay surface. The graphics card then composites the two surfaces into its frame buffer.

To test whether the graphics driver supports hardware overlay, call **IDirectDraw7::GetCaps**. If the **dwMaxVisibleOverlays** field in the **DDCAPS** structure is greater than zero, the driver supports hardware overlay.

Applications can control some behaviors on the Overlay Mixer through the [**IMixerPinConfig2**](/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig2) interface. Game developers can use the Overlay Mixer to display video in DirectDraw Exclusive Mode, as described later in this section. The [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9) now provides better support for video in games, however. For more information, see [Using the Video Mixing Renderer](using-the-video-mixing-renderer.md).

The following information is provided for the benefit of filter developers, and game developers who want to use the Overlay Mixer in DirectDraw Exclusive Mode.

**Overlay Mixer Internal Operations**

The Overlay Mixer exposes an input pin for each incoming stream. Typically, there are three input pins: pin 0 for video data, and pins 1 and 2 for line 21 and DVD subpicture data. Internally, the Overlay Mixer creates a DirectDraw object with a primary surface comprising the entire desktop, plus an overlay surface whose rectangle is defined by the size of the video stream on Pin 0. If the decoder does not specify a color key, the Overlay Mixer uses default color keys: dark gray for more recent graphics cards and magenta for older 256-color cards.

> [!Note]  
> The results are undefined if the decoder delivers two secondary video streams simultaneously in the same place on the overlay surface. (This sometimes occurs with DVDs that contain subpicture and line 21 streams.) The video might flicker, or display only one of the streams.

 

On Windows Vista or later, the Overlay Mixer disables Desktop Window Manager (DWM) composition if the display driver supports hardware overlay. Applications should avoid using the Overlay Mixer filter; use the VMR-9 or the Enhanced Video Renderer (EVR) instead.

**Upstream Connection with the Video Decoder**

Typically the Overlay Mixer's input pins connect to an upstream video decoder. The primary video stream must connect to the pin 0. The line 21 or subpicture streams connect to pin 1 or greater. If the decoder is a software decoder that uses the host CPU exclusively, the connection between the decoder and the Pin 0 is an [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) connection. If the decoder uses hardware acceleration, the connection to Pin 0 must use the [**IAMVideoAccelerator**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator) inferface. These two types of connections are mutually exclusive.

If the decoder draws directly onto the overlay surface, it should use the [**IOverlay**](/windows/desktop/api/Strmif/nn-strmif-ioverlay) interface on pin 0 and implement the [**IOverlayNotify**](/windows/desktop/api/Strmif/nn-strmif-ioverlaynotify) interface.

Filters that wrap a hardware decoder and connect to the Overlay Mixer through a video port must implement the [**IVPConfig**](/previous-versions/windows/desktop/api/Vpconfig/nn-vpconfig-ivpconfig) interface. The Overlay Mixer implements the [**IVPNotify**](/previous-versions/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify) interface. These two interfaces enable the decoder to specify the overlay surfaces it requires, and they enable the Overlay Mixer to inform the decoder of the location of those surfaces in video memory.

The Overlay Mixer also ensures that the video rectangle is scaled correctly. Video capture involves certain issues with respect to scaling the preview image and capturing interleaved video frames. If you are developing a filter or WDM driver for a hardware video capture device, refer to the [**IVPConfig**](/previous-versions/windows/desktop/api/Vpconfig/nn-vpconfig-ivpconfig) and [**IVPNotify**](/previous-versions/windows/desktop/api/Vpnotify/nn-vpnotify-ivpnotify) reference pages for more information on these topics.

The Overlay Mixer is not used in 1394 or USB capture scenarios. It is used in video capture over the PCI bus.

**Downstream Connection with the Video Renderer**

The Overlay Mixer has an output pin that connects to the [Video Renderer](video-renderer-filter.md) filter. The Video Renderer in this case does not render the video; it simply manages the video window.

The pin connection uses the [**IOverlay**](/windows/desktop/api/Strmif/nn-strmif-ioverlay) interface rather than the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface. The Video Renderer passes its window handle through the Overlay Mixer to DirectDraw, which manages the rectangle clipping. Applications can control the Video Renderer through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) and [**IBasicVideo2**](/windows/desktop/api/Control/nn-control-ibasicvideo2) interfaces on the Filter Graph Manager.

**DirectDraw Exclusive Mode**

The Overlay Mixer's DirectDraw exclusive mode enables games to display video on some part of the screen. In this mode, the Overlay Mixer renders the video directly to a DirectDraw surface created by the game application, rather than to a window provided by the Video Renderer. This enables games to control the color key. The Overlay Mixer exposes only one input pin in DirectDraw exclusive mode, which means that no mixing of Line 21 or DVD subpicture can be performed in this mode.

To use the Overlay Mixer in DirectDraw exclusive mode, create an instance of the Overlay Mixer and query it for the [**IDDrawExclModeVideo**](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideo) interface before building the filter graph. Then call [**IDDrawExclModeVideo::SetDDrawSurface**](/windows/desktop/api/Strmif/nf-strmif-iddrawexclmodevideo-setddrawsurface) to specify the DirectDraw surface for rendering. One significant limitation of this mode is that the game does not get access to the actual video bits. If you use **IDDrawExclModeVideo**, your application creates the primary surface, and the Overlay Mixer creates the overlay surface.

You can also use DirectDraw exclusive mode to perform windowless rendering—for example, in a Web page—but this is not recommended, because the Overlay Mixer does not perform any mixing in this mode. This means that no line 21 or subpicture data can be displayed.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




