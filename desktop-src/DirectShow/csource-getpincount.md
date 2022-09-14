---
description: The GetPinCount method retrieves the number of pins on the filter. This method implements the pure virtual CBaseFilter::GetPinCount method.
ms.assetid: 42000814-daee-4f7b-96d2-e09a21fde8cd
title: CSource.GetPinCount method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSource.GetPinCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSource.GetPinCount method

The `GetPinCount` method retrieves the number of pins on the filter. This method implements the pure virtual [**CBaseFilter::GetPinCount**](cbasefilter-getpincount.md) method.

## Syntax


```C++
int GetPinCount();
```



## Parameters

This method has no parameters.

## Return value

Returns the number of pins on this filter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




