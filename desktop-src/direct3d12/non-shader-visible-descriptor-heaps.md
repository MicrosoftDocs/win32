---
title: Non Shader Visible Descriptor Heaps
description: Some descriptor heaps cannot be referenced by shaders through descriptor tables, but exist either to assist the app in staging the descriptors prior to recording a command list or because no shader-visible heap is required.
ms.assetid: 85934873-8889-4564-A717-28A00614B38C
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Non Shader Visible Descriptor Heaps

Some descriptor heaps cannot be referenced by shaders through descriptor tables, but exist either to assist the app in staging the descriptors prior to recording a command list or because no shader-visible heap is required.

-   [Non-visible views](#non-visible-views)
-   [Summary](#summary)
-   [Related topics](#related-topics)

## Non-visible views

All descriptor heaps, including the shader accessible descriptor heaps described previously, can be manipulated by the CPU and/or command lists depending on the memory pool and CPU access properties the application selects for a descriptor heap.

For [Shader Visible Descriptor Heaps](shader-visible-descriptor-heaps.md), the obvious reason to deny shader access to these descriptor heaps is while they are being staged. Then these heaps are made shader-visible, and accessed via descriptor tables at command list execution. However, there is no requirement to stage shader-visible heaps, they can be populated directly.

Other descriptors get bound to the pipeline by having their contents recorded directly into the command list. These descriptors only serve to translate the view parameters at command list record time. These heaps are always non-shader visible and contain the following.

-   Render Target Views (RTVs)
-   Depth Stencil Views (DSVs)

Index Buffer Views (IBVs), Vertex Buffer Views (VBVs), and Stream Output Views (SOVs) are passed directly to API methods, are do not have specific heap types.

After recording into the command list (with a call such as [**OMSetRenderTargets**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetrendertargets), for example) the memory used to hold the descriptors for this call is immediately available for re-use after the call.

Even descriptor tables have options where an app can allow the implementation to choose to record the table contents at command list recording (rather than dereference the table pointer at execution).

## Summary



|                   | Shader visible, CPU write only                                   | Non-shader visible, CPU read/write                                       |
|-------------------|------------------------------------|----------------------------------------|
| **CBV, SRV, UAV** | yes                                | yes                                    |
| **SAMPLER**       | yes                                | yes                                    |
| **RTV**           | no                                 | yes                                    |
| **DSV**           | no                                 | yes                                    |



 

## Related topics

<dl> <dt>

[Descriptor Heaps](descriptor-heaps.md)
</dt> </dl>

 

 




