---
title: Memory Management Strategies
description: A memory manager for Direct3D 12 could get very complicated quickly with all the different tiers of support, for UMA or discrete (non-UMA) adapters, and with a considerable range of architecture differences between GPU adapters.The recommended strategy for Direct3D 12 memory management , described in this section, is \ 0034;classify, budget and stream \ 0034;.
ms.assetid: BC9894F7-D496-46F2-A5C3-C7CA31FD4BA8
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management Strategies

A memory manager for Direct3D 12 could get very complicated quickly with all the different tiers of support, for UMA or discrete (non-UMA) adapters, and with a considerable range of architecture differences between GPU adapters.

The recommended strategy for Direct3D 12 memory management , described in this section, is "classify, budget and stream".

-   [Resource types](#resource-types)
-   [Memory budget](#memory-budget)
-   [Classification strategy](#classification-strategy)
-   [Related topics](#related-topics)

## Resource types

The basic concept of a "committed resource" (creating both virtual and physical address spaces initialized in managed physical memory) has been around since Direct3D 9, though the virtual addressing (VA) and physical addressing can be teased apart in Direct3D 12 to allow the app to carefully manage physical memory.

In addition to committed resources, the heap construct of Direct3D 12 enables two other types of resource: "placed" and "reserved". In Direct3D 11 a "reserved" resource was known as a "tiled resource".

Reserved resources differ from placed resources in that reserved resources have their own unique GPU virtual address space. This allows a large allocation of VA space up front and then enables mapping of VA pages to certain sections of the heap later, and the application reconfigures the arrangement on the fly. The VA space is contiguous, and can be sparsely mapped to.

The reserved resource can be made to reference regions in the heap with API calls such as [**UpdateTileMappings**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-updatetilemappings) and they can be made resident by the app by updating page tables on the fly. When a VA range is mapped to NULL or a non-resident heap, that portion of the resource is considered non-resident. When a VA range is mapped to a resident heap, that portion of the resource is considered resident. Heaps are resident upon creation.

Placed resources are a much simpler design, being simply a pointer to a certain region of a heap (for example, a 1Mb region for a texture in a 5Mb heap). Aliasing barriers enable the use of overlapping placed resources (refer to [**CreatePlacedResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createplacedresource) and [**ResourceBarrier**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resourcebarrier)).

Reserved resources are not available on all Direct3D 12 hardware, and placed resources are a reasonable fallback, though placed resources must be contiguous and cannot be partially resident.

## Memory budget

In Direct3D 12 when you allocate a heap you are creating the physical memory aspect of a committed resource. More explicit memory segment choice is available in Direct3D 12 (choosing between video and system memory). UMA adapters only have a single memory segment, system memory.

GPUs do not support page faulting, so developers must be conscious that they do not over commit, especially to systems say with only 1Gb of system memory. If an app does over commit, then the OS uses coarser-grained scheduling of processes by their demand on physical memory. The scheduler will freeze foreground processes and essentially page some of it out, in order to page-in a background process that wants to run. Available physical memory can vary considerably depending on what the user is doing in the background (such as running a browser or watching a video).

The API for memory budget is [**QueryVideoMemoryInfo**](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-queryvideomemoryinfo). For discrete adapters "local" is video memory, "non-local" is system memory. For UMA adapters non-local is always zero. One design question is whether your engine will manage both budgets or just the local budget. Managing only the local budget is simpler but has some caveats; for example say there is a maximum local budget of 1Gb, then all heaps will come from that 1Gb in a UMA system and there is no overflow to system memory (clearly, as there is none).

Since Direct3D11 managed memory for applications, unused resources would essentially be paged out.

Choose the most appropriate resource dimensions. Consider whether the size of a resource is appropriate for the situation the application is actually running in. Some users may run the application in a window or with a screen resolution of 800x600.

## Classification strategy

In order to manage resources effectively in memory bound scenarios, consider classifying resources into the following:



| Classification      | Examples                                                                                         | Objects and API features                                                                                           | Management notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Critical            | Game UI                                                                                          | Command allocator, command queues, query heaps, resources and resource heaps.                                      | These elements should go in non-pageable/always committed memory.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Scaled/ Optional    | Level-specific models and textures, swap chains, sky boxes, first-person player character models | Resources and heaps. Committed resources, but also placed and reserved resources might work just as well.          | Integrate memory residency budgeting into the rendering algorithms. Choose the appropriate level of available detail and re-evaluate less than once per-frame. Techniques include using variable-sized resources and swap chain scaling.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| Re-used Resources   | Shadow buffers, deferred rendering resources, post-processing resources, lighting data caches    | Resources and heaps. Overlapping placed resources on heaps and aliasing barriers.                                  | Reuse large resources or heap regions within a frame to cut-down on requirements for the entire frame. Use the technique of intra-frame memory reuse. In Direct3D 11, applications could only reuse resources with the same type and potentially large enough dimensions. Direct3D 12 heaps allow overlapping resources for much simpler and greater reuse.<br/>                                                                                                                                                                                                                              |
| Streaming Resources | Terrain, open-world textures and geometry                                                        | Resources and heaps. Free-threaded creation, background CPU threads, and background copy command queues and lists. | Partial residency, commonly based on visibility (using the view-frustum or distance-based evaluation) and re-evaluate residency needs every frame.<br/> The technique of using a per-tile partial residency management and inter-frame reuse is available when the GPU adapter supports reserved resources within heaps.<br/> Using the technique of using inter-frame memory re-use, partial subresource residency can be accomplished, but is less optimal. Placed resources with heaps should enable faster recycling, but committed resources can be used as a fallback.<br/> |



 

The more applications gravitate to streaming resources for most of the work, the more they will leverage placed and reserved resources, which will maximize memory re-use between these four classifications. The more applications stream, the more they budget and prioritize bandwidth.

Typically with Direct3D 12 graphics engines need to honor a more diverse and dynamic budget, and do it more strictly than they did in the past. The best applications will locate all four categories into the budget given to the process, scaling the game play from background mobile app to full-screen discrete budgets. But, many applications will likely struggle by starting with too many critical category types of resources. Direct3D 11 enabled resources to be anonymously created and occupy critical status without impacting performance. However, for Direct3D 12, developers must diligently search for randomly created resources throughout their engine and middleware and re-assign them to one of the other categories.

Other problem areas are middleware components, user controls, and intra-frame streaming. Middleware components may not be exposed to a budget, nor have to work tightly together. Middleware components likely could expose features as rendering techniques; and the application could rely on exposing middleware and engine settings. Developers could rely on Direct3D 11 to do the paging and achieve the right frame rate. In some cases, Direct3D 11 applications may have been paging resource contents in and out every frame; and it resulted in acceptable frame rates for the user. Most engines only stream resource data as a background activity, where it has no graceful fallback to high-priority intra-frame streaming. Asking engines to implement that will erode some of the CPU overhead gains they are seeking by moving to Direct3D 12. Engine developers could consider teasing their frames into phases to provide more opportunity for re-usable resources; and likely work with middleware vendors to support placed resources and heaps for intra-frame memory re-use.

## Related topics

<dl> <dt>

[**CreateCommittedResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcommittedresource)
</dt> <dt>

[**CreateReservedResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createreservedresource)
</dt> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[Memory Management](memory-management.md)
</dt> <dt>

[Resource Binding](resource-binding.md)
</dt> </dl>

 

