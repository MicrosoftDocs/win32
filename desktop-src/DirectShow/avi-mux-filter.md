---
description: AVI Mux Filter
ms.assetid: 31d30c91-fc6a-45ec-a2e0-34e6a1e902a4
title: AVI Mux Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVI Mux Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The AVI Mux filter accepts multiple input streams and interleaves them into AVI format. The filter uses separate input pins for each input stream, and one output pin for the AVI stream.

Video capture or authoring applications can use this filter to save files to disk in AVI format. The filter is typically connected to the [File Writer](file-writer-filter.md) filter, but it can connect to any filter whose input pin supports the IStream and [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interfaces.




| Label | Value |
|--------|-------|
| Filter Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iconfigavimux"><strong>IConfigAviMux</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iconfiginterleaving"><strong>IConfigInterleaving</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipersistmediapropertybag"><strong>IPersistMediaPropertyBag</strong></a>, ISpecifyPropertyPages | 
| Input Pin Media Types | Any major type that corresponds to an old-style FOURCC, or MEDIATYPE_AUXLine21Data. (For more information, see <a href="fourccmap.md"><strong>FOURCCMap Class</strong></a>.)<ul><li>If the major type is MEDIATYPE_Audio, the format must be FORMAT_WaveFormatEx.</li><li>If the major type is MEDIATYPE_Video, the format must be FORMAT_VideoInfo or FORMAT_DvInfo.</li><li>If the major type is MEDIATYPE_Interleaved, the format must be FORMAT_DvInfo.</li></ul> | 
| Input Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol"><strong>IAMStreamControl</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, IPropertyBag, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Output Pin Media Types | MEDIATYPE_Stream, MEDIASUBTYPE_Avi | 
| Output Pin Interfaces | <a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a>, <a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a> | 
| Filter CLSID | CLSID_AviDest | 
| Property Page CLSID | CLSID_AviMuxProptyPage, CLSID_AviMuxProptyPage1 | 
| Executable | qcap.dll | 
| <a href="merit.md">Merit</a> | MERIT_DO_NOT_USE | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

### Remarks

The following remarks describe various aspects of the AVI Mux filter's functionality.

Pins

When the AVI Mux filter is created, it has one input pin. As each input pin is connected, the filter creates a new input pin.

Stream Properties

The input pins support the IPropertyBag interface for setting properties on individual streams. Currently, the following property is defined:



| Property | Description                                                           |
|----------|-----------------------------------------------------------------------|
| name     | The name of the stream. This property is written as a `'strn'` chunk. |



 

If the filter is running or paused, the IPropertyBag::Write method returns VFW\_E\_WRONG\_STATE.

Frame Rates

If the upstream filter does not specify a frame rate in the **AvgTimePerFrame** member of the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure, the AVI Mux uses the time stamps on the first video frame. The AVI file format does not support variable frame rates.

Dropped Frames

The AVI Mux filter calculates dropped frames based on each sample's media times, if available, or else the sample's time stamps. It writes a zero-length index entry for every dropped frame.

IMediaSeeking

The AVI Mux filter implements the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface as follows:

-   The [**GetCurrentPosition**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getcurrentposition) method returns the current progress of the multiplexing. If you are transcoding a file (slower than real time), this value is more accurate than the value returned by the Filter Graph Manager. For more information, see the Remarks section of the GetCurrentPosition reference page.
-   The [**GetDuration**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getduration) method queries each upstream filter and returns the duration of the longest stream. If any of these filters fails the GetDuration call (or does not support IMediaSeeking), the AVI Mux returns a failure code and fills in the *pDuration* parameter with the longest duration found. However, the value of *pDuration* in this case is not necessarily the length of the longest input stream.
-   The AVI Mux does not implement the GetStopPosition, GetPositions, GetAvailable, GetRate, or GetPreroll methods; nor does it implement any Set\* methods for seeking.

AVI 2.0 File Format Extensions

DirectShow currently supports the following AVI 2.0 file format extensions:

-   Increased AVI file size (greater than 1 GB)
-   Hierarchical indexing

For more information, see version 1.02 of the "OpenDML AVI File Format Extensions" published by the OpenDML AVI M-JPEG File Format Subcommittee.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



