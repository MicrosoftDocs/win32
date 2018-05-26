---
title: Multi-Engine and Multi-Adapter Synchronization
description: Provides an overview and lists APIs relevant to multi-engine (the 3D, compute, and copy engines), and multi-adapter.
ms.assetid: D81BE0E6-D7A4-4EB4-8267-2C97E4216A9D
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multi-Engine and Multi-Adapter Synchronization

Provides an overview and lists APIs relevant to multi-engine (the 3D, compute, and copy engines), and multi-adapter.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Synchronization and Multi-Engine](user-mode-heap-synchronization.md)<br/> | Most modern GPUs contain multiple independent engines that provide specialized functionality. Many have one or more dedicated copy engines, and a compute engine, usually distinct from the 3D engine. Each of these engines can execute commands in parallel with each other. Direct3D 12 provides granular access to the 3D, compute and copy engines, using queues and command lists.<br/> |
| [Multi-Adapter](mulit-engine.md)<br/>                                      | Describes support in D3D12 for multi-engine adapter systems, covering scenarios where applications explicitly target multiple GPU adapters, and scenarios where drivers implicitly use multiple GPU adapters on behalf of an application.<br/>                                                                                                                                                |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[Memory Management](memory-management.md)
</dt> </dl>

 

 





