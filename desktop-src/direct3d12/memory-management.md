---
title: Memory Management in Direct3D 12
description: Moving to D3D12 involves doing proper synchronization and management of memory residency.
ms.assetid: 94D47EBB-8060-49F6-A1FF-8B7B98AD5363
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management in Direct3D 12

Moving to D3D12 involves doing proper synchronization and management of memory residency. Managing memory residency means even more synchronization must be done. This section covers memory management strategies, and suballocation within heaps and buffers.

-   [In this section](#in-this-section)
-   [Related topics](#related-topics)

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Memory Management Strategies](memory-management-strategies.md)<br/> | A memory manager for Direct3D 12 could get very complicated quickly with all the different tiers of support, for UMA or discrete (non-UMA) adapters, and with a considerable range of architecture differences between GPU adapters.<br/> The recommended strategy for Direct3D 12 memory management , described in this section, is "classify, budget and stream".<br/> |
| [Suballocation Within Buffers](large-buffers.md)<br/>                | Buffers have all the features necessary in D3D12 for applications to transfer a large range of transient data from the CPU to the GPU. This section covers four common scenarios for the use and management of resources and buffers.<br/>                                                                                                                                     |
| [Suballocation Within Heaps](suballocation-within-heaps.md)<br/>     | Resource heaps transfer data from the CPU to the GPU (upload), and from the GPU to the CPU (read back). <br/>                                                                                                                                                                                                                                                                  |
| [Residency](residency.md)<br/>                                       | An object is considered to be *resident* when it is accessible by the GPU.<br/>                                                                                                                                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[Resource Binding](resource-binding.md)
</dt> </dl>

 

 





