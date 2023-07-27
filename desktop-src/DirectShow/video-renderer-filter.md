---
description: Video Renderer Filter
ms.assetid: '7719ed9d-e3b9-4c84-b587-4e120b5cabf8'
title: Video Renderer Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Renderer Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Video Renderer filter is a robust, all-purpose video renderer.

> [!Note]  
> On Windows XP and later, the default video renderer is the [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7). The VMR-7 and the Video Renderer both have the friendly name "Video Renderer." On earlier platforms, the Video Renderer is the default renderer. See [Choosing the Right Renderer](choosing-the-right-renderer.md).

 

The Video Renderer uses DirectDraw and overlay surfaces, if the video card supports them. The Filter Graph Manager exposes the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface, which enables applications to set and retrieve properties on the Video Renderer. With newer video cards, the Video Renderer supports full-screen rendering. Otherwise, the Filter Graph Manager automatically switches to the [Full Screen Renderer](full-screen-renderer-filter.md) filter for full-screen mode. See [**IVideoWindow::put\_FullScreenMode**](/windows/desktop/api/Control/nf-control-ivideowindow-put_fullscreenmode) for more information.

-   ![Important]  
    > Normally, this filter's video window processes messages on a worker thread created by the Filter Graph Manager. Howerver, if an application directly creates the filter using **CoCreateInstance**, the video window processes messages on the application thread. In that case, the application thread must have a message loop, to dispatch messages to the video window. Also, the thread must not exit until the final **Release** call to the Video Renderer, which occurs when the Filter Graph Manager shuts down. Otherwise, the application might deadlock.

     



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo), [**IBasicVideo2**](/windows/desktop/api/Control/nn-control-ibasicvideo2), [**IDirectDrawVideo**](/previous-versions/windows/desktop/api/Amvideo/nn-amvideo-idirectdrawvideo), [**IKsPropertySet**](ikspropertyset.md), [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), [**IQualProp**](/previous-versions/windows/desktop/api/Amvideo/nn-amvideo-iqualprop), [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) |
| Input Pin Media Types                    | Uncompressed video formats.                                                                                                                                                                                                                                                                                                                                                                              |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IOverlay**](/windows/desktop/api/Strmif/nn-strmif-ioverlay), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IPinConnection**](/windows/desktop/api/Strmif/nn-strmif-ipinconnection), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                                                                                                                                                                           |
| Output Pin Media Types                   | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                          |
| Output Pin Interfaces                    | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                          |
| Filter CLSID                             | CLSID\_VideoRenderer                                                                                                                                                                                                                                                                                                                                                                                     |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                                                                                                                                                                                                        |
| Executable                               | quartz.dll                                                                                                                                                                                                                                                                                                                                                                                               |
| [Merit](merit.md)                       | Windows XP and later: **MERIT\_UNLIKELY**                                                                                                                                                                                                                                                                                                                                                                |
| [Filter Category](filter-categories.md) | **CLSID\_LegacyAmFilterCategory**                                                                                                                                                                                                                                                                                                                                                                        |



 

## Remarks

In the debug version of Quartz.dll, if the LOG\_TRACE debug level is set to 5 or higher, the Video Renderer displays each frame's time stamps on the video window. These numbers do not appear in the retail version of the DLL. For more information, see [Debug Output Functions](debug-output-functions.md).

The following remarks are intended for filter developers:

The Video Renderer accepts YUV formats if the video graphics card supports YUV overlay surfaces. When it first connects to the upstream filter, however, the Video Renderer requires an RGB format that matches the color depth of the current monitor settings. For example, if the current display setting is 24-bit color, the upstream filter must be able to provide 24-bit RGB video. When the filter graph switches to a runing state, the Video Renderer negotiates a dynamic format change to the appropriate YUV color space.

By connecting with an RGB type, the Video Renderer ensures that it can use GDI in case DirectDraw is not available. It will switch to GDI if another application is using the video memory, if the video rectangle straddles two monitors on a multi-monitor system, or if the video rectangle is completely obscured by another window.

> [!Note]  
> The Video Mixing Renderer does not perform this type of dynamic format change, and does not require an RGB media type, because it never uses GDI for rendering.

 

To negotiate a format change, the Video Renderer calls [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) with the new media type. If the upstream filter returns S\_OK, the Video Renderer attaches the new media to the next sample. The upstream filter should call [**IMediaSample::GetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatype) on each sample. If **GetMediaType** returns a non-**NULL** value, it indicates a format change, and the upstream filter should respond by switching output types. (Do not switch types in the **QueryAccept** method.) The upstream filter should accept at least the major RGB types, and ideally should support the common YUV types. During streaming, the Video Renderer might switch back and forth between YUV and RGB types any number of times. The Video Renderer does not accept dynamic format changes initiated by the upstream filter.

When the Video Renderer draws to a DirectDraw overlay surface, it allocates a single buffer for its input pin. If the upstream filter attempts to force a connection using multiple buffers, the Video Renderer will be unable to use the overlay surface.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



