---
description: CBasePin.GetMediaType method - The GetMediaType method retrieves a preferred media type, by index value.
ms.assetid: 96f102b0-e2d1-49a1-84af-aa4622cae2a9
title: CBasePin.GetMediaType method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.GetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.GetMediaType method

The `GetMediaType` method retrieves a preferred media type, by index value.

## Syntax


```C++
virtual HRESULT GetMediaType(
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

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                            | Description                      |
|--------------------------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>              |
| <dl> <dt>**VFW\_S\_NO\_MORE\_ITEMS**</dt> </dl> | Index out of range.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | Index less than zero.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>           | Unexpected error.<br/>     |



 

## Remarks

From the pin's list of preferred media types, this method returns the type with an index value of *iPosition*. The [**CEnumMediaTypes**](cenummediatypes.md) class calls this method to enumerate preferred media types.

The base class returns E\_UNEXPECTED. Override this method in your derived class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




