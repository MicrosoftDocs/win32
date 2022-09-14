---
title: What is Direct3D 12
description: DirectX 12 introduces the next version of Direct3D; the 3D graphics API at the heart of DirectX.
ms.assetid: 09C586BF-11CE-4392-9BFD-A40B05DD0624
ms.topic: article
ms.date: 11/19/2018
---

# What is Direct3D 12?

DirectX 12 introduces the next version of Direct3D&mdash;the 3D graphics API at the heart of DirectX. Direct3D 12 is faster and more efficient than any previous version. Direct3D 12 enables richer scenes, more objects, more complex effects, and full utilization of modern GPU hardware.

## How can Direct3D 12 be so much faster and more efficient?

Direct3D 12 is unique in that it provides a lower level of hardware abstraction than previous versions do, which allows you to significantly improve the multi-core CPU scaling of your title (or other application). For one thing, with Direct3D 12, your title is responsible for its own [memory management](memory-management.md). In addition, by using Direct3D 12, your titles and applications benefit from reduced GPU overhead via features such as [command queues and lists](command-queues-and-command-lists.md), [descriptor tables](descriptor-tables.md), and concise [pipeline state objects](managing-graphics-pipeline-state-in-direct3d-12.md).

Direct3D 12, and Direct3D 11.3, introduce a set of new features for the rendering pipeline.

- [Conservative rasterization](../direct3d11/conservative-rasterization.md) to enable reliable hit detection.
- [Volume tiled resources](../direct3d11/volume-tiled-resources.md) to enable streamed three-dimensional resources to be treated as if they were all in video memory.
- [Rasterizer-ordered views](../direct3d11/rasterizer-order-views.md) to enable reliable transparency rendering.
- Setting the stencil reference within a shader to enable special shadowing and other effects.
- Improved texture mapping and typed unordered access view (UAV) loads.

## How deeply should I invest in Direct3D 12?

Direct3D 12 provides four main benefits to graphics developers (compared with Direct3D 11).

- Vastly reduced CPU overhead.
- Significantly reduced power consumption.
- Up to (approximately) 20% improvement in GPU efficiency.
- Cross-platform development for a Windows 10 device (PC, tablet, console, mobile).

Direct3D 12 is designed for advanced graphics programmers to use. It calls for significant graphics expertise, and a high level of fine-tuning. Direct3D 12 is designed to make full use of multi-threading, careful CPU/GPU synchronization, and the transition and re-use of resources from one purpose to another. These are techniques that require a considerable amount of memory-level programming skill.

Another advantage that Direct3D 12 has is its small API footprint. There are around 200 functions; and about one third of those do all the heavy lifting. That means that you, as a graphics developer, should be able to educate yourselves about&mdash;and master&mdash;the full API set without having to memorize too many API names.

Direct3D 11 continues to be a viable option alongside Direct3D 12. Many of the new rendering features of Direct3D 12 are available in [Direct3D 11.3](../direct3d11/direct3d-11-3-features.md). Direct3D 11.3 is a low-level graphics engine API; and Direct3D 12 goes even deeper.

There are at least two ways that your development team can approach a Direct3D 12 title.

### Use Direct3D 12 exclusively

For a project that takes ultimate advantage of all of the benefits of Direct3D 12, you should develop a highly customized Direct3D 12 engine from the ground up.

If you, as a graphics developer, understand the use and re-use of resources within your titles, and you can take advantage of that by minimizing uploading and copying, then you can develop and customize a highly efficient engine for those titles. The performance improvements could be very considerable, freeing up CPU time to increase the number of draw calls, and so adding more luster to your graphics.

The programming investment is significant, and you should consider debugging and instrumentation of the project from the very start. Threading, synchronization, and other timing bugs can be challenging.

### Use Direct3D 12 in concert with Direct3D 11

A shorter-term approach would be to address known bottlenecks in your Direct3D 11 title. You can address those by using [Direct3D 12 interop and/or D3D11On12](direct3d-12-interop.md) techniques, which enable the two API versions to work together. This approach minimizes the changes necessary to an existing Direct3D 11 graphics engine. However, the performance gains will be limited to the relief of the bottleneck that the Direct3D 12 code addresses.

## Microsoft DirectX 12 (and graphics education) videos

[Enhanced education for graphics developers](https://www.youtube.com/channel/UCiaX2B8XiXR70jaN7NK-FpA). These videos cover topics such as presentation modes, porting to DirectX 12, conservative rasterization, graphics tools, Angle, Win2D, and events such as GDC, Build, and more. Technical DirectX 12 content is prefaced with *DirectX 12*. Come here to learn tips and tricks directly from the Direct3D 12 feature team. We want to help you to use our latest releases and tools to make your game the best it can be!

## Conclusion

Direct3D 12 is all about dramatic graphics engine performance. Ease of development, high level constructs, and compiler support have been scaled back to enable this. Driver support and ease of debugging remain on a par with Direct3D 11.

Direct3D 12 is new territory. Territory that's waiting for the inquisitive expert to come and explore.
