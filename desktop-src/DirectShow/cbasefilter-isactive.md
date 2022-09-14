---
description: The IsActive method determines whether the filter is currently active (running or paused).
ms.assetid: 3bbb50d5-6a07-4932-940c-4466b95e6412
title: CBaseFilter.IsActive method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.IsActive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.IsActive method

The `IsActive` method determines whether the filter is currently active (running or paused).

## Syntax


```C++
BOOL IsActive();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the filter is paused or running, or **FALSE** if it is stopped.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




