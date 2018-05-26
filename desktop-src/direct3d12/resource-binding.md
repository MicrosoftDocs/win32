---
title: Resource Binding
description: Binding is the process of linking resource objects to the shaders of the graphics pipeline.
ms.assetid: CB0065EF-4E53-4E16-9F7E-09A261C360FB
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Binding

Binding is the process of linking resource objects to the shaders of the graphics pipeline.

## In this section



| Topic                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Resource Binding Overview](resource-binding-flow-of-control.md)<br/>                              | The key to resource binding in DirectX 12 are the concepts of a *descriptor*, *descriptor tables*, *descriptor heaps*, and a *root signature*. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Differences in the Binding Model from Direct3D 11](binding-model.md)<br/>                         | One of the main design decisions behind DirectX12 binding is to separate it from other management tasks. This places some requirements on the app to manage certain potential hazards.<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| [Descriptors](descriptors.md)<br/>                                                                 | Descriptors are the primary unit of binding for a single resource in D3D12.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Descriptor Heaps](descriptor-heaps.md)<br/>                                                       | A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Descriptor Tables](descriptor-tables.md)<br/>                                                     | A descriptor table is logically an array of descriptors. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Root Signatures](root-signatures.md)<br/>                                                         | The root signature defines what types of resources are bound to the graphics pipeline. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Capability Querying](capability-querying.md)<br/>                                                 | Applications can discover the level of support for resource binding, and many other features, via the [**ID3D12Device::CheckFeatureSupport**](/windows/win32/D3D12/nf-d3d12-id3d12device-checkfeaturesupport?branch=master) call. <br/>                                                                                                                                                                                                                                                                                                                                                                     |
| [Resource Binding in HLSL](resource-binding-in-hlsl.md)<br/>                                       | This section describes some specific features of using High Level Shading Language (HLSL) [Shader Model 5.1](https://msdn.microsoft.com/library/windows/desktop/dn933277) with Direct3D 12. All Direct3D 12 hardware supports Shader Model 5.1, so support for this model does not depend on what the hardware feature level is.<br/>                                                                                                                                                                                                                                                             |
| [UMA Optimizations: CPU Accessible Textures and Standard Swizzle](default-texture-mapping.md)<br/> | Universal Memory Architecture (UMA) GPUs offer some efficiency advantages over discrete GPUs, especially when optimizing for mobile devices. Giving resources CPU access when the GPU is UMA can reduce the amount of copying that occurs between CPU and GPU. While we don t recommend applications blindly give CPU access to all resources on UMA designs, there are opportunities to improve efficiencies by giving the right resources CPU access. Unlike discrete GPUs, the CPU can technically have a pointer to all resources that the GPU can access.<br/> |
| [Typed Unordered Access View Loads](typed-unordered-access-view-loads.md)<br/>                     | Unordered Access View (UAV) Typed Load is the ability for a shader to read from a UAV with a specific [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059).<br/>                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Volume Tiled Resources](volume-tiled-resources.md)<br/>                                           | Volume (3D) textures can be used as tiled resources, noting that tile resolution is three-dimensional.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Subresources](subresources.md)<br/>                                                               | Describes how a resource is divided into subresources, and how to reference a single, multiple or slice of subresources.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[DirectX advanced learning video tutorials : Resource Binding in DirectX 12](https://www.youtube.com/watch?v=Uwhhdktaofg)
</dt> <dt>

[Memory Management](memory-management.md)
</dt> </dl>

 

 





