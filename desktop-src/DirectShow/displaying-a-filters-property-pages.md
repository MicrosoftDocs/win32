---
description: Displaying a Filter's Property Pages
ms.assetid: 4a5f6938-7b33-4350-b8fa-cf78c5c44bcd
title: Displaying a Filter's Property Pages
ms.topic: article
ms.date: 05/31/2018
---

# Displaying a Filter's Property Pages

A property page is one way for a filter to support properties that the user can set. This article describes how to display a filter's property pages in an application. For more information about property pages, see the Platform SDK documentation.

> [!Note]  
> Although many of the filters provided with DirectShow support property pages, they are intended for debugging purposes, and are not recommended for application use. In most cases the equivalent functionality is provided through a custom interface on the filter. An application should control these filters programmatically, rather than expose their property pages to users.

 

Filters with property pages expose the **ISpecifyPropertyPages** interface. To determine whether a filter defines a property page, query the filter for this interface using **QueryInterface**.

If you directly created an instance of a filter (by calling **CoCreateInstance**), you already have a pointer to the filter. If not, you can enumerate the filters in the graph, using the [**IFilterGraph::EnumFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-enumfilters) method. For details, see [Enumerating Objects in a Filter Graph](enumerating-objects-in-a-filter-graph.md).

Once you have the **ISpecifyPropertyPages** interface pointer, retrieve the filter's property pages by calling the **ISpecifyPropertyPages::GetPages** method. This method fills a counted array of globally unique identifiers (GUIDs) with the class identifier (CLSID) of each property page. A counted array is defined by a **CAUUID** structure, which you must allocate but do not have to initialize. The **GetPages** method allocates the array, which is contained in the **pElems** member of the **CAUUID** structure. When you are done, free the array by calling the **CoTaskMemFree** function.

The **OleCreatePropertyFrame** function provides a simple way to display the property pages inside a modal dialog box.


```C++
IBaseFilter *pFilter;
/* Obtain the filter's IBaseFilter interface. (Not shown) */
ISpecifyPropertyPages *pProp;
HRESULT hr = pFilter->QueryInterface(IID_ISpecifyPropertyPages, (void **)&pProp);
if (SUCCEEDED(hr)) 
{
    // Get the filter's name and IUnknown pointer.
    FILTER_INFO FilterInfo;
    hr = pFilter->QueryFilterInfo(&FilterInfo); 
    IUnknown *pFilterUnk;
    pFilter->QueryInterface(IID_IUnknown, (void **)&pFilterUnk);

    // Show the page. 
    CAUUID caGUID;
    pProp->GetPages(&caGUID);
    pProp->Release();
    OleCreatePropertyFrame(
        hWnd,                   // Parent window
        0, 0,                   // Reserved
        FilterInfo.achName,     // Caption for the dialog box
        1,                      // Number of objects (just the filter)
        &pFilterUnk,            // Array of object pointers. 
        caGUID.cElems,          // Number of property pages
        caGUID.pElems,          // Array of property page CLSIDs
        0,                      // Locale identifier
        0, NULL                 // Reserved
    );

    // Clean up.
    pFilterUnk->Release();
    FilterInfo.pGraph->Release(); 
    CoTaskMemFree(caGUID.pElems);
}
```



## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> </dl>

 

 



