---
title: ID3DX12PipelineParserCallbacks PSCb method
description: Calls the pixel shader subobject callback of an object that implements this interface.
ms.assetid: 3397B018-C26A-426F-88BB-89013BACBEEA
keywords:
- PSCb method
- PSCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, PSCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.PSCb
api_location:
- D3D12.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX12PipelineParserCallbacks::PSCb method

Calls the pixel shader subobject callback of an object that implements this interface.

## Syntax


```C++
void PSCb(
  [ref] const D3D12_SHADER_BYTECODE &amp;PS
);
```



## Parameters

<dl> <dt>

*PS* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_SHADER\_BYTECODE**](/windows/win32/D3D12/ns-d3d12-d3d12_shader_bytecode?branch=master)**

Details of the pixel shader subobject parsed from a pipeline state stream.

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

[**D3D12\_SHADER\_BYTECODE**](/windows/win32/D3D12/ns-d3d12-d3d12_shader_bytecode?branch=master)
</dt> </dl>

 

 





