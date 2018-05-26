---
Description: Enumerating Filters
ms.assetid: 57bcaa4d-37bf-457d-937e-f9d24fb5784f
title: Enumerating Filters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Filters

The Filter Graph Manager supports the [**IFilterGraph::EnumFilters**](/windows/win32/Strmif/nf-strmif-ifiltergraph-enumfilters?branch=master) method, which enumerates all the filters in the filter graph. It returns a pointer to the [**IEnumFilters**](/windows/win32/Strmif/nn-strmif-ienumfilters?branch=master) interface. The [**IEnumFilters::Next**](/windows/win32/Strmif/nf-strmif-ienumfilters-next?branch=master) method retrieves [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master) interface pointers.

The following example shows a function that enumerates the filters in a graph and displays a message box with each filter's name. It uses the [**IBaseFilter::QueryFilterInfo**](/windows/win32/Strmif/nf-strmif-ibasefilter-queryfilterinfo?branch=master) method to retrieve the name of the filter. Note the places where the function calls **Release** on an interface to decrement the reference count.


```C++
HRESULT EnumFilters (IFilterGraph *pGraph) 
{
    IEnumFilters *pEnum = NULL;
    IBaseFilter *pFilter;
    ULONG cFetched;

    HRESULT hr = pGraph->EnumFilters(&amp;pEnum);
    if (FAILED(hr)) return hr;

    while(pEnum->Next(1, &amp;pFilter, &amp;cFetched) == S_OK)
    {
        FILTER_INFO FilterInfo;
        hr = pFilter->QueryFilterInfo(&amp;FilterInfo);
        if (FAILED(hr))
        {
            MessageBox(NULL, TEXT("Could not get the filter info"),
                TEXT("Error"), MB_OK | MB_ICONERROR);
            continue;  // Maybe the next one will work.
        }

#ifdef UNICODE
        MessageBox(NULL, FilterInfo.achName, TEXT("Filter Name"), MB_OK);
#else
        char szName[MAX_FILTER_NAME];
        int cch = WideCharToMultiByte(CP_ACP, 0, FilterInfo.achName,
            MAX_FILTER_NAME, szName, MAX_FILTER_NAME, 0, 0);
        if (cch > 0)
            MessageBox(NULL, szName, TEXT("Filter Name"), MB_OK);
#endif

        // The FILTER_INFO structure holds a pointer to the Filter Graph
        // Manager, with a reference count that must be released.
        if (FilterInfo.pGraph != NULL)
        {
            FilterInfo.pGraph->Release();
        }
        pFilter->Release();
    }

    pEnum->Release();
    return S_OK;
}
```



## Related topics

<dl> <dt>

[Enumerating Objects in a Filter Graph](enumerating-objects-in-a-filter-graph.md)
</dt> </dl>

 

 



