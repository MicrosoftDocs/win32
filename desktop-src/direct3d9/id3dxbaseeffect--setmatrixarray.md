---
description: Sets an array of nontransposed matrices.
ms.assetid: 008de62c-3a36-4499-8a0b-9075756395e9
title: ID3DXBaseEffect::SetMatrixArray method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.SetMatrixArray
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::SetMatrixArray method

Sets an array of nontransposed matrices.

## Syntax


```C++
HRESULT SetMatrixArray(
  [in]       D3DXHANDLE hParameter,
  [in] const D3DXMATRIX *pMatrix,
  [in]       UINT       Count
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pMatrix* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Array of nontransposed matrices. See [**D3DXMATRIX**](d3dxmatrix.md).

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of matrices in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

A nontransposed matrix contains row-major data; that is, each vector is contained in a row.

If the destination matrices are smaller than the source matrices, the additional components of the source matrices will be ignored.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**GetMatrixArray**](id3dxbaseeffect--getmatrixarray.md)
</dt> </dl>

 

 
