---
description: Receiving and Delivering Samples
ms.assetid: 92954b40-1424-4dee-997c-fc41089b7fa5
title: Receiving and Delivering Samples
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Receiving and Delivering Samples

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following pseudocode shows how to implement the **IMemInput::Receive** method:


```C++
HRESULT CMyInputPin::Receive(IMediaSample *pSample)
{
    CAutoLock cObjectLock(&m_csReceive);

    // Perhaps the filter needs to wait on something.
    WaitForSingleObject(m_hSomeEventThatReceiveNeedsToWaitOn, INFINITE);

    // Before using resources, make sure it is safe to proceed. Do not
    // continue if the base-class method returns anything besides S_OK.
    hr = CBaseInputPin::Receive(pSample);
    if (hr != S_OK) 
    {
        return hr;
    }

    /* It is safe to use resources allocated in Active and Pause. */

    // Deliver sample(s), via your output pin(s).
    for (each output pin)
        pOutputPin->Deliver(pSample);

    return hr;
}
```



The **Receive** method holds the streaming lock, not the filter lock. The filter might need to wait on some event before it can process the data, shown here by the call to **WaitForSingleObject**. Not every filter will need to do this. The [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method verifies some general streaming conditions. It returns VFW\_E\_WRONG\_STATE if the filter is stopped, S\_FALSE if the filter is flushing, and so forth. Any return code other than S\_OK indicates that the **Receive** method should return immediately and not process the sample.

After the sample is processed, deliver it to the downstream filter by calling [**CBaseOutputPin::Deliver**](cbaseoutputpin-deliver.md). This helper method calls **IMemInputPin::Receive** on the downstream input pin. A filter might deliver samples to several pins.

 

 



