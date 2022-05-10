---
description: D3DXMatrixOrthoRH function (D3DX10Math.h) - Builds a right-handed orthographic projection matrix.
ms.assetid: e6673ff4-06a2-4a16-b72e-5ca69ddf2438
title: D3DXMatrixOrthoRH function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXMatrixOrthoRH
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixOrthoRH function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Builds a right-handed orthographic projection matrix.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixOrthoRH(
  _Inout_ D3DXMATRIX *pOut,
  _In_    FLOAT      w,
  _In_    FLOAT      h,
  _In_    FLOAT      zn,
  _In_    FLOAT      zf
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the resulting [**D3DXMATRIX**](d3d10-d3dxmatrix.md).

</dd> <dt>

*w* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Width of the view volume.

</dd> <dt>

*h* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Height of the view volume.

</dd> <dt>

*zn* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Minimum z-value of the view volume.

</dd> <dt>

*zf* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Maximum z-value of the view volume.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the resulting [**D3DXMATRIX**](d3d10-d3dxmatrix.md).

## Remarks

All the parameters of the D3DXMatrixOrthoRH function are distances in camera space. The parameters describe the dimensions of the view volume.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixOrthoRH function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
2/w  0    0           0
0    2/h  0           0
0    0    1/(zn-zf)   0
0    0    zn/(zn-zf)  1
```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
