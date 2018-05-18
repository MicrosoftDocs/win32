---
Description: 'Note  This interface is no longer supported by the AVI Splitter. Note  This interface was defined to support older hardware decoders that required AVI files to be read into directly hardware memory.'
ms.assetid: 'bab1e582-928a-408b-a9c5-8e9827e9928b'
title: IAMDevMemoryAllocator interface
---

# IAMDevMemoryAllocator interface

> [!Note]  
> This interface is no longer supported by the AVI Splitter.

 

> [!Note]  
> This interface was defined to support older hardware decoders that required AVI files to be read into directly hardware memory. The interface enables the AVI parser to allocate memory from the downstream filter but still provide its own allocator.

 

Implement this interface when your pin must support the creation of on-board memory allocators. Source filters that are aware of on-board memory and need to create their own allocators should query for this interface, request an amount of memory and then create an allocator (aggregating the device memory control object). Source filters that don't need to create their own allocator could just use the allocator of the downstream pin (which also aggregates the device memory control object). The hardware-based filter can confirm the usage of its on-board memory by calling methods on the aggregated allocator.

Use this interface when applications need to control the memory of codecs with on-board memory.

## Members

The **IAMDevMemoryAllocator** interface inherits from the [**IUnknown**](com.iunknown) interface. **IAMDevMemoryAllocator** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMDevMemoryAllocator** interface has these methods.



| Method                                                                 | Description                                                                                                                              |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| [**Alloc**](iamdevmemoryallocator-alloc.md)                           | Allocates a memory buffer.<br/>                                                                                                    |
| [**CheckMemory**](iamdevmemoryallocator-checkmemory.md)               | Tests whether the particular device of the allocator allocated a memory pointer.<br/>                                              |
| [**Free**](iamdevmemoryallocator-free.md)                             | Frees the previously allocated memory.<br/>                                                                                        |
| [**GetDevMemoryObject**](iamdevmemoryallocator-getdevmemoryobject.md) | Retrieves an **IUnknown** interface pointer to a device memory control object that can be aggregated with a custom allocator.<br/> |
| [**GetInfo**](iamdevmemoryallocator-getinfo.md)                       | Retrieves information about the memory capabilities.<br/>                                                                          |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




