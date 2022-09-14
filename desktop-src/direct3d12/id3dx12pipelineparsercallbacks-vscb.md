---
title: ID3DX12PipelineParserCallbacks VSCb method (D3DX12.h)
description: Calls the vertex shader subobject callback of an object that implements this interface.
ms.assetid: 65A185B7-C790-4254-A3C5-EBBE9C38CA4E
keywords:
- VSCb method
- VSCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, VSCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.VSCb
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::VSCb method

Calls the vertex shader subobject callback of an object that implements this interface.

## Syntax


```C++
void VSCb(
  [ref] const D3D12_SHADER_BYTECODE &VS
);
```



## Parameters

<dl> <dt>

*VS* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_SHADER\_BYTECODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_shader_bytecode)**

Details of the vertex shader subobject parsed from a pipeline state stream.

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

[**D3D12\_SHADER\_BYTECODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_shader_bytecode)
</dt> </dl>

 

 





