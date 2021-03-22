---
description: The SendAnyway method delivers any pending samples.
ms.assetid: b4e3a0c6-0f72-4a00-963e-65ceed265f01
title: COutputQueue.SendAnyway method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.SendAnyway
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.SendAnyway method

The `SendAnyway` method delivers any pending samples.

## Syntax


```C++
void SendAnyway();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the [**COutputQueue::m\_bBatchExact**](coutputqueue-m-bbatchexact.md) member variable is **TRUE**, the object fills the [**COutputQueue::m\_ppSamples**](coutputqueue-m-ppsamples.md) array before it delivers a batch of samples. Call this method to deliver a partial batch. For example, the [**COutputQueue::EOS**](coutputqueue-eos.md) method calls `SendAnyway` to serialize end-of-stream messages.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




