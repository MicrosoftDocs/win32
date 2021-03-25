---
description: Flag that indicates whether the pin tries its own preferred media types before those of the receiving pin.
ms.assetid: 50462ee4-4a61-472f-9a7e-9cdb39be4dea
title: CBasePin::m_bTryMyTypesFirst member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bTryMyTypesFirst
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin::m\_bTryMyTypesFirst member

Flag that indicates whether the pin tries its own preferred media types before those of the receiving pin.

## Syntax


```C++
bool m_bTryMyTypesFirst;
```



## Remarks

This flag defaults to **FALSE**. If the flag is **TRUE**, the [**CBasePin::AgreeMediaType**](cbasepin-agreemediatype.md) method reverses the order in which it tries media types.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




