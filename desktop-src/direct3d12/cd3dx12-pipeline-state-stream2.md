---
title: CD3DX12_PIPELINE_STATE_STREAM2 structure (D3dx12.h)
description: A helper structure for creating and working with graphics and compute pipeline states through a combined interface.
keywords:
- CD3DX12_PIPELINE_STATE_STREAM2 structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM2
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/03/2021
---

# CD3DX12_PIPELINE_STATE_STREAM2 structure

A helper structure for creating and working with graphics and compute pipeline states through a combined interface. See [**D3D12_GRAPHICS_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) and [**D3D12_COMPUTE_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc).

**CD3DX12_PIPELINE_STATE_STREAM2** supports OS Build 19041+ (where there is a mesh shader pipeline).

## Syntax

```cpp
struct CD3DX12_PIPELINE_STATE_STREAM2
{
    CD3DX12_PIPELINE_STATE_STREAM2();
    CD3DX12_PIPELINE_STATE_STREAM2(const D3D12_GRAPHICS_PIPELINE_STATE_DESC& Desc) noexcept;
    CD3DX12_PIPELINE_STATE_STREAM2(const D3DX12_MESH_SHADER_PIPELINE_STATE_DESC& Desc) noexcept;
    CD3DX12_PIPELINE_STATE_STREAM2(const D3D12_COMPUTE_PIPELINE_STATE_DESC& Desc) noexcept;
    CD3DX12_PIPELINE_STATE_STREAM_FLAGS Flags;
    CD3DX12_PIPELINE_STATE_STREAM_NODE_MASK NodeMask;
    CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE pRootSignature;
    CD3DX12_PIPELINE_STATE_STREAM_INPUT_LAYOUT InputLayout;
    CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE IBStripCutValue;
    CD3DX12_PIPELINE_STATE_STREAM_PRIMITIVE_TOPOLOGY PrimitiveTopologyType;
    CD3DX12_PIPELINE_STATE_STREAM_VS VS;
    CD3DX12_PIPELINE_STATE_STREAM_GS GS;
    CD3DX12_PIPELINE_STATE_STREAM_STREAM_OUTPUT StreamOutput;
    CD3DX12_PIPELINE_STATE_STREAM_HS HS;
    CD3DX12_PIPELINE_STATE_STREAM_DS DS;
    CD3DX12_PIPELINE_STATE_STREAM_PS PS;
    CD3DX12_PIPELINE_STATE_STREAM_AS AS;
    CD3DX12_PIPELINE_STATE_STREAM_MS MS;
    CD3DX12_PIPELINE_STATE_STREAM_CS CS;
    CD3DX12_PIPELINE_STATE_STREAM_BLEND_DESC BlendState;
    CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1 DepthStencilState;
    CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL_FORMAT DSVFormat;
    CD3DX12_PIPELINE_STATE_STREAM_RASTERIZER RasterizerState;
    CD3DX12_PIPELINE_STATE_STREAM_RENDER_TARGET_FORMATS RTVFormats;
    CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC SampleDesc;
    CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_MASK SampleMask;
    CD3DX12_PIPELINE_STATE_STREAM_CACHED_PSO CachedPSO;
    CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING ViewInstancingDesc;
    D3D12_GRAPHICS_PIPELINE_STATE_DESC GraphicsDescV0() const noexcept;
    D3D12_COMPUTE_PIPELINE_STATE_DESC ComputeDescV0() const noexcept;
};
```

## Members

### CD3DX12_PIPELINE_STATE_STREAM2

Default constructor. Creates a new, uninitialized, instance of a **CD3DX12_PIPELINE_STATE_STREAM2**.

### CD3DX12_PIPELINE_STATE_STREAM2(const D3D12_GRAPHICS_PIPELINE_STATE_DESC&)

Constructor that creates a new instance of a **CD3DX12_PIPELINE_STATE_STREAM2** initialized with the contents of a [**D3D12_GRAPHICS_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) structure.

You'll then need to set mesh and amplification shaders manually, since they don't have representation in **D3D12_GRAPHICS_PIPELINE_STATE_DESC**.

### CD3DX12_PIPELINE_STATE_STREAM2(const D3DX12_MESH_SHADER_PIPELINE_STATE_DESC&)

Constructor that creates a new instance of a **CD3DX12_PIPELINE_STATE_STREAM2** initialized with the contents of a [**D3DX12_MESH_SHADER_PIPELINE_STATE_DESC**](d3dx12-mesh-shader-pipeline-state-desc.md) structure.

### CD3DX12_PIPELINE_STATE_STREAM2(const D3D12_COMPUTE_PIPELINE_STATE_DESC&)

Constructor that creates a new instance of a **CD3DX12_PIPELINE_STATE_STREAM2** initialized with the contents of a [**D3D12_COMPUTE_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc) structure.

### Flags

Type: **[CD3DX12_PIPELINE_STATE_STREAM_FLAGS](cd3dx12-pipeline-state-stream-flags.md)**

Flags (for example, to indicate that the pipeline state should be compiled with additional information to assist debugging).

### NodeMask

