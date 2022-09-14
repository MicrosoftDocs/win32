---
description: The FreeSamples method frees all pending samples.
ms.assetid: 61b7fe6e-41cc-4d5e-b083-bbc400d04e39
title: COutputQueue.FreeSamples method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.FreeSamples
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.FreeSamples method

The `FreeSamples` method frees all pending samples.

## Syntax


```C++
void FreeSamples();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method removes any pending samples from the queue and from the sample array.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




