---
description: Memory Allocator
ms.assetid: 2dc055a2-b77a-443d-b602-d9636cbe4db3
title: Memory Allocator
ms.topic: article
ms.date: 05/31/2018
---

# Memory Allocator

The Memory Allocator object allocates buffers for media samples. Filters can use this object to allocate shared memory buffers; however, a filter with special requirements can also implement its own memory allocator object. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|----------------------------------------|
| Class Identifier | CLSID\_MemoryAllocator                 |
| Interfaces       | [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



