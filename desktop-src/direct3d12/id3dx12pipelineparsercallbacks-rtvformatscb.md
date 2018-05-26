---
title: ID3DX12PipelineParserCallbacks RTVFormatsCb method
description: Calls the render target format array subobject callback of an object that implements this interface.
ms.assetid: 0D5F0BC4-D9E2-4B16-99B5-509454AF8C02
keywords:
- RTVFormatsCb method
- RTVFormatsCb method, ID3DX12PipelineParserCallbacks interface
- ID3DX12PipelineParserCallbacks interface, RTVFormatsCb method
topic_type:
- apiref
api_name:
- ID3DX12PipelineParserCallbacks.RTVFormatsCb
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

# ID3DX12PipelineParserCallbacks::RTVFormatsCb method

Calls the render target format array subobject callback of an object that implements this interface.

## Syntax


```C++
void RTVFormatsCb(
  [ref] const D3D12_RT_FORMAT_ARRAY &amp;RTVFormats
);
```



## Parameters

<dl> <dt>

*RTVFormats* \[ref\]
</dt> <dd>

Type: **const [**D3D12\_RT\_FORMAT\_ARRAY**](/windows/win32/d3d12/ns-d3d12-d3d12_rt_format_array?branch=master)**

Details of the render target format array subobject parsed from a pipeline state stream.

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

[**D3D12\_RT\_FORMAT\_ARRAY**](/windows/win32/d3d12/ns-d3d12-d3d12_rt_format_array?branch=master)
</dt> </dl>

 

 





