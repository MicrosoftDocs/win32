---
description: Working with Pin Categories
ms.assetid: 1ee648b3-8370-4e4d-b513-d998131512ee
title: Working with Pin Categories
ms.topic: article
ms.date: 05/31/2018
---

# Working with Pin Categories

To search on a filter the the for a pin with a given pin category, you can use the [**ICaptureGraphBuilder2::FindPin**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findpin) method. The following example searches for a video preview pin:


```C++
int i = 0;
hr = pBuild->FindPin(
    pFilter,               // Pointer to a filter to search.
    PINDIR_OUTPUT,         // Which pin direction?
    &PIN_CATEGORY_PREVIEW, // Which category? (NULL means "any category")
    &MEDIATYPE_Video,      // What media type? (NULL means "any type")
    FALSE,                 // Must be connected?
    i,                     // Get the i'th matching pin (0 = first match)
    &pPin                  // Receives a pointer to the pin.
);
```



The first parameter is a pointer to the filter's [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface. The next three parameters specify the direction, pin category, and media type. The value **FALSE** in the fifth parameter indicates that the pin can be either connected or unconnected. (For the exact definitions of these parameters, refer to the documentation for the method.) If the method finds a matching pin, it returns a pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface in the *pPin* parameter.

Although the [**FindPin**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findpin) method is convenient, you can also write your own helper functions if you prefer. To determine a pin's category, call the [**IKsPropertySet::Get**](ikspropertyset-get.md) method as described in the topic [Pin Property Set](pin-property-set.md).

The following code shows a helper function that checks whether a pin matches a specified category:


```C++
// Returns TRUE if a pin matches the specified pin category.

BOOL PinMatchesCategory(IPin *pPin, REFGUID Category)
{
    BOOL bFound = FALSE;

    IKsPropertySet *pKs = NULL;
    HRESULT hr = pPin->QueryInterface(IID_PPV_ARGS(&pKs));
    if (SUCCEEDED(hr))
    {
        GUID PinCategory;
        DWORD cbReturned;
        hr = pKs->Get(AMPROPSETID_Pin, AMPROPERTY_PIN_CATEGORY, NULL, 0, 
            &PinCategory, sizeof(GUID), &cbReturned);
        if (SUCCEEDED(hr) && (cbReturned == sizeof(GUID)))
        {
            bFound = (PinCategory == Category);
        }
        pKs->Release();
    }
    return bFound;
}
```



The next example is a function that searches for a pin by category, similar to the [**FindPin**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findpin) method:


```C++
// Finds the first pin that matches a specified pin category and direction.

HRESULT FindPinByCategory(
    IBaseFilter *pFilter, // Pointer to the filter to search.
    PIN_DIRECTION PinDir, // Direction of the pin.
    REFGUID Category,     // Pin category.
    IPin **ppPin)         // Receives a pointer to the pin.
{
    *ppPin = 0;

    HRESULT hr = S_OK;
    BOOL bFound = FALSE;

    IEnumPins *pEnum = 0;
    IPin *pPin = 0;

    hr = pFilter->EnumPins(&pEnum);
    if (FAILED(hr))
    {
        goto done;
    }

    while (hr = pEnum->Next(1, &pPin, 0), hr == S_OK)
    {
        PIN_DIRECTION ThisPinDir;
        hr = pPin->QueryDirection(&ThisPinDir);
        if (FAILED(hr))
        {
            goto done;
        }
        if ((ThisPinDir == PinDir) && 
            PinMatchesCategory(pPin, Category))
        {
            *ppPin = pPin;
            (*ppPin)->AddRef();   // The caller must release the interface.
            bFound = TRUE;
            break;
        }
        SafeRelease(&pPin);
    }

done:
    SafeRelease(&pPin);
    SafeRelease(&pEnum);
    if (SUCCEEDED(hr) && !bFound)
    {
        hr = E_FAIL;
    }
    return hr;
}
```



The following code uses the previous function to search for a video port pin on a filter:


```C++
IPin *pVP; 
hr = FindPinByCategory(pFilter, PINDIR_OUTPUT, 
    PIN_CATEGORY_VIDEOPORT, &pVP);
if (SUCCEEDED(hr))
{
    // Use pVP ... 
    // Release when you are done.
    pVP->Release();
}
```



For more information about property sets, refer to the [Windows Driver Kit (WDK)](/windows-hardware/drivers/gettingstarted/) documentation.

## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> <dt>

[Pin Property Set](pin-property-set.md)
</dt> <dt>

[DirectShow Video Capture Filters](directshow-video-capture-filters.md)
</dt> </dl>

 

 
