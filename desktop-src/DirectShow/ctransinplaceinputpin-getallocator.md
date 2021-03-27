---
description: The GetAllocator method retrieves the memory allocator proposed by this pin. This method implements the IMemInputPin::GetAllocator method.
ms.assetid: e9db4aa0-4f53-4ca4-babb-5e0215c7c284
title: CTransInPlaceInputPin.GetAllocator method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceInputPin.GetAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceInputPin.GetAllocator method

The `GetAllocator` method retrieves the memory allocator proposed by this pin. This method implements the [**IMemInputPin::GetAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocator) method.

## Syntax


```C++
HRESULT GetAllocator(
   IMemAllocator **ppAllocator
);
```



## Parameters

<dl> <dt>

*ppAllocator* 
</dt> <dd>

Receives a pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                          | Description                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Success.<br/>                   |
| <dl> <dt>**VFW\_E\_NO\_ALLOCATOR**</dt> </dl> | No allocator is available.<br/> |



 

## Remarks

If the filter's output pin is connected, this method requests an allocator from the downstream filter's input pin.

If the filter's output pin is not connected, this method creates a temporary allocator. Later, when the output pin is connected, the filter will reconnect the input pin and renegotiate the allocator.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




