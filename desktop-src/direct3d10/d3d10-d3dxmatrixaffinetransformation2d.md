---
description: Builds a 2D affine transformation matrix in the x-y plane. NULL arguments are treated as identity transformations.
ms.assetid: f46a307c-4566-42c8-8def-fb189116144e
title: D3DXMatrixAffineTransformation2D function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixAffineTransformation2D
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixAffineTransformation2D function (D3DX10Math.h)

Builds a 2D affine transformation matrix in the x-y plane. **NULL** arguments are treated as identity transformations.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixAffineTransformation2D(
  _In_       D3DXMATRIX  *pOut,
  _In_       FLOAT       Scaling,
  _In_ const D3DXVECTOR2 *pRotationCenter,
  _In_       FLOAT       Rotation,
  _In_ const D3DXVECTOR2 *pTranslation
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) that is the result of the operation.

</dd> <dt>

*Scaling* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Scaling factor.

</dd> <dt>

*pRotationCenter* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](../direct3d9/d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3d10-d3dxvector2.md), a point identifying the center of rotation. If this argument is **NULL**, an identity M<sub>rc</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*Rotation* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The angle of rotation.

</dd> <dt>

*pTranslation* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](../direct3d9/d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3d10-d3dxvector2.md), representing the translation. If this argument is **NULL**, an identity Mₜ matrix is applied to the formula in Remarks.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a D3DXMATRIX structure that is an affine transformation matrix.

## Remarks

This function calculates the affine transformation matrix with the following formula, with matrix concatenation evaluated in left-to-right order:

M<sub>out</sub> = Mₛ \* (M<sub>rc</sub>)-1 \* M<sub>r</sub> \* M<sub>rc</sub> \* Mₜ

where:

M<sub>out</sub> = output matrix (pOut)

Mₛ = scaling matrix (Scaling)

M<sub>rc</sub> = center of rotation matrix (pRotationCenter)

M<sub>r</sub> = rotation matrix (Rotation)

Mₜ = translation matrix (pTranslation)

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixAffineTransformation2D function can be used as a parameter for another function.

For 3D affine transformations, use D3DXMatrixAffineTransformation.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
