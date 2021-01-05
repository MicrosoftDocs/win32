---
description: This topic describes how to implement a preview pin on a DirectShow capture filter.
ms.assetid: 60306702-97d4-4627-8fbe-e7c8750f3902
title: Implementing a Preview Pin (Optional)
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Preview Pin (Optional)

This topic describes how to implement a preview pin on a DirectShow capture filter.

If your filter has a preview pin, the preview pin must send a copy of the data delivered by the capture pin. Only send data from the preview pin when doing so will not cause the capture pin to drop frames. The capture pin always has priority over the preview pin.

The capture pin and the preview pin must send data with the same format. Therefore, they must connect using identical media types. If the capture pin connects first, the preview pin should offer the same media type, and reject any others types. If the preview pin connects first, and the capture pin connects with a different media type, the preview pin should reconnect using the new media type. If the filter downstream from the preview pin rejects the new type, the capture pin should also reject the type. Use the [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) method to query the filter downstream from the preview pin, and use the [**IFilterGraph::Reconnect**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-reconnect) method to reconnect the pin. These rules also apply if the Filter Graph Manager reconnects the capture pin.

The following example shows an outline of this process:


```C++
// Override CBasePin::CheckMediaType.
CCapturePin::CheckMediaType(CMediaType *pmt)
{
    if (m_pMyPreviewPin->IsConnected()) 
    {
        // The preview pin is already connected, so query the pin it is
        // connected to. If the other pin rejects it, so do we.
        hr = m_pMyPreviewPin->GetConnected()->QueryAccept(pmt);
        if (hr != S_OK) 
        {
            // The preview pin cannot reconnect with this media type.
            return E_INVALIDARG;
        }
        // The preview pin will reconnect when SetMediaType is called.
    }
    // Decide whether the capture pin accepts the format. 
    BOOL fAcceptThisType = ...  // (Not shown.)
    return (fAcceptThisType? S_OK : E_FAIL);
}

// Override CBasePin::SetMediaType.
CCapturePin::SetMediaType(CMediaType *pmt);
{
    if (m_pMyPreviewPin->IsConnected()) 
    {
        // The preview pin is already connected, so it must reconnect.
        if (m_pMyPreviewPin->GetConnected()->QueryAccept(pmt) == S_OK)
        {
            // The downstream pin will accept the new type, so it's safe
            // to reconnect. 
            m_pFilter->m_pGraph->Reconnect(m_pMyPreviewPin);
        }
        else
        {
            return VFW_E_INVALIDMEDIATYPE;
        }
    }
    // Now do anything that the capture pin needs to set the type.
    hr = MyInternalSetMediaType(pmt);

    // And finally, call the base-class method.
    return CBasePin::SetMediaType(pmt);
}

CPreviewPin::CheckMediaType(CMediaType *pmt)
{
    if (m_pMyCapturePin->IsConnected())
    {
       // The preview pin must connect with the same type.
       CMediaType cmt = m_pMyCapturePin->m_mt;
       return (*pmt == cmt ? S_OK : VFW_E_INVALIDMEDIATYPE);
    }
    // Decide whether the preview pin accepts the format. You can use your 
    // knowledge of which types the capture pin will accept. Regardless,
    // when the capture pin connects, the preview pin will reconnect.
    return (fAcceptThisType? S_OK : E_FAIL);
}
```



## Related topics

<dl> <dt>

[How Filters Connect](how-filters-connect.md)
</dt> <dt>

[Writing Capture Filters](writing-capture-filters.md)
</dt> </dl>

 

 



