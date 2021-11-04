---
description: This operator tests for equality between CMediaType objects.
ms.assetid: d50f3a72-c5e8-44a5-aa0e-b1c40a19fee3
title: CMediaType.CMediaType::operator== method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.CMediaType::operator==
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.CMediaType::operator== method

This operator tests for equality between [**CMediaType**](cmediatype.md) objects.

## Syntax


```C++
BOOL CMediaType::operator==(
  [ref] const CMediaType &rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to the **CMediaType** object to compare.

</dd> </dl>

## Return value

Returns **TRUE** if *rt* is equal to this object. Otherwise, returns **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




