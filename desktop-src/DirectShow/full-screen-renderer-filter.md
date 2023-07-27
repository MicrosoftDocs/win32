---
description: Full Screen Renderer Filter
ms.assetid: 59332096-bdfe-4208-b99a-1f434652f287
title: Full Screen Renderer Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Full Screen Renderer Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Full Screen Renderer filter provides full-screen video rendering on older hardware. Newer video cards can stretch the video efficiently enough that the Full Screen Renderer is not required. Therefore, the use of this filter is now deprecated.

Do not manually add this filter to the filter graph. If an application calls [**IVideoWindow::put\_FullScreenMode**](/windows/desktop/api/Control/nf-control-ivideowindow-put_fullscreenmode), the Filter Graph Manager automatically selects the appropriate video renderer for full-screen mode. The selection is transparent to the application. With current video cards, the Filter Graph Manager is unlikely to select the Full Screen Renderer.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IFullScreenVideoEx**](/previous-versions/windows/desktop/api/Amvideo/nn-amvideo-ifullscreenvideoex), [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), [**IQualProp**](/previous-versions/windows/desktop/api/Amvideo/nn-amvideo-iqualprop) |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_Null                                                                                                                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                                                                                             |
| Output Pin Media Types                   | Not applicable                                                                                                                                                                                                                                     |
| Output Pin Interfaces                    | Not applicable                                                                                                                                                                                                                                     |
| Filter CLSID                             | CLSID\_ModexRenderer                                                                                                                                                                                                                               |
| Property Page CLSID                      | CLSID\_ModexProperties                                                                                                                                                                                                                             |
| Executable                               | quartz.dll                                                                                                                                                                                                                                         |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                                                                                                                    |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                                                      |



 

## Remarks

The Full Screen Renderer supports a static set of display modes. The video card on the user's system might not support every mode, however. To determine whether the card supports a particular mode, call the [**IFullScreenVideoEx::IsModeAvailable**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-ifullscreenvideoex-ismodeavailable) method. You can also disable a particular display mode programmatically, by calling the [**IFullScreenVideoEx::SetEnabled**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-ifullscreenvideoex-setenabled). The Full Screen Renderer currently supports the display modes shown in the following table:



| Mode | Width | Height | Bit depth |
|------|-------|--------|-----------|
| 0    | 320   | 200    | 16        |
| 1    | 320   | 200    | 8         |
| 2    | 320   | 240    | 16        |
| 3    | 320   | 240    | 8         |
| 4    | 640   | 400    | 16        |
| 5    | 640   | 400    | 8         |
| 6    | 640   | 480    | 16        |
| 7    | 640   | 480    | 8         |
| 8    | 800   | 600    | 16        |
| 9    | 800   | 600    | 8         |
| 10   | 1024  | 768    | 16        |
| 11   | 1024  | 768    | 8         |
| 12   | 1152  | 864    | 16        |
| 13   | 1152  | 864    | 8         |
| 14   | 1280  | 1024   | 16        |
| 15   | 1280  | 1024   | 8         |



 

(All modes are RGB.) This list is subject to change, however. Use the [**IFullScreenVideoEx::GetModeInfo**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-ifullscreenvideoex-getmodeinfo) method to get information about the modes. The Full Screen Renderer always chooses the lowest-resolution mode available, limited by a property called the *clip factor*, which determines how much of the video the Full Screen Renderer is allowed to clip. For more information, see [**IFullScreenVideoEx::GetClipFactor**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-ifullscreenvideoex-getclipfactor).

When the application runs or pauses the filter graph, the Full Screen Renderer switches to the display mode that was chosen. When the graph stops, the Full Screen Renderer restores the original display mode.

The Full Screen Renderer can function only as the foreground active window. If the user switches to another application, the Full Screen Renderer hides the video by minimizing or hiding the video window.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



