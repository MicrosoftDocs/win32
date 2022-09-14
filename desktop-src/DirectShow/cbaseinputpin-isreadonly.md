---
description: Queries whether the allocator uses read-only media samples.
ms.assetid: 2cb692da-f030-4265-afe4-b1608b51fd47
title: CBaseInputPin.IsReadOnly method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.IsReadOnly
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseInputPin.IsReadOnly method

Queries whether the allocator uses read-only media samples.

## Syntax


```C++
BOOL IsReadOnly();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of the [**CBaseInputPin::m\_bReadOnly**](cbaseinputpin-m-breadonly.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




