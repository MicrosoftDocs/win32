---
Description: Memory Allocator
ms.assetid: 2dc055a2-b77a-443d-b602-d9636cbe4db3
title: Memory Allocator
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Memory Allocator

The Memory Allocator object allocates buffers for media samples. Filters can use this object to allocate shared memory buffers; however, a filter with special requirements can also implement its own memory allocator object. Create this object by calling **CoCreateInstance**.



|                  |                                        |
|------------------|----------------------------------------|
| Class Identifier | CLSID\_MemoryAllocator                 |
| Interfaces       | [**IMemAllocator**](/windows/win32/Strmif/nn-strmif-imemallocator?branch=master) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



