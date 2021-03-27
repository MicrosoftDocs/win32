---
description: The CurrentMediaType method retrieves the media type for the current pin connection.
ms.assetid: d46f4d8e-9e9d-49d3-b823-f2f0fcf25383
title: CTransformInputPin.CurrentMediaType method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.CurrentMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformInputPin.CurrentMediaType method

The `CurrentMediaType` method retrieves the media type for the current pin connection.

## Syntax


```C++
CMediaType& CurrentMediaType();
```



## Parameters

This method has no parameters.

## Return value

Returns a reference to the [**CBasePin::m\_mt**](cbasepin-m-mt.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




