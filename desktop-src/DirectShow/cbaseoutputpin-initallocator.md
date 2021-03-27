---
description: The InitAllocator method creates a memory allocator.
ms.assetid: a1fa0ffb-ed43-446d-811e-6c3594743592
title: CBaseOutputPin.InitAllocator method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseOutputPin.InitAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseOutputPin.InitAllocator method

The `InitAllocator` method creates a memory allocator.

## Syntax


```C++
virtual HRESULT InitAllocator(
   IMemAllocator **ppAlloc
);
```



## Parameters

<dl> <dt>

*ppAlloc* 
</dt> <dd>

Address of a variable that receives a pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an error code from the **CoCreateInstance** function.

## Remarks

If the input pin does not provide a memory allocator, the [**CBaseOutputPin::DecideAllocator**](cbaseoutputpin-decideallocator.md) method calls this method to create an allocator.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




