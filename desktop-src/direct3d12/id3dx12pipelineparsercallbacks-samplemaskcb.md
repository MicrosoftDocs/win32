---
title: ID3DX12PipelineParserCallbacks SampleMaskCb method (D3DX12.h)
description: Calls the sample mask subobject callback of an object that implements this interface.
ms.assetid: 4D729414-1E04-407B-B32F-ECE1EA9FF414
keywords:
- SampleMaskCb method
- SampleMaskCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, SampleMaskCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.SampleMaskCb
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::SampleMaskCb method

Calls the sample mask subobject callback of an object that implements this interface.

## Syntax


```C++
void SampleMaskCb(
   
        UINT
           SampleMask
);
```



## Parameters

<dl> <dt>

*SampleMask* 
</dt> <dd>

Type: **UINT**

Details of the sample mask subobject parsed from a pipeline state stream.

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
</dt> </dl>

 

 





