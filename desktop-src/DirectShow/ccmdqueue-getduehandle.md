---
description: The GetDueHandle method retrieves the event handle to be signaled.
ms.assetid: 495ea76d-8b94-48a9-8025-06ab18b66693
title: CCmdQueue.GetDueHandle method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.GetDueHandle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCmdQueue.GetDueHandle method

The `GetDueHandle` method retrieves the event handle to be signaled.

## Syntax


```C++
HANDLE GetDueHandle();
```



## Parameters

This method has no parameters.

## Return value

Returns the event handle.

## Remarks

Return the event handle whenever there are deferred commands that are due for execution (when [**CCmdQueue::GetDueCommand**](ccmdqueue-getduecommand.md) will not block).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




