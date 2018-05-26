---
title: ID3DX12PipelineParserCallbacks PrimitiveTopologyTypeCb method
description: Calls the primitive topology type subobject callback of an object that implements this interface.
ms.assetid: FF9D8D5C-3A6A-40D8-8EA4-3EA305EB4568
keywords:
- PrimitiveTopologyTypeCb method
- PrimitiveTopologyTypeCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, PrimitiveTopologyTypeCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.PrimitiveTopologyTypeCb
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

# ID3DX12PipelineParserCallbacks::PrimitiveTopologyTypeCb method

Calls the primitive topology type subobject callback of an object that implements this interface.

## Syntax


```C++
void PrimitiveTopologyTypeCb(
   D3D12_PRIMITIVE_TOPOLOGY_TYPE PrimitiveTopologyType
);
```



## Parameters

<dl> <dt>

*PrimitiveTopologyType* 
</dt> <dd>

Type: **[**D3D12\_PRIMITIVE\_TOPOLOGY\_TYPE**](/windows/win32/D3D12/ne-d3d12-d3d12_primitive_topology_type?branch=master)**

Details of the primitive topology type subobject parsed from a pipeline state stream.

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

[**D3D12\_PRIMITIVE\_TOPOLOGY\_TYPE**](/windows/win32/D3D12/ne-d3d12-d3d12_primitive_topology_type?branch=master)
</dt> </dl>

 

 





