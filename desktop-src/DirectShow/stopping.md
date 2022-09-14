---
description: Stopping
ms.assetid: e2796b69-05e5-4ced-b238-257952d81211
title: Stopping
ms.topic: article
ms.date: 05/31/2018
---

# Stopping

The **Stop** method must unblock the **Receive** method and decommit the filter's allocators. Decommitting an allocator forces any pending **GetBuffer** calls to return, which unblocks upstream filters that are waiting for samples. The **Stop** method holds the filter lock and then calls the [**CBaseFilter::Stop**](cbasefilter-stop.md) method, which calls [**CBasePin::Inactive**](cbasepin-inactive.md) on all of the filter's pins:


```C++
HRESULT CMyFilter::Stop()
{
    CAutoLock lock_it(m_pLock);
    // Inactivate all the pins, to protect the filter resources.
    hr = CBaseFilter::Stop();

    /* Safe to destroy filter resources used by the streaming thread. */

    return hr;
}
```



Override the input pin's **Inactive** method as follows:


```C++
HRESULT CMyInputPin::Inactive()
{
    // You do not need to hold the filter lock here. 
    // It is already locked in Stop.

    // Unblock Receive.
    SetEvent(m_hSomeEventThatReceiveNeedsToWaitOn);

    // Make sure Receive will fail. 
    // This also decommits the allocator.
    HRESULT hr = CBaseInputPin::Inactive();

    // Make sure Receive has completed, and is not using resources.
    {
        CAutoLock c(&m_csReceive);

        /* It is now safe to destroy filter resources used by the
           streaming thread. */
    }
    return hr;
}
```



 

 



