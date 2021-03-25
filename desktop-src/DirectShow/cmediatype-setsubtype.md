---
description: The SetSubtype method specifies the subtype.
ms.assetid: cf52e0dc-d75b-408e-a63c-481d55151d4a
title: CMediaType.SetSubtype method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetSubtype
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetSubtype method

The `SetSubtype` method specifies the subtype.

## Syntax


```C++
void SetSubtype(
   const GUID *psubtype
);
```



## Parameters

<dl> <dt>

*psubtype* 
</dt> <dd>

Pointer to a **GUID** that specifies the subtype.

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

 

 




