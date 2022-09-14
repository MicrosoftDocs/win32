---
description: The EOS method delivers an end-of-stream call to the input pin.
ms.assetid: 65e8db14-6ca8-4c4f-8bd8-2442f743499e
title: COutputQueue.EOS method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.EOS
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.EOS method

The `EOS` method delivers an end-of-stream call to the input pin.

## Syntax


```C++
void EOS();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the object is using a thread, it queues an EOS\_PACKET control message. The thread delivers any pending samples and calls the [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) method on the input pin.

If the object is not using a thread, it calls the [**COutputQueue::SendAnyway**](coutputqueue-sendanyway.md) method to deliver any pending samples. Then it calls **IPin::EndOfStream** on the input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




