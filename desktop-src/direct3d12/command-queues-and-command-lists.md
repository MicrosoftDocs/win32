---
title: Work submission in Direct3D 12
description: To improve the CPU efficiency of Direct3D apps, Direct3D 12 no longer supports an immediate context associated with a device.
ms.assetid: BE2F46EA-D4A9-47F7-A2D1-6A486DD4DC1A
ms.topic: article
ms.date: 11/15/2018
---

# Work submission in Direct3D 12

To improve the CPU efficiency of Direct3D apps, as of version 12, Direct3D no longer supports an immediate context associated with a device. Instead, your application records and then submits *command lists*, which contain drawing and resource management calls. You can submit these command lists from multiple threads to one or more command queues, which manage the execution of the commands. This fundamental change increases single-threaded efficiency by allowing your application to pre-compute rendering work for later re-use, and it takes advantage of multi-core systems by spreading rendering work across multiple threads.

## In this section

| Topic | Description |
|-|-|
| [Design philosophy of command queues and command lists](design-philosophy-of-command-queues-and-command-lists.md) | The goals of enabling reuse of rendering work and of multi-threaded scaling, required fundamental changes to how Direct3D apps submit rendering work to the GPU. |
| [Creating and recording command lists and bundles](recording-command-lists-and-bundles.md) | This topic describes recording command lists and bundles in Direct3D 12 apps. Command lists and bundles both allow apps to record drawing or state-changing calls for later execution on the graphics processing unit (GPU). |
| [Executing and synchronizing command lists](executing-and-synchronizing-command-lists.md) | In Microsoft Direct3D 12, the immediate mode of previous versions is no longer present. Instead, apps create command lists and bundles and then record sets of GPU commands. Command queues are used to submit command lists to be executed. This model allows developers to have more control over the efficient usage of both GPU and CPU. |
| [Managing graphics pipeline state in Direct3D 12](managing-graphics-pipeline-state-in-direct3d-12.md) | This topic describes how graphics pipeline state is set in Direct3D 12. |
| [Using resource barriers to synchronize resource states in Direct3D 12](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md) | To reduce overall CPU usage and enable driver multi-threading and pre-processing, Direct3D 12 moves the responsibility of per-resource state management from the graphics driver to the application. |
| [Pipelines and shaders with Direct3D 12](pipelines-and-shaders-with-directx-12.md) | The Direct3D 12 programmable pipeline significantly increases rendering performance compared to previous generation graphics programming interfaces. |
| [Variable-rate shading (VRS)](vrs.md) | Variable-rate shading&mdash;or coarse pixel shading&mdash;is a mechanism that lets you allocate rendering performance/power at rates that vary across your rendered image. |
| [Render passes](direct3d-12-render-passes.md) | The render passes feature helps your renderer improve GPU efficiency by reducing memory traffic to/from off-chip memory; it does this by enabling your application to better identify resource rendering ordering requirements and data dependencies. |

## Related topics

* [Direct3D 12 programming guide](directx-12-programming-guide.md)
