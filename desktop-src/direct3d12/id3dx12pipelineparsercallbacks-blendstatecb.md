---
title: ID3DX12PipelineParserCallbacks BlendStateCb method
description: Calls the blend state description subobject callback of an object that implements this interface.
ms.assetid: C00C733B-4123-4795-9A93-973F30BE456B
keywords:
- BlendStateCb method
- BlendStateCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, BlendStateCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.BlendStateCb
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

# ID3DX12PipelineParserCallbacks::BlendStateCb method

Calls the blend state description subobject callback of an object that implements this interface.

## Syntax


```C++
void BlendStateCb(
  [ref] const D3D12_BLEND_DESC &amp;BlendState
);
```



## Parameters

<dl> <dt>

*BlendState* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_BLEND\_DESC**](/windows/win32/D3D12/ns-d3d12-d3d12_blend_desc?branch=master)**

Details of the blend state description subobject parsed from a pipeline state stream.

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

[**D3D12\_BLEND\_DESC**](/windows/win32/D3D12/ns-d3d12-d3d12_blend_desc?branch=master)
</dt> </dl>

 

 





