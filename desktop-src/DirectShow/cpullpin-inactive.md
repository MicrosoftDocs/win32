---
description: The Inactive method shuts down the worker thread that pulls data from the output pin. This method also decommits the allocator.
ms.assetid: 90b91686-b9a8-4196-b559-de924334f11c
title: CPullPin.Inactive method (Pullpin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.Inactive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




