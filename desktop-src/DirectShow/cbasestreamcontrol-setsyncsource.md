---
Description: The SetSyncSource method notifies the base class of the current reference clock.
ms.assetid: 056385ac-682c-456e-9a5f-86490bd6e05f
title: CBaseStreamControl.SetSyncSource method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseStreamControl.SetSyncSource method

The `SetSyncSource` method notifies the base class of the current reference clock.

## Syntax


```C++
void SetSyncSource(
   IReferenceClock *pRefClock
);
```



## Parameters

<dl> <dt>

*pRefClock* 
</dt> <dd>

Pointer to the [**IReferenceClock**](/windows/win32/Strmif/nn-strmif-ireferenceclock?branch=master) interface of the reference clock.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Call this method from inside the filter's [**IMediaFilter::SetSyncSource**](/windows/win32/Strmif/nf-strmif-imediafilter-setsyncsource?branch=master) method. The **CBaseStreamControl** class uses the **IReferenceClock** interface to ensure that it does not discard samples too quickly.

## Examples


```C++
STDMETHODIMP CMyFilter::SetSyncSource(IReferenceClock *pClock)
{
    // Note: It's OK if pClock is NULL.

    m_pMyPin->SetSyncSource(pClock);
    return CBaseFilter::SetSyncSource(pClock);
}
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




