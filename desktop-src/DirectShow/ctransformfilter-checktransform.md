---
description: The CheckTransform method checks whether an input media type is compatible with an output media type.
ms.assetid: 349145e5-c12d-41df-ae37-7846f8aaa423
title: CTransformFilter.CheckTransform method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.CheckTransform
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.CheckTransform method

The `CheckTransform` method checks whether an input media type is compatible with an output media type.

## Syntax


```C++
virtual HRESULT CheckTransform(
   const CMediaType *mtIn,
   const CMediaType *mtOut
) = 0;
```



## Parameters

<dl> <dt>

*mtIn* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the input type.

</dd> <dt>

*mtOut* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the output type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                | Description                                    |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The media types are compatible.<br/>     |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | The media types are not compatible.<br/> |



 

## Remarks

The derived class must implement this method. Return S\_OK if the filter can accept both of the specified media types, or an error code otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




