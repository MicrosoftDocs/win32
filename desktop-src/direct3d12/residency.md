---
title: Residency
description: An object is considered to be resident when it is accessible by the GPU.
ms.assetid: 956F80D7-EEC8-4D88-B251-EE325614F31E
ms.topic: article
ms.date: 05/31/2018
---

# Residency

An object is considered to be *resident* when it is accessible by the GPU.

-   [Residency budget](#residency-budget)
-   [Heap resources](#heap-resources)
-   [Residency priorities](#residency-priorities)
    -   [Default priority algorithm](#default-priority-algorithm)
-   [Programming residency management](#programming-residency-management)
-   [Related topics](#related-topics)

## Residency budget

GPUs do not yet support page-faulting, so applications must commit data into physical memory while the GPU could access it. This process is known as “making something resident”, and must be done for both physical system memory and physical discrete video memory. In D3D12, most API objects encapsulate some amount of GPU-accessible memory. That GPU-accessible memory is made resident during the creation of the API object, and evicted on API object destruction.

The amount of physical memory available for the process is known as the video memory budget. The budget can fluctuate noticeably as background processes wake-up and sleep; and fluctuate dramatically when the user switches away to another application. The application can be notified when the budget changes and poll both the current budget and the currently consumed amount of memory. If an application doesn’t stay within its budget, the process will be intermittently frozen to allow other applications to run and/or the creation APIs will return failure. The [**IDXGIAdapter3**](/windows/desktop/api/dxgi1_4/nn-dxgi1_4-idxgiadapter3) interface provides the methods pertaining to this functionality, in particular [**QueryVideoMemoryInfo**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-queryvideomemoryinfo) and [**RegisterVideoMemoryBudgetChangeNotificationEvent**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-registervideomemorybudgetchangenotificationevent).

Applications are encouraged to use a reservation to denote the amount of memory they cannot go without. Ideally, the user-specified “low” graphics settings, or something even lower, is the right value for such a reservation. Setting a reservation won’t ever give an application a higher budget than it would normally receive. Instead, the reservation information helps the OS kernel quickly minimize the impact of large memory pressure situations. Even the reservation is not guaranteed to be available to the application when the application isn’t the foreground application.

## Heap resources

While many API objects encapsulate some GPU-accessible memory, heaps & resources are expected to be the most significant way applications consume and manage physical memory. A heap is the lowest level unit to manage physical memory, so it’s good to have some familiarity with their residency properties.

-   Heaps cannot be made partially resident, but workarounds exists with reserved resources.
-   Heaps should be budgeted as part of a particular pool. UMA adapters have one pool, while discrete adapters have two pools. While it is true that kernel can shift some heaps on discrete adapters from video memory to system memory, it does so only as an extreme last resort. Applications should not rely on the over-budget behavior of the kernel, and should focus on good budget management instead.
-   Heaps can be evicted from residency, which allows their content to be paged out to disk. But, destruction of heaps is a more reliable technique to free up residency across all adapter architectures. On adapters where *theMaxGPUVirtualAddressBitsPerProcess* field of [**D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_gpu_virtual_address_support) is near the budget size, [**Evict**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-evict) won’t reliably reclaim residency.
-   Heap creation can be slow; but it is optimized for background thread processing. It’s recommended to create heaps on background threads to avoid glitching the render thread. In D3D12, multiple threads may safely call create routines concurrently.

D3D12 introduces more flexibility and orthogonality into its resource model in order to enable more options for applications. There are three high-level types of resources in D3D12: committed, placed, and reserved.

-   Committed resources create both a resource and a heap at the same time. The heap is implicit and cannot be accessed directly. The heap is appropriately sized to locate the entire resource within the heap.
-   Placed resources allow the placement of a resource at a non-zero offset within a heap. Offsets must typically be aligned to 64KB; but some exceptions exist in both directions. MSAA resources require 4MB offset alignment, and 4KB offset alignment is available for small textures. Placed resources cannot be relocated or remapped to another heap directly; but they enable simple relocation of the resource data between heaps. After creating a new placed resource in a different heap and copying the resource data, new resource descriptors will have to be used for the new resource data location.
-   Reserved resources are only available when the adapter supports tiled resources tier 1 or greater. When available, they offer the most advanced residency management techniques available; but not all adapters currently support them. They enable remapping a resource without requiring regeneration of resource descriptors, partial mip level residency, and sparse texture scenarios, etc. Not all resources types are supported even when reserved resources are available, so a fully general page-based residency manager isn’t yet feasible.

## Residency priorities

The Windows 10 Creators Update enables developers to influence which heaps and resources will be prefered to stay resident when memory pressure requires that some of its resources be demoted. This helps developers create better performing applications by leveraging knowlege that the runtime can't infer from API usage. Its expected that developers will become more comfortable and capable specifying priorities as they transition from using commited resources to resereved and tiled resources.

Applying these priorities must be easier than manageing two dynamic memory budgets, manually demoting and promoting resources bettween them, since applications can already do that. Therefore, the design of the residency priority API is coursely-grained with reasonable default priorities assigned to each heap or resource as its created. For more information, see [**ID3D12Device1::SetResidencyPriority**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device1-setresidencypriority) and the [**D3D12\_RESIDENCY\_PRIORITY**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_residency_priority) enumeration.

With priorities, developers are expected to either:

-   Raise the priority of a few exceptional heaps to better mitigate the experienced performance impact of these heaps being demoted sooner or more frequently than their natural access patterns would demand. This approach is expected to be leveraged by applications ported from graphics APIs such as Direct3D 11 or OpenGL, who's resource management model is significantly different than that of Direct3D 12.
-   Override nearly all heap priorities with the application's own bucketization scheme, either fixed, based on the programmer's knowlege of access frequency, or dynamic; a fixed scheme is simpler to manage than a dynamic one, but can be less effective and require programmer intevention as use patterns change over the course of development. This approach is expected to be leveraged by applications that are built with Direct3D 12-style resource management in mind, such as those that use the residency library (especially dynamic schemes).

### Default priority algorithm

An application can't specify useful priorities for any heap it attempts to manage without first understaning the default priority algorithm. This is because the value of assigning a particular priority to a heap is derived from its relative priority to other prioritized heaps that compete for the same memory.

The strategy chosen for generating default priorities is to categorize heaps into two buckets, favoring (giving higher priority to) heaps that are assumed to be written frequently by the GPU over heaps that aren't.

The high-priority bucket contains heaps and resources that are created with flags that identify them as render targets, depth-stencil buffers, or Unordered Access Views (UAVs). These are assigned priority values in the range starting at **D3D12\_RESIDENCY\_PRIORITY\_HIGH**; to further prioritize among these heaps and resources, the lowest 16-bits of the priority are set to the size of the heap or resource divided by 10MB (saturating to 0xFFFF for extremely large heaps). This additional prioritization favors larger heaps and resources.

The low-priority bucket contains all other heaps and resources, which are assigned a priority value of **D3D12\_RESIDENCY\_PRIORITY\_NORMAL**. No further prioritization among these heaps and resources is attempted.

## Programming residency management

Simple applications may be able to get by merely creating committed resources until experiencing out-of-memory failures. Upon failure, the application can destroy other committed resources or API objects to enable further resource creations to succeed. But, even simple applications are strongly recommended to watch for negative budget changes and destroy unused API objects roughly once a frame.

The complexity of a residency management design will go up when trying to optimize for adapter architectures or incorporating residency priorities. Discretely budgeting and managing two pools of discrete memory will be more complex than managing only one, and assigning fixed priorities on a wide scale can become a maintainance burden if use patterns evolve. Overflowing textures into system memory adds more complexity, as the wrong resource in system-memory can severely impact frame rate. And, there is no simple functionality to help identify the resources that would either benefit from higher GPU bandwidth or tolerate lower GPU bandwidth.

Even more complicated designs will query for the features of the current adapter. This information is available in [**D3D12\_FEATURE\_DATA\_GPU\_VIRTUAL\_ADDRESS\_SUPPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_gpu_virtual_address_support), [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_architecture), [**D3D12\_TILED\_RESOURCES\_TIER**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_tiled_resources_tier), and [**D3D12\_RESOURCE\_HEAP\_TIER**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_heap_tier).

Multiple parts of an application will likely wind up using different techniques. For example, some large textures and rarely exercised code paths may use committed resources, while many textures may be designated with a streaming property and use a general placed-resource technique.

## Related topics

<dl> <dt>

[**ID3D12Heap**](/windows/desktop/api/d3d12/nn-d3d12-id3d12heap)
</dt> <dt>

[Memory Management](memory-management.md)
</dt> </dl>

 

 
