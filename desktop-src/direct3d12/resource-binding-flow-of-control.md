---
title: Resource Binding Overview
description: The key to resource binding in DirectX 12 are the concepts of a descriptor, descriptor tables, descriptor heaps, and a root signature.
ms.assetid: 92E100CA-822D-46B1-BD37-FF57C3FB703D
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Resource Binding Overview

The key to resource binding in DirectX 12 are the concepts of a *descriptor*, *descriptor tables*, *descriptor heaps*, and a *root signature*.

-   [Resources and the Graphics Pipeline](#resources-and-the-graphics-pipeline)
-   [Resource types and views](#resource-types-and-views)
-   [Resource Binding Flow of Control](#Resource-Binding-Flow-of-Control)
-   [Suballocation](#suballocation)
-   [Freeing Resources](#freeing-resources)
-   [Related topics](#related-topics)

## Resources and the Graphics Pipeline

Shader resources (such as textures, constant tables, images, buffers and so on) are not bound directly to the shader pipeline; instead, they are referenced through a *descriptor*. A descriptor is a small object that contains information about one resource.

Descriptors are grouped together to form *descriptor tables*. Each descriptor table stores information about one range of types of resource. There are many different types of resources. The most common resources are:

-   Constant buffer views (CBVs)
-   Unordered access views (UAVs)
-   Shader resource views (SRVs)
-   Samplers

SRV, UAV, and CBVs descriptors can be combined into the same descriptor table.

The graphics and compute pipelines gain access to resources by referencing into descriptor tables by index.

Descriptor tables are stored in a *descriptor heap*. Descriptor heaps will ideally contain all the descriptors (in descriptor tables) for one or more frames to be rendered. All the resources will be stored in user mode heaps.

Another concept is that of a *root signature*. The root signature is a binding convention, defined by the application, that is used by shaders to locate the resources that they need access to. The root signature can store:

-   Indexes to descriptor tables in a descriptor heap, where the layout of the descriptor table has been pre-defined.
-   Constants, so apps can bind user-defined constants (known as *root constants*) directly to shaders without having to go through descriptors and descriptor tables.
-   A very small number of descriptors directly inside the root signature, such as a constant buffer view (CBV) that changes per draw, thereby saving the application from needing to put those descriptors in a descriptor heap.

In other words, the root signature provides performance optimizations suitable for small amounts of data that change per draw.

The Direct3D 12 design for binding separates it from other tasks, such as memory management, object lifetime management, state tracking, and memory synchronization (refer to [Differences in the Binding Model from Direct3D 11](binding-model.md)). Direct3D 12 binding is designed to be low overhead and optimized for the API calls that are made most frequently. It is also scalable across low end to high end hardware, and scalable from older (the more linear Direct3D 11 pipeline) to the newer (more parallel) approaches to graphics engine programming.

## Resource types and views

Resource types are the same as Direct3D 11, namely:

-   Texture1D, and Texture1DArray
-   Texture2D, and Texture2DArray, Texture2DMS, Texture2DMSArray
-   Texture3D
-   Buffers (typed, structured and raw)

Resource views are similar but slightly different from Direct3D 11, vertex and index buffer views have been added.

-   Constant buffer view (CBV)
-   Unordered access view (UAV)
-   Shader resource view (SRV)
-   Samplers
-   Render Target View (RTV)
-   Depth Stencil View (DSV)
-   Index Buffer View (IBV)
-   Vertex Buffer View (VBV)
-   Stream Output View (SOV)

Only the first four of these views are actually visible to shaders, refer to [Shader Visible Descriptor Heaps](shader-visible-descriptor-heaps.md) and [Non Shader Visible Descriptor Heaps](non-shader-visible-descriptor-heaps.md).

## Resource Binding Flow of Control

Focusing just on root signatures, root descriptors, root constants, descriptor tables, and descriptor heaps, the flow of rendering logic for an app should be similar to the following:

-   Create one or more root signature objects – one for every different binding configuration an application needs.
-   Create shaders and pipeline state with the root signature objects they will be used with.
-   Create one (or, if necessary, more) descriptor heaps that will contain all the SRV, UAV, and CBV descriptors for each frame of rendering.
-   Initialize the descriptor heap(s) with descriptors where possible for sets of descriptors that will be reused across many frames.
-   For each frame to be rendered:
    -   For each command list:
        -   Set the current root signature to use (and change if needed during rendering – which is rarely required).
        -   Update some root signature’s constants and/or root signature descriptors for the new view (such as world/view projections).
        -   For each item to draw:
            -   Define any new descriptors in descriptor heaps as needed for per-object rendering. For shader-visible descriptor heaps, the app must make sure to use descriptor heap space that isn’t already being referenced by rendering that could be in flight – for example, linearly allocating space through the descriptor heap during rendering.
            -   Update the root signature with pointers to the required regions of the descriptor heaps. For example, one descriptor table might point to some static (unchanging) descriptors initialized earlier, while another descriptor table might point to some dynamic descriptors configured for the current rendering.
            -   Update some root signature’s constants and/or root signature descriptors for per-item rendering.
            -   Set the pipeline state for the item to draw (only if change needed), compatible with the currently bound root signature.
            -   Draw
        -   Repeat (next item)
    -   Repeat (next command list)
    -   Strictly when the GPU has finished with any memory that will no longer be used, it can be released. Descriptors' references to it do not need to be deleted if additional rendering that uses those descriptors is not submitted. So, subsequent rendering can point to other areas in descriptor heaps, or stale descriptors can be overwritten with valid descriptors to reuse the descriptor heap space.
-   Repeat (next frame)

Note that other descriptor types, render target views (RTVs), depth stencil views (DSV), index buffer views (IBVs), vertex buffer views (VBVs), and shader object views (SOV), are managed differently. The driver handles the versioning of the set of descriptors bound for each draw during recording of the command list (similar to how the root signature bindings are versioned by the hardware/driver). This is different from the contents of shader-visible descriptor heaps, for which the application must manually allocate through the heap as it references different descriptors between draws. Versioning of heap content that is shader-visible is left to the application because it allows applications to do things like reuse descriptors that don’t change, or use large static sets of descriptors and use shader indexing (such as by material ID) to select descriptors to use from the descriptor heap, or use combinations of techniques for different sets of descriptors. The hardware isn’t equipped to handle this type of flexibility for the other descriptor types (RTV, DSV, IBV, VBV, SOV).

## Suballocation

In Direct3D 12, the app has low-level control over memory management. In earlier versions of Direct3D, including Direct3D 11, there would be one allocation per resource. In Direct3D 12, the app can use the API to allocate a large block of memory, larger than any single object would need. After this is done, the app can create descriptors to point to sections of that large memory block. This process of deciding what to put where (smaller blocks inside the large block) is known as *suballocation*. Enabling the app to do this can yield gains in efficient use of computation and memory. For example, resource renaming is rendered obsolete. In place of this, apps can use fences to determine when a particular resource is being used and when it's not by fencing on command list executions where the command list requires the use of that particular resource.

## Freeing Resources

Before any memory that has been bound to the pipeline can be freed, the GPU must be finished with it.

Waiting for frame rendering is probably the coarsest way to be certain that the GPU has finished. At a finer grain, you can again use fences—when a command is recorded into a command list that you want to track the completion of, insert a fence immediately after it. Then, you can do various synchronization operations with the fence. You submit new work (command lists) that waits until a specified fence has passed on the GPU, which indicates that everything before it is complete, or you can request that a CPU event be raised when the fence has passed (which the app can be waiting on with a sleeping thread). In Direct3D 11, this was `EnqueueSetEvent`().

## Related topics

<dl> <dt>

[Resource Binding](resource-binding.md)
</dt> </dl>

 

 




