---
title: Multi-Adapter
description: Describes support in D3D12 for multi-engine adapter systems, covering scenarios where applications explicitly target multiple GPU adapters, and scenarios where drivers implicitly use multiple GPU adapters on behalf of an application.
ms.assetid: 'CC4C6594-D48F-40C1-93EE-9F98532BC038'
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

Similar to previous D3D APIs, each set of linked adapters is enumerated as a single [**IDXGIAdapter3**](https://msdn.microsoft.com/library/windows/desktop/dn933221) object. All outputs attached to any adapter in the link are enumerated as attached to the single **IDXGIAdapter3** object.

### Single nodes

Applications can determine the number of physical adapters associated with a given device with a call to [**ID3D12Device::GetNodeCount**](id3d12device-getnodecount.md). Many APIs in D3D12 accept a *NodeMask*, which indicates the set of nodes which the API call refers to.

When calling the following (single node) APIs, applications specify a single node that the API call will be associated with. Most of the time this is specified by a *NodeMask*. Each bit in the mask corresponds to a single node. For all of the APIs described in this section, exactly 1 bit must be set in the *NodeMask*.

-   [**D3D12\_COMMAND\_QUEUE\_DESC**](d3d12-command-queue-desc.md) : has a *NodeMask* member.
-   [**CreateCommandQueue**](id3d12device-createcommandqueue.md) : creates a queue from a [**D3D12\_COMMAND\_QUEUE\_DESC**](d3d12-command-queue-desc.md) structure.
-   [**CreateCommandList**](id3d12device-createcommandlist.md) : takes a *nodeMask* parameter.
-   [**D3D12\_DESCRIPTOR\_HEAP\_DESC**](d3d12-descriptor-heap-desc.md) : has a *NodeMask* member.
-   [**CreateDescriptorHeap**](id3d12device-createdescriptorheap.md) : creates a descriptor heap from a [**D3D12\_DESCRIPTOR\_HEAP\_DESC**](d3d12-descriptor-heap-desc.md) structure.
-   [**D3D12\_QUERY\_HEAP\_DESC**](d3d12-query-heap-desc.md) : has a *NodeMask* member.
-   [**CreateQueryHeap**](id3d12device-createqueryheap.md) : creates a query heap from a [**D3D12\_QUERY\_HEAP\_DESC**](d3d12-query-heap-desc.md) structure.

### Multiple nodes

When calling the following APIs, applications specify a set of nodes that the API call will be associated with. Node affinity is specified as a bit mask. If the application passes 0 for the bit mask, then the D3D12 driver converts this to the bit mask 1 (indicating that the object is associated with node 0).

-   [**D3D12\_CROSS\_NODE\_SHARING\_TIER**](d3d12-cross-node-sharing-tier.md) : determines the support for cross node sharing.
-   [**D3D12\_FEATURE\_DATA\_D3D12\_OPTIONS**](d3d12-feature-data-d3d12-options.md) : structure referencing [**D3D12\_CROSS\_NODE\_SHARING\_TIER**](d3d12-cross-node-sharing-tier.md).
-   [**D3D12\_FEATURE\_DATA\_ARCHITECTURE**](d3d12-feature-data-architecture.md) : contains a *NodeIndex* member.
-   [**D3D12\_GRAPHICS\_PIPELINE\_STATE\_DESC**](d3d12-graphics-pipeline-state-desc.md) : has a *NodeMask* member.
-   [**CreateGraphicsPipelineState**](id3d12device-creategraphicspipelinestate.md) : creates a graphics pipeline state object from a [**D3D12\_GRAPHICS\_PIPELINE\_STATE\_DESC**](d3d12-graphics-pipeline-state-desc.md) structure.
-   [**D3D12\_COMPUTE\_PIPELINE\_STATE\_DESC**](d3d12-compute-pipeline-state-desc.md) : has a *NodeMask* member.
-   [**CreateComputePipelineState**](id3d12device-createcomputepipelinestate.md) : creates a compute pipeline state object from a [**D3D12\_COMPUTE\_PIPELINE\_STATE\_DESC**](d3d12-compute-pipeline-state-desc.md) structure.
-   [**CreateRootSignature**](id3d12device-createrootsignature.md): takes a *nodeMask* parameter.
-   [**D3D12\_COMMAND\_SIGNATURE\_DESC**](d3d12-command-signature-desc.md): has a *NodeMask* member.
-   [**CreateCommandSignature**](id3d12device-createcommandsignature.md) : creates a command signature object from a [**D3D12\_COMMAND\_SIGNATURE\_DESC**](d3d12-command-signature-desc.md) structure.

### Resource creation APIs

The following APIs reference node masks:

-   [**D3D12\_HEAP\_PROPERTIES**](d3d12-heap-properties.md) : has both *CreationNodeMask* and *VisibleNodeMask* members.
-   [**GetResourceAllocationInfo**](id3d12device-getresourceallocationinfo.md) : has a *visibleMask* parameter.
-   [**GetCustomHeapProperties**](id3d12device-getcustomheapproperties.md) : has a *nodeMask* parameter.

When creating reserved resource no node index or mask is specified. The reserved resource can be mapped onto a heap on any node (following the cross-node sharing rules).

The method [**MakeResident**](id3d12device-makeresident.md) works internally with adapter queues, there is no need for the application to specify anything for this.

When calling the following [**ID3D12Device**](id3d12device.md) APIs, applications do not need to specify a set of nodes that the API call will be associated with because the API call applies to all nodes:

-   [**CreateFence**](id3d12device-createfence.md)
-   [**GetDescriptorHandleIncrementSize**](id3d12device-getdescriptorhandleincrementsize.md)
-   [**SetStablePowerState**](id3d12device-setstablepowerstate.md)
-   [**CheckFeatureSupport**](id3d12device-checkfeaturesupport.md)
-   [**CreateSampler**](id3d12device-createsampler.md)
-   [**CopyDescriptors**](id3d12device-copydescriptors.md)
-   [**CopyDescriptorsSimple**](id3d12device-copydescriptorssimple.md)
-   [**CreateSharedHandle**](id3d12device-createsharedhandle.md)
-   [**OpenSharedHandleByName**](id3d12device-opensharedhandlebyname.md)
-   [**OpenSharedHandle**](id3d12device-opensharedhandle.md) : with a *fence* as a parameter. With a *resource* or a *heap* as parameters this method does not accept nodes as parameters because node masks are inherited from previously created objects.
-   [**CreateCommandAllocator**](id3d12device-createcommandallocator.md)
-   [**CreateConstantBufferView**](id3d12device-createconstantbufferview.md)
-   [**CreateRenderTargetView**](id3d12device-createrendertargetview.md)
-   [**CreateUnorderedAccessView**](id3d12device-createunorderedaccessview.md)
-   [**CreateDepthStencilView**](id3d12device-createdepthstencilview.md)
-   [**CreateShaderResourceView**](id3d12device-createshaderresourceview.md)

## Related topics

<dl> <dt>

[Multi-engine and multi-adapter synchronization](mulit-engine-and-multi-gpu-synchronization.md)
</dt> </dl>

 

 




