---
title: D3DX12_MESH_SHADER_PIPELINE_STATE_DESC structure (D3dx12.h)
description: For [mesh/amplifications shaders](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html), you can use the data from an [EffectPipelineStateDescription](https://github.com/Microsoft/DirectXTK12/wiki/EffectPipelineStateDescription), with **D3DX12_MESH_SHADER_PIPELINE_STATE_DESC**, to provide all the state.
keywords:
- D3DX12_MESH_SHADER_PIPELINE_STATE_DESC structure
topic_type:
- apiref
api_name:
- D3DX12_MESH_SHADER_PIPELINE_STATE_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/02/2021
---

# D3DX12_MESH_SHADER_PIPELINE_STATE_DESC structure

For [mesh/amplifications shaders](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html), you can use the data from an [EffectPipelineStateDescription](https://github.com/Microsoft/DirectXTK12/wiki/EffectPipelineStateDescription), with **D3DX12_MESH_SHADER_PIPELINE_STATE_DESC**, to provide all the state.

Also see [CD3DX12_PIPELINE_STATE_STREAM2](cd3dx12-pipeline-state-stream1.md).

For a code example, see [Mesh shaders](https://github.com/Microsoft/DirectXTK12/wiki/EffectPipelineStateDescription#mesh-shaders).

## Syntax

```cpp
struct D3DX12_MESH_SHADER_PIPELINE_STATE_DESC
{
    ID3D12RootSignature* pRootSignature;
    D3D12_SHADER_BYTECODE         AS;
    D3D12_SHADER_BYTECODE         MS;
    D3D12_SHADER_BYTECODE         PS;
    D3D12_BLEND_DESC              BlendState;
    UINT                          SampleMask;
    D3D12_RASTERIZER_DESC         RasterizerState;
    D3D12_DEPTH_STENCIL_DESC      DepthStencilState;
    D3D12_PRIMITIVE_TOPOLOGY_TYPE PrimitiveTopologyType;
    UINT                          NumRenderTargets;
    DXGI_FORMAT                   RTVFormats[D3D12_SIMULTANEOUS_RENDER_TARGET_COUNT];
    DXGI_FORMAT                   DSVFormat;
    DXGI_SAMPLE_DESC              SampleDesc;
    UINT                          NodeMask;
    D3D12_CACHED_PIPELINE_STATE   CachedPSO;
    D3D12_PIPELINE_STATE_FLAGS    Flags;
};
```

## Members

`pRootSignature`

Type: **[ID3D12RootSignature](/windows/win32/api/d3d12/nn-d3d12-id3d12rootsignature)\***

A root signature object defining what resources are bound to the pipeline.

`AS`

Type: **[D3D12_SHADER_BYTECODE](/windows/win32/api/d3d12/ns-d3d12-d3d12_shader_bytecode)**

Contains the data representing the amplification shader program.

`MS`

Type: **[D3D12_SHADER_BYTECODE](/windows/win32/api/d3d12/ns-d3d12-d3d12_shader_bytecode)**

Contains the data representing the mesh shader program.

`PS`

Type: **[D3D12_SHADER_BYTECODE](/windows/win32/api/d3d12/ns-d3d12-d3d12_shader_bytecode)**

Contains the data representing the pixel shader program.

`BlendState`

Type: **[D3D12_BLEND_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_blend_desc)**

Describes the blend state.

`SampleMask`

Type: **[UINT](../winprog/windows-data-types.md)**

The sample mask for the blend state.

`RasterizerState`

Type: **[D3D12_RASTERIZER_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_rasterizer_desc)**

Describes the rasterizer state.

`DepthStencilState`

Type: **[D3D12_DEPTH_STENCIL_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_depth_stencil_desc)**

Describes the depth-stencil state.

`PrimitiveTopologyType`

Type: **[D3D12_PRIMITIVE_TOPOLOGY_TYPE](/windows/win32/api/d3d12/ne-d3d12-d3d12_primitive_topology_type)**

Describes the type and ordering of the primitive data.

`NumRenderTargets`

Type: **[UINT](../winprog/windows-data-types.md)**

The number of render target formats in the *RTVFormats* member.

`RTVFormats`

Type: **[DXGI_FORMAT](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)**

An array of values for the render target formats.

`DSVFormat`

Type: **[DXGI_FORMAT](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)**

A value for the depth-stencil format.

`SampleDesc`

Type: **[DXGI_SAMPLE_DESC](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)**

Specifies multisampling parameters.

`CachedPSO`

Type: **[D3D12_CACHED_PIPELINE_STATE](/windows/win32/api/d3d12/ns-d3d12-d3d12_cached_pipeline_state)**

A cached pipeline state object. *pCachedBlob* and *CachedBlobSizeInBytes* may be set to NULL and 0 respectively.

`Flags`

Type: **[D3D12_PIPELINE_STATE_FLAGS](/windows/win32/api/d3d12/ne-d3d12-d3d12_pipeline_state_flags)**

A flag enumeration constant (for example, to indicate that the pipeline state should be compiled with additional information to assist debugging).

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
* [CD3DX12_PIPELINE_STATE_STREAM2](cd3dx12-pipeline-state-stream1.md)
* [mesh/amplifications shaders](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html)
* [EffectPipelineStateDescription](https://github.com/Microsoft/DirectXTK12/wiki/EffectPipelineStateDescription)
