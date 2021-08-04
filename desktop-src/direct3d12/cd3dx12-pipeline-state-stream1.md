---
title: CD3DX12_PIPELINE_STATE_STREAM1 structure (D3dx12.h)
description: A helper structure for creating and working with graphics and compute pipeline states through a combined interface. See [D3D12_GRAPHICS_PIPELINE_STATE_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) and [D3D12_COMPUTE_PIPELINE_STATE_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc).
ms.assetid: 4D3E4D99-E820-4220-92F3-4924791E780F
keywords:
- CD3DX12_PIPELINE_STATE_STREAM1 structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM1
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12_PIPELINE_STATE_STREAM1 structure

A helper structure for creating and working with graphics and compute pipeline states through a combined interface. See [D3D12_GRAPHICS_PIPELINE_STATE_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) and [D3D12_COMPUTE_PIPELINE_STATE_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc).

CD3DX12_PIPELINE_STATE_STREAM1 supports the Windows 10 Fall Creators Update with new features such as view instancing.

See [CD3DX12_PIPELINE_STATE_STREAM2](cd3dx12-pipeline-state-stream2.md) for support for OS Build 19041+ (where there is a mesh shader pipeline).

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM1 {
  CD3DX12_PIPELINE_STATE_STREAM1                      CD3DX12_PIPELINE_STATE_STREAM1();
  CD3DX12_PIPELINE_STATE_STREAM1                      CD3DX12_PIPELINE_STATE_STREAM1(const D3D12_GRAPHICS_PIPELINE_STATE_DESC& Desc);
  CD3DX12_PIPELINE_STATE_STREAM1                      CD3DX12_PIPELINE_STATE_STREAM1(const D3D12_COMPUTE_PIPELINE_STATE_DESC& Desc);
  D3D12_GRAPHICS_PIPELINE_STATE_DESC                  GraphicsDescV0();
  D3D12_COMPUTE_PIPELINE_STATE_DESC                   ComputeDescV0();
  CD3DX12_PIPELINE_STATE_STREAM_FLAGS                 Flags;
  CD3DX12_PIPELINE_STATE_STREAM_NODE_MASK             NodeMask;
  CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE        pRootSignature;
  CD3DX12_PIPELINE_STATE_STREAM_INPUT_LAYOUT          InputLayout;
  CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE    IBStripCutValue;
  CD3DX12_PIPELINE_STATE_STREAM_PRIMITIVE_TOPOLOGY    PrimitiveTopologyType;
  CD3DX12_PIPELINE_STATE_STREAM_VS                    VS;
  CD3DX12_PIPELINE_STATE_STREAM_GS                    GS;
  CD3DX12_PIPELINE_STATE_STREAM_STREAM_OUTPUT         StreamOutput;
  CD3DX12_PIPELINE_STATE_STREAM_HS                    HS;
  CD3DX12_PIPELINE_STATE_STREAM_DS                    DS;
  CD3DX12_PIPELINE_STATE_STREAM_PS                    PS;
  CD3DX12_PIPELINE_STATE_STREAM_CS                    CS;
  CD3DX12_PIPELINE_STATE_STREAM_BLEND_DESC            BlendState;
  CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1        DepthStencilState;
  CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL_FORMAT  DSVFormat;
  CD3DX12_PIPELINE_STATE_STREAM_RASTERIZER            RasterizerState;
  CD3DX12_PIPELINE_STATE_STREAM_RENDER_TARGET_FORMATS RTVFormats;
  CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC           SampleDesc;
  CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_MASK           SampleMask;
  CD3DX12_PIPELINE_STATE_STREAM_CACHED_PSO            CachedPSO;
};
```



## Members

<dl> <dt>

**CD3DX12_PIPELINE_STATE_STREAM1()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12_PIPELINE_STATE_STREAM1.

</dd> <dt>

**CD3DX12_PIPELINE_STATE_STREAM1(const D3D12_GRAPHICS_PIPELINE_STATE_DESC& Desc)**
</dt> <dd>

Creates a new instance of a CD3DX12_PIPELINE_STATE_STREAM1, initialized with values copied from a **CD3DX12_PIPELINE_STATE_STREAM1** structure.

</dd> <dt>

**CD3DX12_PIPELINE_STATE_STREAM1(const D3D12_COMPUTE_PIPELINE_STATE_DESC& Desc)**
</dt> <dd>

Creates a new instance of a CD3DX12_PIPELINE_STATE_STREAM1, initialized with values copied from a **CD3DX12_PIPELINE_STATE_STREAM1** structure.

</dd> <dt>

**GraphicsDescV0()**
</dt> <dd>

returns the contents of the CD3DX12_PIPELINE_STATE_STREAM1 object as a D3D12_GRAPHICS_PIPELINE_STATE_DESC structure by value. Note that D3D12_GRAPHICS_PIPELINE_STATE_DESC does not include the **CS** member, so this value is lost in the conversion.

</dd> <dt>

**ComputeDescV0()**
</dt> <dd>

returns the contents of the CD3DX12_PIPELINE_STATE_STREAM1 object as a D3D12_COMPUTE_PIPELINE_STATE_DESC structure by value. Note that D3D12_COMPUTE_PIPELINE_STATE_DESC does not include the **InputLayout**, **IBStripCutValue**, **PrimitiveTopologyType**, **VS**, **GS**, **StreamOutput**, **HS**, **DS**, **PS**, **BlendState**, **DepthStencilState**, **DSVFormat**, **RasterizerState**, **NumRootSignature**, **RTVFormats**, **SampleDesc**, or **SampleMask** members, so these values are lost in the conversion.

</dd> <dt>

**Flags**
</dt> <dd>

Describes the pipeline state flags, which control features such as "tool debug".

</dd> <dt>

**NodeMask**
</dt> <dd>

Describes the pipeline state node mask, which is used to identify the nodes (physical adapters of the device) that the PSO applies to in Multi-Adapter scenarios; each bit in the mask corresponds to a single node. For single-adapter scenarios, set this value to 0.

</dd> <dt>

**pRootSignature**
</dt> <dd>

Describes the root signature.

</dd> <dt>

**InputLayout**
</dt> <dd>

Describes the input-buffer format for the input-assembler stage

</dd> <dt>

**IBStripCutValue**
</dt> <dd>

Describes the special index value of the input buffer that indicates a cut (discontinuity) when using triangle-strip topology.

</dd> <dt>

**PrimitiveTopologyType**
</dt> <dd>

Describes the primitive topology and its order.

</dd> <dt>

**VS**
</dt> <dd>

Describes the vertex shader.

</dd> <dt>

**GS**
</dt> <dd>

Describes the geometry shader.

</dd> <dt>

**StreamOutput**
</dt> <dd>

Describes the streaming output-buffer.

</dd> <dt>

**HS**
</dt> <dd>

Describes the hull shader.

</dd> <dt>

**DS**
</dt> <dd>

Describes the domain shader.

</dd> <dt>

**PS**
</dt> <dd>

Describes the pixel shader.

</dd> <dt>

**CS**
</dt> <dd>

Describes the compute shader.

</dd> <dt>

**BlendState**
</dt> <dd>

Describes the blend state.

</dd> <dt>

**DepthStencilState**
</dt> <dd>

Describes the depth-stencil state.

</dd> <dt>

**DSVFormat**
</dt> <dd>

Describes the depth-stencil format.

</dd> <dt>

**RasterizerState**
</dt> <dd>

Describes the rasterizer state.

</dd> <dt>

**RTVFormats**
</dt> <dd>

Describes the render target formats.

</dd> <dt>

**SampleDesc**
</dt> <dd>

Describes the sample count and quality.

</dd> <dt>

**SampleMask**
</dt> <dd>

Describes the sample mask used with the blend state.

</dd> <dt>

**CachedPSO**
</dt> <dd>

Describes a cached PSO.

</dd> </dl>

## Remarks

[CD3DX12_PIPELINE_STATE_STREAM](cd3dx12-pipeline-state-stream.md) supports the Windows 10 Fall Creators Update, but doesn't support subobject types added in Windows 10 Fall Creators update, such as for view instancing. To support the new subobject types, use **CD3DX12_PIPELINE_STATE_STREAM1** instead.

The accessible member variables of this structure are all typedefs of the [**CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT**](/windows/win32/direct3d12/cd3dx12-pipeline-state-stream-subobject) template, which combines the subobject type-marker and subobject data into a single object suitable for a stream description.

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries/D3DX12) |

## See also

* [Helper structures for D3D12](helper-structures-for-d3d12.md)
* [**CD3DX12_PIPELINE_STATE_STREAM**](cd3dx12-pipeline-state-stream.md)
* [**D3D12_GRAPHICS_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc)
* [**D3D12_COMPUTE_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc)
