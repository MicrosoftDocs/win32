---
title: Copying Descriptors
description: The ID3D12Device CopyDescriptors and ID3D12Device CopyDescriptorsSimple methods on the device interface use the CPU to immediately copy descriptors.
ms.assetid: 65AE4D96-6221-46B5-BF55-F86479FCF97C
ms.topic: article
ms.date: 05/31/2018
---

# Copying Descriptors

The [**ID3D12Device::CopyDescriptors**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptors) and [**ID3D12Device::CopyDescriptorsSimple**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptorssimple) methods on the device interface use the CPU to immediately copy descriptors. They can be called free threaded as long as multiple threads on the CPU or GPU do not perform any potentially conflicting writes.

## Copying Descriptors Immediately (CPU Timeline)

The number of source descriptors (to copy from), specified as a set of descriptor ranges, must equal the number of destination descriptors (to copy to), specified as a separate set of descriptor ranges. The source and destination ranges do not otherwise have to line up. For example, a sparse set of descriptors could be copied to a contiguous destination, vice versa, or in some combination.

Multiple descriptor heaps can be involved in the copy operation, both as source and destination. The use of descriptor handles as parameters means the copy methods don’t care about which heaps any given descriptor lies in – they are all just memory.

The descriptor heap types being copied from and to must match, so the methods take a single descriptor heap type as input. The driver needs to know the heap type of all the descriptors in the given copy operation, so it knows what size of data is involved in the copy operation. The driver might also need to do custom copying work if a given descriptor heap type warrants it – an implementation detail. Note that descriptor handles themselves do not otherwise identify what type they are pointing to; therefore, an additional parameter is required for the copy operation.

An alternative API to [**CopyDescriptors**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptors) is provided for the simple case of copying a single range of descriptors from one location to another – [**CopyDescriptorsSimple**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptorssimple).

For these device based (CPU timeline) descriptor copy methods, source descriptors must come from a non-shader visible descriptor heap. The destination descriptors can be in any descriptor heap that is CPU visible (shader visible or not).

## Related topics

<dl> <dt>

[Descriptors](descriptors.md)
</dt> </dl>

 

 




