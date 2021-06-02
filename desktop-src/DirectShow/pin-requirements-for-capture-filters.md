---
description: This topic describes the requirements for implementing an output pin on a DirectShow capture filter.
ms.assetid: cb9cda1c-efa2-4abb-934b-21ba8cb80f30
title: Pin Requirements for Capture Filters
ms.topic: article
ms.date: 05/31/2018
---

# Pin Requirements for Capture Filters

This topic describes the requirements for implementing an output pin on a DirectShow capture filter.

## Pin Name

You can give a pin any name. If the pin name begins with the tilde (~) character, the Filter Graph Manager does not automatically render that pin when an application calls [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile). For example, if the filter has a capture pin and a preview pin, you might name them "~Capture" and "Preview," respectively. If an application renders that filter in a graph, the preview pin will connect to its default renderer, and nothing will connect to the capture pin, which is a reasonable default behavior. This can also apply to pins that deliver informational data that is not meant to be rendered, or pins that need custom properties set. Note that pins with the tilde (~) prefix can still be connected manually by the application.

## Pin Category

A capture filter always has a capture pin, and might have a preview pin. Some capture filters might have other output pins, to deliver other types of data, such as control information. Each output pin must expose the [**IKsPropertySet**](ikspropertyset.md) interface. Applications use this interface to determine the pin category. The pin typically returns either PIN\_CATEGORY\_CAPTURE or PIN\_CATEGORY\_PREVIEW. For more information, see [Pin Property Set](pin-property-set.md).

The following example shows how to implement [**IKsPropertySet**](ikspropertyset.md) to return the pin category on a capture pin:


```C++
// Set: Cannot set any properties.
HRESULT CMyCapturePin::Set(REFGUID guidPropSet, DWORD dwID,
    void *pInstanceData, DWORD cbInstanceData, void *pPropData, 
    DWORD cbPropData)
{
    return E_NOTIMPL;
}

// Get: Return the pin category (our only property). 
HRESULT CMyCapturePin::Get(
    REFGUID guidPropSet,   // Which property set.
    DWORD dwPropID,        // Which property in that set.
    void *pInstanceData,   // Instance data (ignore).
    DWORD cbInstanceData,  // Size of the instance data (ignore).
    void *pPropData,       // Buffer to receive the property data.
    DWORD cbPropData,      // Size of the buffer.
    DWORD *pcbReturned     // Return the size of the property.
)
{
    if (guidPropSet != AMPROPSETID_Pin) 
        return E_PROP_SET_UNSUPPORTED;
    if (dwPropID != AMPROPERTY_PIN_CATEGORY)
        return E_PROP_ID_UNSUPPORTED;
    if (pPropData == NULL && pcbReturned == NULL)
        return E_POINTER;
    if (pcbReturned)
        *pcbReturned = sizeof(GUID);
    if (pPropData == NULL)  // Caller just wants to know the size.
        return S_OK;
    if (cbPropData < sizeof(GUID)) // The buffer is too small.
        return E_UNEXPECTED;
    *(GUID *)pPropData = PIN_CATEGORY_CAPTURE;
    return S_OK;
}

// QuerySupported: Query whether the pin supports the specified property.
HRESULT CMyCapturePin::QuerySupported(REFGUID guidPropSet, DWORD dwPropID,
    DWORD *pTypeSupport)
{
    if (guidPropSet != AMPROPSETID_Pin)
        return E_PROP_SET_UNSUPPORTED;
    if (dwPropID != AMPROPERTY_PIN_CATEGORY)
        return E_PROP_ID_UNSUPPORTED;
    if (pTypeSupport)
        // We support getting this property, but not setting it.
        *pTypeSupport = KSPROPERTY_SUPPORT_GET; 
    return S_OK;
}
```



## Related topics

<dl> <dt>

[Writing Capture Filters](writing-capture-filters.md)
</dt> </dl>

 

 



