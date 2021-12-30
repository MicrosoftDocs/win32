---
title: ID3DX12PipelineParserCallbacks GSCb method (D3DX12.h)
description: Calls the geometry shader subobject callback of an object that implements this interface.
ms.assetid: 0D8846C5-15E4-43EB-AA82-163BB514C5B7
keywords:
- GSCb method
- GSCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, GSCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.GSCb
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::GSCb method

Calls the geometry shader subobject callback of an object that implements this interface.

## Syntax


```C++
void GSCb(
  [ref] const D3D12_SHADER_BYTECODE &GS
);
```



## Parameters

<dl> <dt>

*GS* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_SHADER\_BYTECODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_shader_bytecode)**

Details of the geometry shader subobject parsed from a pipeline state stream.

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

 

 





