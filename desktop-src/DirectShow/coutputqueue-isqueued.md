---
Description: The IsQueued method determines whether the object is using a worker thread to deliver samples.
ms.assetid: 8d26661f-6cd7-42ea-bc4b-8746d22a7ca0
title: COutputQueue.IsQueued method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COutputQueue.IsQueued method

The `IsQueued` method determines whether the object is using a worker thread to deliver samples.

## Syntax


```C++
BOOL IsQueued();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the object is using a worker thread, or **FALSE** otherwise.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




