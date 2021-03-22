---
description: The Wait method blocks until the event is signaled, or until a time-out occurs.
ms.assetid: bcc13723-a59b-4e8a-bfc8-eadb6facf116
title: CAMEvent.Wait method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent.Wait
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMEvent.Wait method

The `Wait` method blocks until the event is signaled, or until a time-out occurs.

## Syntax


```C++
BOOL Wait(
   DWORD dwTimeout = INFINITE
);
```



## Parameters

<dl> <dt>

*dwTimeout* 
</dt> <dd>

Optional time-out value, represented in milliseconds.

</dd> </dl>

## Return value

Returns **TRUE** if the event is signaled. Otherwise, returns **FALSE**.

## Remarks

For auto-reset events, the event is reset to a nonsignaled state when this method returns.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMEvent Class**](camevent.md)
</dt> </dl>

 

 




