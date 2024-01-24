---
title: Working Samples
description: Working samples are available for download, showing the usage of a number of features of Direct3D 12.
ms.assetid: 4C4475D4-534F-484F-8D60-9ACEA09AC109
ms.topic: article
ms.date: 05/31/2018
---

# Working Samples

Working samples are available for download, showing the usage of a number of features of Direct3D 12.

## Working samples

Working samples (in the form of Visual Studio 2015 projects) can be downloaded from [GitHub/Microsoft/DirectX-Graphics-Samples](https://github.com/Microsoft/DirectX-Graphics-Samples).

> [!Note]  
> The exact list of samples available at this location will vary as samples are added and updated.

 



<table>
<thead>
<tr class="header">
<th>Sample title</th>
<th>Description</th>
<th>Desktop</th>
<th>UWP</th>
<th>Walk-through</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HelloWorld<dl> HelloWindow<br />
HelloTriangle<br />
HelloBundles<br />
HelloConstBuffers<br />
HelloTexture<br />
</dl></td>
<td>The HelloWorld sample set contains the following simple projects to help you get started with Direct3D 12.<dl> Creates a window in preparation of rendering Direct3D 12 content.<br />
Renders a simple triangle using Direct3D 12.<br />
Demonstrates the usage of a bundle for rendering using Direct3D 12.<br />
Demonstrates how to use constant buffers to pass data to the GPU used for rendering in Direct3D 12.<br />
Demonstrates how to apply a texture to a triangle using Direct3D 12.<br />
</dl></td>
<td>Y</td>
<td>Y</td>
<td><a href="creating-a-basic-direct3d-12-component.md">Creating a basic Direct3D 12 component</a></td>
</tr>
<tr class="even">
<td>D3D12Bundles</td>
<td>Demonstrates frame buffering and synchronization best practices as well as rendering a simple mesh using bundles.</td>
<td>Y</td>
<td>Y</td>

</tr>
<tr class="odd">
<td>D3D12Multithreading</td>
<td>An example of how to build a multithreaded capable application.</td>
<td>Y</td>
<td>N</td>

</tr>
<tr class="even">
<td>D3D12nBodyGravity</td>
<td>Demonstrates how multi-engine can be used to do asynchronous compute work alongside 3D work on the same GPU.</td>
<td>Y</td>
<td>Y</td>
<td><a href="multi-engine-n-body-gravity-simulation.md">Multi-engine n-body gravity simulation</a></td>
</tr>
<tr class="odd">
<td>D3D12PredicationQueries</td>
<td>Demonstrates occlusion culling using query heaps and predication.</td>
<td>Y</td>
<td>Y</td>
<td><a href="predication-queries.md">Predication queries</a></td>
</tr>
<tr class="even">
<td>D3D12DynamicIndexing</td>
<td>Demonstrates the dynamic indexing capabilities of DirectX 12 and HLSL.</td>
<td>Y</td>
<td>Y</td>
<td><a href="dynamic-indexing-using-hlsl-5-1.md">Dynamic Indexing using HLSL 5.1</a></td>
</tr>
<tr class="odd">
<td>D3D1211on12</td>
<td>Demonstrates basic usage of the 11on12 layer. This sample renders text using D2D using the Direct3D 11 API on a Direct3D 12 11on12 device.</td>
<td>Y</td>
<td>Y</td>
<td><a href="d2d-using-d3d11on12.md">D2D using D3D11on12</a></td>
</tr>
<tr class="even">
<td>D3D12ExecuteIndirect</td>
<td>Demonstrates compute engine culling in conjunction with the execute indirect feature to only render objects that pass the culling test.</td>
<td>Y</td>
<td>Y</td>
<td><a href="indirect-drawing-and-gpu-culling-.md">Indirect drawing and GPU culling</a></td>
</tr>
<tr class="odd">
<td>D3D12PipelineStateCache</td>
<td>Demonstrates Pipeline State Object (PSO) caching.</td>
<td>Y</td>
<td>Y</td>

</tr>
<tr class="even">
<td>D3D12Fullscreen</td>
<td>Demonstrates how to handle fullscreen to windowed transitions and window resizing in DirectX 12.</td>
<td>Y</td>
<td>Y</td>

</tr>
<tr class="odd">
<td>D3D12HeterogeneousMultiadapter</td>
<td>Demonstrates how to share workloads amongst multiple heterogenous GPUs using shared heaps.</td>
<td>Y</td>
<td>Y</td>

</tr>
<tr class="even">
<td>D3D12ReservedResources</td>
<td>Demonstrates the use of reserved (tiled) resources. In this sample a quad is textured with a reserved resource containing a full mip chain.</td>
<td>Y</td>
<td>Y</td>

</tr>
<tr class="odd">
<td>D3D12Residency</td>
<td>This is intended as a low-integration-cost solution to managing your Direct3D 12 heaps and committed resources, using memory management techniques from Direct3D 11.</td>
<td>Y</td>
<td>Y</td>

</tr>
<tr class="even">
<td>D3D12SmallResources</td>
<td>Demonstrates the use of small placed resources, showing the potential memory savings gained using placed resources (with a 4K alignment) over committed and reserved resources (with a 64K alignment).</td>
<td>Y</td>
<td>Y</td>

</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[D3D12 Code Walk-Throughs](d3d12-code-walk-throughs.md)
</dt> </dl>

 

 




