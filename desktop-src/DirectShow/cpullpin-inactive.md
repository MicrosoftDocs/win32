---
Description: The Inactive method shuts down the worker thread that pulls data from the output pin. This method also decommits the allocator.
ms.assetid: 90b91686-b9a8-4196-b559-de924334f11c
title: CPullPin.Inactive method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPullPin.Inactive method

The `Inactive` method shuts down the worker thread that pulls data from the output pin. This method also decommits the allocator.

## Syntax


```C++
HRESULT Inactive();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

Call this method when the owning filter becomes inactive. (If your input pin derives from [**CBasePin**](cbasepin.md), override the [**CBasePin::Inactive**](cbasepin-inactive.md) method.)

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




