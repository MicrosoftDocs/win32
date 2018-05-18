---
title: Shared Heaps
description: Sharing is useful for multi-process and multi-adapter architectures.
ms.assetid: '67C6B1D4-BF76-45A9-BADC-7C9520C900EB'
---

# Shared Heaps

Sharing is useful for multi-process and multi-adapter architectures.

-   [Sharing overview](#sharing-overview)
-   [Sharing heaps across processes](#sharing-heaps-across-processes)
-   [Sharing heaps across adapters](#sharing-heaps-across-adapters)
-   [Related topics](#related-topics)

## Sharing overview

Shared heaps enable two things: sharing data in a heap across one or more processes, and precluding a non-deterministic choice of undefined texture layout for resources placed within the heap. Sharing heaps across adapters also removes the need for CPU marshaling of the data.

Both heaps and committed resources can be shared. Sharing a committed resource actually shares the implicit heap along with the committed resource description, such that a compatible resource description can be mapped to the heap from another device.

All methods are free-threaded and inherit the existing D3D11 semantics of the NT handle sharing design.

-   [**ID3D12Device::CreateSharedHandle**](id3d12device-createsharedhandle.md)
-   [**ID3D12Device::OpenSharedHandle**](id3d12device-opensharedhandle.md)
-   [**ID3D12Device::OpenSharedHandleByName**](id3d12device-opensharedhandlebyname.md)

## Sharing heaps across processes

Shared heaps are specified with the D3D12\_HEAP\_FLAG\_SHARED member of the [**D3D12\_HEAP\_FLAGS**](d3d12-heap-flags.md) enum.

Shared heaps are not supported on CPU-accessible heaps: D3D12\_HEAP\_TYPE\_UPLOAD, D3D12\_HEAP\_TYPE\_READBACK, and D3D12\_HEAP\_TYPE\_CUSTOM without D3D12\_CPU\_PAGE\_PROPERTY\_NOT\_AVAILABLE.

Precluding a non-deterministic choice of undefined texture layout can significantly impair deferred rendering scenarios on some GPUs, so it is not the default behavior for placed and committed resources. Deferred rendering is impaired on some GPU architectures because deterministic texture layouts decrease the effective memory bandwidth achieved when rendering simultaneously to multiple render target textures of the same format and size. GPU architectures are evolving away from leveraging non-deterministic texture layouts in order to support standardized swizzle patterns and standardized layouts efficiently for deferred rendering.

Shared heaps come with other minor costs as well:

-   Shared heap data cannot be recycled as flexibly as in-process heaps due to information disclosure concerns, so physical memory is zero'ed more often.
-   There is a minor additional CPU overhead and increased system memory usage during creation and destruction of shared heaps.

## Sharing heaps across adapters

Shared heaps across adapters is specified with the D3D12\_HEAP\_FLAG\_SHARED\_CROSS\_ADAPTER member of the [**D3D12\_HEAP\_FLAGS**](d3d12-heap-flags.md) enum.

Cross adapter shared heaps enable multiple adapters to share data without the CPU marshaling the data between them. While varying adapter capabilities determine how efficient adapters can pass data between them, merely enabling GPU copies increases the effective bandwidth achieved. Some texture layouts are allowed on cross adapter heaps to support an interchange of texture data, even if such texture layouts are not otherwise supported. Certain restrictions may apply to such textures, such as only supporting copying.

Cross-adapter sharing works with heaps created by calling [**ID3D12Device::CreateHeap**](id3d12device-createheap.md). Applications can then create resources via [**CreatePlacedResource**](id3d12device-createplacedresource.md). It is also allowed by resources/heaps created by [**CreateCommittedResource**](id3d12device-createcommittedresource.md) but only for row-major D3D12\_RESOURCE\_DIMENSION\_TEXTURE2D resources (refer to [**D3D12\_RESOURCE\_DIMENSION**](d3d12-resource-dimension.md)). Cross-adapter sharing does not work with [**CreateReservedResource**](id3d12device-createreservedresource.md).

For cross-adapter sharing, all of the usual cross-queue resource sharing rules still apply. Applications must issue the appropriate barriers to ensure proper synchronization and coherence between the two adapters. Applications should use cross-adapter fences to coordinate the scheduling of command lists submitted to multiple adapters. There is no mechanism to share cross-adapter resources across D3D API versions. Cross-adapter shared resources are only supported in system memory. Cross-adapter shared heaps/resources are supported in D3D12\_HEAP\_TYPE\_DEFAULT heaps and D3D12\_HEAP\_TYPE\_CUSTOM heaps (with the L0 memory pool, and write-combine CPU page properties). Drivers must be sure that GPU read/write operations to cross-adapter shared heaps are coherent with other GPUs on the system. For example, the driver may need to exclude the heap data from residing in GPU caches that typically don’t need to be flushed when the CPU cannot directly access the heap data.

Applications should confine the usage of cross adapter heaps to only those scenarios which require the functionality they provide. Cross-adapter heaps are located in D3D12\_MEMORY\_POOL\_L0, which is not always what [**GetCustomHeapProperties**](id3d12device-getcustomheapproperties.md) suggests. That memory pool is not efficient for discrete/ NUMA adapter architectures. And, the most efficient texture layouts are not always available.

The following limitations also apply:

-   The heap flags related to heap tiers must be D3D12\_HEAP\_FLAG\_ALLOW\_ALL\_BUFFERS\_AND\_TEXTURES.
-   D3D12\_HEAP\_FLAG\_SHARED must also be set.
-   Either D3D12\_HEAP\_TYPE\_DEFAULT must be set or D3D12\_HEAP\_TYPE\_CUSTOM with D3D12\_MEMORY\_POOL\_L0 and D3D12\_CPU\_PAGE\_PROPERTY\_NOT\_AVAILABLE must be set.
-   Only resources with D3D12\_RESOURCE\_FLAG\_ALLOW\_CROSS\_ADAPTER may be placed on cross-adapter heaps.

For more information on using multiple adapters, refer to the [Multi-Adapter](mulit-engine.md) section.

## Related topics

<dl> <dt>

[Suballocation Within Heaps](suballocation-within-heaps.md)
</dt> </dl>

 

 




