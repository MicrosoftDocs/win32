---
description: The GetSchedule method retrieves a pointer to the clock's scheduling object.
ms.assetid: ae509f16-d85f-4365-8cf2-c6585cbbdc3d
title: CBaseReferenceClock.GetSchedule method (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.GetSchedule
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




