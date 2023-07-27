---
description: Remove All the Filters in the Graph
ms.assetid: a11af581-c331-4607-be8b-5f65961bd422
title: Remove All the Filters in the Graph
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Remove All the Filters in the Graph

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The easiest way to remove all of the filters in a filter graph is simply to release the Filter Graph Manager and create a new one. Make sure to release every pointer that your application has to any interfaces on the Filter Graph Managers, as well as pointers to objects in the graph, including filters, pins, the reference clock, and so forth.

Alternatively, you can remove the filters one at a time, using the [**IFilterGraph::RemoveFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-removefilter) method:


```C++
// Stop the graph.
pControl->Stop();

// Enumerate the filters in the graph.
IEnumFilters *pEnum = NULL;
HRESULT hr = pGraph->EnumFilters(&pEnum);
if (SUCCEEDED(hr))
{
    IBaseFilter *pFilter = NULL;
    while (S_OK == pEnum->Next(1, &pFilter, NULL))
     {
         // Remove the filter.
         pGraph->RemoveFilter(pFilter);
         // Reset the enumerator.
         pEnum->Reset();
         pFilter->Release();
    }
    pEnum->Release();
}
```



This example uses the [**IFilterGraph::EnumFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-enumfilters) method to enumerate the filters in the graph. Removing a filter causes the enumerator object to become out of sync with the graph. Use the [**IEnumFilters::Reset**](/windows/desktop/api/Strmif/nf-strmif-ienumfilters-reset) method to reset the enumerator. Otherwise, any subsequent call to [**IEnumFilters::Next**](/windows/desktop/api/Strmif/nf-strmif-ienumfilters-next) will fail.

 

 



