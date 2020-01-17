---
title: Address space available for tiled resources
description: This section specifies the virtual address space that is available for tiled resources.
ms.assetid: A3D08564-3C7A-4578-BC38-EE202045580A
ms.topic: article
ms.date: 05/31/2018
---

# Address space available for tiled resources

This section specifies the virtual address space that is available for tiled resources.

On 64-bit operating systems, at least 40 bits of virtual address space (1 Terabyte) is available.

For 32-bit operating systems, the address space is 32 bit (4 GB). For 32-bit ARM systems, individual tiled resource creation can fail if the allocation would use more than 27 bits of address space (128 MB). This includes any hidden padding in the address space the hardware may use for mipmaps, packed tile padding, and possibly padding surface dimensions to powers of 2.

On graphics systems with a separate page table for the graphics processing unit (GPU), most of this address space will be available to GPU resources made by the application, though GPU allocations made by the display driver fit in the same space.

On future systems with a page table shared between the CPU and GPU, the available address space is shared between all CPU and GPU allocations in a process.

## Related topics

<dl> <dt>

[Tiled resource creation parameters](tiled-resource-creation-parameters.md)
</dt> </dl>

 

 




