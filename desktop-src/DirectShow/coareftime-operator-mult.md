---
description: This operator multiplies a reference time by a value.
ms.assetid: f575fd41-1d3e-43a6-abf8-8e64093e408e
title: COARefTime.operator* method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COARefTime.operator*
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COARefTime.operator\* method

This operator multiplies a reference time by a value.

## Syntax


```C++
COARefTime operator*(
   LONG l
);
```



## Parameters

<dl> <dt>

*l* 
</dt> <dd>

Multiplier.

</dd> </dl>

## Return value

Returns a new **COARefTime** object equal to the product of this object and **l**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




