---
description: The IsActive method determines whether the object is active (running or paused).
ms.assetid: 6531cf1f-e057-4094-9354-d5a32371c83c
title: CBaseMediaFilter.IsActive method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseMediaFilter.IsActive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseMediaFilter.IsActive method

The `IsActive` method determines whether the object is active (running or paused).

## Syntax


```C++
BOOL IsActive();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the object is paused or running, or **FALSE** if it is stopped.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




