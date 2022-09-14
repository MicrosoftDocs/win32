---
description: The GetNextAdviseTime method retrieves the time of the next advise request.
ms.assetid: 2a376250-fb39-46d7-a5a8-e3a3143cd209
title: CAMSchedule.GetNextAdviseTime method (Dsschedule.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule.GetNextAdviseTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMSchedule.GetNextAdviseTime method

The `GetNextAdviseTime` method retrieves the time of the next advise request.

## Syntax


```C++
REFERENCE_TIME GetNextAdviseTime();
```



## Parameters

This method has no parameters.

## Return value

Returns the reference time of the next advise request, or MAX\_TIME no requests are scheduled.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMSchedule Class**](camschedule.md)
</dt> </dl>

 

 




