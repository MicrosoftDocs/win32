---
title: ID3DX12PipelineParserCallbacks interface (D3DX12.h)
description: An interface that represents a collection of parser and error callbacks used by the D3DX12parsePipelineStream helper function.
ms.assetid: CBC04D17-2E19-4755-B1CB-FC42BF5083E5
keywords:
- ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, described
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks
api_location:
- D3D12.dll
api_type:
- COM
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks interface

An interface that represents a collection of parser and error callbacks used by the [**D3DX12parsePipelineStream**](d3dx12parsepipelinestream.md) helper function.

-   [Methods](#methods)

### Methods

The **ID3DX12PipelineParserCallbacks** interface has these methods.



| Method                                                                                    | Description                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BlendStateCb**](id3dx12pipelineparsercallbacks-blendstatecb.md)                       | Calls the blend state description subobject callback of an object that implements this interface.<br/>                                                                 |
| [**CachedPSOCb**](id3dx12pipelineparsercallbacks-cachedpsocb.md)                         | Calls the cached PSO (Pipeline State Object) subobject callback of an object that implements this interface.<br/>                                                      |
| [**CSCb**](id3dx12pipelineparsercallbacks-cscb.md)                                       | Calls the compute shader subobject callback of an object that implements this interface.<br/>                                                                          |
| [**DepthStencilState1Cb**](id3dx12pipelineparsercallbacks-depthstencilstate1cb.md)       | Calls the depth stencil state ([**D3D12\_DEPTH\_STENCIL\_DESC1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_depth_stencil_desc1)) subobject callback of an object that implements this interface.<br/> |
| [**DepthStencilStateCb**](id3dx12pipelineparsercallbacks-dsvformatcb.md)                 | Calls the depth stencil value format subobject callback of an object that implements this interface.<br/>                                                              |
| [**DepthStencilStateCb**](id3dx12pipelineparsercallbacks-depthstencilstatecb.md)         | Calls the depth stencil state subobject callback of an object that implements this interface.<br/>                                                                     |
| [**DSCb**](id3dx12pipelineparsercallbacks-dscb.md)                                       | Calls the domain shader subobject callback of an object that implements this interface.<br/>                                                                           |
| [**ErrorBadInputParameter**](id3dx12pipelineparsercallbacks-errorbadinputparameter.md)   | Calls the bad input parameter error callback of an object that implements this interface.<br/>                                                                         |
| [**ErrorDuplicateSubobject**](id3dx12pipelineparsercallbacks-errorduplicatesubobject.md) | Calls the duplicate subobject error callback of an object that implements this interface.<br/>                                                                         |
| [**ErrorUnknownSubobject**](id3dx12pipelineparsercallbacks-errorunknownsubobject.md)     | Calls the unknown subobject error callback of an object that implements this interface.<br/>                                                                           |
| [**FlagsCb**](id3dx12pipelineparsercallbacks-flagscb.md)                                 | Calls the flags subobject callback of an object that implements this interface.<br/>                                                                                   |
| [**GSCb**](id3dx12pipelineparsercallbacks-gscb.md)                                       | Calls the geometry shader subobject callback of an object that implements this interface.<br/>                                                                         |
| [**HSCb**](id3dx12pipelineparsercallbacks-hscb.md)                                       | Calls the hull shader subobject callback of an object that implements this interface.<br/>                                                                             |
| [**IBStripCutValueCb**](id3dx12pipelineparsercallbacks-ibstripcutvaluecb.md)             | Calls the index buffer strip-cut value subobject callback of an object that implements this interface.<br/>                                                            |
| [**InputLayoutCb**](id3dx12pipelineparsercallbacks-inputlayoutcb.md)                     | Calls the input layout subobject callback of an object that implements this interface.<br/>                                                                            |
| [**NodemaskCb**](id3dx12pipelineparsercallbacks-nodemaskcb.md)                           | Calls the nodemask subobject callback of an object that implements this interface.<br/>                                                                                |
| [**PrimitiveTopologyTypeCb**](id3dx12pipelineparsercallbacks-primitivetopologytypecb.md) | Calls the primitive topology type subobject callback of an object that implements this interface.<br/>                                                                 |
| [**PSCb**](id3dx12pipelineparsercallbacks-pscb.md)                                       | Calls the pixel shader subobject callback of an object that implements this interface.<br/>                                                                            |
| [**RasterizerStateCb**](id3dx12pipelineparsercallbacks-rasterizerstatecb.md)             | Calls the rasterizer state description subobject callback of an object that implements this interface.<br/>                                                            |
| [**RootSignatureCB**](id3dx12pipelineparsercallbacks-rootsignaturecb.md)                 | Calls the root signature subobject callback of an object that implements this interface.<br/>                                                                          |
| [**RTVFormatsCb**](id3dx12pipelineparsercallbacks-rtvformatscb.md)                       | Calls the render target format array subobject callback of an object that implements this interface.<br/>                                                              |
| [**SampleDescCb**](id3dx12pipelineparsercallbacks-sampledesccb.md)                       | Calls the sample description subobject callback of an object that implements this interface.<br/>                                                                      |
| [**SampleMaskCb**](id3dx12pipelineparsercallbacks-samplemaskcb.md)                       | Calls the sample mask subobject callback of an object that implements this interface.<br/>                                                                             |
| [**StreamOutputCb**](id3dx12pipelineparsercallbacks-streamoutputcb.md)                   | Calls the stream output description subobject callback of an object that implements this interface.<br/>                                                               |
| [**VSCb**](id3dx12pipelineparsercallbacks-vscb.md)                                       | Calls the vertex shader subobject callback of an object that implements this interface.<br/>                                                                           |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[Helper Interfaces for Direct3D 12](helper-interfaces-for-d3d12.md)
</dt> <dt>

[**D3DX12parsePipelineStream**](d3dx12parsepipelinestream.md)
</dt> </dl>

 

 





