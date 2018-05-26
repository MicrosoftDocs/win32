---
Description: Creates a texture shader object from the compiled shader.
ms.assetid: 3e8017f7-fe6b-4f4e-a80e-b16b16c0b348
title: D3DXCreateTextureShader function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to the function DWORD stream.

</dd> <dt>

*ppTextureShader* \[out\]
</dt> <dd>

Type: **[**LPD3DXTEXTURESHADER**](id3dxtextureshader.md)\***

Returns an [**ID3DXTextureShader**](id3dxtextureshader.md) object which can be used to procedurally fill the contents of a texture using the [**D3DXFillTextureTX**](d3dxfilltexturetx.md) functions.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 




