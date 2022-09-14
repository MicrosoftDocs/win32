---
description: CTransformInputPin.CheckMediaType method - The CheckMediaType method determines if the pin accepts a specific media type.
ms.assetid: e09a4a3e-ac39-4d0e-9e8c-3e8f18057d0d
title: CTransformInputPin.CheckMediaType method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.CheckMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformInputPin.CheckMediaType method

The `CheckMediaType` method determines if the pin accepts a specific media type.

## Syntax


```C++
HRESULT CheckMediaType(
   const CMediaType *mtIn
);
```



## Parameters

<dl> <dt>

*mtIn* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that contains the proposed media type.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

This method implements the pure virtual [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method. It calls the filter's [**CTransformFilter::CheckInputType**](ctransformfilter-checkinputtype.md) method, which is also pure virtual. The filter's derived class must implement **CheckInputType** to determine whether a given input type is acceptable.

If the filter's output pin is connected, this method also calls the filter's [**CTransformFilter::CheckTransform**](ctransformfilter-checktransform.md) method to determine whether the input type is compatible with the output type. The **CheckTransform** method is pure virtual as well.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