Type: **[CD3DX12_PIPELINE_STATE_STREAM_NODE_MASK](cd3dx12-pipeline-state-stream-node-mask.md)**

Describes the pipeline state node mask, which is used to identify the nodes (physical adapters of the device) that the PSO applies to in multi-adapter scenarios; each bit in the mask corresponds to a single node. For single-adapter scenarios, use 0.

### pRootSignature

Type: **[CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE](cd3dx12-pipeline-state-stream-root-signature.md)**

Describes the root signature.

### InputLayout

Type: **[CD3DX12_PIPELINE_STATE_STREAM_INPUT_LAYOUT](cd3dx12-pipeline-state-stream-input-layout.md)**

Describes the input-buffer format for the input-assembler stage

### IBStripCutValue

Type: **[CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE](cd3dx12-pipeline-state-stream-ib-strip-cut-value.md)**

Describes the special index value of the input buffer that indicates a cut (discontinuity) when using triangle-strip topology.

### PrimitiveTopologyType

Type: **[CD3DX12_PIPELINE_STATE_STREAM_PRIMITIVE_TOPOLOGY](cd3dx12-pipeline-state-stream-primitive-topology.md)**

Describes the primitive topology and its order.

### VS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_VS](cd3dx12-pipeline-state-stream-vs.md)**

Describes the vertex shader.

### GS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_GS](cd3dx12-pipeline-state-stream-gs.md)**

Describes the geometry shader.

### StreamOutput

Type: **[CD3DX12_PIPELINE_STATE_STREAM_STREAM_OUTPUT](cd3dx12-pipeline-state-stream-stream-output.md)**

Describes the streaming output-buffer.

### HS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_HS](cd3dx12-pipeline-state-stream-hs.md)**

Describes the hull shader.

### DS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_DS](cd3dx12-pipeline-state-stream-ds.md)**

Describes the domain shader.

### PS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_PS](cd3dx12-pipeline-state-stream-ps.md)**

Describes the pixel shader.

### AS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_AS](cd3dx12-pipeline-state-stream-as.md)**

Describes the amplification shader.

### MS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_MS](cd3dx12-pipeline-state-stream-ms.md)**

Describes the mesh shader.

### CS

Type: **[CD3DX12_PIPELINE_STATE_STREAM_CS](cd3dx12-pipeline-state-stream-cs.md)**

Describes the compute shader.

### BlendState

Type: **[CD3DX12_PIPELINE_STATE_STREAM_BLEND_DESC](cd3dx12-pipeline-state-stream-blend-desc.md)**

Describes the blend state.

### DepthStencilState

Type: **[CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1](cd3dx12-pipeline-state-stream-depth-stencil1.md)**

Describes the depth-stencil state.

### DSVFormat

Type: **[CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL_FORMAT](cd3dx12-pipeline-state-stream-depth-stencil-format.md)**

Describes the depth-stencil format.

### RasterizerState

Type: **[CD3DX12_PIPELINE_STATE_STREAM_RASTERIZER](cd3dx12-pipeline-state-stream-rasterizer.md)**

Describes the rasterizer state.

### RTVFormats

Type: **[CD3DX12_PIPELINE_STATE_STREAM_RENDER_TARGET_FORMATS](cd3dx12-pipeline-state-stream-render-target-formats.md)**

Describes the render target formats.

### SampleDesc

Type: **[CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC](cd3dx12-pipeline-state-stream-sample-desc.md)**

Describes the sample count and quality.

### SampleMask

Type: **[CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_MASK](cd3dx12-pipeline-state-stream-sample-mask.md)**

Describes the sample mask used with the blend state.

### CachedPSO

Type: **[CD3DX12_PIPELINE_STATE_STREAM_CACHED_PSO](cd3dx12-pipeline-state-stream-cached-pso.md)**

Describes a cached PSO.

### ViewInstancingDesc

Type: **[CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING](cd3dx12-pipeline-state-stream-view-instancing.md)**

Describes a view instancing configuration.

### GraphicsDescV0

Returns [**D3D12_GRAPHICS_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc).

returns the contents of the **CD3DX12_PIPELINE_STATE_STREAM2** object as a **D3D12_GRAPHICS_PIPELINE_STATE_DESC** structure by value. **D3D12_GRAPHICS_PIPELINE_STATE_DESC** doesn't include the *CS* member, so that value is lost in the conversion.

### ComputeDescV0

Returns [**D3D12_COMPUTE_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc).

returns the contents of the **CD3DX12_PIPELINE_STATE_STREAM2** object as a **D3D12_COMPUTE_PIPELINE_STATE_DESC** structure by value. **D3D12_COMPUTE_PIPELINE_STATE_DESC** doesn't include the members *InputLayout*, *IBStripCutValue*, *PrimitiveTopologyType*, *VS*, *GS*, *StreamOutput*, *HS*, *DS*, *PS*, *BlendState*, *DepthStencilState*, *DSVFormat*, *RasterizerState*, *NumRootSignature*, *RTVFormats*, *SampleDesc*, and *SampleMask*, so those values are lost in the conversion.

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries/D3DX12) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
