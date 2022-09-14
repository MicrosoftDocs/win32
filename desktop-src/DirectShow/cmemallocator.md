---
description: Implements an allocator that supports the IMemAllocator interface.
ms.assetid: c40eccef-d915-4bf3-81b2-b20e000718fb
title: CMemAllocator class (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMemAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMemAllocator class

![cmemallocator class hierarchy](images/filter10.png)

Implements an allocator that supports the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

This class derives from [**CBaseAllocator**](cbaseallocator.md). For more information about allocators, refer to the documentation for [**CBaseAllocator**](cbaseallocator.md).



| Protected Member Variables                              | Description                                                              |
|---------------------------------------------------------|--------------------------------------------------------------------------|
| [**m\_pBuffer**](cmemallocator-m-pbuffer.md)           | Pointer to the memory block that contains the buffers.                   |
| Protected Methods                                       | Description                                                              |
| [**Free**](cmemallocator-free.md)                      | Placeholder method; called during a decommit operation.                  |
| [**ReallyFree**](cmemallocator-reallyfree.md)          | Releases the memory for the buffers.                                     |
| [**Alloc**](cmemallocator-alloc.md)                    | Allocates memory for the buffers.                                        |
| Public Methods                                          | Description                                                              |
| [**CMemAllocator**](cmemallocator-cmemallocator.md)    | Constructor method.                                                      |
| [**~ CMemAllocator**](cmemallocator--cmemallocator.md) | Destructor method.                                                       |
| [**CreateInstance**](cmemallocator-createinstance.md)  | Creates a new instance of the **CMemAllocator** class.                   |
| IMemAllocator Methods                                   | Description                                                              |
| [**SetProperties**](cmemallocator-setproperties.md)    | Specifies the number of buffers to allocate and the size of each buffer. |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Providing a Custom Allocator](providing-a-custom-allocator.md)
</dt> </dl>

 

 




