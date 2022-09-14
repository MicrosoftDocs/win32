---
title: Suballocation Within Heaps
description: Resource heaps transfer data from the CPU to the GPU (upload), and from the GPU to the CPU (read back).
ms.assetid: 7E319BCF-FF3F-43CB-9C48-A9DD2A043592
ms.topic: article
ms.date: 05/31/2018
---

# Suballocation Within Heaps

Resource heaps transfer data from the CPU to the GPU (upload), and from the GPU to the CPU (read back).

## In this section



| Topic                                                                                       | Description                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Memory Aliasing and Data Inheritance](memory-aliasing-and-data-inheritance.md)<br/> | Placed and reserved resource may alias physical memory within a heap. Placed resources enable more data inheritance scenarios than reserved resources when the heap has the shared flag set or when the aliased resources have fully defined memory layouts. <br/> |
| [Shared Heaps](shared-heaps.md)<br/>                                                 | Sharing is useful for multi-process and multi-adapter architectures.<br/>                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[**ID3D12Device::CreateHeap**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createheap)
</dt> <dt>

[**ID3D12Heap**](/windows/desktop/api/d3d12/nn-d3d12-id3d12heap)
</dt> <dt>

[Memory Management](memory-management.md)
</dt> </dl>

 

 





