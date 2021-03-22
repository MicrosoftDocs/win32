---
description: The GetUnits method retrieves the reference time in 100-nanosecond units.
ms.assetid: f27dada1-67a6-424a-8bf5-979ad375736f
title: CRefTime.GetUnits method (Reftime.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRefTime.GetUnits
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRefTime.GetUnits method

The `GetUnits` method retrieves the reference time in 100-nanosecond units.

## Syntax


```C++
LONGLONG GetUnits();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CRefTime::m\_time**](creftime-m-time.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




