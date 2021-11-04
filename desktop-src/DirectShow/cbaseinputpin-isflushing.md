---
description: The IsFlushing method queries whether the filter is currently flushing.
ms.assetid: 366b6162-7a2c-4882-8774-8b4bf83012b4
title: CBaseInputPin.IsFlushing method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.IsFlushing
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseInputPin.IsFlushing method

The `IsFlushing` method queries whether the filter is currently flushing.

## Syntax


```C++
BOOL IsFlushing();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseInputPin::m\_bFlushing**](cbaseinputpin-m-bflushing.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




