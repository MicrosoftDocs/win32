---
Description: 'Raised after the IMFMediaSession::SetTopology method completes asynchronously. The Media Session raises this event after it resolves the topology into a full topology and queues the topology for playback.'
ms.assetid: '22a298b7-d32b-44ed-b0a1-4e0398ecfe04'
title: MESessionTopologySet event
---

# MESessionTopologySet event

Raised after the [**IMFMediaSession::SetTopology**](imfmediasession-settopology.md) method completes asynchronously. The Media Session raises this event after it resolves the topology into a full topology and queues the topology for playback.

## Event values

Possible values retrieved from [**IMFMediaEvent::GetValue**](imfmediaevent-getvalue.md) include the following.



| VARTYPE                | Description                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------------------|
| VT\_EMPTY<br/>   | No event data.<br/> <br/>                                                                    |
| VT\_UNKNOWN<br/> | Pointer to the [**IMFTopology**](imftopology.md) interface of the full topology.<br/> <br/> |



## Examples

The following example retrieves the [**IMFTopology**](imftopology.md) pointer from an MESessionTopologySet event.


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

 

 




