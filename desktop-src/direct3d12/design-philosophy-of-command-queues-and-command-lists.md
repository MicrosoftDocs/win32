---
title: Design Philosophy of Command Queues and Command Lists
description: The goals of enabling reuse of rendering work and of multi-threaded scaling, required fundamental changes to how Direct3D apps submit rendering work to the GPU.
ms.assetid: C85C8C41-2306-4568-8FAE-F57EDA624298
keywords:
- command list
- bundle
ms.topic: article
ms.date: 05/31/2018
---

# Design Philosophy of Command Queues and Command Lists

The goals of enabling reuse of rendering work and of multi-threaded scaling, required fundamental changes to how Direct3D apps submit rendering work to the GPU. In Direct3D 12, the process of submitting rendering work differs from earlier versions in three important ways:

<dl> 1. Elimination of the immediate context. This enables multi-threading.  
2. Apps now own how rendering calls are grouped into graphics processing unit (GPU) work items. This enables re-use.  
3. Apps now explicitly control when work is submitted to the GPU . This enables items 1 and 2.  
</dl>

-   [Removal of the immediate context](#removal-of-the-immediate-context)
-   [Grouping of GPU work items](#grouping-of-gpu-work-items)
-   [GPU work submission](#gpu-work-submission)
-   [Related topics](#related-topics)

## Removal of the immediate context

The largest change from Microsoft Direct3D 11 to Microsoft Direct3D 12 is that there is no longer a single, immediate context associated with a device. Instead, to render, apps create command lists in which traditional rendering APIs can be called. A command list looks similar to the render method of a Direct3D 11 app that used the immediate context in that it contains calls that draw primitives or change the rendering state. Like immediate contexts, each command list is not free-threaded; however, multiple command lists can be recorded concurrently, which takes advantage of modern, multi-core processors.

Command lists are typically executed once. However, a command list can be executed multiple times if the application ensures that the previous executions are complete before submitting new executions. For more information about command list synchronization, see [Executing and synchronizing command lists](executing-and-synchronizing-command-lists.md).

## Grouping of GPU work items

In addition to command lists, Direct3D 12 takes advantage of functionality present in all hardware today by adding a second level of command lists, which are called *bundles*. To help to distinguish these two types, the first-level command lists can be referred to as *direct command lists*. The purpose of bundles is to allow apps to group a small number of API commands together for later, repeated execution from within direct command lists. At the time of creating a bundle, the driver will perform as much pre-processing as possible to make later execution efficient. Bundles can then be executed from within multiple command lists and multiple times within the same command list.

The re-use of bundles is a large driver of improved efficiency with single CPU threads. Because bundles are pre-processed and can be submitted multiple times, there are certain restrictions on what operations can be performed within a bundle. For more information, see [Creating and recording command lists and bundles](recording-command-lists-and-bundles.md).

## GPU work submission

To execute work on the GPU, an app must explicitly submit a command list to a command queue associated with the Direct3D device. A direct command list can be submitted for execution multiple times, but the app is responsible for ensuring that the direct command list has finished executing on the GPU before submitting it again. Bundles have no concurrent-use restrictions and can be executed multiple times in multiple command lists, but bundles cannot be directly submitted to a command queue for execution.

Any thread may submit a command list to any command queue at any time, and the runtime will automatically serialize submission of the command list in the command queue while preserving the submission order.

## Related topics

<dl> <dt>

[Work Submission in Direct3D 12](command-queues-and-command-lists.md)
</dt> </dl>

 

 




