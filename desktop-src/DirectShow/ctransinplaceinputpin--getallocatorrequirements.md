---
description: The GetAllocatorRequirements method retrieves the allocator properties requested by the pin. This method implements the IMemInputPin::GetAllocatorRequirements method.
ms.assetid: 1355facc-f863-44b2-9284-8f06f62d39a2
title: CTransInPlaceInputPin.GetAllocatorRequirements method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceInputPin.GetAllocatorRequirements
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceInputPin.GetAllocatorRequirements method

The `GetAllocatorRequirements` method retrieves the allocator properties requested by the pin. This method implements the [**IMemInputPin::GetAllocatorRequirements**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocatorrequirements) method.

## Syntax


```C++
HRESULT GetAllocatorRequirements(
   ALLOCATOR_PROPERTIES *pProps
);
```



## Parameters

<dl> <dt>

*pProps* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure, which is filled in with the requirements.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                               | Description                                                                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                                                                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The output pin is not connected, or the downstream input pin does not support the method.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument<br/>                                                                 |



 

## Remarks

If the output pin is connected, this method passes the call to the downstream input pin. Otherwise, it returns E\_NOTIMPL.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




