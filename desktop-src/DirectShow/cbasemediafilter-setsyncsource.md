---
Description: 'The SetSyncSource method sets a reference clock for the object. This method implements the IMediaFilter::SetSyncSource method.'
ms.assetid: 'ae296741-e3da-4376-a88a-8470f0a414ed'
title: 'CBaseMediaFilter.SetSyncSource method'
---

# CBaseMediaFilter.SetSyncSource method

The `SetSyncSource` method sets a reference clock for the object. This method implements the [**IMediaFilter::SetSyncSource**](imediafilter-setsyncsource.md) method.

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

Returns S\_OK.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




