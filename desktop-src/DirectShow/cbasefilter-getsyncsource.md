---
description: The GetSyncSource method retrieves the reference clock that the filter is using. This method implements the IMediaFilter::GetSyncSource method.
ms.assetid: b8c95838-bd6e-41c5-b3ab-71ebb33136f0
title: CBaseFilter.GetSyncSource method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.GetSyncSource
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.GetSyncSource method

The `GetSyncSource` method retrieves the reference clock that the filter is using. This method implements the [**IMediaFilter::GetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-getsyncsource) method.

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

Address of a variable that receives a pointer to the clock's [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock) interface.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Remarks

If the filter is not using a reference clock, *\*pClock* is set to **NULL**. When the method returns, if *\*pClock* is non-**NULL**, the **IReferenceClock** interface has an outstanding reference count. Be sure to release it when you are done.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




