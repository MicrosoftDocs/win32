---
description: The SetProperties method specifies the number of buffers to allocate and the size of each buffer.
ms.assetid: 01f63379-1d66-4a72-b87c-de55504b0bb4
title: CMemAllocator.SetProperties method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMemAllocator.SetProperties
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMemAllocator.SetProperties method

The `SetProperties` method specifies the number of buffers to allocate and the size of each buffer.

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

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                                 | Description                                                           |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success.<br/>                                                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>                   | **NULL** pointer argument.<br/>                                 |
| <dl> <dt>**VFW\_E\_ALREADY\_COMMITTED**</dt> </dl>   | Cannot change allocated memory while the filter is active.<br/> |
| <dl> <dt>**VFW\_E\_BADALIGN**</dt> </dl>             | An invalid alignment was specified.<br/>                        |
| <dl> <dt>**VFW\_E\_BUFFERS\_OUTSTANDING**</dt> </dl> | One or more buffers are still active.<br/>                      |



 

## Remarks

This method overrides the [**CBaseAllocator::SetProperties**](cbaseallocator-setproperties.md) method.

The buffer alignment, specified by the **cbAlign** member of the **ALLOCATOR\_PROPERTIES** structure, must be an even power of two.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




