---
description: Gets a nontransposed matrix.
ms.assetid: d507c82c-b1a5-4e83-8921-5d45f52faba0
title: ID3DXBaseEffect::GetMatrix method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetMatrix
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetMatrix method

Gets a nontransposed matrix.

## Syntax


```C++
HRESULT GetMatrix(
  [in]  D3DXHANDLE hParameter,
  [out] D3DXMATRIX *pMatrix
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pMatrix* \[out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Returns a nontransposed matrix. See [**D3DXMATRIX**](d3dxmatrix.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

A nontransposed matrix contains row-major data; that is, each vector is contained in a row.

If the destination matrix is larger than the source matrix, only the upper-left components of the destination matrix will be filled, and the remaining components will be set to zero.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**SetMatrix**](id3dxbaseeffect--setmatrix.md)
</dt> </dl>

 

 




