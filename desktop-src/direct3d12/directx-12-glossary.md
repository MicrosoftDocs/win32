---
title: Direct3D 12 glossary
description: These terms are distinctive of Direct3D 12.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 46B0F055-7E4F-4F8D-9915-3D195FD695B7
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 12 glossary

These terms are distinctive of Direct3D 12.

<dl> <dt>

<span id="direct3d12.directx_12_glossary_binding"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_BINDING"></span>**binding**
</dt> <dd>

The process of attaching memory to the graphics pipeline. Resource binding, for example, involves the binding of a resource such as a texture to the pipeline, for use in rendering an object.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_buffer"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_BUFFER"></span>**buffer**
</dt> <dd>

A type of D3D resource that is synonymous with a contiguous memory allocation.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_bundle"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_BUNDLE"></span>**bundle**
</dt> <dd>

A command buffer that the graphics processing unit (GPU) can execute only directly via a *direct command list*. A bundle inherits all GPU state (except for the currently set *pipeline state object* and primitive topology).

</dd> <dt>

<span id="direct3d12.directx_12_glossary_command_allocator"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_COMMAND_ALLOCATOR"></span>**command allocator**
</dt> <dd>

The underlying memory allocations in which GPU commands are stored. The command allocator object applies to both *direct command lists* and *bundles*.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_command_list"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_COMMAND_LIST"></span>**command list**
</dt> <dd>

A command list corresponds to a set of commands which the GPU executes. These include commands such as to set state, draw, clear, and copy. The D3D12 command list interface is significantly different than the D3D11 command list interface. The D3D12 command list interface contains APIs similar to the D3D11 device context rendering APIs.

A D3D12 command list does not map or unmap resources, change tile mappings, resize tile pools, get query data, nor does it ever implicitly submit commands to the GPU for execution.

Unlike D3D11 deferred contexts, D3D12 command lists only support two levels of indirection. A *direct command list* corresponds to a command buffer which the GPU can execute. A *bundle* can be executed only directly via a direct command list.

A direct command list does not inherit any GPU state. A bundle inherits all GPU state (except for the currently set pipeline state object and primitive topology).

Memory for a command list is set by the *command allocator*. The purpose of command lists is that they can be submitted to a GPU as a single rendering request.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_command_queue"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_COMMAND_QUEUE"></span>**command queue**
</dt> <dd>

A queue of *command lists* that the GPU executes in succession. Applications must explicitly submit *command lists* to a command queue for execution. Typically there are three command queues: 3D graphics, compute and copy, corresponding to the 3D graphics pipeline, the compute engine, and one or more copy engines, on the GPU.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_conservative_rasterization"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_CONSERVATIVE_RASTERIZATION"></span>**conservative rasterization**
</dt> <dd>

Conservative rasterization is a mode of operation for the rasterizer stage of the Direct3D graphics pipeline. It disables the standard sample-based rasterization, and will instead rasterize a pixel that is covered by any amount by a primitive. One important distinction is that, while any coverage at all produces a rasterized pixel, that coverage cannot be characterized by the hardware, so coverage always appears binary to a pixel shader: either fully covered or not covered. It is left to the pixel shader code to analytically determine the actual coverage.

Conservative rasterization can help with such problems as collision and hit detection, binning, and occlusion culling, where the color of a pixel is more certain and edge cases can be eliminated. See [Conservative Rasterization](conservative-rasterization.md).

</dd> <dt>

<span id="direct3d12.directx_12_glossary_cbv"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_CBV"></span>**Constant Buffer View (CBV)**
</dt> <dd>

Constant buffers contain shader constant data, such as a camera view, projection matrices, and world matrices. A "constant buffer view" is the format-specific view of the buffer as seen by the graphics pipeline.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_default_heap"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_DEFAULT_HEAP"></span>**default heap**
</dt> <dd>

A user-mode heap that is focused on supporting persistent GPU resource types, including GPU-written resources.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_descriptor"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_DESCRIPTOR"></span>**descriptor**
</dt> <dd>

Descriptors are the primary unit of binding for a single resource in D3D12. A descriptor is a relatively small block of data that fully describes an object to the GPU, in a GPU specific format. There are many different types of descriptors: Shader Resource Views (SRVs), Unordered Access Views (UAVs), Constant Buffer Views (CBVs), and Samplers are a few examples.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_descriptor_heap"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_DESCRIPTOR_HEAP"></span>**descriptor heap**
</dt> <dd>

A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor. The primary point of a descriptor heap is to encompass the bulk of memory allocation required for storing the descriptor specifications of object types that shaders reference for as large of a window of rendering as possible (ideally an entire frame of rendering or more).

