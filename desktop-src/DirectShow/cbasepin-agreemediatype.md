---
description: The AgreeMediaType method searches for a media type to make a pin connection.
ms.assetid: 545186d2-b5e8-4833-b0ff-11160c1dd53b
title: CBasePin.AgreeMediaType method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.AgreeMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.AgreeMediaType method

The `AgreeMediaType` method searches for a media type to make a pin connection.

## Syntax


```C++
virtual HRESULT AgreeMediaType(
         IPin       *pReceivePin,
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the receiving pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies a media type, or **NULL**.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                                  | Description                                    |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                            |
| <dl> <dt>**VFW\_E\_NO\_ACCEPTABLE\_TYPES**</dt> </dl> | No acceptable media type was found.<br/> |



 

## Remarks

If the *pmt* parameter is non-**NULL** and fully specifies a media type, this method attempts a connection using that media type. If the attempt fails, the method returns an error.

If the *pmt* parameter is **NULL** or specifies a partial media type, this method tries media types in the following order:

1.  The receiving pin's preferred media types.
2.  This pin's preferred media types.

Preferred media types are enumerated with the [**CBasePin::EnumMediaTypes**](cbasepin-enummediatypes.md) method, and the resulting enumerator is passed to the [**CBasePin::TryMediaTypes**](cbasepin-trymediatypes.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




