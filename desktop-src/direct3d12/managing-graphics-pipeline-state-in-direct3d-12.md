---
title: Managing Graphics Pipeline State in Direct3D 12
description: This topic describes how graphics pipeline state is set in Direct3D 12.
ms.assetid: AAF97BD2-D532-469D-9242-CC94C06727C3
keywords:
- pipeline state
- pipeline state object
ms.topic: article
ms.date: 05/31/2018
---

# Managing Graphics Pipeline State in Direct3D 12

This topic describes how graphics pipeline state is set in Direct3D 12.

## Pipeline state overview

When geometry is submitted to the graphics processing unit (GPU) to be drawn, there are a wide range of hardware settings that determine how the input data is interpreted and rendered. Collectively, these settings are called the graphics pipeline state and include common settings such as the rasterizer state, blend state, and depth stencil state, as well as the primitive topology type of the submitted geometry and the shaders that will be used for rendering. In Microsoft Direct3D 12, most graphics pipeline state is set by using pipeline state objects (PSO). An app can create an unlimited number of these objects, represented by the [**ID3D12PipelineState**](/windows/win32/api/d3d12/nn-d3d12-id3d12pipelinestate) interface, typically at initialization time. Then, at render time, command lists can quickly switch multiple settings of the pipeline state by calling [**ID3D12GraphicsCommandList::SetPipelineState**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setpipelinestate) in a direct command list or bundle to set the active PSO.

In Direct3D 11, graphics pipeline state was bundled into large, coarse-grained state objects like [**ID3D11BlendState**](/windows/win32/api/d3d11/nn-d3d11-id3d11blendstate) that could be created and set at render time in the immediate context with methods like [**ID3D11DeviceContext::OMSetBlendState**](/windows/win32/api/d3d10/nf-d3d10-id3d10device-omsetblendstate). The idea behind this was that the GPU could gain efficiencies by setting related settings, like the blend state settings, all at once. However, with today's graphics hardware, there are dependencies between the different hardware units. For example, the hardware blend state might have dependencies on the raster state as well as the blend state. PSOs in Direct3D 12 were designed to allow the GPU to pre-process all of the dependent settings in each pipeline state, typically during initialization, to make switching between states at render time as efficient as possible.

Note that while most of the pipeline state settings are set using PSOs, there are some state settings which are set separately using APIs provided by [**ID3D12GraphicsCommandList**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist). These settings and the associated APIs are discussed in detail below. Also, there are differences in the way that graphics pipeline state is inherited by and persisted from direct command lists and bundles. This topic provides details on both of these below.

## Graphics pipeline states set with pipeline state objects

The easiest way to see all of the different pipeline states that can be set using a pipeline state object is to look at the reference topic for the [**D3D12\_GRAPHICS\_PIPELINE\_STATE\_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) which you pass to [**ID3D12Device::CreateGraphicsPipelineState**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-creategraphicspipelinestate) when you initialize the object. A quick summary of the states that can be set includes:

-   The bytecode for all shaders including, vertex, pixel, domain, hull, and geometry shaders.
-   The input vertex format.
-   The primitive topology type. Note that the input-assembler primitive topology type (point, line, triangle, patch) is set within the PSO using the [**D3D12\_PRIMITIVE\_TOPOLOGY\_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_primitive_topology_type) enumeration. The primitive adjacency and ordering (line list, line strip, line strip with adjacency data, etc.) is set from within a command list using the [**ID3D12GraphicsCommandList::IASetPrimitiveTopology**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetprimitivetopology) method.
-   The blend state, rasterizer state, depth stencil state.
-   The depth stencil and render target formats, as well as the render target count.
-   Multi-sampling parameters.
-   A streaming output buffer.
-   The root signature. For more information, see [Root Signatures](root-signatures.md).

## Graphics pipeline states set outside of the pipeline state object

Most graphics pipeline states are set using PSOs. However, there are a set of pipeline state parameters that are set by calling methods of the [**ID3D12GraphicsCommandList**](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist) interface from within a command list. The following table shows the states that are set this way and the corresponding methods.

|State|Method|
|-|-|
|Resource bindings|[**IASetIndexBuffer**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetindexbuffer)<br/>[**IASetVertexBuffers**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetvertexbuffers)<br/>[**SOSetTargets**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-sosettargets)<br/>[**OMSetRenderTargets**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetrendertargets)<br/>[**SetDescriptorHeaps**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setdescriptorheaps)<br/>All **SetGraphicsRoot...** methods<br/>All **SetComputeRoot...** methods<br/>
|Viewports|<a href="/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetviewports">**RSSetViewports**</a>|
|Scissor rects|<a href="/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetscissorrects">**RSSetScissorRects**</a>|
|Blend factor|<a href="/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetblendfactor">**OMSetBlendFactor**</a>|
|The depth stencil reference value|<a href="/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetstencilref">**OMSetStencilRef**</a>|
|The input-assembler primitive topology order and adjacency type|<a href="/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetprimitivetopology">**IASetPrimitiveTopology**</a>|

## Graphics pipeline state inheritance

Because direct command lists are generally intended for one use at a time and bundles are intended to be used multiple times concurrently, there are different rules about how they inherit graphics pipeline state that was set by previous command lists or bundles.

For the graphics pipeline states that are set using PSOs, none of these states are inherited by either direct command lists or bundles. The initial graphics pipeline state for both direct command lists and bundles is set at creation time with the [**ID3D12PipelineState**](/windows/win32/api/d3d12/nn-d3d12-id3d12pipelinestate) parameter to [**ID3D12Device::CreateCommandList**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandlist). If no PSO is specified in the call, a default initial state is used. You can change the current PSO within a command list by calling [**ID3D12GraphicsCommandList::SetPipelineState**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setpipelinestate).

Direct command lists also do not inherit state that is set with command list methods like [**RSSetViewports**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetviewports). For details about the default initial values for non-PSO states, see [**ID3D12GraphicsCommandList::ClearState**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearstate).

Bundles inherit all graphics pipeline state that is not set with PSOs except for the primitive topology type. The primitive topology is always set to [**D3D12\_PRIMITIVE\_TOPOLOGY\_TYPE\_UNDEFINED**](/windows/win32/api/d3d12/ne-d3d12-d3d12_primitive_topology_type) when a bundle begins executing. Any state that is set within a bundle (the PSO itself, non-PSO-based state, and resource bindings) affects the state of its parent direct command list. For example, if a [**RSSetViewports**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetviewports) is called from within a bundle, the specified viewports will continue to be set in the parent direct command list for calls subsequent to the [**ExecuteBundle**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-executebundle) call that set the viewports.

Resource bindings that are set within a command list or bundle do persist. So resource bindings modified in a direct command list will still be set within subsequent child bundle execution. And resource bindings modified from within a bundle will still be set for subsequent calls within the parent direct command list.

For more information on bindings, refer to the **Bundle Semantics** section of [Using a Root Signature](using-a-root-signature.md).

## Related topics

* [Work Submission in Direct3D 12](command-queues-and-command-lists.md)
