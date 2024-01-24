---
title: Important Changes from Direct3D 11 to Direct3D 12
description: Direct3D 12 represents a significant departure from the Direct3D 11 programming model. Direct3D 12 lets apps get closer to hardware than ever before.
ms.assetid: CE5066C9-7EA6-437D-9EB0-AACFB6CFAD9E
ms.topic: article
ms.date: 05/31/2018
---

# Important Changes from Direct3D 11 to Direct3D 12

Direct3D 12 represents a significant departure from the Direct3D 11 programming model. Direct3D 12 lets apps get closer to hardware than ever before. By being closer to hardware, Direct3D 12 is faster and more efficient. But, the trade-off of your app having increased speed and efficiency with Direct3D 12 is that you are responsible for more tasks than you were with Direct3D 11.

-   [Explicit Synchronization](#explicit-synchronization)
-   [Physical Memory Residency Management](#physical-memory-residency-management)
-   [Pipeline state objects](#pipeline-state-objects)
-   [Command lists and bundles](#command-lists-and-bundles)
-   [Descriptor heaps and tables](#descriptor-heaps-and-tables)
-   [Porting from Direct3D 11](#porting-from-direct3d-11)
-   [Related topics](#related-topics)

Direct3D 12 is a return to low-level programming; it gives you more control over the graphical elements of your games and apps by introducing these new features: objects to represent the overall state of the pipeline, command lists and bundles for work submission, and descriptor heaps and tables for resource access.

Your app has increased speed and efficiency with Direct3D 12, but you are responsible for more tasks than you were with Direct3D 11.

## Explicit Synchronization

-   In Direct3D 12, CPU-GPU synchronization is now the explicit responsibility of the app and is no longer implicitly performed by the runtime, as it is in Direct3D 11. This fact also means that no automatic checking for pipeline hazards is performed by Direct3D 12, so again this is the apps responsibility.
-   In Direct3D 12, apps are responsible for pipelining data updates. That is, the "Map/Lock-DISCARD" pattern in Direct3D 11 must be performed manually in Direct3D 12. In Direct3D 11, if the GPU is still using the buffer when you call [**ID3D11DeviceContext::Map**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-map) with [**D3D11\_MAP\_WRITE\_DISCARD**](/windows/desktop/api/d3d11/ne-d3d11-d3d11_map), the runtime returns a pointer to a new region of memory instead of the old buffer data. This allows the GPU to continue using the old data while the app places data in the new buffer. No additional memory management is required in the app; the old buffer is reused or destroyed automatically when the GPU is finished with it.
-   In Direct3D 12, all dynamic updates (including constant buffers, dynamic vertex buffers, dynamic textures, and so on) are explicitly controlled by the app. These dynamic updates include any required GPU fences or buffering. The app is responsible for keeping the memory available until it is no longer needed.
-   Direct3D 12 uses COM-style reference counting only for the lifetimes of interfaces (by using the weak reference model of Direct3D tied to the lifetime of the device). All resource and description memory lifetimes are the sole responsibly of the app to maintain for the proper duration, and are not reference counted. Direct3D 11 uses reference counting to manage the lifetimes of interface dependencies as well.

## Physical Memory Residency Management

A Direct3D 12 application must prevent race-conditions between multiple queues, multiple adapters, and the CPU threads. D3D12 no longer synchronizes the CPU and GPU, nor supports convenient mechanisms for resource renaming or multi-buffering. Fences must be used to avoid multiple processing units from over-writing memory before another processing unit finishes using it.

The Direct3D 12 application must ensure data is resident in memory while the GPU reads it. Memory used by each object is made resident during the creation of the object. Applications which call these methods must use fences to ensure the GPU doesn't access objects which have been evicted.

Resource barriers are another type of synchronization needed, used to synchronize resource and subresource transitions at a very granular level.

Refer to [Memory Management in Direct3D 12](memory-management.md).

## Pipeline state objects

Direct3D 11 allows pipeline state manipulation through a large set of independent objects. For example, input assembler state, pixel shader state, rasterizer state, and output merger state can all be independently modified. This design provides a convenient and relatively high-level representation of the graphics pipeline, but it doesn’t utilize the capabilities of modern hardware, primarily because the various states are often interdependent. For example, many GPUs combine pixel shader and output merger state into a single hardware representation. But because the Direct3D 11 API allows these pipeline stages to be set separately, the display driver can't resolve issues of pipeline state until the state is finalized, which isn’t until draw time. This scheme delays hardware state setup, which means extra overhead and fewer maximum draw calls per frame.

Direct3D 12 addresses this scheme by unifying much of the pipeline state into immutable pipeline state objects (PSOs), which are finalized upon creation. Hardware and drivers can then immediately convert the PSO into whatever hardware native instructions and state are required to execute GPU work. You can still dynamically change which PSO is in use, but to do so, the hardware only needs to copy the minimal amount of pre-computed state directly to the hardware registers, rather than computing the hardware state on the fly. By using PSOs, draw call overhead is reduced significantly, and many more draw calls can occur per frame. For more information about PSOs, see [Managing graphics pipeline state in Direct3D 12](managing-graphics-pipeline-state-in-direct3d-12.md).

## Command lists and bundles

In Direct3D 11, all work submission is done via the [immediate context](/windows/desktop/direct3d11/overviews-direct3d-11-render-multi-thread-render), which represents a single stream of commands that go to the GPU. To achieve multithreaded scaling, games also have [deferred contexts](/windows/desktop/direct3d11/overviews-direct3d-11-render-multi-thread-render) available to them. Deferred contexts in Direct3D 11 don't map perfectly to hardware, so relatively little work can be done in them.

Direct3D 12 introduces a new model for work submission based on command lists that contain the entirety of information needed to execute a particular workload on the GPU. Each new command list contains information such as which PSO to use, what texture and buffer resources are needed, and the arguments to all draw calls. Because each command list is self-contained and inherits no state, the driver can pre-compute all necessary GPU commands up-front and in a free-threaded manner. The only serial process necessary is the final submission of command lists to the GPU via the command queue.

In addition to command lists, Direct3D 12 also introduces a second level of work pre-computation: *bundles*. Unlike command lists, which are completely self-contained and are typically constructed, submitted once, and discarded, bundles provide a form of state inheritance that permits reuse. For example, if a game wants to draw two character models with different textures, one approach is to record a command list with two sets of identical draw calls. But another approach is to "record" one bundle that draws a single character model, then "play back" the bundle twice on the command list using different resources. In the latter case, the display driver only has to compute the appropriate instructions once, and creating the command list essentially amounts to two low-cost function calls.

For more information about command lists and bundles, see [Work Submission in Direct3D 12](command-queues-and-command-lists.md).

## Descriptor heaps and tables

Resource binding in Direct3D 11 is highly abstracted and convenient, but leaves many modern hardware capabilities underutilized. In Direct3D 11, games create *view* objects of resources, then bind those views to several *slots* at various shader stages in the pipeline. Shaders, in turn, read data from those explicit bind slots, which are fixed at draw time. This model means that whenever a game will draw using different resources, it must re-bind different views to different slots, and call draw again. This case also represents overhead that can be eliminated by fully utilizing modern hardware capabilities.

Direct3D 12 changes the binding model to match modern hardware and significantly improves performance. Instead of requiring standalone resource views and explicit mapping to slots, Direct3D 12 provides a descriptor heap into which games create their various resource views. This scheme provides a mechanism for the GPU to directly write the hardware-native resource description (descriptor) to memory up-front. To declare which resources are to be used by the pipeline for a particular draw call, games specify one or more descriptor tables that represent sub-ranges of the full descriptor heap. As the descriptor heap has already been populated with the appropriate hardware-specific descriptor data, changing descriptor tables is an extremely low-cost operation.

In addition to the improved performance offered by descriptor heaps and tables, Direct3D 12 also allows resources to be dynamically indexed in shaders, which provides unprecedented flexibility and unlocks new rendering techniques. As an example, modern deferred rendering engines typically encode a material or object identifier of some kind to the intermediate g-buffer. In Direct3D 11, these engines must be careful to avoid using too many materials, as including too many in one g-buffer can significantly slow down the final render pass. With dynamically indexable resources, a scene with a thousand materials can be finalized just as quickly as one with only ten.

For more information about descriptor heaps and tables, see [Resource Binding](resource-binding.md), and [Differences in the Binding Model from Direct3D 11](binding-model.md).

## Porting from Direct3D 11

Porting from Direct3D 11 is an involved process, described in [Porting from Direct3D 11 to Direct3D 12](porting-from-direct3d-11-to-direct3d-12.md). Also refer to the range of options in [Working with Direct3D 11, Direct3D 10 and Direct2D](direct3d-12-interop.md).

## Related topics

<dl> <dt>

[Understanding Direct3D 12](directx-12-getting-started.md)
</dt> </dl>

 

 
