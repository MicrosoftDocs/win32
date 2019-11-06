---
Description: This operator overloads the assignment operator to copy a media type.
ms.assetid: 28115548-97a5-426d-97cd-c5e759d8e39e
title: CMediaType.CMediaType::operator= method (Mtype.h)
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

# CMediaType.CMediaType::operator= method

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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




