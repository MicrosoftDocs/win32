---
Description: The GetSchedule method retrieves a pointer to the clocks scheduling object.
ms.assetid: ae509f16-d85f-4365-8cf2-c6585cbbdc3d
title: CBaseReferenceClock.GetSchedule method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseReferenceClock.GetSchedule method

The `GetSchedule` method retrieves a pointer to the clock's scheduling object.

## Syntax


```C++
CAMSchedule* GetSchedule();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseReferenceClock::m\_pSchedule**](cbasereferenceclock-m-pschedule.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




