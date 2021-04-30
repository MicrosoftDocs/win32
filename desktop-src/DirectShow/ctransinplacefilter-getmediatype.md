---
description: CTransInPlaceFilter.GetMediaType method - The GetMediaType method retrieves a preferred media type for the output pin.
ms.assetid: 1bc6c06d-f399-4b8a-81f2-7fffe4630236
title: CTransInPlaceFilter.GetMediaType method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.GetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.GetMediaType method

The `GetMediaType` method retrieves a preferred media type for the output pin.

## Syntax


```C++
HRESULT GetMediaType(
   int        iPosition,
   CMediaType *pMediaType
);
```



## Parameters

<dl> <dt>

*iPosition* 
</dt> <dd>

Zero-based index value.

</dd> <dt>

*pMediaType* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that receives the media type.

</dd> </dl>

## Return value

Returns E\_UNEXPECTED.

## Remarks

This method overrides the [**CTransformFilter::GetMediaType**](ctransformfilter-getmediatype.md) method. In the **CTransInPlaceFilter** class, each pin calls the opposite connected pin to enumerate preferred media types. The input pin calls the downstream filter's input pin, and the output pin calls the upstream filter's output pin. Therefore, the filter's `GetMediaType` method is never called.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