</dd> <dt>

<span id="direct3d12.directx_12_glossary_descriptor_table"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_DESCRIPTOR_TABLE"></span>**descriptor table**
</dt> <dd>

A descriptor table is logically an array of descriptors. Each descriptor table stores descriptors of one or more types, including SRVs, UAVe, CBVs, and Samplers. A descriptor table is not an allocation of memory, it is simply an offset and length into a descriptor heap.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_direct_command_list"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_DIRECT_COMMAND_LIST"></span>**direct command list**
</dt> <dd>

A command buffer that the GPU can execute. A direct command list doesn't inherit any GPU state.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_fence"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_FENCE"></span>**fence**
</dt> <dd>

A mechanism to synchronize the GPU and CPU. Both the GPU and CPU can be instructed to wait at a fence, waiting in effect for the other processor to catch up. See [Multi-engine synchronization](./user-mode-heap-synchronization.md).

</dd> <dt>

<span id="direct3d12.directx_12_glossary_hazard"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_HAZARD"></span>**hazard, hazard tracking**
</dt> <dd>

A hazard occurs when a resource has been used for one purpose, and the app intends to reuse it for another purpose. In order to use the resource again, intermediate caches will need to be flushed or invalidated, compression requirements will need to be consistent with the second use, and the resource should be in the required state to avoid reading the resource after it has been written to and invalidated for the intended purpose.

The process of maintaining resources and avoiding these sync issues is known as hazard tracking. If there is no hazard tracking by the driver, then the app is responsible for this. In most earlier versions of DirectX, hazard tracking was handled by the driver. To improve performance, methods without hazard tracking are available in DirectX 12.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_hlsl"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_HLSL"></span>**High-Level Shader Language (HLSL)**
</dt> <dd>

A computer language, similar but distinct in many ways from C, that is used to write shader code. Vertex, pixel, geometry, compute, domain, and hull shaders are all written using HLSL. A compiler converts the HLSL source into a binary format for the GPU to consume.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_multiengine"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_MULTIENGINE"></span>**multiengine**
</dt> <dd>

The different instances and types of engines in a single GPU. The types of engines include: graphics, compute, and copy.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_multigpu"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_MULTIGPU"></span>**MultiGPU**
</dt> <dd>

A hardware configuration where there is more than one graphics adapter. The separate adapters are sometimes referred to as nodes. Having multiple GPUs can make the task of synchronizing them with the CPU, and each other, considerably more complex than with a single GPU.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_pipeline_state_object"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_PIPELINE_STATE_OBJECT"></span>**Pipeline State object (PSO)**
</dt> <dd>

A significant portion of the state of the GPU. This state includes all currently set shaders and certain fixed-function state objects. The only way to change states contained within the pipeline object is to change the currently bound pipeline object.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_predication"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_PREDICATION"></span>**predication**
</dt> <dd>

Predication is a feature that enables the GPU rather than the CPU to determine to not draw, copy or dispatch an object. For example, if a bounding box of an object is totally occluded by another object or perspective has reduced the object to less than the size of a pixel, there may be no point in attempting to draw the hidden object at all. See [Predication](predication.md).

</dd> <dt>

<span id="direct3d12.directx_12_glossary_rov"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_ROV"></span>**Rasterizer Order View (ROV)**
</dt> <dd>

Standard graphics pipelines may have trouble correctly compositing together multiple textures that contain transparency. Objects such as wire fences, smoke, fire, vegetation, and colored glass use transparency to get the desired effect. Problems arise when multiple textures that contain transparency are in line with each other (smoke in front of a fence in front of a glass building containing vegetation, as an example). Rasterizer ordered views (ROVs) enable the underlying Order Independent Transparency (OIT) algorithms to use features of the hardware to try to resolve the transparency order correctly. Transparency is handled by the pixel shader.

Rasterizer Ordered Views (ROVs) allow pixel shader code to mark Unordered Access View (UAV) bindings with a declaration that alters the normal requirements for the order of graphics pipeline results for UAVs.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_readback_heap"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_READBACK_HEAP"></span>**readback heap**
</dt> <dd>

A user-mode heap that is focused on data transfer from the GPU back to the CPU.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_resource"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_RESOURCE"></span>**resource**
</dt> <dd>

An entity that provides data to the pipeline and defines what is rendered during your scene. Resources can be loaded from your game media or created dynamically at run time. Typically, resources include texture data, vertex data, and shader data. Most Direct3D applications create and destroy resources extensively throughout their lifespan.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_resource_barrier"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_RESOURCE_BARRIER"></span>**resource barrier**
</dt> <dd>

