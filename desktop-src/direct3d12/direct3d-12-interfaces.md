---
title: Core Interfaces
description: The following interfaces are declared in d3d12.h.
ms.assetid: 'A9BD5910-8FF2-4540-BB8E-E8EA5C10528C'
---

# Core Interfaces

The following interfaces are declared in d3d12.h.

## In this section



| Topic                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D12CommandAllocator**](id3d12commandallocator.md)<br/>                                     | Represents the allocations of storage for graphics processing unit (GPU) commands.<br/>                                                                                                                                                                                                                                                                            |
| [**ID3D12CommandList**](id3d12commandlist.md)<br/>                                               | An interface from which [**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md) inherits from. It represents an ordered set of commands that the GPU executes, while allowing for extension to support other command lists than just those for graphics (such as compute and copy).<br/>                                                                    |
| [**ID3D12CommandQueue**](id3d12commandqueue.md)<br/>                                             | Provides methods for submitting command lists, synchronizing command list execution, instrumenting the command queue, and updating resource tile mappings.<br/>                                                                                                                                                                                                    |
| [**ID3D12CommandSignature**](id3d12commandsignature.md)<br/>                                     | A command signature object enables apps to specify indirect drawing, including the buffer format, command type and resource bindings to be used.<br/>                                                                                                                                                                                                              |
| [**ID3D12DescriptorHeap**](id3d12descriptorheap.md)<br/>                                         | A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor. Descriptor heaps contain many object types that are not part of a Pipeline State Object (PSO), such as Shader Resource Views (SRVs), Unordered Access Views (UAVs), Constant Buffer Views (CBVs), and Samplers.<br/>                              |
| [**ID3D12Device**](id3d12device.md)<br/>                                                         | Represents a virtual adapter; it is used to create command allocators, command lists, command queues, fences, resources, pipeline state objects, heaps, root signatures, samplers, and many resource views.<br/>                                                                                                                                                   |
| [**ID3D12Device1**](id3d12device1.md)<br/>                                                       | Represents a virtual adapter, and expands on the range of methods provided by [**ID3D12Device**](id3d12device.md).<br/>                                                                                                                                                                                                                                           |
| [**ID3D12Device2**](id3d12device2.md)<br/>                                                       | Represents a virtual adapter. This interface extends [**ID3D12Device1**](id3d12device1.md) to create pipeline state objects from pipeline state stream descriptions.<br/>                                                                                                                                                                                         |
| [**ID3D12Device3**](id3d12device3.md)<br/>                                                       | Represents a virtual adapter. This interface extends [**Id3d12device2**](id3d12device2.md) to support the creation of special-purpose diagnostic heaps in system memory that persist even in the event of a GPU-fault or device-removed scenario.<br/>                                                                                                            |
| [**ID3D12DeviceChild**](id3d12devicechild.md)<br/>                                               | An interface from which other core interfaces inherit from, including [**ID3D12PipelineLibrary**](id3d12pipelinelibrary.md), [**ID3D12CommandList**](id3d12commandlist.md), [**ID3D12Pageable**](id3d12pageable.md), and [**ID3D12RootSignature**](id3d12rootsignature.md). It provides a method to get back to the device object it was created against.<br/> |
| [**ID3D12Fence**](id3d12fence.md)<br/>                                                           | Represents a fence, an object used for synchronization of the CPU and one or more GPUs. <br/>                                                                                                                                                                                                                                                                      |
| [**ID3D12Fence1**](id3d12fence1.md)<br/>                                                         | Represents a fence. This interface extends [**ID3D12Fence**](id3d12fence.md), and supports the retrieval of the flags used to create the original fence. <br/>                                                                                                                                                                                                    |
| [**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md)<br/>                               | Encapsulates a list of graphics commands for rendering. Includes APIs for instrumenting the command list execution, and for setting and clearing the pipeline state.<br/>                                                                                                                                                                                          |
| [**ID3D12GraphicsCommandList1**](id3d12graphicscommandlist1.md)<br/>                             | Encapsulates a list of graphics commands for rendering, extending the inteface to support programmable sample positions, atomic copies for implementing late-latch techniques, and optional depth-bounds testing.<br/>                                                                                                                                             |
| [**ID3D12GraphicsCommandList2**](id3d12graphicscommandlist2.md)<br/>                             | Encapsulates a list of graphics commands for rendering, extending the interface to support writing immediate values directly to a buffer.<br/>                                                                                                                                                                                                                     |
| [**ID3D12Heap**](id3d12heap.md)<br/>                                                             | A heap is an abstraction of contiguous memory allocation, used to manage physical memory. This heap can be used with [**ID3D12Resource**](id3d12resource.md) objects to support placed resources or reserved resources.<br/>                                                                                                                                      |
| [**ID3D12Object**](id3d12object.md)<br/>                                                         | An interface from which [**ID3D12Device**](id3d12device.md) and [**ID3D12DeviceChild**](id3d12devicechild.md) inherit from. It provides methods to associate private data and annotate object names.<br/>                                                                                                                                                        |
| [**ID3D12Pageable**](id3d12pageable.md)<br/>                                                     | An interface from which many other core interfaces inherit from. It indicates that the object type encapsulates some amount of GPU-accessible memory; but does not strongly indicate whether the application can manipulate the object's residency. <br/>                                                                                                          |
| [**ID3D12PipelineLibrary**](id3d12pipelinelibrary.md)<br/>                                       | Manages a pipeline library, in particular loading and retrieving individual PSOs.<br/>                                                                                                                                                                                                                                                                             |
| [**ID3D12PipelineLibrary1**](id3d12pipelinelibrary1.md)<br/>                                     | Manages a pipeline library. This interface extends [**ID3D12PipelineLibrary**](id3d12pipelinelibrary.md) to load PSOs from a pipeline state stream description.<br/>                                                                                                                                                                                              |
| [**ID3D12PipelineState**](id3d12pipelinestate.md)<br/>                                           | Represents the state of all currently set shaders as well as certain fixed function state objects.<br/>                                                                                                                                                                                                                                                            |
| [**ID3D12QueryHeap**](id3d12queryheap.md)<br/>                                                   | Manages a query heap. A query heap holds an array of queries, referenced by indexes.<br/>                                                                                                                                                                                                                                                                          |
| [**ID3D12Resource**](id3d12resource.md)<br/>                                                     | Encapsulates a generalized ability of the CPU and GPU to read and write to physical memory, or heaps. It contains abstractions for organizing and manipulating simple arrays of data as well as multidimensional data optimized for shader sampling.<br/>                                                                                                          |
| [**ID3D12RootSignature**](id3d12rootsignature.md)<br/>                                           | The root signature defines what resources are bound to the graphics pipeline. A root signature is configured by the app and links command lists to the resources the shaders require. Currently, there is one graphics and one compute root signature per app.<br/>                                                                                                |
| [**ID3D12RootSignatureDeserializer**](id3d12rootsignaturedeserializer.md)<br/>                   | Contains a method to return the deserialized [**D3D12\_ROOT\_SIGNATURE\_DESC**](d3d12-root-signature-desc.md) data structure, of a serialized root signature version 1.0. <br/>                                                                                                                                                                                   |
| [**ID3D12Tools**](id3d12tools.md)<br/>                                                           | This interface is used to configure the runtime for tools such as PIX. Its not intended or supported for any other scenario.<br/>                                                                                                                                                                                                                                  |
| [**ID3D12VersionedRootSignatureDeserializer**](id3d12versionedrootsignaturedeserializer.md)<br/> | Contains methods to return the deserialized [**D3D12\_ROOT\_SIGNATURE\_DESC1**](d3d12-root-signature-desc1.md) data structure, of any version of a serialized root signature. <br/>                                                                                                                                                                               |



 

## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> <dt>

[Interface Hierarchy](interface-hierarchy.md)
</dt> </dl>

 

 





