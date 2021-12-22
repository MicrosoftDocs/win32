---
title: ID3DX12PipelineParserCallbacks ErrorBadInputParameter method (D3DX12.h)
description: Calls the bad input parameter error callback of an object that implements this interface.
ms.assetid: CB1F9A77-B120-4D72-99D3-16594E668520
keywords:
- ErrorBadInputParameter method
- ErrorBadInputParameter method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, ErrorBadInputParameter method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.ErrorBadInputParameter
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::ErrorBadInputParameter method

Calls the bad input parameter error callback of an object that implements this interface.

## Syntax


```C++
void ErrorBadInputParameter(
   
        UINT
           ParameterIndex
);
```



## Parameters

<dl> <dt>

*ParameterIndex* 
</dt> <dd>

Type: **UINT**

The position of the parameter that contains bad input. The left-most parameter is at position 1, not position 0.

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

 

 





