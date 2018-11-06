---
title: Descriptor Heaps Overview
description: Descriptor heaps contain many object types that are not part of a Pipeline State Object (PSO), such as Shader Resource Views (SRVs), Unordered Access Views (UAVs), Constant Buffer Views (CBVs), and Samplers.
ms.assetid: 14561E77-44E0-4A58-8456-F40D59ECA175
ms.topic: article
ms.date: 05/31/2018
---

# Descriptor Heaps Overview

Descriptor heaps contain many object types that are not part of a Pipeline State Object (PSO), such as Shader Resource Views (SRVs), Unordered Access Views (UAVs), Constant Buffer Views (CBVs), and Samplers.

-   [The Purpose of Descriptor Heaps](#the-purpose-of-descriptor-heaps)
-   [Synchronization](#synchronization)
-   [Binding](#binding)
-   [Switching heaps](#switching-heaps)
-   [Bundles](#bundles)
-   [Management](#management)
-   [Related topics](#related-topics)

## The Purpose of Descriptor Heaps

The primary purpose of a descriptor heap is to encompass the bulk of memory allocation required for storing the descriptor specifications of object types that shaders reference for as large of a window of rendering as possible (ideally an entire frame of rendering or more). If an application is switching which textures the pipeline sees rapidly from the API, there has to be space in the descriptor heap to define descriptor tables on the fly for every set of state needed. The application can choose to reuse definitions if the resources are used again in another object, for example, or just assign the heap space sequentially as it switches various object types.

Descriptor heaps also allow individual software components to manage descriptor storage separately from each other.

All heaps are visible to the CPU. The application can also request which CPU access properties a descriptor heap should have (if any) – write combined, write back, and so on. Apps can create as many descriptor heaps as desired with whatever properties are desired. Apps always have the option to create descriptor heaps that are purely for staging purposes that are unconstrained in size, and copying to descriptor heaps that are used for rendering as necessary.

There are some restrictions in what can go in the same descriptor heap. CBV, UAV and SRV entries can be in the same descriptor heap. However, Samplers entries cannot share a heap with CBV, UAV or SRV entries. Typically, there are two sets of descriptor heaps, one for the common resources and the second for Samplers.

The use of descriptor heaps by Direct3D 12 mirrors what most GPU hardware does, which is to either require descriptors live only in descriptor heaps, or simply that fewer addressing bits are needed if these heaps are used. Direct3D 12 does require the use of descriptor heaps, there is no option to put descriptors anywhere in memory.

Descriptor heaps can only be edited immediately by the CPU, there is no option to edit a descriptor heap by the GPU.

## Synchronization

Descriptor heap contents can be changed before, during and after recording command lists that reference it. However, descriptors cannot be changed while a command list submitted for execution might reference that location, as this could invoke a race condition.

## Binding

At most one CBV/SRV/UAV combined heap and one Sampler heap can be bound at any one time. These heaps are shared between both the graphics and compute pipelines (described in their PSOs).

## Switching heaps

It is acceptable for an application to switch heaps within the same command list or in different ones using the [**SetDescriptorHeaps**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setdescriptorheaps) and [**Reset**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-reset) APIs. On some hardware, this can be an expensive operation, requiring a GPU stall to flush all work that depends on the currently bound descriptor heap. As a result, if descriptor heaps must be changed, applications should try to do so when the GPU workload is relatively light, perhaps limiting changes to the start of a command list.

## Bundles

With bundles there can only be one call to the [**SetDescriptorHeaps**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setdescriptorheaps) method, and the descriptor heaps set must match exactly those of the command list calling the bundle. If the bundle does not change descriptor tables, it does not need to set the descriptor heaps.

For a list of API calls that cannot be used with bundles, refer to [Creating and Recording Command Lists and Bundles](recording-command-lists-and-bundles.md).

## Management

To render all of the objects in a scene, many descriptors will be needed, and there are some different management strategies that can be followed.

The most basic strategy would be to fill in a fresh area of the descriptor heap with all of the requirements for the next draw call. So, just before issuing the draw call on the command list, a descriptor table pointer would be set to the start of the freshly populated table. The upside is that there is no need to record where any particular descriptor is in the heap.

The downside to this strategy is that there could be a lot of repetition of descriptors in the descriptor heap, especially when a very similar scene is being rendered, and that descriptor heap space is going to be used up quickly. Separate descriptor heaps for those being rendered on the GPU and for those being recorded by the CPU, would probably be necessary to avoid conflict. Alternatively a sub-allocation system could be used.

Also, the basic system could be further optimized by careful use of overlapping descriptor tables from one draw call to the next, so that only the new descriptors required are added.

A more efficient strategy than the basic one would be to pre-fill descriptor heaps with descriptors required for the objects (or materials) that are known to be part of the scene. The idea here is that it is only necessary to set the descriptor table at draw time, as the descriptor heap is populated ahead of time.

A variation of the pre-filling strategy is to treat the descriptor heap as one huge array, containing all the required descriptors in fixed known locations. Then the draw call needs only to receive a set of constants which are the indices into the array of where the descriptors are that need to be used.

A further optimization is to ensure root constants and root descriptors contain those that change most frequently, rather than place constants in the descriptor heap. For most hardware this is an efficient way of handling constants.

In practice a graphics engine might use a different strategy in different situations, and combine elements of each strategy to suit the particular drawing requirements.

## Related topics

<dl> <dt>

[Descriptor Heaps](descriptor-heaps.md)
</dt> </dl>

 

 




