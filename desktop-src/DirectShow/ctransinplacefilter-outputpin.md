---
Description: The OutputPin method retrieves a pointer to the filters output pin.
ms.assetid: 8c8c125e-553d-43c5-bc63-a0c7d5b01260
title: CTransInPlaceFilter.OutputPin method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransInPlaceFilter.OutputPin method

The `OutputPin` method retrieves a pointer to the filter's output pin.

## Syntax


```C++
CTransInPlaceOutputPin* OutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CTransformFilter::m\_pOutput**](ctransformfilter-m-poutput.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




