---
title: ID3DX12PipelineParserCallbacks DepthStencilStateCb method (D3DX12.h) (DSV)
description: Calls the depth stencil value format subobject callback of an object that implements this interface.
ms.assetid: BDD3AB24-34C6-41C8-984D-78A45867BF24
keywords:
- DepthStencilStateCb method
- DepthStencilStateCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, DepthStencilStateCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.DepthStencilStateCb
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks DepthStencilStateCb method (D3DX12.h) for depth stencil value

Calls the depth stencil value format subobject callback of an object that implements this interface.

## Syntax


```C++
void DepthStencilStateCb(
   DXGI_FORMAT DepthStencilState
);
```



## Parameters

<dl> <dt>

*DepthStencilState* 
</dt> <dd>

Type: **[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)**

Details of the depth stencil value format subobject parsed from a pipeline state stream.

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

[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)
</dt> </dl>

 

