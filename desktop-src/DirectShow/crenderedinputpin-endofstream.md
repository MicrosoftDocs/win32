---
description: The EndOfStream method notifies the pin that no additional data is expected, until a new run command is issued to the filter. This method implements the IPin::EndOfStream method.
ms.assetid: 915beab4-2fc3-4acd-bb30-c0851df058db
title: CRenderedInputPin.EndOfStream method (Amextra.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRenderedInputPin.EndOfStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRenderedInputPin.EndOfStream method

The `EndOfStream` method notifies the pin that no additional data is expected, until a new run command is issued to the filter. This method implements the [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) method.

## Syntax


```C++
HRESULT EndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an error code otherwise.

## Remarks

If the filter is running, this method sends an [**EC\_COMPLETE**](ec-complete.md) event to the Filter Graph Manager. Otherwise, is sets a flag so that the EC\_COMPLETE event is sent when the filter next runs. Flushing the filter clears the flag.

You should override this method to hold the pin's streaming lock:


```C++
class CMyInputPin : public CRenderedInputPin
{
private:
    CCritSec * const m_pReceiveLock; // Streaming lock.
public:
    STDMETHODIMP EndOfStream(void);

    /* (Remainder of the class declaration not shown.) */
};

STDMETHODIMP CMyInputPin::EndOfStream(void)
{
    CAutoLock lock(m_pReceiveLock);  
    return CRenderedInputPin::EndOfStream();
} 
```



Also, if the filter processes **Receive** calls asynchronously, the pin should wait to send the EC\_COMPLETE event until the filter has processed all pending samples.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amextra.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRenderedInputPin Class**](crenderedinputpin.md)
</dt> </dl>

 

 




