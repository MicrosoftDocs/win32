---
Description: 'The SetSyncSource method sets a reference clock for the filter. This method implements the IMediaFilter::SetSyncSource method.'
ms.assetid: '298039fc-dd38-4063-8752-2669b134b8ef'
title: 'CBaseFilter.SetSyncSource method'
---

# CBaseFilter.SetSyncSource method

The **SetSyncSource** method sets a reference clock for the filter. This method implements the [**IMediaFilter::SetSyncSource**](imediafilter-setsyncsource.md) method.

## Syntax


```C++
HRESULT SetSyncSource(
   IReferenceClock *pClock
);
```



## Parameters

<dl> <dt>

*pClock* 
</dt> <dd>

Pointer to the clock's [**IReferenceClock**](ireferenceclock.md) interface, or **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




