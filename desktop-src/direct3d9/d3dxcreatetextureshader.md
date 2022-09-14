---
description: Creates a texture shader object from the compiled shader.
ms.assetid: 3e8017f7-fe6b-4f4e-a80e-b16b16c0b348
title: D3DXCreateTextureShader function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCreateTextureShader
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreateTextureShader function

Creates a texture shader object from the compiled shader.

## Syntax


```C++
HRESULT D3DXCreateTextureShader(
  _In_  const DWORD               *pFunction,
  _Out_       LPD3DXTEXTURESHADER *ppTextureShader
);
```



## Parameters

<dl> <dt>

*pFunction* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the function DWORD stream.

</dd> <dt>

*ppTextureShader* \[out\]
</dt> <dd>

Type: **[**LPD3DXTEXTURESHADER**](id3dxtextureshader.md)\***

Returns an [**ID3DXTextureShader**](id3dxtextureshader.md) object which can be used to procedurally fill the contents of a texture using the [**D3DXFillTextureTX**](d3dxfilltexturetx.md) functions.

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

 

 
