---
description: Setting the Graph Clock
ms.assetid: 23deab26-6c9a-4f94-b750-11c9b1a14ce3
title: Setting the Graph Clock
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting the Graph Clock

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you build a filter graph, the Filter Graph Manager automatically chooses a reference clock for the graph. All filters in the graph are synchronized to the reference clock. In particular, renderer filters use the reference clock to determine the presentation time of each sample.

There is usually no reason for an application to override the Filter Graph Manager's choice of reference clock. However, you can do so by calling the [**IMediaFilter::SetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-setsyncsource) method on the Filter Graph Manager. This method takes a pointer to the clock's **IReferenceClock** interface. Call the method while the graph is stopped.

If a filter provides a clock, you can get the **IReferenceClock** pointer by calling **QueryInterface** on the filter. Alternatively, you can implement an external reference clock that is not provided by a filter, as long as your external clock implements **IReferenceClock**. The following example shows how to specify a clock:


```C++
IGraphBuilder *pGraph = 0;
IReferenceClock *pClock = 0;

CoCreateInstance(CLSID_FilterGraph, NULL, CLSCTX_INPROC_SERVER, 
    IID_IGraphBuilder, (void **)&pGraph);

// Build the graph.
pGraph->RenderFile(L"C:\\Example.avi", 0);

// Create your clock.
hr = CreateMyPrivateClock(&pClock);
if (SUCCEEDED(hr))
{
    // Set the graph clock.
    IMediaFilter *pMediaFilter = 0;
    pGraph->QueryInterface(IID_IMediaFilter, (void**)&pMediaFilter);
    pMediaFilter->SetSyncSource(pClock);
    pClock->Release();
    pMediaFilter->Release();
}
```



This example assumes that CreateMyPrivateClock is an application-defined function that creates a clock and returns an **IReferenceClock** pointer.

You can also set the filter graph to run with no clock, by calling **SetSyncSource** with the value **NULL**. If there is no clock, the graph runs as quickly as possible. With no clock, renderer filters do not wait for a sample's presentation time. Instead, they render each sample as soon as it arrives. Setting the graph to run without a clock is useful if you want to process data quickly, rather than previewing it in real time.

## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



