---
title: What is Direct3D 12
description: DirectX 12 introduces the next version of Direct3D, the 3D graphics API at the heart of DirectX.
ms.assetid: 09C586BF-11CE-4392-9BFD-A40B05DD0624
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What is Direct3D 12?

DirectX 12 introduces the next version of Direct3D, the 3D graphics API at the heart of DirectX. This version of Direct3D is faster and more efficient than any previous version. Direct3D 12 enables richer scenes, more objects, more complex effects, and full utilization of modern GPU hardware.

## What makes Direct3D 12 better?

Direct3D 12 provides a lower level of hardware abstraction than ever before, which allows developers to significantly improve the multi-thread scaling and CPU utilization of their titles. With Direct3D 12, titles are responsible for their [memory management](memory-management.md). In addition, by using Direct3D 12, games and titles benefit from reduced GPU overhead via features such as [command queues and lists](command-queues-and-command-lists.md), [descriptor tables](descriptor-tables.md), and concise [pipeline state objects](managing-graphics-pipeline-state-in-direct3d-12.md).

Direct3D 12, and Direct3D 11.3, introduce a set of new features for the rendering pipeline: conservative rasterization to enable reliable hit detection, volume-tiled resources to enable streamed three dimension resources to be treated as if they were all in video memory, rasterizer ordered views to enable reliable transparency rendering, setting the stencil reference within a shader to enable special shadowing and other effects, and also improved texture mapping and typed Unordered Access View (UAV) loads.

## Who is Direct3D 12 for?

Direct3D 12 provides four main benefits to graphics developers (compared with Direct3D 11): vastly reduced CPU overhead, significantly improved power consumption, up to around twenty percent improvement in GPU efficiency, and cross-platform development for a Windows 10 device (PC, tablet, console or phone).

Direct3D 12 is certainly for advanced graphics programmers, it requires a fine level of tuning and significant graphics expertise. Direct3D 12 is designed to make full use of multi-threading, careful CPU/GPU synchronization, and the transition and re-use of resources from one purpose to another. All techniques that require a considerable amount of memory level programming skill.

Another advantage that Direct3D 12 has is its small API footprint. There are around 200 methods, and about one third of these do all the heavy lifting. This means that a graphics developer should be able to educate themselves on - and master - the full API set without the weight of having to memorize a great volume of API calls.

Direct3D 12 does not replace Direct3D 11. The new rendering features of Direct3D 12 are available in Direct3D 11.3. Direct3D 11.3 is a low level graphics engine API, and Direct3D 12 goes even deeper.

There are at least two ways a development team can approach a Direct3D 12 title.

For a project that takes full advantage of the benefits of Direct3D 12, a highly customized Direct3D 12 game engine should be developed from the ground up.

One approach is that if graphics developers understand the use and re-use of resources within their titles, and can take advantage of this by minimizing uploading and copying, then a highly efficient engine can be developed and customized for these titles. The performance improvements could be very considerable, freeing up CPU time to increase the number of draw calls, and so adding more luster to graphics rendering.

The programming investment is significant, and debugging and instrumentation of the project should be considered from the very start: threading, synchronization and other timing bugs can be challenging.

A shorter term approach would be to address known bottlenecks in a Direct3D 11 title; these can be addressed by using the 11on12 or interop techniques enabling the two APIs to work together. This approach minimizes the changes necessary to an existing Direct3D 11 graphics engine, however the performance gains will be limited to the relief of the bottleneck that the Direct3D 12 code addresses.

Direct3D 12 is all about dramatic graphics engine performance: ease of development, high level constructs, and compiler support have been scaled back to enable this. Driver support and ease of debugging remain on a par with Direct3D 11.

Direct3D 12 is new territory, for the inquisitive expert to explore.

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[DirectX advanced learning video tutorials](https://www.youtube.com/channel/UCiaX2B8XiXR70jaN7NK-FpA)
</dt> </dl>

 

 




