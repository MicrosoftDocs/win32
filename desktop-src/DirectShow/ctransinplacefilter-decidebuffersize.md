---
description: CTransInPlaceFilter.DecideBufferSize method - The DecideBufferSize method sets the output pin's buffer requirements.
ms.assetid: f1ddc39e-dcd5-4a44-8a8e-e384692408e1
title: CTransInPlaceFilter.DecideBufferSize method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.DecideBufferSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.DecideBufferSize method

The `DecideBufferSize` method sets the output pin's buffer requirements.

## Syntax


```C++
HRESULT DecideBufferSize(
   IMemAllocator        *pAlloc,
   ALLOCATOR_PROPERTIES *pProperties
);
```



## Parameters

<dl> <dt>

*pAlloc* 
</dt> <dd>

Pointer to the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) object used by the output pin.

</dd> <dt>

*pProperties* 
</dt> <dd>

Pointer to the requested allocator properties for count, size, and alignment, as specified by the [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                            | Description        |
|----------------------------------------------------------------------------------------|--------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Failure<br/> |



 

## Remarks

This method is called when the **CTransInPlaceFilter** class needs to provide a buffer size to the downstream filter. If the **CTransInPlaceFilter** filter is already connected upstream, it uses the allocator properties on the upstream pin connection. Otherwise, it sets the buffer size to 1 byte as a temporary place-holder value. When the upstream filter connects, the **CTransInPlaceFilter** class renegotiates the downstream allocator. For more information about the pin connection process in this class, see [**CTransInPlaceFilter Class**](ctransinplacefilter.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




