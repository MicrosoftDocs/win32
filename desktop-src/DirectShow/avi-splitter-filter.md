---
Description: AVI Splitter Filter
ms.assetid: df3c7d11-7ecc-499a-af36-b74437e21999
title: AVI Splitter Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVI Splitter Filter

The AVI Splitter Filter is used for playback of AVI files. It accepts data in AVI format and splits it into its constituent streams for further processing and/or rendering.



|                                          |                                                                                                                                                                     |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMMediaContent**](/windows/win32/Qnetwork/nn-qnetwork-iammediacontent?branch=master), [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IPersistMediaPropertyBag**](/windows/win32/Strmif/nn-strmif-ipersistmediapropertybag?branch=master)                        |
| Input Pin Media Types                    | MEDIATYPE\_Stream, MEDIASUBTYPE\_Avi                                                                                                                                |
| Input Pin Interfaces                     | [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                                                    |
| Output Pin Media Types                   | Typically **MEDIATYPE\_Video** or **MEDIATYPE\_Audio**. The exact type depends on the content of the file, whether the file is compressed, and what codec was used. |
| Output Pin Interfaces                    | [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), IPropertyBag, [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)    |
| Filter CLSID                             | CLSID\_AviSplitter                                                                                                                                                  |
| Property Page CLSID                      | No property page.                                                                                                                                                   |
| Executable                               | quartz.dll                                                                                                                                                          |
| [Merit](merit.md)                       | MERIT\_NORMAL                                                                                                                                                       |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                       |



 

## Remarks

This filter is typically connected to the [Async File Source](file-source--async--filter.md) filter on its input pin. It can connect to any filter whose output pin supports [**IAsyncReader**](/windows/win32/Strmif/nn-strmif-iasyncreader?branch=master) and offers the correct media type to the AVI Splitter filter's input pin.

The output pins on the AVI Splitter support the IPropertyBag::Read method for reading properties from individual streams. Currently, the following property is defined.



| Property | Description                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| name     | Returns the name of the stream, taken from the `'strn'` chunk in the AVI file. If this chunk is absent, the Read method returns E\_INVALIDARG. |



 

The IPropertyBag::Write method returns E\_FAIL. The [AVI Mux](avi-mux-filter.md) filter supports IPropertyBag::Write for saving stream properties into an AVI file.

The AVI Splitter does not allow downstream filters to use their own allocator.

The interleaving duration in the file determines how much memory the AVI Splitter will allocate to process it. A file that is interleaved in one second chunks will require much more memory to process than a file whose interleave duration is set to one or two frames. On modern computers, this is generally not an issue unless you are running multiple instances of the AVI Splitter simultaneously.

### Seeking

If the file contains a video stream, the AVI Splitter supports seeking by frame number. To enable frame-based seeking, call [**IMediaSeeking::SetTimeFormat**](/windows/win32/Strmif/nf-strmif-imediaseeking-settimeformat?branch=master) on the [Filter Graph Manager](filter-graph-manager.md) with the value **TIME\_FORMAT\_FRAME**.

If the file contains an audio stream, the AVI Splitter supports seeking by sample number. To enable sample-based seeking, call [**SetTimeFormat**](/windows/win32/Strmif/nf-strmif-imediaseeking-settimeformat?branch=master) on the Filter Graph Manager with the value **TIME\_FORMAT\_SAMPLE**.

In both cases, the output pin for that stream must be connected to a renderer filter.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



