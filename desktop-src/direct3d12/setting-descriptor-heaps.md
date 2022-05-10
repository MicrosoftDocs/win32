---
title: Setting and Populating Descriptor Heaps
description: The descriptor heap types that can be set on a command list are those that contain descriptors for which descriptor tables can be used (at most one of each at a time).
ms.assetid: F0FF3D7C-1DAC-48C3-B47D-0378BE369F37
ms.topic: article
ms.date: 05/31/2018
---

# Setting and Populating Descriptor Heaps

The descriptor heap types that can be set on a command list are those that contain descriptors for which descriptor tables can be used (at most one of each at a time).

-   [Setting descriptor heaps](#setting-and-populating-descriptor-heaps)
-   [Populating descriptor heaps](#populating-descriptor-heaps)
-   [Related topics](#related-topics)

## Setting descriptor heaps

The types of descriptor heap that can be set on a command list are:

``` syntax
D3D12_DESCRIPTOR_HEAP_TYPE_CBV_SRV_UAV
D3D12_DESCRIPTOR_HEAP_TYPE_SAMPLER
```

The heaps being set on the command list must also have been created as shader visible. There are three types of command list: DIRECT, BUNDLE, and COMPUTE.

After a descriptor heap is set on a command list, subsequent calls that define descriptor tables refer to the current descriptor heap. Descriptor table state is undefined at the beginning of a command list and after descriptor heaps are changed on a command list. Redundantly setting the same descriptor heap does not cause descriptor table settings to be undefined.

In a bundle, by contrast, the descriptor heaps can only be set once (redundant calls setting the same heap twice do not produce an error); otherwise, the behavior is undefined. The descriptor heaps that are set must match the state when any command list calls the bundle; otherwise, the behavior is undefined. This allows bundles to inherit and edit the command list’s descriptor table settings. Bundles that don’t change descriptor tables (only inherit them) don’t need to set a descriptor heap at all and will just inherit from the calling command list.

When descriptor heaps are set (using [**ID3D12GraphicsCommandList::SetDescriptorHeaps**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setdescriptorheaps)), all the heaps being used are set in a single call (and all previously set heaps are unset by the call). At most one heap of each type listed above can be set in the call.

## Populating descriptor heaps

After an application has created a descriptor heap, it can then use methods on the device to either generate descriptors directly into the heap or copy descriptors from one place to another.

The initial contents of descriptor heap memory is undefined, so asking the GPU or driver to reference uninitialized memory for rendering can cause undefined results such as a device reset.

If the application configures a descriptor heap to be CPU visible, then the CPU can call methods to create descriptors into the heap and copy from place to place (including across heaps) in an immediate, free threaded manner. If the heap has been configured as SHADER_VISIBLE, reading by the CPU is not permitted.



## Related topics

<dl> <dt>

[Descriptor Heaps](descriptor-heaps.md)
</dt> </dl>

 

 




