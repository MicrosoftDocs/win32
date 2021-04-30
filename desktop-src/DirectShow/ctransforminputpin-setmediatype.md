---
description: CTransformInputPin.SetMediaType method - The SetMediaType method sets the media type for the connection.
ms.assetid: 8e83380f-ba38-4fb8-ac32-40d68a4efea6
title: CTransformInputPin.SetMediaType method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.SetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformInputPin.SetMediaType method

The `SetMediaType` method sets the media type for the connection.

## Syntax


```C++
HRESULT SetMediaType(
   const CMediaType *mt
);
```



## Parameters

<dl> <dt>

*mt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the media type.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method overrides the [**CBasePin::SetMediaType**](cbasepin-setmediatype.md) method. It calls the filter's [**CTransformFilter::SetMediaType**](ctransformfilter-setmediatype.md) method to inform the filter.

The pin must verify that the media type is acceptable before calling this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




