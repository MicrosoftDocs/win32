---
description: The SetType method specifies the major type.
ms.assetid: 3fd93d5e-73ea-453e-8f08-652d5a81239f
title: CMediaType.SetType method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetType method

The `SetType` method specifies the major type.

## Syntax


```C++
void SetType(
   const GUID *ptype
);
```



## Parameters

<dl> <dt>

*ptype* 
</dt> <dd>

Pointer to a **GUID** that specifies the major type.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




