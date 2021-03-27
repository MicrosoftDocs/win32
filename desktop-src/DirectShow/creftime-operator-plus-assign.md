---
description: The += operator adds two reference times.
ms.assetid: 016d3dac-4d7c-490a-83aa-1d88a2080748
title: CRefTime.operator+= method (Reftime.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRefTime.operator+=
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRefTime.operator+= method

The += operator adds two reference times.

## Syntax


```C++
CRefTime& operator+=(
  [ref] const CRefTime &rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to a **CRefTime** object.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




