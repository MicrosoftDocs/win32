---
title: Core interfaces
description: The following interfaces are declared in d3d12.h.
ms.assetid: A9BD5910-8FF2-4540-BB8E-E8EA5C10528C
ms.topic: article
ms.date: 11/27/2018
---

# Core interfaces

The following interfaces are declared in d3d12.h.

## In this section

| Topic | Description |
|-|-|
| [**ID3D12CommandAllocator**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandallocator) | Represents the allocations of storage for graphics processing unit (GPU) commands. |
| [**ID3D12CommandList**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandlist) | An interface from which [**ID3D12GraphicsCommandList**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist) inherits from. It represents an ordered set of commands that the GPU executes, while allowing for extension to support other command lists than just those for graphics (such as compute and copy). |
| [**ID3D12CommandQueue**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandqueue) | Provides methods for submitting command lists, synchronizing command list execution, instrumenting the command queue, and updating resource tile mappings. |
| [**ID3D12CommandSignature**](https://msdn.microsoft.com/en-us/library/Dn891446(v=VS.85).aspx) | A command signature object enables apps to specify indirect drawing, including the buffer format, command type and resource bindings to be used. |
| [**ID3D12DescriptorHeap**](/windows/desktop/api/d3d12/nn-d3d12-id3d12descriptorheap) | A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor. Descriptor heaps contain many object types that are not part of a Pipeline State Object (PSO), such as Shader Resource Views (SRVs), Unordered Access Views (UAVs), Constant Buffer Views (CBVs), and Samplers. |
| [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device) | Represents a virtual adapter; it is used to create command allocators, command lists, command queues, fences, resources, pipeline state objects, heaps, root signatures, samplers, and many resource views. |
| [**ID3D12Device1**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device1) | Represents a virtual adapter, and expands on the range of methods provided by [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device). |
| [**ID3D12Device2**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device2) | Represents a virtual adapter. This interface extends [**ID3D12Device1**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device1) to create pipeline state objects from pipeline state stream descriptions. |
| [**ID3D12Device3**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device3) | Represents a virtual adapter. This interface extends [**Id3d12device2**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device2) to support the creation of special-purpose diagnostic heaps in system memory that persist even in the event of a GPU-fault or device-removed scenario. |
| [**ID3D12Device5**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device5) | Represents a virtual adapter. This interface extends **Id3d12device4**. |
| [**ID3D12DeviceChild**](/windows/desktop/api/d3d12/nn-d3d12-id3d12devicechild) | An interface from which other core interfaces inherit from, including [**ID3D12PipelineLibrary**](/windows/desktop/api/d3d12/nn-d3d12-id3d12pipelinelibrary), [**ID3D12CommandList**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandlist), [**ID3D12Pageable**](https://msdn.microsoft.com/en-us/library/Dn788704(v=VS.85).aspx), and [**ID3D12RootSignature**](https://msdn.microsoft.com/en-us/library/Dn788714(v=VS.85).aspx). It provides a method to get back to the device object it was created against. |
| [**ID3D12Fence**](/windows/desktop/api/d3d12/nn-d3d12-id3d12fence) | Represents a fence, an object used for synchronization of the CPU and one or more GPUs.  |
| [**ID3D12Fence1**](/windows/desktop/api/d3d12/nn-d3d12-id3d12fence1) | Represents a fence. This interface extends [**ID3D12Fence**](/windows/desktop/api/d3d12/nn-d3d12-id3d12fence), and supports the retrieval of the flags used to create the original fence.  |
| [**ID3D12GraphicsCommandList**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist) | Encapsulates a list of graphics commands for rendering. Includes APIs for instrumenting the command list execution, and for setting and clearing the pipeline state. |
| [**ID3D12GraphicsCommandList1**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist1) | Encapsulates a list of graphics commands for rendering, extending the inteface to support programmable sample positions, atomic copies for implementing late-latch techniques, and optional depth-bounds testing. |
| [**ID3D12GraphicsCommandList2**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist2) | Encapsulates a list of graphics commands for rendering, extending the interface to support writing immediate values directly to a buffer. |
| [**ID3D12GraphicsCommandList3**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist3) | Encapsulates a list of graphics commands for rendering. |
| [**ID3D12GraphicsCommandList4**](/windows/desktop/api/d3d12/nn-d3d12-id3d12graphicscommandlist4) | Encapsulates a list of graphics commands for rendering, extending the interface to support ray tracing and render passes. |
| [**ID3D12Heap**](/windows/desktop/api/d3d12/nn-d3d12-id3d12heap) | A heap is an abstraction of contiguous memory allocation, used to manage physical memory. This heap can be used with [**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource) objects to support placed resources or reserved resources. |
| [**ID3D12MetaCommand**](/windows/desktop/api/d3d12/nn-d3d12-id3d12metacommand) | Represents a meta command. A meta command is a Direct3D 12 object representing an algorithm that is accelerated by independent hardware vendors (IHVs). It's an opaque reference to a command generator that is implemented by the driver. |
| [**ID3D12Object**](/windows/desktop/api/d3d12/nn-d3d12-id3d12object) | An interface from which [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device) and [**ID3D12DeviceChild**](/windows/desktop/api/d3d12/nn-d3d12-id3d12devicechild) inherit from. It provides methods to associate private data and annotate object names. |
| [**ID3D12Pageable**](https://msdn.microsoft.com/en-us/library/Dn788704(v=VS.85).aspx) | An interface from which many other core interfaces inherit from. It indicates that the object type encapsulates some amount of GPU-accessible memory; but does not strongly indicate whether the application can manipulate the object's residency.  |
| [**ID3D12PipelineLibrary**](/windows/desktop/api/d3d12/nn-d3d12-id3d12pipelinelibrary) | Manages a pipeline library, in particular loading and retrieving individual PSOs. |
| [**ID3D12PipelineLibrary1**](/windows/desktop/api/d3d12/nn-d3d12-id3d12pipelinelibrary1) | Manages a pipeline library. This interface extends [**ID3D12PipelineLibrary**](/windows/desktop/api/d3d12/nn-d3d12-id3d12pipelinelibrary) to load PSOs from a pipeline state stream description. |
| [**ID3D12PipelineState**](/windows/desktop/api/d3d12/nn-d3d12-id3d12pipelinestate) | Represents the state of all currently set shaders as well as certain fixed function state objects. |
| [**ID3D12QueryHeap**](https://msdn.microsoft.com/en-us/library/Dn891447(v=VS.85).aspx) | Manages a query heap. A query heap holds an array of queries, referenced by indexes. |
| [**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource) | Encapsulates a generalized ability of the CPU and GPU to read and write to physical memory, or heaps. It contains abstractions for organizing and manipulating simple arrays of data as well as multidimensional data optimized for shader sampling. |
| [**ID3D12RootSignature**](https://msdn.microsoft.com/en-us/library/Dn788714(v=VS.85).aspx) | The root signature defines what resources are bound to the graphics pipeline. A root signature is configured by the app and links command lists to the resources the shaders require. Currently, there is one graphics and one compute root signature per app. |
| [**ID3D12RootSignatureDeserializer**](/windows/desktop/api/d3d12/nn-d3d12-id3d12rootsignaturedeserializer) | Contains a method to return the deserialized [**D3D12-ROOT-SIGNATURE-DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_signature_desc) data structure, of a serialized root signature version 1.0.  |
| [**ID3D12StateObject**](/windows/desktop/api/d3d12/nn-d3d12-id3d12stateobject) | Represents a variable amount of configuration state, including shaders, that an application manages as a single unit and which is given to a driver atomically to process, such as compile or optimize.  |
| [**ID3D12StateObjectProperties**](/windows/desktop/api/d3d12/nn-d3d12-id3d12stateobjectproperties) | Provides methods for getting and setting the properties of an [**ID3D12StateObject**](/windows/desktop/api/d3d12/nn-d3d12-id3d12stateobject).  |
| [**ID3D12Tools**](/windows/desktop/api/d3d12/nn-d3d12-id3d12tools) | This interface is used to configure the runtime for tools such as PIX. Its not intended or supported for any other scenario. |
| [**ID3D12VersionedRootSignatureDeserializer**](/windows/desktop/api/d3d12/nn-d3d12-id3d12versionedrootsignaturedeserializer) | Contains methods to return the deserialized [**D3D12-ROOT-SIGNATURE-DESC1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_signature_desc1) data structure, of any version of a serialized root signature.  |

## Related topics

* [Core reference](direct3d-12-core-reference.md)
* [Direct3D 12 reference](direct3d-12-reference.md)
* [Interface hierarchy](interface-hierarchy.md)
