---
description: The ChangeRate method is called when the playback rate changes.
ms.assetid: c4f1f9d0-6c09-4cab-8a37-dd1ff3f5619f
title: CSourceSeeking.ChangeRate method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.ChangeRate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.ChangeRate method

The `ChangeRate` method is called when the playback rate changes.

## Syntax


```C++
virtual HRESULT ChangeRate() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

The [**CSourceSeeking::SetRate**](csourceseeking-setrate.md) method calls this method, which the derived class must implement. The **SetRate** method updates the [**CSourceSeeking::m\_dRateSeeking**](csourceseeking-m-drateseeking.md) member variable, but does not validate the new value. A rate of zero should always be rejected. Rates less than zero indicate negative playback. Most filters do not support negative rates.

The following example shows a possible implementation:


```C++
HRESULT CMyStream::ChangeRate( )
{
    {   // Scope for critical section lock.
        CAutoLock cAutoLockSeeking(CSourceSeeking::m_pLock);
        if( m_dRateSeeking <= 0 ) {
            m_dRateSeeking = 1.0;  // Reset to a reasonable value.
            return E_FAIL;
        }
    }
    UpdateFromSeek();
    return S_OK;
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




