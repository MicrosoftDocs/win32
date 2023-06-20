---
description: Find a Filters Peer
ms.assetid: 74d9fe65-f7f4-4971-9550-27884ac4146b
title: Find a Filters Peer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Find a Filters Peer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Given a filter, you can traverse the graph by finding the filters to which it is connected. Start by enumerating the filter's pins. For each pin, check whether that pin is connected to another pin. If so, query the other pin for it's owning filter. You can walk the graph in the upstream direction by enumerating the filter's input pins, or in the downstream direction by enumerating the output pins.

The following function searches upstream or downstream for a connected filter. It returns the first matching filter that it finds:


```C++
// Get the first upstream or downstream filter
HRESULT GetNextFilter(
    IBaseFilter *pFilter, // Pointer to the starting filter
    PIN_DIRECTION Dir,    // Direction to search (upstream or downstream)
    IBaseFilter **ppNext) // Receives a pointer to the next filter.
{
    if (!pFilter || !ppNext) return E_POINTER;

    IEnumPins *pEnum = 0;
    IPin *pPin = 0;
    HRESULT hr = pFilter->EnumPins(&pEnum);
    if (FAILED(hr)) return hr;
    while (S_OK == pEnum->Next(1, &pPin, 0))
    {
        // See if this pin matches the specified direction.
        PIN_DIRECTION ThisPinDir;
        hr = pPin->QueryDirection(&ThisPinDir);
        if (FAILED(hr))
        {
            // Something strange happened.
            hr = E_UNEXPECTED;
            pPin->Release();
            break;
        }
        if (ThisPinDir == Dir)
        {
            // Check if the pin is connected to another pin.
            IPin *pPinNext = 0;
            hr = pPin->ConnectedTo(&pPinNext);
            if (SUCCEEDED(hr))
            {
                // Get the filter that owns that pin.
                PIN_INFO PinInfo;
                hr = pPinNext->QueryPinInfo(&PinInfo);
                pPinNext->Release();
                pPin->Release();
                pEnum->Release();
                if (FAILED(hr) || (PinInfo.pFilter == NULL))
                {
                    // Something strange happened.
                    return E_UNEXPECTED;
                }
                // This is the filter we're looking for.
                *ppNext = PinInfo.pFilter; // Client must release.
                return S_OK;
            }
        }
        pPin->Release();
    }
    pEnum->Release();
    // Did not find a matching filter.
    return E_FAIL;
}
```



The function calls [**IBaseFilter::EnumPins**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-enumpins) to enumerate the first filter's pins. For each pin, it calls [**IPin::QueryDirection**](/windows/desktop/api/Strmif/nf-strmif-ipin-querydirection) to check whether the pin matches the specified direction (input or output). If so, the function determines whether that pin is connected to another pin, by calling the [**IPin::ConnectedTo**](/windows/desktop/api/Strmif/nf-strmif-ipin-connectedto) method. Finally, it calls [**IPin::QueryPinInfo**](/windows/desktop/api/Strmif/nf-strmif-ipin-querypininfo) on the connected pin. This method returns a structure that contains, among other things, a pointer to that pin's owning filter. This pointer is returned to the caller in the *ppNext* parameter. The caller must release the pointer.

The following code shows how to call this function:


```C++
IBaseFilter *pF; // Pointer to some filter.
IBaseFilter *pUpstream = NULL;
if (SUCCEEDED(GetNextFilter(pF, PINDIR_INPUT, &pUpstream)))
{
    // Use pUpstream ...
    pUpstream->Release();
}
```



A filter might be connected to two or more filters in either direction. For example, it might be a splitter filter, with several filters downstream from it. Or it might be a mux filter, with several filters upstream from it. Therefore, you might want to collect all of them into a list.

The following code shows one possible way to implement such a function. It uses the DirectShow [**CGenericList**](cgenericlist.md) class; you could write an equivalent function using some other data structure.


```C++
#include <streams.h>  // Link to the DirectShow base class library
// Define a typedef for a list of filters.
typedef CGenericList<IBaseFilter> CFilterList;

// Forward declaration. Adds a filter to the list unless it's a duplicate.
void AddFilterUnique(CFilterList &FilterList, IBaseFilter *pNew);

// Find all the immediate upstream or downstream peers of a filter.
HRESULT GetPeerFilters(
    IBaseFilter *pFilter, // Pointer to the starting filter
    PIN_DIRECTION Dir,    // Direction to search (upstream or downstream)
    CFilterList &FilterList)  // Collect the results in this list.
{
    if (!pFilter) return E_POINTER;

    IEnumPins *pEnum = 0;
    IPin *pPin = 0;
    HRESULT hr = pFilter->EnumPins(&pEnum);
    if (FAILED(hr)) return hr;
    while (S_OK == pEnum->Next(1, &pPin, 0))
    {
        // See if this pin matches the specified direction.
        PIN_DIRECTION ThisPinDir;
        hr = pPin->QueryDirection(&ThisPinDir);
        if (FAILED(hr))
        {
            // Something strange happened.
            hr = E_UNEXPECTED;
            pPin->Release();
            break;
        }
        if (ThisPinDir == Dir)
        {
            // Check if the pin is connected to another pin.
            IPin *pPinNext = 0;
            hr = pPin->ConnectedTo(&pPinNext);
            if (SUCCEEDED(hr))
            {
                // Get the filter that owns that pin.
                PIN_INFO PinInfo;
                hr = pPinNext->QueryPinInfo(&PinInfo);
                pPinNext->Release();
                if (FAILED(hr) || (PinInfo.pFilter == NULL))
                {
                    // Something strange happened.
                    pPin->Release();
                    pEnum->Release();
                    return E_UNEXPECTED;
                }
                // Insert the filter into the list.
                AddFilterUnique(FilterList, PinInfo.pFilter);
                PinInfo.pFilter->Release();
            }
        }
        pPin->Release();
    }
    pEnum->Release();
    return S_OK;
}
void AddFilterUnique(CFilterList &FilterList, IBaseFilter *pNew)
{
    if (pNew == NULL) return;

    POSITION pos = FilterList.GetHeadPosition();
    while (pos)
    {
        IBaseFilter *pF = FilterList.GetNext(pos);
        if (IsEqualObject(pF, pNew))
        {
            return;
        }
    }
    pNew->AddRef();  // The caller must release everything in the list.
    FilterList.AddTail(pNew);
}
```



To complicate matters somewhat, a filter can have multiple pin connections to the same filter. To avoid putting duplicates into the list, query each **IBaseFilter** pointer for **IUnknown** and compare the **IUnknown** pointers. By the rules of COM, two interface pointers refer to the same object if and only if they return identical **IUnknown** pointers. In the previous example, the AddFilterUnique function handles this detail.

The following example shows how to use the GetPeerFilters function:


```C++
IBaseFilter *pF; // Pointer to some filter.
CFilterList FList(NAME("MyList"));  // List to hold the downstream peers.
hr = GetPeerFilters(pF, PINDIR_OUTPUT, FList);
if (SUCCEEDED(hr))
{
    POSITION pos = FList.GetHeadPosition();
    while (pos)
    {
        IBaseFilter *pDownstream = FList.GetNext(pos);
        pDownstream->Release();
    }
}
```



## Related topics

<dl> <dt>

[General Graph-Building Techniques](general-graph-building-techniques.md)
</dt> </dl>

 

 



