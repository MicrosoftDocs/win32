---
title: Direct3D 12 programming guide
description: Direct3D 12 provides an API and platform that allows apps to take advantage of the graphics and computing capabilities of PCs equipped with one or more Direct3D 12-compatible GPUs.
ms.assetid: 16F78A6B-74C4-4ED1-809F-FE6DE157F368
ms.custom: 19H1
ms.topic: article
ms.date: 04/19/2019
---

# Direct3D 12 programming guide

Direct3D 12 provides an API and platform that allows apps to take advantage of the graphics and computing capabilities of PCs equipped with one or more Direct3D 12-compatible GPUs.

## In this section

| Topic | Description |
|-|-|
| [What is Direct3D 12?](what-is-directx-12-.md) | DirectX 12 introduces the next version of Direct3D, the 3D graphics API at the heart of DirectX. This version of Direct3D is faster and more efficient than any previous version. Direct3D 12 enables richer scenes, more objects, more complex effects, and full utilization of modern GPU hardware.  |
| [What's new in Direct3D 12](new-releases.md) | Describes the most significant new documentation available with the latest SDK release. |
| [Understanding Direct3D 12](directx-12-getting-started.md) | To write 3D games and apps for Windows 10 and Windows 10 Mobile, you must understand the basics of the Direct3D 12 technology, and how to prepare to use it in your games and apps. |
| [Work submission in Direct3D 12](command-queues-and-command-lists.md) | To improve the CPU efficiency of Direct3D apps, Direct3D 12 no longer supports an immediate context associated with a device. Instead, apps record and then submit *command lists*, which contain drawing and resource management calls. These command lists can be submitted from multiple threads to one or more command queues, which manage the execution of the commands. This fundamental change increases single-threaded efficiency by allowing apps to pre-compute rendering work for later re-use, and it takes advantage of multi-core systems by spreading rendering work across multiple threads.  |
| [Resource binding in Direct3D 12](resource-binding.md) | Binding is the process of linking resource objects to the shaders of the graphics pipeline.  |
| [Memory management in Direct3D 12](memory-management.md) | Moving to D3D12 involves doing proper synchronization and management of memory residency. Managing memory residency means even more synchronization must be done. This section covers memory management strategies, and suballocation within heaps and buffers.  |
| [Multi-adapter systems](multi-engine.md) | Describes support in Direct3D 12 for systems that have multiple adapters installed, covering scenarios where your application explicitly targets multiple GPU adapters, and scenarios where drivers implicitly use multiple GPU adapters on behalf of your application. |
| [Multi-engine synchronization](user-mode-heap-synchronization.md) | This topic discusses synchronizing access to the multiple independent engines found in most modern GPUs. |
| [Rendering](rendering.md) | This section contains information about rendering features new to Direct3D 12 (and Direct3D 11.3). |
| [Counters, queries and performance measurement](performance-measurement.md) | The following sections describe features for use in performance testing and improvement, such as queries, counters, timing, and predication. |
| [Working with Direct3D 11, Direct3D 10 and Direct2D](direct3d-12-interop.md) | This section covers interop techniques with earlier versions of Direct3D and Direct2D, the Direct3D 11on12 API, and porting guidelines from Direct3D 11 to Direct3D 12. |
| [Working samples](working-samples.md) | Working samples are available for download, showing the usage of a number of features of Direct3D 12. |
| [D3D12 code walk-throughs](d3d12-code-walk-throughs.md) | This section provides code for sample scenarios. Many of the walk-throughs provide details on what coding is required to be added to a basic sample, to avoid repeating the basic component code for each scenario. |
| [Debugging and diagnostics with Direct3D 12](understanding-the-d3d12-debug-layer.md) | Includes topics that describes how to make best use of the Direct3D 12 Debug Layer with GPU-based validation (GBV), and how to use Device Removed Extended Data (DRED). |

## Related topics

* [Direct3D 12 Graphics](direct3d-12-graphics.md)
* [Direct3D 12 Reference](direct3d-12-reference.md)
* [DirectX advanced learning video tutorials](https://www.youtube.com/channel/UCiaX2B8XiXR70jaN7NK-FpA)
