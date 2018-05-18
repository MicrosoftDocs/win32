---
title: ID3DX12PipelineParserCallbacks CachedPSOCb method
description: Calls the cached PSO (Pipeline State Object) subobject callback of an object that implements this interface.
ms.assetid: '9EF8C468-1D86-4F49-9091-36B6125F1B68'
keywords: ["CachedPSOCb method", "CachedPSOCb method, ID3DX12PipelineParserCallbacks interface", "ID3DX12PipelineParserCallbacks interface, CachedPSOCb method"]
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.CachedPSOCb
api_location:
- D3D12.dll
api_type:
- COM
---

# ID3DX12PipelineParserCallbacks::CachedPSOCb method

Calls the cached PSO (Pipeline State Object) subobject callback of an object that implements this interface.

## Syntax


```C++
void CachedPSOCb(
  [ref] const D3D12_CACHED_PIPELINE_STATE &amp;CachedPSO
);
```



## Parameters

<dl> <dt>

*CachedPSO* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_CACHED\_PIPELINE\_STATE**](d3d12-cached-pipeline-state.md)**

Details of the cached PSO (Pipeline State Object) subobject parsed from a pipeline state stream.

</dd> </dl>

## Return value

Returns nothing.

## Requirements



|                    |                                                                                      |
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

[**D3D12\_CACHED\_PIPELINE\_STATE**](d3d12-cached-pipeline-state.md)
</dt> </dl>

 

 





