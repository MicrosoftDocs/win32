---
title: ID3DX12PipelineParserCallbacks ErrorUnknownSubobject method (D3DX12.h)
description: Calls the unknown subobject error callback of an object that implements this interface.
ms.assetid: 612D7C44-4DC5-4DEA-B369-09C27123D45E
keywords:
- ErrorUnknownSubobject method
- ErrorUnknownSubobject method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, ErrorUnknownSubobject method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.ErrorUnknownSubobject
api_location:
- D3D12.dll
api_type:
- COM
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX12PipelineParserCallbacks::ErrorUnknownSubobject method

Calls the unknown subobject error callback of an object that implements this interface.

## Syntax


```C++
void ErrorUnknownSubobject(
   
        UINT
           UnknownTypeValue
);
```



## Parameters

<dl> <dt>

*UnknownTypeValue* 
</dt> <dd>

Type: **UINT**

The unrecognized subobject type of the attempted subobject.

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

 

 





