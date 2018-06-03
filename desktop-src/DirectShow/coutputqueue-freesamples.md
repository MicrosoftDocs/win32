---
Description: The FreeSamples method frees all pending samples.
ms.assetid: 61b7fe6e-41cc-4d5e-b083-bbc400d04e39
title: COutputQueue.FreeSamples method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




