---
description: CMemAllocator.Alloc method - The Alloc method allocates memory for the buffers.
ms.assetid: 81886163-2f7d-4d4f-be90-4491f76b8514
title: CMemAllocator.Alloc method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMemAllocator.Alloc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMemAllocator.Alloc method

The `Alloc` method allocates memory for the buffers.

## Syntax


```C++
HRESULT Alloc();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                       | Description                                  |
|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>     | Insufficient memory.<br/>              |
| <dl> <dt>**VFW\_E\_SIZENOTSET**</dt> </dl> | Buffer requirements were not set.<br/> |



 

## Remarks

This method is called by the [**CBaseAllocator::Commit**](cbaseallocator-commit.md) method. It allocates a contiguous block of memory sufficient for the buffer requirements given in the [**CMemAllocator::SetProperties**](cmemallocator-setproperties.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




