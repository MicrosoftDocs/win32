---
description: The GetEvent method retrieves an event handle, which is used to signal a change in the next advise time.
ms.assetid: 2548a321-df65-4a5b-9e6a-8bbc031254c7
title: CAMSchedule.GetEvent method (Dsschedule.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule.GetEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMSchedule.GetEvent method

The `GetEvent` method retrieves an event handle, which is used to signal a change in the next advise time.

## Syntax


```C++
HANDLE GetEvent();
```



## Parameters

This method has no parameters.

## Return value

Returns a handle to an event.

## Remarks

If the next advise time changes in other words, if a new advise request is added to the front of the list the scheduler signals this event. The clock should call the [**CAMSchedule::Advise**](camschedule-advise.md) method to determine the next advise time.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMSchedule Class**](camschedule.md)
</dt> </dl>

 

 




