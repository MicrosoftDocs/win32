---
description: The DecideAllocator method selects a memory allocator.
ms.assetid: cdc15b0e-ea1b-43aa-9267-95fa9db56ed5
title: CBaseOutputPin.DecideAllocator method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseOutputPin.DecideAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseOutputPin.DecideAllocator method

The `DecideAllocator` method selects a memory allocator.

## Syntax


```C++
virtual HRESULT DecideAllocator(
   IMemInputPin  *pPin,
   IMemAllocator **pAlloc
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the input pin's [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface.

</dd> <dt>

*pAlloc* 
</dt> <dd>

Address of a variable that receives a pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

This method is called at the end of the pin connection process. It performs the following steps:

1.  Calls the [**IMemInputPin::GetAllocatorRequirements**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocatorrequirements) method to retrieve the input pin's buffer requirements, if any.
2.  Calls the [**IMemInputPin::GetAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocator) method to request an allocator from the input pin. If the input pin does not provide an allocator, the output pin creates one by calling the [**CBaseOutputPin::InitAllocator**](cbaseoutputpin-initallocator.md) class method.
3.  Calls the [**CBaseOutputPin::DecideBufferSize**](cbaseoutputpin-decidebuffersize.md) class method, which sets the allocator properties. This is a pure virtual method; the derived class must implement it.
4.  Calls the [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator) method, which notifies the input pin of the allocator being used.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




