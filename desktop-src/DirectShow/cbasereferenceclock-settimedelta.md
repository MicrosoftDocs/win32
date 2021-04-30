---
description: The SetTimeDelta method adjusts the internal clock time.
ms.assetid: 51534c92-5573-4e2a-baeb-b1a82ccf88de
title: CBaseReferenceClock.SetTimeDelta method (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.SetTimeDelta
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseReferenceClock.SetTimeDelta method

The `SetTimeDelta` method adjusts the internal clock time.

## Syntax


```C++
HRESULT SetTimeDelta(
  [ref] const REFERENCE_TIME &TimeDelta
);
```



## Parameters

<dl> <dt>

*TimeDelta* \[ref\]
</dt> <dd>

Amount to adjust the clock time, in 100-nanosecond units. A positive value moves the clock forward, and a negative value moves the clock backward.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

The derived class can use this method to adjust the internal clock, if it drifts from the device that is providing timing information.

The [**CBaseReferenceClock::GetTime**](cbasereferenceclock-gettime.md) method never returns decreasing values. If you adjust the clock backward, **GetTime** returns the previous value until the clock reaches that value again.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




