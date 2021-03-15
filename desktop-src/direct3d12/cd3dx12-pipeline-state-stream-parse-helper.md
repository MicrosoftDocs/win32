---
title: CD3DX12_PIPELINE_STATE_STREAM_PARSE_HELPER structure (D3dx12.h)
description: Builds an internal CD3DX12\_PIPELINE\_STATE\_STREAM object from subobject details passed into the corresponding member functions. This struct implements the ID3DX12PipelineParserCallbacks interface.
ms.assetid: 7D4FFD1D-9FA3-4482-A67B-E742611030BC
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_PARSE_HELPER structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_PARSE_HELPER
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_PARSE\_HELPER structure

Builds an internal CD3DX12\_PIPELINE\_STATE\_STREAM object from subobject details passed into the corresponding member functions. This struct implements the [**ID3DX12PipelineParserCallbacks**](id3dx12pipelineparsercallbacks.md) interface.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_PARSE_HELPER  : public ID3DX12PipelineParserCallbacks{
  CD3DX12_PIPELINE_STATE_STREAM1 PipelineStream;
  void                           FlagsCb(D3D12_PIPELINE_STATE_FLAGS Flags);
  void                           NodeMaskCb(UINT NodeMask);
  void                           RootSignatureCb(ID3D12RootSignature* pRootSignature);
  void                           InputLayoutCb(const D3D12_INPUT_LAYOUT_DESC& InputLayout);
  void                           IBStripCutValueCb(D3D12_INDEX_BUFFER_STRIP_CUT_VALUE IBStripCutValue);
  void                           PrimitiveTopologyTypeCb(D3D12_PRIMITIVE_TOPOLOGY_TYPE PrimitiveTopologyType);
  void                           VSCb(const D3D12_SHADER_BYTECODE& VS);
  void                           GSCb(const D3D12_SHADER_BYTECODE& GS);
  void                           StreamOutputCb(const D3D12_STREAM_OUTPUT_DESC& StreamOutput);
  void                           HSCb(const D3D12_SHADER_BYTECODE& HS);
  void                           DSCb(const D3D12_SHADER_BYTECODE& DS);
  void                           PSCb(const D3D12_SHADER_BYTECODE& PS);
  void                           CSCb(const D3D12_SHADER_BYTECODE& CS);
  void                           BlendStateCb(const D3D12_BLEND_DESC& BlendState);
  void                           DepthStencilStateCb(const D3D12_DEPTH_STENCIL_DESC& DepthStencilState);
  void                           DepthStencilState1Cb(const D3D12_DEPTH_STENCIL_DESC1& DepthStencilState);
  void                           DSVFormatCb(DXGI_FORMAT DSVFormat);
  void                           RasterizerStateCb(const D3D12_RASTERIZER_DESC& RasterizerState);
  void                           RTVFormatsCb(const D3D12_RT_FORMAT_ARRAY& RTVFormats);
  void                           SampleDescCb(const DXGI_SAMPLE_DESC& SampleDesc);
  void                           SampleMaskCb(UINT SampleMask);
  void                           ViewInstancingCb(const D3D12_VIEW_INSTANCING_DESC& ViewInstancingDesc);
  void                           CachedPSOCb(const D3D12_CACHED_PIPELINE_STATE& CachedPSO);
  void                           ErrorBadInputParameter(UINT);
  void                           ErrorDuplicateSubobject(D3D12_PIPELINE_STATE_SUBOBJECT_TYPE);
  void                           ErrorUnknownSubobject(UINT);
};
```



## Members

<dl> <dt>

**PipelineStream**
</dt> <dd>

The internal [**CD3DX12\_PIPELINE\_STATE\_STREAM1**](cd3dx12-pipeline-state-stream1.md). Its current state represents the cumulative effect of callback methods that have been called on this object.

</dd> <dt>

**FlagsCb(D3D12\_PIPELINE\_STATE\_FLAGS Flags)**
</dt> <dd>

Initializes the **Flags** member of **PipelineStream** using the value of the *Flags* parameter.

</dd> <dt>

**NodeMaskCb(UINT NodeMask)**
</dt> <dd>

Initializes the **NodeMask** member of **PipelineStream** using the value of the *Nodemask* parameter.

</dd> <dt>

**RootSignatureCb(ID3D12RootSignature\* pRootSignature)**
</dt> <dd>

Initializes the **pRootSignature** member of **PipelineStream** using the value of the *pRootSignature* parameter.

</dd> <dt>

**InputLayoutCb(const D3D12\_INPUT\_LAYOUT\_DESC& InputLayout)**
</dt> <dd>

Initializes the **InputLayout** member of **PipelineStream** using the value of the *InputLayout* parameter.

</dd> <dt>

**IBStripCutValueCb(D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE IBStripCutValue)**
</dt> <dd>

Initializes the **IBStripCutValue** member of **PipelineStream** using the value of the *IBStripCutValue* parameter.

</dd> <dt>

**PrimitiveTopologyTypeCb(D3D12\_PRIMITIVE\_TOPOLOGY\_TYPE PrimitiveTopologyType)**
</dt> <dd>

Initializes the **PrimitiveTopologyType** member of **PipelineStream** using the value of the *PrimitiveTopologyType* parameter.

</dd> <dt>

**VSCb(const D3D12\_SHADER\_BYTECODE& VS)**
</dt> <dd>

Initializes the **VS** (vertex shader) member of **PipelineStream** using the value of the *VS* parameter.

</dd> <dt>

**GSCb(const D3D12\_SHADER\_BYTECODE& GS)**
</dt> <dd>

Initializes the **GS** (geometry shader) member of **PipelineStream** using the value of the *GS* parameter.

</dd> <dt>

**StreamOutputCb(const D3D12\_STREAM\_OUTPUT\_DESC& StreamOutput)**
</dt> <dd>

Initializes the **StreamOutput** member of **PipelineStream** using the value of the *StreamOutput* parameter.

</dd> <dt>

**HSCb(const D3D12\_SHADER\_BYTECODE& HS)**
</dt> <dd>

Initializes the **HS** (hull shader) member of **PipelineStream** using the value of the *HS* parameter.

</dd> <dt>

**DSCb(const D3D12\_SHADER\_BYTECODE& DS)**
</dt> <dd>

Initializes the **DS** (domain shader) member of **PipelineStream** using the value of the *DS* parameter.

</dd> <dt>

**PSCb(const D3D12\_SHADER\_BYTECODE& PS)**
</dt> <dd>

Initializes the **PS** (pixel shader) member of **PipelineStream** using the value of the *PS* parameter.

</dd> <dt>

**CSCb(const D3D12\_SHADER\_BYTECODE& CS)**
</dt> <dd>

Initializes the **CS** member of **PipelineStream** using the value of the *CS* parameter.

</dd> <dt>

**BlendStateCb(const D3D12\_BLEND\_DESC& BlendState)**
</dt> <dd>

Initializes the **BlendState** member of **PipelineStream** using the value of the *BlendState* parameter.

</dd> <dt>

**DepthStencilStateCb(const D3D12\_DEPTH\_STENCIL\_DESC& DepthStencilState)**
</dt> <dd>

Initializes the **DepthStencilState** member of **PipelineStream** using the value of the *DepthStencilState* parameter, a [**D3D12\_DEPTH\_STENCIL\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_depth_stencil_desc).

</dd> <dt>

**DepthStencilState1Cb(const D3D12\_DEPTH\_STENCIL\_DESC1& DepthStencilState)**
</dt> <dd>

Initializes the **DepthStencilState** member of **PipelineStream** using the value of the *DepthStencilState* parameter, a [**D3D12\_DEPTH\_STENCIL\_DESC1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_depth_stencil_desc1).

</dd> <dt>

**DSVFormatCb(DXGI\_FORMAT DSVFormat)**
</dt> <dd>

Initializes the **DSVFormat** member of **PipelineStream** using the value of the *DSVFormat* parameter.

</dd> <dt>

**RasterizerStateCb(const D3D12\_RASTERIZER\_DESC& RasterizerState)**
</dt> <dd>

Initializes the **RasterizerState** member of **PipelineStream** using the value of the *RasterizerState* parameter.

</dd> <dt>

**RTVFormatsCb(const D3D12\_RT\_FORMAT\_ARRAY& RTVFormats)**
</dt> <dd>

Initializes the **RTVFormats** member of **PipelineStream** using the value of the *RTVFormats* parameter.

</dd> <dt>

**SampleDescCb(const DXGI\_SAMPLE\_DESC& SampleDesc)**
</dt> <dd>

Initializes the **SampleDesc** member of **PipelineStream** using the value of the *SampleDesc* parameter.

</dd> <dt>

**SampleMaskCb(UINT SampleMask)**
</dt> <dd>

Initializes the **SampleMask** member of **PipelineStream** using the value of the *SampleMask* parameter.

</dd> <dt>

**ViewInstancingCb(const D3D12\_VIEW\_INSTANCING\_DESC& ViewInstancingDesc)**
</dt> <dd>

Initializes the **ViewInstancingDesc** member of **PipelineStream** using the value of the *ViewInstancingDesc* parameter.

</dd> <dt>

**CachedPSOCb(const D3D12\_CACHED\_PIPELINE\_STATE& CachedPSO)**
</dt> <dd>

Initializes the **CachedPSO** member of **PipelineStream** using the value of the *CachedPSO* parameter.

</dd> <dt>

**ErrorBadInputParameter(UINT)**
</dt> <dd>

Does nothing.

</dd> <dt>

**ErrorDuplicateSubobject(D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE)**
</dt> <dd>

Does nothing.

</dd> <dt>

**ErrorUnknownSubobject(UINT)**
</dt> <dd>

Does nothing.

</dd> </dl>

## Remarks

When passed as the second parameter to the [**D3DX12ParsePipelineStream**](d3dx12parsepipelinestream.md) function, the details of the internal [**CD3DX12\_PIPELINE\_STATE\_STREAM1**](cd3dx12-pipeline-state-stream1.md) object are cloned from the [**D3D12\_PIPELINE\_STATE\_STREAM\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_pipeline_state_stream_desc) passed as the first parameter. This process validates the source stream description. If D3DX12ParsePipelineStream returns **S\_OK**, then both the source stream description and the resulting **CD3DX12\_PIPELINE\_STATE\_STREAM1PipelineStream** are valid; otherwise both are invalid. Invalid streams and other errors are reported only through the return value of D3DX12ParsePipelineStream; this structure implements the error callbacks to do nothing.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[Helper Structures for Direct3D 12](helper-structures-for-d3d12.md)
</dt> <dt>

[**ID3DX12PipelineParserCallbacks**](id3dx12pipelineparsercallbacks.md)
</dt> </dl>

 

 





