---
description: Delivering the End of Stream
ms.assetid: 23afdb2e-93b0-4a74-94bd-e38eb82a5995
title: Delivering the End of Stream
ms.topic: article
ms.date: 05/31/2018
---

# Delivering the End of Stream

When the input pin receives an end-of-stream notification, it propagates the call downstream. Any downstream filters that receive data from this input pin should also get the end-of-stream notification. Again, take the streaming lock and not the filter lock. If the filter has pending data that was not yet delivered, the filter should deliver it now, before it sends the end-of-stream notification. It should not send any data after the end of the stream.


```C++
HRESULT CMyInputPin::EndOfStream()
{
    CAutoLock lock_it(&m_csReceive);

    /* If the pin has not delivered all of the data in the stream 
       (based on what it received previously), do so now.  */

    // Propagate EndOfStream call downstream, via your output pin(s).
    for (each output pin)
    {    
        hr = pOutputPin->DeliverEndOfStream();
    }
    return S_OK;
}
```



The [**CBaseOutputPin::DeliverEndOfStream**](cbaseoutputpin-deliverendofstream.md) method calls [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) on the downstream input pin.

## Related topics

<dl> <dt>

[Threads and Critical Sections](threads-and-critical-sections.md)
</dt> </dl>

 

 



