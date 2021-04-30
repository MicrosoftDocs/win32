---
description: The Advise method dispatches all requests that are scheduled for a specified time or earlier.
ms.assetid: 09ea84b7-517a-4ea6-9e03-0d9cd8f72e1f
title: CAMSchedule.Advise method (Dsschedule.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule.Advise
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMSchedule.Advise method

The `Advise` method dispatches all requests that are scheduled for a specified time or earlier.

## Syntax


```C++
REFERENCE_TIME Advise(
  [ref] const REFERENCE_TIME &rtTime
);
```



## Parameters

<dl> <dt>

*rtTime* \[ref\]
</dt> <dd>

Value that specifies the current reference time.

</dd> </dl>

## Return value

Returns the reference time of the next scheduled advise request, or MAX\_TIME if there are none left.

## Remarks

When the clock calls this method, it specifies the current reference time. The scheduler determines which advise requests have expired, if any, and dispatches them. If a one-shot request expires, the scheduler deletes it. If a periodic request expires, the scheduler re-schedules it for the next advise time. The method returns the time of the next pending request.

To dispatch an advise request, the scheduler signals the event or semaphore given in the *hNotify* parameter of the [**CAMSchedule::AddAdvisePacket**](camschedule-addadvisepacket.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMSchedule Class**](camschedule.md)
</dt> </dl>

 

 




