---
title: Descriptor Heaps
description: A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor.
ms.assetid: '04d3facf-21ec-45ca-ad9b-78fdcddc7136'
ms.topic: article
ms.date: 05/31/2018
---

# Descriptor Heaps

A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Descriptor Heaps Overview](descriptor-heaps-overview.md)<br/>                             | Descriptor heaps contain many object types that are not part of a Pipeline State Object (PSO), such as Shader Resource Views (SRVs), Unordered Access Views (UAVs), Constant Buffer Views (CBVs), and Samplers. <br/>                |
| [Hardware Tiers](hardware-support.md)<br/>                                                 | The levels of hardware from Tier 1 to Tier 3 have increasing resources available to the pipeline. <br/>                                                                                                                              |
| [Shader Visible Descriptor Heaps](shader-visible-descriptor-heaps.md)<br/>                 | Shader visible descriptor heaps, are descriptor heaps that can be referenced by shaders through descriptor tables.<br/>                                                                                                              |
| [Non Shader Visible Descriptor Heaps](non-shader-visible-descriptor-heaps.md)<br/>         | Some descriptor heaps cannot be referenced by shaders through descriptor tables, but exist either to assist the app in staging the descriptors prior to recording a command list or because no shader-visible heap is required.<br/> |
| [Creating Descriptor Heaps](creating-descriptor-heaps.md)<br/>                             | To create and configure a descriptor heap, you must select a descriptor heap type, determine how many descriptors it contains, and set flags that indicate whether it is CPU visible and/or shader visible. <br/>                    |
| [Setting and Populating Descriptor Heaps](setting-descriptor-heaps.md)<br/>                | The descriptor heap types that can be set on a command list are those that contain descriptors for which descriptor tables can be used (at most one of each at a time). <br/>                                                        |
| [Descriptor Heap Configurability Summary](descriptor-heap-configurability-summary.md)<br/> | The following table summarizes information about Shader and non-Shader visible heap support.<br/>                                                                                                                                    |



 

## Related topics

<dl> <dt>

[Descriptors](descriptors.md)
</dt> <dt>

[Descriptor Tables](descriptor-tables.md)
</dt> <dt>

[**ID3D12DescriptorHeap**](/windows/desktop/api/d3d12/nn-d3d12-id3d12descriptorheap)
</dt> <dt>

[Resource Binding](resource-binding.md)
</dt> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 





