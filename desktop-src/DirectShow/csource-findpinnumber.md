---
description: The FindPinNumber method retrieves the number of a specified pin on the filter.
ms.assetid: c9366fcc-7b13-4e43-883e-6003c32fadec
title: CSource.FindPinNumber method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSource.FindPinNumber
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSource.FindPinNumber method

The `FindPinNumber` method retrieves the number of a specified pin on the filter.

## Syntax


```C++
int FindPinNumber(
   IPin *iPin
);
```



## Parameters

<dl> <dt>

*iPin* 
</dt> <dd>

Pointer to the pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns the pin number, or  1 if the pin is not found on this filter. The first pin is numbered zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




