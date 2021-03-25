---
description: The CMediaType.CMediaType::operator= method (Mtype.h) overloads the assignment operator to copy a media type.
ms.assetid: 28115548-97a5-426d-97cd-c5e759d8e39e
title: CMediaType.CMediaType::operator= method (Mtype.h) - cmtype parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.CMediaType::operator=
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.CMediaType::operator= method (Mtype.h) - cmtype parameter

This operator overloads the assignment operator to copy a media type.

## Syntax


```C++
CMediaType& CMediaType::operator=(
  [ref] const CMediaType &cmtype
);
```



## Parameters

<dl> <dt>

*cmtype* \[ref\]
</dt> <dd>

Reference to a **CMediaType** object.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements

| Requirement                   | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Mtype.h (include Streams.h)                                                                                     |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




