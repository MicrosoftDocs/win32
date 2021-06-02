---
description: The GetDefaultTimerResolution method returns the current resolution of the reference clock's timer.
ms.assetid: 14176f9c-7fa1-47f6-a261-9c66e271a3f2
title: CBaseReferenceClock.GetDefaultTimerResolution method (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.GetDefaultTimerResolution
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseReferenceClock.GetDefaultTimerResolution method

The `GetDefaultTimerResolution` method returns the current resolution of the reference clock's timer.

## Syntax


```C++
STDMETHODIMP GetDefaultTimerResolution(
   REFERENCE_TIME *pTimerResolution
);
```



## Parameters

<dl> <dt>

*pTimerResolution* 
</dt> <dd>

Receives the requested timer resolution, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This method implements the [**IReferenceClockTimerControl::GetDefaultTimerResolution**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclocktimercontrol-getdefaulttimerresolution) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




