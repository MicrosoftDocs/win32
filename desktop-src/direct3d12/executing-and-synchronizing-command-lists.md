---
title: Executing and Synchronizing Command Lists
description: In Microsoft Direct3D 12, the immediate mode of previous versions is no longer present.
ms.assetid: D5013102-2302-4D66-8F59-079C03BA65FD
keywords:
- command list
- synchronization
- execution
ms.topic: article
ms.date: 05/31/2018
---

# Executing and Synchronizing Command Lists

In Microsoft Direct3D 12, the immediate mode of previous versions is no longer present. Instead, apps create command lists and bundles and then record sets of GPU commands. Command queues are used to submit command lists to be executed. This model allows developers to have more control over the efficient usage of both graphics processing unit (GPU) and CPU.

-   [Command queue overview](#command-queue-overview)
-   [Initializing a command queue](#initializing-a-command-queue)
-   [Executing command Lists](#executing-command-lists)
-   [Accessing resources from multiple command queues](#accessing-resources-from-multiple-command-queues)
-   [Synchronizing command list execution using command queue fences](#synchronizing-command-list-execution-using-command-queue-fences)
-   [Synchronizing resources accessed by command queues](#synchronizing-resources-accessed-by-command-queues)
-   [Command queue support for tiled resources](#command-queue-support-for-tiled-resources)
-   [Related topics](#related-topics)

## Command queue overview

Direct3D 12 command queues replace runtime and driver synchronization of immediate mode work submission, previously not-exposed to the developer, with APIs for explicitly managing concurrency, parallelism and synchronization. Command queues provide the following improvements for developers:

-   Allows developers to avoid accidental inefficiencies caused by unexpected synchronization.
-   Allows developers to introduce synchronization at a higher level where the required synchronization can be determined more efficiently and accurately. This means the runtime and the graphics driver will spend less time reactively engineering parallelism.
-   Makes expensive operations more explicit.

These improvements enable or enhance the following scenarios:

-   Increased parallelism - Applications can use deeper queues for background workloads, such as video decoding, when they have separate queues for foreground work.
-   Asynchronous and low-priority GPU work - The command queue model enables concurrent execution of low-priority GPU work and atomic operations that enable one GPU thread to consume the results of another unsynchronized thread without blocking.
-   High-priority compute work - This design enables scenarios that require interrupting 3D rendering to do a small amount of high-priority compute work so that the result can be obtained early for additional processing on the CPU.

## Initializing a command queue

Command queues can be created by calling [**ID3D12Device::CreateCommandQueue**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcommandqueue). This method takes a [**D3D12\_COMMAND\_LIST\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_command_list_type) indicating what type of queue should be created, and therefore, what type of commands can be submitted to that queue. Remember that bundles can only be called from direct command lists and can't be submitted directly to a queue. The supported queue types are:

-   [**D3D12\_COMMAND\_LIST\_TYPE\_DIRECT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_command_list_type)
-   [**D3D12\_COMMAND\_LIST\_TYPE\_COMPUTE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_command_list_type)
-   [**D3D12\_COMMAND\_LIST\_TYPE\_COPY**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_command_list_type)

In general, DIRECT queues and command lists accept any command, COMPUTE queues and command lists accept compute and copy related commands, and COPY queues and command lists accept only copy commands.

## Executing command Lists

After you have recorded a command list and either retrieved the default command queue or created a new one, you execute command lists by calling [**ID3D12CommandQueue::ExecuteCommandLists**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists).

Applications can submit command lists to any command queue from multiple threads. The runtime will perform the work of serializing these requests in the order of submission.

The runtime will validate the submitted command list and will drop the call to [**ExecuteCommandLists**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists) if any of the restrictions are violated. Calls will be dropped for the following reasons:

-   The supplied command list is a bundle, not a direct command list.
-   [**ID3D12GraphicsCommandList::Close**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-close) has not been called on the supplied command list to complete recording.
-   [**ID3D12CommandAllocator::Reset**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandallocator-reset) has been called on the command allocator associated with the command list since it was recorded. For more information about command allocators, see [Creating and recording command lists and bundles](recording-command-lists-and-bundles.md).
-   The command queue fence indicates that a previous execution of the command list has not yet completed. Command queue fences are discussed in detail below.
-   The before and after states of queries, set with calls to [**ID3D12GraphicsCommandList::BeginQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery) and [**ID3D12GraphicsCommandList::EndQuery**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery), are not matched properly.
-   The before and after states of resource transition barriers are not matched properly. For more information, see [Using resource barriers to synchronize resource states](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md).

## Accessing resources from multiple command queues

There are a couple of rules imposed by the runtime that restrict the access of resources from multiple command queues. These rules are as follows:

1. A resource cannot be written to from multiple command queues simultaneously. When a resource has transitioned to a writeable state on a queue, it is considered exclusively owned by that queue, and must transition to a read or COMMON state (refer to [**D3D12_RESOURCE_STATES**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_states)) before it can be accessed by another queue.

2. When in a read state, a resource can be read from multiple command queues simultaneously, including across processes, based on its read state.

For more information about resource access restrictions and using resource barriers to synchronize access to resources, see [Using resource barriers to synchronize resource states](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md).

## Synchronizing command list execution using command queue fences

The support for multiple parallel command queues in Direct3D 12 gives you more flexibility and control over the prioritization of asynchronous work on the GPU. This design also means that apps need to explicitly manage the synchronization of work, especially when the command lists in one queue depend on resources that are being operated on by another command queue. Some examples of this include waiting for an operation on a compute queue to complete so that the result can be used for a rendering operation on the 3D queue, and waiting for a 3D operation to complete so that an operation on the compute queue can access a resource for writing. To enable the synchronization of work between queues, Direct3D 12 uses the concept of fences, which are represented in the API by the [**ID3D12Fence**](/windows/desktop/api/d3d12/nn-d3d12-id3d12fence) interface.

A fence is an integer that represents the current unit of work being processed. When the app advances the fence, by calling [**ID3D12CommandQueue::Signal**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-signal), the integer is updated. Apps can check the value of a fence and determine if a unit of work has been completed in order to decide whether a subsequent operation can be started.

## Synchronizing resources accessed by command queues

In Direct3D 12, synchronizing the state of some resources is implemented with resource barriers. At each resource barrier, an app declares the before and after states of a resource. A common example is for a resource to transition between a shader resource view to a render target view. For the most part, these resource barriers are managed within command lists. When the debug layers are enabled, the system enforces that the before and after states of all resources match up, guaranteeing that the resource is in the correct state for a particular operation at a barrier transition.

For more information about synchronizing resource state, see [Using resource barriers to synchronize resource states](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md).

## Command queue support for tiled resources

Methods for managing tiled resources, which were exposed through the [**ID3D11DeviceContext2**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2) interface in Direct3D 11, are provided by the [**ID3D12CommandQueue**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandqueue) interface in Direct3D 12. These methods include:



| Method                                                              | Description                                                                                              |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**CopyTileMappings**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-copytilemappings)     | Copies mappings from a source tiled resource to a destination tiled resource.<br/>                 |
| [**UpdateTileMappings**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-updatetilemappings) | Updates mappings of tile locations in tiled resources to memory locations in a resource heap.<br/> |



 

For more information about using tiled resources in Direct3D 12 apps, refer to [Direct3D11 Tiled Resources](/windows/desktop/direct3d11/tiled-resources).

## Related topics

<dl> <dt>

[Work Submission in Direct3D 12](command-queues-and-command-lists.md)
</dt> </dl>

 

