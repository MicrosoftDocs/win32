---
title: D3DStripShader function
description: Removes unwanted blobs from a compilation result.
ms.assetid: 'd6f51f57-02e1-485d-8f49-60a9bfb62cf5'
keywords: ["D3DStripShader function HLSL"]
topic_type:
- apiref
api_name:
- D3DStripShader
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
---

# D3DStripShader function

Removes unwanted blobs from a compilation result.

## Syntax

``` syntax
HRESULT WINAPI D3DStripShader(
  in  LPCVOID pShaderBytecode,
  in  SIZE_T BytecodeLength,
  in  UINT uStripFlags,
  out ID3DBlob ppStrippedBlob
);
```

## Parameters

<dl> <dt>

*pShaderBytecode* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to source data as compiled HLSL code.

</dd> <dt>

*BytecodeLength* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of *pSrcData*.

</dd> <dt>

*uStripFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Strip flag options, represented by [**D3DCOMPILER\_STRIP\_FLAGS**](d3dcompiler-strip-flags.md).

</dd> <dt>

*ppStrippedBlob* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access the unwanted stripped out shader code.

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

 

 





