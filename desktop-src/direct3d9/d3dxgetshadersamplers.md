---
description: Get the sampler names referenced in a shader.
ms.assetid: fe769917-daac-43b8-bf63-fb337915ff53
title: D3DXGetShaderSamplers function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXGetShaderSamplers
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXGetShaderSamplers function

Get the sampler names referenced in a shader.

## Syntax


```C++
HRESULT D3DXGetShaderSamplers(
  _In_    const DWORD  *pFunction,
  _Inout_       LPCSTR *pSamplers,
  _Out_         UINT   *pCount
);
```



## Parameters

<dl> <dt>

*pFunction* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the shader function DWORD stream.

</dd> <dt>

*pSamplers* \[in, out\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)\***

Pointer to an array of LPCSTRs. The function will fill this array with pointers to the sampler names contained within *pFunction*. The maximum array size is the maximum number of sampler registers (16 for vs\_3\_0 and ps\_3\_0).

To find the number of samplers used, check *pCount* after calling **D3DXGetShaderSamplers** with pSamplers = **NULL**.

</dd> <dt>

*pCount* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Returns the number of samplers referenced by the shader.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 
