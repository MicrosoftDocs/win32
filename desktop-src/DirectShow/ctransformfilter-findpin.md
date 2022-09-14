---
description: The FindPin method gets the pin with the specified identifier. This method implements the IBaseFilter::FindPin method.
ms.assetid: 56ee3e0d-9e3f-4d25-846b-50119b55a122
title: CTransformFilter.FindPin method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.FindPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.FindPin method

The **FindPin** method gets the pin with the specified identifier. This method implements the [**IBaseFilter::FindPin**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-findpin) method.

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

Wide-character string that contains the pin identifier.

</dd> <dt>

*ppPin* 
</dt> <dd>

Receives a pointer to the pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface. If the method fails, `*ppPin` is set to **NULL**.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                       | Description                                           |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>     | Insufficient memory.<br/>                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | **NULL** pointer argument.<br/>                 |
| <dl> <dt>**VFW\_E\_NOT\_FOUND**</dt> </dl> | Could not find a pin with this identifier.<br/> |



 

## Remarks

> [!IMPORTANT]
> The implementation of this method does not call [**IPin::QueryId**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryid) to match the pin identifier. Instead, the method assumes that the input pin is named "In", and the output pin is named "Out". If you use a different set of pin identifiers, override this method.

 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




