---
description: CTransformOutputPin.CheckMediaType method - The CheckMediaType method determines if the pin accepts a specific media type.
ms.assetid: 9e31480b-129c-4741-846a-854c70c65606
title: CTransformOutputPin.CheckMediaType method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformOutputPin.CheckMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformOutputPin.CheckMediaType method

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

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The filter's input pin is not connected.<br/> |



 

## Remarks

This method implements the pure virtual [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method. The method fails if the filter's input pin is not connected. Otherwise, it calls the filter's [**CTransformFilter::CheckTransform**](ctransformfilter-checktransform.md) method, which is also pure virtual. The filter's derived class must implement **CheckTransform**, which determines if the proposed output media type is compatible with the input media type.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




