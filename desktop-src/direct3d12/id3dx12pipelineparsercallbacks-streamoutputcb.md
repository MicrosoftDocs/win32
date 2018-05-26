---
title: ID3DX12PipelineParserCallbacks StreamOutputCb method
description: Calls the stream output description subobject callback of an object that implements this interface.
ms.assetid: 93447ABE-A942-4562-A532-600EC63072DA
keywords:
- StreamOutputCb method
- StreamOutputCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, StreamOutputCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.StreamOutputCb
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

# ID3DX12PipelineParserCallbacks::StreamOutputCb method

Calls the stream output description subobject callback of an object that implements this interface.

## Syntax


```C++
void StreamOutputCb(
  [ref] const D3D12_STREAM_OUTPUT_DESC &amp;StreamOutput
);
```



## Parameters

<dl> <dt>

*StreamOutput* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_STREAM\_OUTPUT\_DESC**](/windows/win32/D3D12/ns-d3d12-d3d12_stream_output_desc?branch=master)**

Details of the stream output description subobject parsed from a pipeline state stream.

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

[**D3D12\_STREAM\_OUTPUT\_DESC**](/windows/win32/D3D12/ns-d3d12-d3d12_stream_output_desc?branch=master)
</dt> </dl>

 

 





