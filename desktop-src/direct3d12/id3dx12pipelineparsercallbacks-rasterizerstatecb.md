---
title: ID3DX12PipelineParserCallbacks RasterizerStateCb method (D3DX12.h)
description: Calls the rasterizer state description subobject callback of an object that implements this interface.
ms.assetid: 125FC6EC-B749-4EE2-9D34-14BD12993BDC
keywords:
- RasterizerStateCb method
- RasterizerStateCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, RasterizerStateCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.RasterizerStateCb
api_location:
- D3D12.dll
api_type:
- COM
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::RasterizerStateCb method

Calls the rasterizer state description subobject callback of an object that implements this interface.

## Syntax


```C++
void RasterizerStateCb(
  [ref] const D3D12_RASTERIZER_DESC &RasterizerState
);
```



## Parameters

<dl> <dt>

*RasterizerState* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_RASTERIZER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_rasterizer_desc)**

Details of the rasterizer state description subobject parsed from a pipeline state stream.

</dd> </dl>

## Return value

Returns nothing.

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

[**ID3DX12PipelineParserCallbacks**](id3dx12pipelineparsercallbacks.md)
</dt> <dt>

[**D3D12\_RASTERIZER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_rasterizer_desc)
</dt> </dl>

 

 





