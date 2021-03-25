---
description: The SetProperties method specifies the number of buffers to allocate and the size of each buffer. This method overrides the CBaseAllocator::SetProperties method.
ms.assetid: 8d419432-a9a7-44fb-b916-8dacd08eb6ec
title: CImageAllocator.SetProperties method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageAllocator.SetProperties
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageAllocator.SetProperties method

The `SetProperties` method specifies the number of buffers to allocate and the size of each buffer. This method overrides the [**CBaseAllocator::SetProperties**](cbaseallocator-setproperties.md) method.

## Syntax


```C++
HRESULT SetProperties(
   ALLOCATOR_PROPERTIES *pRequest,
   ALLOCATOR_PROPERTIES *pActual
);
```



## Parameters

<dl> <dt>

*pRequest* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure that contains the buffer requirements.

</dd> <dt>

*pActual* 
</dt> <dd>

Pointer to an **ALLOCATOR\_PROPERTIES** structure that receives the actual buffer properties.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This method calls [**CImageAllocator::CheckSizes**](cimageallocator-checksizes.md) to validate the requested buffer size. It also calls the base-class version of `SetProperties`.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageAllocator Class**](cimageallocator.md)
</dt> </dl>

 

 




