---
Description: 'The IsIdle method determines whether the object is waiting for data.'
ms.assetid: 'be1b5633-f9e9-497e-8b6f-5634eae91273'
title: 'COutputQueue.IsIdle method'
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




