---
description: Constructor method.
ms.assetid: 35198320-d028-42d4-823f-4f8346d8f977
title: CMediaType.CMediaType constructor (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.CMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.CMediaType constructor (Mtype.h)

Constructor method.

## Syntax


```C++
CMediaType(
  [ref] const CMediaType &cmtype,
              HRESULT    *phr = NULL
);
```



## Parameters

<dl> <dt>

*cmtype* \[ref\]
</dt> <dd>

Reference to a `CMediaType` object. The constructor copies the media type to the new object, including the format block, if any.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an HRESULT value. This parameter can be a **NULL** pointer. Otherwise, the caller must set the value to S\_OK before calling the constructor. If the constructor fails, it sets the value to a failure code.

</dd> </dl>

## Remarks

The constructor calls the [**CMediaType::InitMediaType**](cmediatype-initmediatype.md) method to initialize the media type.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




