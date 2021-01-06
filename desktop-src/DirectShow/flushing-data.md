---
description: Flushing Data
ms.assetid: 528763a2-c0f2-4981-91dc-dd17987f5bd5
title: Flushing Data
ms.topic: article
ms.date: 05/31/2018
---

# Flushing Data

The following pseudocode shows how to implement the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method:


```C++
HRESULT CMyInputPin::BeginFlush()
{
    CAutoLock lock_it(m_pLock);
   
    // First, make sure the Receive method will fail from now on.
    HRESULT hr = CBaseInputPin::BeginFlush();
    
    // Force downstream filters to release samples. If our Receive method
    // is blocked in GetBuffer or Deliver, this will unblock it.
    for (each output pin)
    {
        hr = pOutputPin->DeliverBeginFlush();
    }

    // Unblock our Receive method if it is waiting on an event.
    SetEvent(m_hSomeEventThatReceiveNeedsToWaitOn);

    // At this point, the Receive method can't be blocked. Make sure 
    // it finishes, by taking the streaming lock. (Not necessary if this 
    // is the last step.)
    { 
        CAutoLock lock_2(&m_csReceive);

        /* Now it's safe to do anything that would crash or hang 
           if Receive were executing. */
    }
    return hr;
}
```



When flushing starts, the **BeginFlush** method takes the filter lock, which serializes the state change. It is not yet safe to take the streaming lock, because flushing happens on the application thread, and the streaming thread might be in the middle of a **Receive** call. The pin needs to guarantee that **Receive** is not blocked, and that any subsequent calls to **Receive** will fail. The [**CBaseInputPin::BeginFlush**](cbaseinputpin-beginflush.md) method sets an internal flag, [**CBaseInputPin::m\_bFlushing**](cbaseinputpin-m-bflushing.md). When the flag is **TRUE**, the **Receive** method fails.

By delivering the **BeginFlush** call downstream, the pin guarantees that all downstream filters release their samples and return from **Receive** calls. This in turn guarantees that the input pin is not blocked waiting for **GetBuffer** or **Receive**. If your pin's **Receive** method ever waits on an event (for example, to get resources), the **BeginFlush** method should force the wait to terminate by setting the event. At this point, the **Receive** method is guaranteed to return, and the **m\_bFlushing** flag prevents new **Receive** calls from doing any work.

For some filters, that is all **BeginFlush** needs to do. The **EndFlush** method will signal to the filter that it can start receiving samples again. Other filters may need to use variables or resources in **BeginFlush** that are also used in **Receive**. In that case, the filter should hold the streaming lock first. Be sure not to do this before any of the previous steps, because you might cause a deadlock.

The **EndFlush** method holds the filter lock and propagates the call downstream:


```C++
HRESULT CMyInputPin::EndFlush()
{
    CAutoLock lock_it(m_pLock);
    for (each output pin)
        hr = pOutputPin->DeliverEndFlush();
    return CBaseInputPin::EndFlush();
}
```



The [**CBaseInputPin::EndFlush**](cbaseinputpin-endflush.md) method resets the **m\_bFlushing** flag to **FALSE**, which allows the **Receive** method to start receiving samples again. This should be the last step in **EndFlush**, because the pin must not receive any samples until flushing is complete and all downstream filters are notified.

## Related topics

<dl> <dt>

[Threads and Critical Sections](threads-and-critical-sections.md)
</dt> </dl>

 

 



