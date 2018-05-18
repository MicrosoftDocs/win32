---
title: D3DDisassemble10Effect function
description: Disassembles compiled HLSL code from a Direct3D10 effect.
ms.assetid: 'fb6668ae-db7f-4d69-aed4-4b50f3a2b315'
keywords: ["D3DDisassemble10Effect function HLSL"]
topic_type:
- apiref
api_name:
- D3DDisassemble10Effect
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
---

# D3DDisassemble10Effect function

Disassembles compiled HLSL code from a Direct3D10 effect.

## Syntax

``` syntax
HRESULT WINAPI D3DDisassemble10Effect(
  in  ID3D10Effect pEffect,
  in  UINT Flags,
  out ID3DBlob ppDisassembly
);
```

## Parameters

<dl> <dt>

*pEffect* \[in\]
</dt> <dd>

Type: **[**ID3D10Effect**](https://msdn.microsoft.com/library/windows/desktop/bb173630)\***

A pointer to source data as compiled HLSL code.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Shader [compile options](http://msdn.microsoft.com/library/bb172416(VS.85).aspx).

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that contains disassembly text.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3dcompiler\_47.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3dcompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





