---
description: The IsIdle method determines whether the object is waiting for data.
ms.assetid: be1b5633-f9e9-497e-8b6f-5634eae91273
title: COutputQueue.IsIdle method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.IsIdle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.IsIdle method

The `IsIdle` method determines whether the object is waiting for data.

## Syntax


```C++
BOOL IsIdle();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the thread is waiting and the sample array is empty. Otherwise, returns **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




