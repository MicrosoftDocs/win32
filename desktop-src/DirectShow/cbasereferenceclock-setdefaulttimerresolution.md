---
Description: The SetDefaultTimerResolution method sets the resolution of the reference clocks timer.
ms.assetid: 891b809a-15d3-41f3-853e-aca9ddcd56e8
title: CBaseReferenceClock.SetDefaultTimerResolution method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseReferenceClock.SetDefaultTimerResolution method

The `SetDefaultTimerResolution` method sets the resolution of the reference clock's timer.

## Syntax


```C++
STDMETHODIMP SetDefaultTimerResolution(
   REFERENCE_TIME timerResolution
);
```



## Parameters

<dl> <dt>

*timerResolution* 
</dt> <dd>

Minimum timer resolution, in 100-nanosecond units. If the value is zero, the reference clock cancels its previous request.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This method implements the [**IReferenceClockTimerControl::SetDefaultTimerResolution**](/windows/win32/Strmif/nf-strmif-ireferenceclocktimercontrol-setdefaulttimerresolution?branch=master) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




