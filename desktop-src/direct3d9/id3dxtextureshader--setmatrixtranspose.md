---
description: ID3DXTextureShader::SetMatrixTranspose method - Sets a transposed matrix.
ms.assetid: 5339a9de-528f-4404-880b-73964192b766
title: ID3DXTextureShader::SetMatrixTranspose method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXTextureShader.SetMatrixTranspose
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureShader::SetMatrixTranspose method

Sets a transposed matrix.

## Syntax


```C++
HRESULT SetMatrixTranspose(
  [in]       D3DXHANDLE hConstant,
  [in] const D3DXMATRIX *pMatrix
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the matrix of constants. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*pMatrix* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a transposed matrix. See [**D3DXMATRIX**](d3dxmatrix.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

A transposed matrix contains column-major data; that is, each vector is contained in a column.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




