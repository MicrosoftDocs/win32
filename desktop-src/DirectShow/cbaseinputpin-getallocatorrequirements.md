---
Description: The GetAllocatorRequirements method retrieves the allocator properties requested by the input pin.
ms.assetid: 81564924-6d5b-4b2a-b549-e3f358f18371
title: CBaseInputPin.GetAllocatorRequirements method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.GetAllocatorRequirements
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseInputPin.GetAllocatorRequirements method

The `GetAllocatorRequirements` method retrieves the allocator properties requested by the input pin.

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

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/desktop/api/strmif/ns-strmif-_allocatorproperties) structure, which is filled in with the requirements.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

When an output pin initializes a memory allocator, it can call this method to determine whether the input pin has any buffer requirements. For more information, see [**CBaseOutputPin::DecideAllocator**](cbaseoutputpin-decideallocator.md).

Implementing this method is optional. If the filter has specific alignment or prefix requirements, override this method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




