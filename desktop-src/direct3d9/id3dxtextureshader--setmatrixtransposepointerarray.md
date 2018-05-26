---
Description: Sets an array of pointers to transposed matrices.
ms.assetid: 2b9f1efe-b2ea-416b-a370-202db57b1925
title: ID3DXTextureShaderSetMatrixTransposePointerArray method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXTextureShader::SetMatrixTransposePointerArray method

Sets an array of pointers to transposed matrices.

## Syntax


```C++
HRESULT SetMatrixTransposePointerArray(
  [in]       D3DXHANDLE hConstant,
  [in] const D3DXMATRIX **ppMatrix,
  [in]       UINT       Count
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the array of matrix constants. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*ppMatrix* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\*\***

Array of pointers to transposed matrices. See [**D3DXMATRIX**](d3dxmatrix.md).

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of matrices in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

A transposed matrix contains column-major data; that is, each vector is contained in a column.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




