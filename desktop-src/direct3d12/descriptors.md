---
title: Descriptors
description: Descriptors are the primary unit of binding for a single resource in D3D12.
ms.assetid: 'f35b5776-46b0-4659-9e61-c6ebfdb55f87'
ms.topic: article
ms.date: 05/31/2018
---

# Descriptors

Descriptors are the primary unit of binding for a single resource in D3D12.

## In this section



| Topic                                                       | Description                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Descriptors Overview](descriptors-overview.md)<br/> | Descriptors are created by API calls and identify resources.<br/>                                                                                                                                                                                                                                                                                                                   |
| [Creating Descriptors](creating-descriptors.md)<br/> | Describes and shows examples for creating index, vertex, and constant buffer views; shader resource, render target, unordered access, stream output and depth-stencil views; and samplers. All methods for creating descriptors are free threaded.<br/>                                                                                                                             |
| [Copying Descriptors](copying-descriptors.md)<br/>   | The [**ID3D12Device::CopyDescriptors**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptors) and [**ID3D12Device::CopyDescriptorsSimple**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptorssimple) methods on the device interface use the CPU to immediately copy descriptors. They can be called free threaded as long as multiple threads on the CPU or GPU do not perform any potentially conflicting writes.<br/> |



 

## Related topics

<dl> <dt>

[Descriptor Heaps](descriptor-heaps.md)
</dt> <dt>

[Descriptor Tables](descriptor-tables.md)
</dt> <dt>

[Resource Binding](resource-binding.md)
</dt> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 





