---
description: CBaseAllocator.Alloc method - The Alloc method allocates memory for the buffers.
ms.assetid: a22c97ef-6a8d-4cad-b5a5-3e6b225f5c81
title: CBaseAllocator.Alloc method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.Alloc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator.Alloc method

The `Alloc` method allocates memory for the buffers.

## Syntax


```C++
virtual HRESULT Alloc();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                       | Description                                      |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>           | Buffer requirements have not changed.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>              | Buffer requirements have changed.<br/>     |
| <dl> <dt>**VFW\_E\_SIZENOTSET**</dt> </dl> | Buffer requirements were not set.<br/>     |



 

## Remarks

This method is called by the [**CBaseAllocator::Commit**](cbaseallocator-commit.md) method.

In the base class, this method does not allocate any memory. It returns an error if the buffer requirements were not set, S\_FALSE if the requirements have not changed, and S\_OK if the requirements have changed.

A derived class should override this method to perform the actual memory allocation. Typically, the derived class will perform the following steps:

1.  Call the base class implementation, to determine whether the memory truly needs allocating.
2.  Allocate memory.
3.  Create [**CMediaSample**](cmediasample.md) objects that contain chunks of memory from step 2.
4.  Add each **CMediaSample** object to the list of free samples ([**CBaseAllocator::m\_lFree**](cbaseallocator-m-lfree.md)).

For an example, see [**CMemAllocator::Alloc**](cmemallocator-alloc.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




