---
title: Multi-Adapter
description: Describes support in D3D12 for multi-engine adapter systems, covering scenarios where applications explicitly target multiple GPU adapters, and scenarios where drivers implicitly use multiple GPU adapters on behalf of an application.
ms.assetid: CC4C6594-D48F-40C1-93EE-9F98532BC038
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Multi-Adapter

Describes support in D3D12 for multi-engine adapter systems, covering scenarios where applications explicitly target multiple GPU adapters, and scenarios where drivers implicitly use multiple GPU adapters on behalf of an application.

-   [Multi-adapter Overview](#multi-adapter-overview)
-   [Sharing heaps across adapters](#sharing-heaps-across-adapters)
-   [Multi-adapter APIs](#multi-adapter-apis)
    -   [Single nodes](#single-nodes)
    -   [Multiple nodes](#multiple-nodes)
    -   [Resource creation APIs](#resource-creation-apis)
-   [Related topics](#related-topics)

## Multi-adapter Overview

A GPU adapter can be any graphics adapter (including an on-board adapter), from any manufacturer, that supports D3D12.

Multiple adapters are referenced as *nodes.* in the API. These nodes are indexed from zero, but in the bit masks used to refer to the nodes, zero translates to bit 1, 1 to bit 2, and so on. A number of elements, such as the queues, apply to each node, so if there are two nodes, there will be two default 3D queues. Other elements, such as the pipeline state and root and command signatures, can refer to one or more or all of the nodes, as shown in the following diagram.

![queues apply to each graphics adapter](images/multigpu.png)

## Sharing heaps across adapters

Refer to the [Shared Heaps](shared-heaps.md) section.

## Multi-adapter APIs

Similar to previous D3D APIs, each set of linked adapters is enumerated as a single [**IDXGIAdapter3**](https://docs.microsoft.com/windows/desktop/api/dxgi1_4/nn-dxgi1_4-idxgiadapter3) object. All outputs attached to any adapter in the link are enumerated as attached to the single **IDXGIAdapter3** object.

### Single nodes

Applications can determine the number of physical adapters associated with a given device with a call to [**ID3D12Device::GetNodeCount**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getnodecount). Many APIs in D3D12 accept a *NodeMask*, which indicates the set of nodes which the API call refers to.

When calling the following (single node) APIs, applications specify a single node that the API call will be associated with. Most of the time this is specified by a *NodeMask*. Each bit in the mask corresponds to a single node. For all of the APIs described in this section, exactly 1 bit must be set in the *NodeMask*.

-   [**D3D12\_COMMAND\_QUEUE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_command_queue_desc) : has a *NodeMask* member.
-   [**CreateCommandQueue**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcommandqueue) : creates a queue from a [**D3D12\_COMMAND\_QUEUE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_command_queue_desc) structure.
-   [**CreateCommandList**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcommandlist) : takes a *nodeMask* parameter.
-   [**D3D12\_DESCRIPTOR\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_heap_desc) : has a *NodeMask* member.
-   [**CreateDescriptorHeap**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createdescriptorheap) : creates a descriptor heap from a [**D3D12\_DESCRIPTOR\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_heap_desc) structure.
-   [**D3D12\_QUERY\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_query_heap_desc) : has a *NodeMask* member.
-   [**CreateQueryHeap**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createqueryheap) : creates a query heap from a [**D3D12\_QUERY\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_query_heap_desc) structure.

### Multiple nodes

When calling the following APIs, applications specify a set of nodes that the API call will be associated with. Node affinity is specified as a bit mask. If the application passes 0 for the bit mask, then the D3D12 driver converts this to the bit mask 1 (indicating that the object is associated with node 0).

-   [**D3D12\_CROSS\_NODE\_SHARING\_TIER**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_cross_node_sharing_tier) : determines the support for cross node sharing.
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options) : structure referencing [**D3D12\_CROSS\_NODE\_SHARING\_TIER**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_cross_node_sharing_tier).
-   [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_architecture) : contains a *NodeIndex* member.
-   [**D3D12\_GRAPHICS\_PIPELINE\_STATE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) : has a *NodeMask* member.
-   [**CreateGraphicsPipelineState**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-creategraphicspipelinestate) : creates a graphics pipeline state object from a [**D3D12\_GRAPHICS\_PIPELINE\_STATE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) structure.
-   [**D3D12\_COMPUTE\_PIPELINE\_STATE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc) : has a *NodeMask* member.
-   [**CreateComputePipelineState**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcomputepipelinestate) : creates a compute pipeline state object from a [**D3D12\_COMPUTE\_PIPELINE\_STATE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc) structure.
-   [**CreateRootSignature**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createrootsignature): takes a *nodeMask* parameter.
-   [**D3D12\_COMMAND\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_command_signature_desc): has a *NodeMask* member.
-   [**CreateCommandSignature**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcommandsignature) : creates a command signature object from a [**D3D12\_COMMAND\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_command_signature_desc) structure.

### Resource creation APIs

The following APIs reference node masks:

-   [**D3D12\_HEAP\_PROPERTIES**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_properties) : has both *CreationNodeMask* and *VisibleNodeMask* members.
-   [**GetResourceAllocationInfo**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getresourceallocationinfo) : has a *visibleMask* parameter.
-   [**GetCustomHeapProperties**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getcustomheapproperties) : has a *nodeMask* parameter.

When creating reserved resource no node index or mask is specified. The reserved resource can be mapped onto a heap on any node (following the cross-node sharing rules).

The method [**MakeResident**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-makeresident) works internally with adapter queues, there is no need for the application to specify anything for this.

When calling the following [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device) APIs, applications do not need to specify a set of nodes that the API call will be associated with because the API call applies to all nodes:

-   [**CreateFence**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createfence)
-   [**GetDescriptorHandleIncrementSize**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getdescriptorhandleincrementsize)
-   [**SetStablePowerState**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-setstablepowerstate)
-   [**CheckFeatureSupport**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport)
-   [**CreateSampler**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createsampler)
-   [**CopyDescriptors**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptors)
-   [**CopyDescriptorsSimple**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-copydescriptorssimple)
-   [**CreateSharedHandle**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createsharedhandle)
-   [**OpenSharedHandleByName**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-opensharedhandlebyname)
-   [**OpenSharedHandle**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-opensharedhandle) : with a *fence* as a parameter. With a *resource* or a *heap* as parameters this method does not accept nodes as parameters because node masks are inherited from previously created objects.
-   [**CreateCommandAllocator**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createcommandallocator)
-   [**CreateConstantBufferView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createconstantbufferview)
-   [**CreateRenderTargetView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createrendertargetview)
-   [**CreateUnorderedAccessView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createunorderedaccessview)
-   [**CreateDepthStencilView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createdepthstencilview)
-   [**CreateShaderResourceView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createshaderresourceview)

## Related topics

<dl> <dt>

[Multi-engine and multi-adapter synchronization](multi-engine-and-multi-gpu-synchronization.md)
</dt> </dl>

 

 




