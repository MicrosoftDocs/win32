---
title: D3DX11_STATE_BLOCK_MASK structure (D3dx11effect.h)
description: Indicates the device state.
ms.assetid: 42044a6d-6a11-4f90-889a-82e7954da6c7
keywords:
- D3DX11_STATE_BLOCK_MASK structure Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11_STATE_BLOCK_MASK
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX11\_STATE\_BLOCK\_MASK structure

Indicates the device state.

## Syntax


```C++
typedef struct _D3DX11_STATE_BLOCK_MASK {
  BYTE VS;
  BYTE VSSamplers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_SAMPLER_SLOT_COUNT)];
  BYTE VSShaderResources[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE VSConstantBuffers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)];
  BYTE VSInterfaces[D3DX11_BYTES_FROM_BITS(D3D11_SHADER_MAX_INTERFACES)];
  BYTE HS;
  BYTE HSSamplers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_SAMPLER_SLOT_COUNT)];
  BYTE HSShaderResources[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE HSConstantBuffers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)];
  BYTE HSInterfaces[D3DX11_BYTES_FROM_BITS(D3D11_SHADER_MAX_INTERFACES)];
  BYTE DS;
  BYTE DSSamplers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_SAMPLER_SLOT_COUNT)];
  BYTE DSShaderResources[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE DSConstantBuffers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)];
  BYTE DSInterfaces[D3DX11_BYTES_FROM_BITS(D3D11_SHADER_MAX_INTERFACES)];
  BYTE GS;
  BYTE GSSamplers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_SAMPLER_SLOT_COUNT)];
  BYTE GSShaderResources[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE GSConstantBuffers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)];
  BYTE GSInterfaces[D3DX11_BYTES_FROM_BITS(D3D11_SHADER_MAX_INTERFACES)];
  BYTE PS;
  BYTE PSSamplers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_SAMPLER_SLOT_COUNT)];
  BYTE PSShaderResources[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE PSConstantBuffers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)];
  BYTE PSInterfaces[D3DX11_BYTES_FROM_BITS(D3D11_SHADER_MAX_INTERFACES)];
  BYTE PSUnorderedAccessViews;
  BYTE CS;
  BYTE CSSamplers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_SAMPLER_SLOT_COUNT)];
  BYTE CSShaderResources[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE CSConstantBuffers[D3DX11_BYTES_FROM_BITS(D3D11_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)];
  BYTE CSInterfaces[D3DX11_BYTES_FROM_BITS(D3D11_SHADER_MAX_INTERFACES)];
  BYTE CSUnorderedAccessViews;
  BYTE IAVertexBuffers[D3DX11_BYTES_FROM_BITS(D3D11_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT)];
  BYTE IAIndexBuffer;
  BYTE IAInputLayout;
  BYTE IAPrimitiveTopology;
  BYTE OMRenderTargets;
  BYTE OMDepthStencilState;
  BYTE OMBlendState;
  BYTE RSViewports;
  BYTE RSScissorRects;
  BYTE RSRasterizerState;
  BYTE SOBuffers;
  BYTE Predication;
} D3DX11_STATE_BLOCK_MASK;
```



## Members

<dl> <dt>

**VS**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the vertex shader state.

</dd> <dt>

**VSSamplers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of vertex-shader samplers. The array is a multi-byte bitmask where each bit represents one sampler slot.

</dd> <dt>

**VSShaderResources**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of vertex-shader resources. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**VSConstantBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of vertex-shader constant buffers. The array is a multi-byte bitmask where each bit represents one constant buffer slot.

</dd> <dt>

**VSInterfaces**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of vertex-shader interfaces. The array is a multi-byte bitmask where each bit represents one interface slot.

</dd> <dt>

**HS**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the hull shader state.

</dd> <dt>

**HSSamplers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of hull-shader samplers. The array is a multi-byte bitmask where each bit represents one sampler slot.

</dd> <dt>

**HSShaderResources**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of hull-shader resources. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**HSConstantBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of hull-shader constant buffers. The array is a multi-byte bitmask where each bit represents one constant buffer slot.

</dd> <dt>

**HSInterfaces**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of hull-shader interfaces. The array is a multi-byte bitmask where each bit represents one interface slot.

</dd> <dt>

**DS**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the domain shader state.

</dd> <dt>

**DSSamplers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of domain-shader samplers. The array is a multi-byte bitmask where each bit represents one sampler slot.

</dd> <dt>

**DSShaderResources**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of domain-shader resources. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**DSConstantBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of domain-shader constant buffers. The array is a multi-byte bitmask where each bit represents one buffer slot.

</dd> <dt>

**DSInterfaces**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of domain-shader interfaces. The array is a multi-byte bitmask where each bit represents one interface slot.

</dd> <dt>

**GS**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the geometry shader state.

</dd> <dt>

**GSSamplers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of geometry-shader samplers. The array is a multi-byte bitmask where each bit represents one sampler slot.

</dd> <dt>

**GSShaderResources**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of geometry-shader resources. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**GSConstantBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of geometry-shader constant buffers. The array is a multi-byte bitmask where each bit represents one buffer slot.

</dd> <dt>

**GSInterfaces**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of geometry-shader interfaces. The array is a multi-byte bitmask where each bit represents one interface slot.

</dd> <dt>

**PS**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the pixel shader state.

</dd> <dt>

**PSSamplers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of pixel-shader samplers. The array is a multi-byte bitmask where each bit represents one sampler slot.

</dd> <dt>

**PSShaderResources**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of pixel-shader resources. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**PSConstantBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of pixel-shader constant buffers. The array is a multi-byte bitmask where each bit represents one constant buffer slot.

</dd> <dt>

**PSInterfaces**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of pixel-shader interfaces. The array is a multi-byte bitmask where each bit represents one interface slot.

</dd> <dt>

**PSUnorderedAccessViews**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the pixel shader unordered access views.

</dd> <dt>

**CS**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the compute shader state.

</dd> <dt>

**CSSamplers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of compute-shader samplers. The array is a multi-byte bitmask where each bit represents one sampler slot.

</dd> <dt>

**CSShaderResources**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of compute-shader resources. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**CSConstantBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of compute-shader constant buffers. The array is a multi-byte bitmask where each bit represents one constant buffer slot.

</dd> <dt>

**CSInterfaces**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of compute-shader interfaces. The array is a multi-byte bitmask where each bit represents one interface slot.

</dd> <dt>

**CSUnorderedAccessViews**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the compute shader unordered access views.

</dd> <dt>

**IAVertexBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Array of vertex buffers. The array is a multi-byte bitmask where each bit represents one resource slot.

</dd> <dt>

**IAIndexBuffer**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the index buffer state.

</dd> <dt>

**IAInputLayout**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the input layout state.

</dd> <dt>

**IAPrimitiveTopology**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the primitive topology state.

</dd> <dt>

**OMRenderTargets**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the render targets states.

</dd> <dt>

**OMDepthStencilState**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the depth-stencil state.

</dd> <dt>

**OMBlendState**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the blend state.

</dd> <dt>

**RSViewports**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the viewports states.

</dd> <dt>

**RSScissorRects**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the scissor rectangles states.

</dd> <dt>

**RSRasterizerState**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the rasterizer state.

</dd> <dt>

**SOBuffers**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the stream-out buffers states.

</dd> <dt>

**Predication**
</dt> <dd>

Type: **[**BYTE**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Boolean value indicating whether to save the predication state.

</dd> </dl>

## Remarks

A state-block mask indicates the device states that a pass or a technique changes.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Structures](d3d11-graphics-reference-effects11-structures.md)
</dt> </dl>

 

