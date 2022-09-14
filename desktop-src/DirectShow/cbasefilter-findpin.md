---
description: CBaseFilter.FindPin method - The FindPin method retrieves the pin with the specified identifier. This method implements the IBaseFilter::FindPin method.
ms.assetid: 152e4ff3-2809-4c57-b9c8-f51fc50b3703
title: CBaseFilter.FindPin method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.FindPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseFilter.FindPin method

The `FindPin` method retrieves the pin with the specified identifier. This method implements the [**IBaseFilter::FindPin**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-findpin) method.

## Syntax


```C++
HRESULT FindPin(
   LPCWSTR Id,
   IPin    **ppPin
);
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

Pointer to a constant, null-terminated Unicode string that identifies the pin.

</dd> <dt>

*ppPin* 
</dt> <dd>

Address of a variable that receives a pointer to the pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                       | Description                               |
|---------------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | **NULL** pointer argument.<br/>     |
| <dl> <dt>**VFW\_E\_NOT\_FOUND**</dt> </dl> | Could not find a matching pin.<br/> |



 

## Remarks

This method calls the [**CBasePin::Name**](cbasepin-name.md) method to compare each pin's name against the string specified by the *Id* parameter.

If the method succeeds, the **IPin** interface has an outstanding reference count. Be sure to release it when you are done.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




