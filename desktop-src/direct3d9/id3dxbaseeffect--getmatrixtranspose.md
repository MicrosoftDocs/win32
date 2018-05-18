---
Description: 'Gets a transposed matrix.'
ms.assetid: '255c1e20-0a60-49eb-abaa-66a67322ce73'
title: 'ID3DXBaseEffect::GetMatrixTranspose method'
---

# ID3DXBaseEffect::GetMatrixTranspose method

Gets a transposed matrix.

## Syntax


```C++
HRESULT GetMatrixTranspose(
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

Returns a transposed matrix. See [**D3DXMATRIX**](d3dxmatrix.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

A transposed matrix contains column-major data; that is, each vector is contained in a column.

If the destination matrix is larger than the source matrix, only the upper-left elements of the destination matrix will be filled, and the remaining destination matrix components will be set to zero.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**SetMatrixTranspose**](id3dxbaseeffect--setmatrixtranspose.md)
</dt> </dl>

 

 




