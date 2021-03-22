---
description: The GetMediaType method retrieves a preferred media type, by index value.
ms.assetid: d106e6d1-66ff-4460-9ea2-c93f16116cf4
title: CTransformOutputPin.GetMediaType method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformOutputPin.GetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformOutputPin.GetMediaType method

The `GetMediaType` method retrieves a preferred media type, by index value.

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

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                            | Description                   |
|--------------------------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success<br/>            |
| <dl> <dt>**VFW\_S\_NO\_MORE\_ITEMS**</dt> </dl> | Index out of range<br/> |



 

## Remarks

This method overrides the [**CBasePin::GetMediaType**](cbasepin-getmediatype.md) method. If the filter's input pin is not connected, the method returns VFW\_S\_NO\_MORE\_ITEMS. Otherwise, it calls the filter's [**CTransformFilter::GetMediaType**](ctransformfilter-getmediatype.md) method to retrieve the media type. The **CTransformFilter::GetMediaType** method is pure virtual; the filter's derived class must override it.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




