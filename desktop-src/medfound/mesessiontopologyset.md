---
Description: Raised after the IMFMediaSessionSetTopology method completes asynchronously. The Media Session raises this event after it resolves the topology into a full topology and queues the topology for playback.
ms.assetid: 22a298b7-d32b-44ed-b0a1-4e0398ecfe04
title: MESessionTopologySet event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MESessionTopologySet event

Raised after the [**IMFMediaSession::SetTopology**](/windows/win32/mfidl/nf-mfidl-imfmediasession-settopology?branch=master) method completes asynchronously. The Media Session raises this event after it resolves the topology into a full topology and queues the topology for playback.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](/windows/win32/mfobjects/nf-mfobjects-imfmediaevent-getvalue?branch=master) include the following.



| VARTYPE                | Description                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/>   | No event data.<br/> <br/>                                                                    |
| VT\_UNKNOWN<br/> | Pointer to the [**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master) interface of the full topology.<br/> <br/> |



## Examples

The following example retrieves the [**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master) pointer from an MESessionTopologySet event.


```
HRESULT GetTopologyFromEvent(IMFMediaEvent *pEvent, IMFTopology **ppTopology)
{
    HRESULT hr = S_OK;
    PROPVARIANT var;

    PropVariantInit(&amp;var);
    hr = pEvent->GetValue(&amp;var);
    if (SUCCEEDED(hr))
    {
        if (var.vt != VT_UNKNOWN)
        {
            hr = E_UNEXPECTED;
        }
    }
    if (SUCCEEDED(hr))
    {
        hr = var.punkVal->QueryInterface(__uuidof(IMFTopology), (void**)ppTopology);
    }
    PropVariantClear(&amp;var);
    return hr;
}
```



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Events](media-foundation-events.md)
</dt> </dl>

 

 




