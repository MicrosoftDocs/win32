---
Description: The SetTimeAdvise method sets up a timer event with the reference clock.
ms.assetid: d0ab5c21-3585-413b-ba75-8591ed4527e4
title: CCmdQueue.SetTimeAdvise method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CCmdQueue.SetTimeAdvise method

The `SetTimeAdvise` method sets up a timer event with the reference clock.

## Syntax


```C++
void SetTimeAdvise();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This member function calls the [**IReferenceClock::AdviseTime**](/windows/win32/Strmif/nf-strmif-ireferenceclock-advisetime?branch=master) method to set up a notification for the earliest time required in the queue. Presentation-time commands that are deferred are always checked. If the filter graph is in running mode, deferred commands using stream time are also checked.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




