---
description: CEnumMediaTypes.CEnumMediaTypes constructor - Constructor method.
ms.assetid: fae2e05c-3f7b-4511-9b9d-5a37ea03f851
title: CEnumMediaTypes.CEnumMediaTypes constructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CEnumMediaTypes.CEnumMediaTypes
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CEnumMediaTypes.CEnumMediaTypes constructor

Constructor method.

## Syntax


```C++
CEnumMediaTypes(
   CBasePin        *pPin,
   CEnumMediaTypes *pEnumMediaTypes
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the pin on which the enumeration is to be performed.

</dd> <dt>

*pEnumMediaTypes* 
</dt> <dd>

Pointer to the [**IEnumMediaTypes**](/windows/desktop/api/Strmif/nn-strmif-ienummediatypes) interface of an enumerator to clone, or **NULL**.

</dd> </dl>

## Remarks

If *pEnumMediaTypes* is **NULL**, this method initializes the enumerator to the beginning of the enumeration sequence. Otherwise, it duplicates the internal state of the enumerator specified by *pEnumMediaTypes*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CEnumMediaTypes Class**](cenummediatypes.md)
</dt> </dl>

 

 




