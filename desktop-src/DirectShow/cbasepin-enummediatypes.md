---
description: The EnumMediaTypes method enumerates the pin's preferred media types. This method implements the IPin::EnumMediaTypes method.
ms.assetid: 0360f9fc-6876-4a54-8de1-bf289e0e10ae
title: CBasePin.EnumMediaTypes method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.EnumMediaTypes
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.EnumMediaTypes method

The `EnumMediaTypes` method enumerates the pin's preferred media types. This method implements the [**IPin::EnumMediaTypes**](/windows/desktop/api/Strmif/nf-strmif-ipin-enummediatypes) method.

## Syntax


```C++
HRESULT EnumMediaTypes(
   IEnumMediaTypes **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* 
</dt> <dd>

Address of a variable that receives a pointer to the [**IEnumMediaTypes**](/windows/desktop/api/Strmif/nn-strmif-ienummediatypes) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                   | Description                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/> |



 

## Remarks

Input pins are not required to enumerate any preferred types. Output pins must enumerate at least one preferred type. Otherwise, both pins could lack a preferred type, making a connection impossible.

The **IEnumMediaTypes** interface works like a standard COM enumerator. For more information, see [Enumerating Objects in a Filter Graph](enumerating-objects-in-a-filter-graph.md). If the method succeeds, the **IEnumMediaTypes** interface has an outstanding reference count. Be sure to release it when you are done.

The [**CEnumMediaTypes**](cenummediatypes.md) base class implements **IEnumMediaTypes**. It calls the pin's [**CBasePin::GetMediaType**](cbasepin-getmediatype.md) method to enumerate the media types.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




