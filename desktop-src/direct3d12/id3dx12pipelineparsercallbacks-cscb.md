---
title: ID3DX12PipelineParserCallbacks CSCb method (D3DX12.h)
description: Calls the compute shader subobject callback of an object that implements this interface.
ms.assetid: DE1ABA3D-D372-4D7F-9DB6-4E3360EAFAC2
keywords:
- CSCb method
- CSCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, CSCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.CSCb
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::CSCb method

Calls the compute shader subobject callback of an object that implements this interface.

## Syntax


```C++
void CSCb(
  [ref] const D3D12_SHADER_BYTECODE &CS
);
```



## Parameters

<dl> <dt>

*CS* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_SHADER\_BYTECODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_shader_bytecode)**

Details of the compute shader subobject parsed from a pipeline state stream.

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

 

 





