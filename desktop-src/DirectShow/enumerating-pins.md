---
Description: Enumerating Pins
ms.assetid: '231f10c1-46b4-4b66-b0ce-06a191237dfb'
title: Enumerating Pins
---

# Enumerating Pins

Filters support the [**IBaseFilter::EnumPins**](ibasefilter-enumpins.md) method, which enumerates the pins available on the filter. It returns a pointer to the [**IEnumPins**](ienumpins.md) interface. The [**IEnumPins::Next**](ienumpins-next.md) method retrieves [**IPin**](ipin.md) interface pointers.

The following example shows a function that locates a pin with a given direction (input or output) on a given filter. It uses the [**PIN\_DIRECTION**](pin-direction.md) enumeration to specify the pin direction, and the [**IPin::QueryDirection**](ipin-querydirection.md) method to find the direction of each enumerated pin. If this function finds a matching pin, it returns an **IPin** interface pointer with an outstanding reference count. The caller is responsible for releasing the interface.


```C++
HRESULT GetPin(IBaseFilter *pFilter, PIN_DIRECTION PinDir, IPin **ppPin)
{
    IEnumPins  *pEnum = NULL;
    IPin       *pPin = NULL;
    HRESULT    hr;

    if (ppPin == NULL)
    {
        return E_POINTER;
    }

    hr = pFilter->EnumPins(&amp;pEnum);
    if (FAILED(hr))
    {
        return hr;
    }
    while(pEnum->Next(1, &amp;pPin, 0) == S_OK)
    {
        PIN_DIRECTION PinDirThis;
        hr = pPin->QueryDirection(&amp;PinDirThis);
        if (FAILED(hr))
        {
            pPin->Release();
            pEnum->Release();
            return hr;
        }
        if (PinDir == PinDirThis)
        {
            // Found a match. Return the IPin pointer to the caller.
            *ppPin = pPin;
            pEnum->Release();
            return S_OK;
        }
        // Release the pin for the next time through the loop.
        pPin->Release();
    }
    // No more pins. We did not find a match.
    pEnum->Release();
    return E_FAIL;  
}
```



This function could easily be modified to return the nth pin with the specified direction, or the *n*th unconnected pin. (To find out if a pin is connected to another pin, call the [**IPin::ConnectedTo**](ipin-connectedto.md) method.)

## Related topics

<dl> <dt>

[Enumerating Objects in a Filter Graph](enumerating-objects-in-a-filter-graph.md)
</dt> <dt>

[Find an Unconnected Pin on a Filter](find-an-unconnected-pin-on-a-filter.md)
</dt> <dt>

[General Graph-Building Techniques](general-graph-building-techniques.md)
</dt> <dt>

[Pin Property Set](pin-property-set.md)
</dt> </dl>

 

 



