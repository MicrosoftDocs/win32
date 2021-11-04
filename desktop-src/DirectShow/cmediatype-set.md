---
description: "The CMediaType.Set method (Mtype.h) sets the media type from another media type. The method uses the 'cmtype' parameter."
ms.assetid: 71c19d0f-93b6-41db-8659-c64411b83e7c
title: CMediaType.Set method (Mtype.h) - cmtype [ref] parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.Set
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.Set method (Mtype.h) - cmtype [ref] parameter

The `Set` method sets the media type from another media type.

## Syntax


```C++
HRESULT Set(
  [ref] const CMediaType &cmtype
);
```



## Parameters

<dl> <dt>

*cmtype* \[ref\]
</dt> <dd>

Reference to a [**CMediaType**](cmediatype.md) object.

</dd> </dl>

## Return value

Returns S\_OK or E\_OUTOFMEMORY.

## Remarks

This method copies the entire media type from *cmtype*.

## Requirements

| Requirement                   | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Mtype.h (include Streams.h)                                                                                     |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




