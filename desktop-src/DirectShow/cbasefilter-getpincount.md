---
description: The GetPinCount method retrieves the number of pins.
ms.assetid: 6cbeb123-d899-4f13-8b40-5666adec610f
title: CBaseFilter.GetPinCount method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.GetPinCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.GetPinCount method

The `GetPinCount` method retrieves the number of pins.

## Syntax


```C++
virtual int GetPinCount() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns the number of pins.

## Remarks

The derived class must implement this pure virtual method. Return the number of pins that are currently available on this filter. Filters can dynamically create or destroy pins.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




