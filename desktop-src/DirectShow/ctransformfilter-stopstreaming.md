---
Description: The StopStreaming method is called when the filter switches to the stopped state.
ms.assetid: cfebfed2-4105-4dea-8d47-60d6160ee337
title: CTransformFilter.StopStreaming method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter.StopStreaming method

The `StopStreaming` method is called when the filter switches to the stopped state.

## Syntax


```C++
virtual HRESULT StopStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method does nothing in the base class, but the derived class can override it.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




