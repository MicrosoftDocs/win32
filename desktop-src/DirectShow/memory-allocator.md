---
Description: Memory Allocator
ms.assetid: '2dc055a2-b77a-443d-b602-d9636cbe4db3'
title: Memory Allocator
---

# Memory Allocator

The Memory Allocator object allocates buffers for media samples. Filters can use this object to allocate shared memory buffers; however, a filter with special requirements can also implement its own memory allocator object. Create this object by calling **CoCreateInstance**.



|                  |                                        |
|------------------|----------------------------------------|
| Class Identifier | CLSID\_MemoryAllocator                 |
| Interfaces       | [**IMemAllocator**](imemallocator.md) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



