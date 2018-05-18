---
title: ID3DX12PipelineParserCallbacks InputLayoutCb method
description: Calls the input layout subobject callback of an object that implements this interface.
ms.assetid: 'A21AB7A1-6E51-42CB-BA98-C0BD08D43009'
keywords: ["InputLayoutCb method", "InputLayoutCb method, ID3DX12PipelineParserCallbacks interface", "ID3DX12PipelineParserCallbacks interface, InputLayoutCb method"]
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.InputLayoutCb
api_location:
- D3D12.dll
api_type:
- COM
---

# ID3DX12PipelineParserCallbacks::InputLayoutCb method

Calls the input layout subobject callback of an object that implements this interface.

## Syntax


```C++
void InputLayoutCb(
  [ref] const D3D12_INPUT_LAYOUT_DESC &amp;InputLayout
);
```



## Parameters

<dl> <dt>

*InputLayout* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_INPUT\_LAYOUT\_DESC**](d3d12-input-layout-desc.md)**

Details of the input layout subobject parsed from a pipeline state stream.

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

[**D3D12\_INPUT\_LAYOUT\_DESC**](d3d12-input-layout-desc.md)
</dt> </dl>

 

 





