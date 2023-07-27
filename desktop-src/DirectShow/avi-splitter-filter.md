---
description: AVI Splitter Filter
ms.assetid: df3c7d11-7ecc-499a-af36-b74437e21999
title: AVI Splitter Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVI Splitter Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The AVI Splitter Filter is used for playback of AVI files. It accepts data in AVI format and splits it into its constituent streams for further processing and/or rendering.



| Label | Value |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMMediaContent**](/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IPersistMediaPropertyBag**](/windows/desktop/api/Strmif/nn-strmif-ipersistmediapropertybag)                        |
| Input Pin Media Types                    | MEDIATYPE\_Stream, MEDIASUBTYPE\_Avi                                                                                                                                |
| Input Pin Interfaces                     | [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                                                    |
| Output Pin Media Types                   | Typically **MEDIATYPE\_Video** or **MEDIATYPE\_Audio**. The exact type depends on the content of the file, whether the file is compressed, and what codec was used. |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), IPropertyBag, [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)    |
| Filter CLSID                             | CLSID\_AviSplitter                                                                                                                                                  |
| Property Page CLSID                      | No property page.                                                                                                                                                   |
| Executable                               | quartz.dll                                                                                                                                                          |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                                       |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                       |



 

## Remarks

This filter is typically connected to the [Async File Source](file-source--async--filter.md) filter on its input pin. It can connect to any filter whose output pin supports [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) and offers the correct media type to the AVI Splitter filter's input pin.

The output pins on the AVI Splitter support the IPropertyBag::Read method for reading properties from individual streams. Currently, the following property is defined.



| Property | Description                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| name     | Returns the name of the stream, taken from the `'strn'` chunk in the AVI file. If this chunk is absent, the Read method returns E\_INVALIDARG. |



 

The IPropertyBag::Write method returns E\_FAIL. The [AVI Mux](avi-mux-filter.md) filter supports IPropertyBag::Write for saving stream properties into an AVI file.

The AVI Splitter does not allow downstream filters to use their own allocator.

The interleaving duration in the file determines how much memory the AVI Splitter will allocate to process it. A file that is interleaved in one second chunks will require much more memory to process than a file whose interleave duration is set to one or two frames. On modern computers, this is generally not an issue unless you are running multiple instances of the AVI Splitter simultaneously.

### Seeking

If the file contains a video stream, the AVI Splitter supports seeking by frame number. To enable frame-based seeking, call [**IMediaSeeking::SetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-settimeformat) on the [Filter Graph Manager](filter-graph-manager.md) with the value **TIME\_FORMAT\_FRAME**.

If the file contains an audio stream, the AVI Splitter supports seeking by sample number. To enable sample-based seeking, call [**SetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-settimeformat) on the Filter Graph Manager with the value **TIME\_FORMAT\_SAMPLE**.

In both cases, the output pin for that stream must be connected to a renderer filter.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



