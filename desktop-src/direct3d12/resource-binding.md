---
title: Resource Binding
description: Binding is the process of linking resource objects to the shaders of the graphics pipeline.
ms.assetid: CB0065EF-4E53-4E16-9F7E-09A261C360FB
ms.topic: article
ms.date: 05/31/2018
---

# Resource Binding

Binding is the process of linking resource objects to the shaders of the graphics pipeline.

## In this section

| Topic | Description |
|-|-|
| [Resource Binding Overview](resource-binding-flow-of-control.md) | The key to resource binding in DirectX 12 are the concepts of a *descriptor*, *descriptor tables*, *descriptor heaps*, and a *root signature*. |
| [Differences in the Binding Model from Direct3D 11](binding-model.md) | One of the main design decisions behind DirectX12 binding is to separate it from other management tasks. This places some requirements on the app to manage certain potential hazards. |
| [Descriptors](descriptors.md) | Descriptors are the primary unit of binding for a single resource in D3D12. |
| [Descriptor Heaps](descriptor-heaps.md) | A descriptor heap is a collection of contiguous allocations of descriptors, one allocation for every descriptor. |
| [Descriptor Tables](descriptor-tables.md) | A descriptor table is logically an array of descriptors. |
| [Root Signatures](root-signatures.md) | The root signature defines what types of resources are bound to the graphics pipeline. |
| [Capability Querying](capability-querying.md) | Your application can discover the level of support for resource binding, and many other features, with a call to [**ID3D12Device::CheckFeatureSupport**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport). |
| [Resource binding in HLSL](resource-binding-in-hlsl.md) | This topic describes some specific features of using High Level Shader Language (HLSL) [Shader Model 5.1](/windows/desktop/direct3dhlsl/shader-model-5-1) with Direct3D 12. All Direct3D 12 hardware supports Shader Model 5.1, so support for this model does not depend on what the hardware feature level is. |
| [UMA Optimizations: CPU Accessible Textures and Standard Swizzle](default-texture-mapping.md) | Universal Memory Architecture (UMA) GPUs offer some efficiency advantages over discrete GPUs, especially when optimizing for mobile devices. Giving resources CPU access when the GPU is UMA can reduce the amount of copying that occurs between CPU and GPU. While we don t recommend applications blindly give CPU access to all resources on UMA designs, there are opportunities to improve efficiencies by giving the right resources CPU access. Unlike discrete GPUs, the CPU can technically have a pointer to all resources that the GPU can access. |
| [Typed Unordered Access View Loads](typed-unordered-access-view-loads.md) | Unordered Access View (UAV) Typed Load is the ability for a shader to read from a UAV with a specific [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format). |
| [Volume Tiled Resources](volume-tiled-resources.md) | Volume (3D) textures can be used as tiled resources, noting that tile resolution is three-dimensional. |
| [Subresources](subresources.md) | Describes how a resource is divided into subresources, and how to reference a single, multiple or slice of subresources. |

## Related topics

* [Direct3D 12 Programming Guide](directx-12-programming-guide.md)
* [DirectX advanced learning video tutorials : Resource Binding in DirectX 12](https://www.youtube.com/watch?v=Uwhhdktaofg)
* [Memory Management](memory-management.md)