A resource barrier notifies the driver that synchronization of multiple accesses to a single resource may be required, for example, reading and writing to the same texture.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_resource_binding"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_RESOURCE_BINDING"></span>**resource binding**
</dt> <dd>

Resource binding is the process of linking resources (textures, vertex buffers, index buffers, and so on), to the graphics pipeline, enabling the shaders of the pipeline to process the correct resource.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_resource_heaps"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_RESOURCE_HEAPS"></span>**resource heaps**
</dt> <dd>

Resource heaps is a generic term for the heaps that are memory buffers set aside to hold resources as they are transferred to and from the GPU. A transfer to the GPU requires an Upload Heap, from the GPU to the CPU requires a Readback Heap, and a persistent heap for the GPU to maintain over multiple rendering frames is called a Default Heap.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_root_signature"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_ROOT_SIGNATURE"></span>**root signature**
</dt> <dd>

Root signatures define all the resources that are to be bound to the graphics, or compute, pipelines. A root signature is configured by the app and links command lists to the resources that the shaders require Typically, there is one graphics and one compute root signature per app.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_sampler"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_SAMPLER"></span>**sampler**
</dt> <dd>

A sampler is code that reads from a texture.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_srv"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_SRV"></span>**Shader Resource View (SRV)**
</dt> <dd>

A format-specific way to look at the data in a shader resource, such as a texture.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_static_heap"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_STATIC_HEAP"></span>**static heap**
</dt> <dd>

A user-mode heap that is focused on multiple GPU-read-only resources that are typically used at the same time and are not changed frequently.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_swap_chain"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_SWAP_CHAIN"></span>**swap chain**
</dt> <dd>

Swap chains control the back buffer rotation, forming the basis of graphics animation. Swap chains are handled by the low level API set DXGI (see [DXGI Overview](../direct3ddxgi/d3d10-graphics-programming-guide-dxgi.md)).

</dd> <dt>

<span id="direct3d12.directx_12_glossary_swizzle"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_SWIZZLE"></span>**swizzle**
</dt> <dd>

A technique of locating multidimensional data in memory such that data of nearby dimensionality tends to have nearby addresses. In particular, all the data for one row is not located contiguously before the data for the next row. A "Parameterized Swizzle" describes a standardized way to describe swizzle patterns.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_static_texture"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_STATIC_TEXTURE"></span>**texture**
</dt> <dd>

A type of D3D resource that is multi-dimensional and has a memory layout that is optimized for multi-dimensional access from the GPU. Textures often contain the raw image required to render onto a surface, before lighting and blending takes place, but can contain other forms of data such as color gradients and reference colors. Direct3D 12 supports one, two, and three dimensional textures.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_tile"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_TILE"></span>**tile**
</dt> <dd>

A page of video memory, similar to a CPU/System page of memory. The tile notation helps to distinguish the GPU virtual memory subsystem from the CPU virtual memory subsystem. GPUs provide similar virtual memory capabilities as system virtual memory. Some GPUs have shared virtual memory capabilities, which allow for the sharing of some pages of the virtual memory subsystem with both the CPU and GPU.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_tiled_resources"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_TILED_RESOURCES"></span>**tiled resources**
</dt> <dd>

Tiled resources are needed so less GPU memory is wasted storing regions of surfaces that the application knows will not be accessed, and the hardware can understand how to filter across adjacent tiles. Tiled resources are large logical resources, but requiring small amounts of physical memory.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_uav"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_UAV"></span>**Unordered Access View (UAV)**
</dt> <dd>

An unordered access view into a resource (which includes buffers, textures, and texture arrays - without multi-sampling), allows temporally unordered read/write access from multiple threads. This means that this resource type can be read/written simultaneously by multiple threads without generating memory conflicts.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_upload_heap"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_UPLOAD_HEAP"></span>**upload heap**
</dt> <dd>

A user-mode heap that is focused on data transfer from the CPU to the GPU.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_user_mode_heap"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_USER_MODE_HEAP"></span>**user-mode heap**
</dt> <dd>

A collection of large, contiguous memory allocations that are recycled without any kernel component's awareness: the allocation and destruction methods do not call kernel allocation and destruction methods during steady state. Upload, Readback, and Default heaps are variants of user mode heaps.

</dd> <dt>

<span id="direct3d12.directx_12_glossary_volume_tiled_resources"></span><span id="DIRECT3D12.DIRECTX_12_GLOSSARY_VOLUME_TILED_RESOURCES"></span>**volume tiled resources**
</dt> <dd>

Three-dimensional [tiled resources](/windows).

</dd> </dl>

 

 
