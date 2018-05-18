---
Description: 'The GetSyncSource method retrieves the reference clock that the object is using. This method implements the IMediaFilter::GetSyncSource method.'
ms.assetid: '7e74d6ce-cd34-4345-8ff9-174e0acb243a'
title: 'CBaseMediaFilter.GetSyncSource method'
---

# CBaseMediaFilter.GetSyncSource method

The `GetSyncSource` method retrieves the reference clock that the object is using. This method implements the [**IMediaFilter::GetSyncSource**](imediafilter-getsyncsource.md) method.

## Syntax


```C++
HRESULT GetSyncSource(
   IReferenceClock **pClock
);
```



## Parameters

<dl> <dt>

*pClock* 
</dt> <dd>

Address of a variable that receives a pointer to the clock's [**IReferenceClock**](ireferenceclock.md) interface.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Remarks

If the object is not using a reference clock, *\*pClock* is set to **NULL**. When the method returns, if *\*pClock* is non-**NULL**, the **IReferenceClock** interface has an outstanding reference count. Be sure to release it when you are done.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




