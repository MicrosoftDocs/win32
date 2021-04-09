---
description: Constructor method.
ms.assetid: c1282676-6f2b-438a-850e-17bb6d7a2c68
title: CRefTime.CRefTime constructor (Reftime.h) - rt parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRefTime.CRefTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRefTime.CRefTime constructor (Reftime.h)

Constructor method.

## Syntax


```C++
CRefTime(
   REFERENCE_TIME rt
);
```



## Parameters

<dl> <dt>

*rt* 
</dt> <dd>

Time in 100-nanosecond units.

</dd> </dl>

## Remarks

The reference time defaults to zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




