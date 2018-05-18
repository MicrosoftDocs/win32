---
title: ID3DX12PipelineParserCallbacks IBStripCutValueCb method
description: Calls the index buffer strip-cut value subobject callback of an object that implements this interface.
ms.assetid: '702CA90A-FF20-4554-9469-C86428C203BC'
keywords: ["IBStripCutValueCb method", "IBStripCutValueCb method, ID3DX12PipelineParserCallbacks interface", "ID3DX12PipelineParserCallbacks interface, IBStripCutValueCb method"]
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.IBStripCutValueCb
api_location:
- D3D12.dll
api_type:
- COM
---

# ID3DX12PipelineParserCallbacks::IBStripCutValueCb method

Calls the index buffer strip-cut value subobject callback of an object that implements this interface.

## Syntax


```C++
void IBStripCutValueCb(
   D3D12_INDEX_BUFFER_STRIP_CUT_VALUE IBStripCutValue
);
```



## Parameters

<dl> <dt>

*IBStripCutValue* 
</dt> <dd>

Type: **[**D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE**](d3d12-index-buffer-strip-cut-value.md)**

Details of the index buffer strip-cut value subobject parsed from a pipeline state stream.

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

[**D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE**](d3d12-index-buffer-strip-cut-value.md)
</dt> </dl>

 

 





