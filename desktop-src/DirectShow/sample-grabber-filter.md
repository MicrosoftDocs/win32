---
description: The Sample Grabber filter provides a way to retrieve samples as they pass through the filter graph.
ms.assetid: 3c2fb52f-2b44-449a-ae96-3cf35a0a401d
title: Sample Grabber Filter (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Sample
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# Sample Grabber Filter

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Sample Grabber filter provides a way to retrieve samples as they pass through the filter graph. It is a transform filter with one input pin and one output pin. It passes all samples downstream unchanged, so you can insert it into a filter graph without altering the data stream. Your application can then retrieve individual samples from the filter by calling methods on the [**ISampleGrabber**](isamplegrabber.md) interface.

If you want to retrieve samples without rendering the data, connect the Sample Grabber filter to the [**Null Renderer**](null-renderer-filter.md) filter.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**ISampleGrabber**](isamplegrabber.md)                                                                       |
| Input pin media types                    | Any media type.                                                                                                                                    |
| Input pin interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                             |
| Output pin media types                   | Any media type. Matches input media type.                                                                                                          |
| Output pin interfaces                    | [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) |
| Filter CLSID                             | CLSID\_SampleGrabber                                                                                                                               |
| Property Page CLSID                      | No property page.                                                                                                                                  |
| Executable                               | Qedit.dll                                                                                                                                          |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                      |



 

## Remarks

To use this filter, add it to the filter graph and call [**ISampleGrabber::SetMediaType**](isamplegrabber-setmediatype.md) with the desired media type. This method specifies the media type for the filter's input and output pin connections. Then connect the filter to other filters in the graph.

If you call [**ISampleGrabber::SetBufferSamples**](isamplegrabber-setbuffersamples.md) with the value **TRUE**, the filter buffers each sample that it receives before passing it downstream. Call the [**ISampleGrabber::GetCurrentBuffer**](isamplegrabber-getcurrentbuffer.md) method to retrieve the current contents of the buffer. Alternatively, you can call [**ISampleGrabber::SetCallback**](isamplegrabber-setcallback.md) to have the filter invoke a callback function whenever it receives a sample.

The filter has the following limitations for video formats:

-   It does not support video types with top-down orientation (negative **biHeight**).
-   It does not support the [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) format structure (format type equal to **FORMAT\_VideoInfo2**).
-   It rejects any video type where the surface stride does not match the video width.

As a result, the Sample Grabber will not connect to the Video Mixing Renderer (VMR) for some video types.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Editing Services Objects](directshow-editing-services-objects.md)
</dt> <dt>

[Using the Sample Grabber](using-the-sample-grabber.md)
</dt> </dl>

 

 




