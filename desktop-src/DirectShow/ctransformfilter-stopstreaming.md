---
description: The StopStreaming method is called when the filter switches to the stopped state.
ms.assetid: cfebfed2-4105-4dea-8d47-60d6160ee337
title: CTransformFilter.StopStreaming method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.StopStreaming
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




