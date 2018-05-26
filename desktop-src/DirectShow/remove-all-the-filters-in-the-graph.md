---
Description: Remove All the Filters in the Graph
ms.assetid: a11af581-c331-4607-be8b-5f65961bd422
title: Remove All the Filters in the Graph
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Remove All the Filters in the Graph

The easiest way to remove all of the filters in a filter graph is simply to release the Filter Graph Manager and create a new one. Make sure to release every pointer that your application has to any interfaces on the Filter Graph Managers, as well as pointers to objects in the graph, including filters, pins, the reference clock, and so forth.

Alternatively, you can remove the filters one at a time, using the [**IFilterGraph::RemoveFilter**](/windows/win32/Strmif/nf-strmif-ifiltergraph-removefilter?branch=master) method:


```C++
// Stop the graph.
pControl->Stop();

// Enumerate the filters in the graph.
IEnumFilters *pEnum = NULL;
HRESULT hr = pGraph->EnumFilters(&amp;pEnum);
if (SUCCEEDED(hr))
{
    IBaseFilter *pFilter = NULL;
    while (S_OK == pEnum->Next(1, &amp;pFilter, NULL))
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



This example uses the [**IFilterGraph::EnumFilters**](/windows/win32/Strmif/nf-strmif-ifiltergraph-enumfilters?branch=master) method to enumerate the filters in the graph. Removing a filter causes the enumerator object to become out of sync with the graph. Use the [**IEnumFilters::Reset**](/windows/win32/Strmif/nf-strmif-ienumfilters-reset?branch=master) method to reset the enumerator. Otherwise, any subsequent call to [**IEnumFilters::Next**](/windows/win32/Strmif/nf-strmif-ienumfilters-next?branch=master) will fail.

 

 



