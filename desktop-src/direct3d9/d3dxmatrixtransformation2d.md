---
description: D3DXMatrixTransformation2D function (D3dx9math.h) - Builds a 2D transformation matrix that represents transformations in the xy plane. NULL arguments are treated as identity transformations.
ms.assetid: 671d3d67-b474-4fc1-9913-d21f05d66d9a
title: D3DXMatrixTransformation2D function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixTransformation2D
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXMatrixTransformation2D function (D3dx9math.h)

Builds a 2D transformation matrix that represents transformations in the xy plane. **NULL** arguments are treated as identity transformations.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixTransformation2D(
  _Inout_       D3DXMATRIX  *pOut,
  _In_    const D3DXVECTOR2 *pScalingCenter,
  _In_          FLOAT       pScalingRotation,
  _In_    const D3DXVECTOR2 *pScaling,
  _In_    const D3DXVECTOR2 *pRotationCenter,
  _In_          FLOAT       Rotation,
  _In_    const D3DXVECTOR2 *pTranslation
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure that contains the result of the transformations.

</dd> <dt>

*pScalingCenter* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure, a point identifying the scaling center. If this argument is **NULL**, an identity M<sub>sc</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*pScalingRotation* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The scaling rotation factor.

</dd> <dt>

*pScaling* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure, a point identifying the scale. If this argument is **NULL**, an identity Mₛ matrix is applied to the formula in Remarks.

</dd> <dt>

*pRotationCenter* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure, a point identifying the rotation center. If this argument is **NULL**, an identity M<sub>rc</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*Rotation* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The angle of rotation in radians.

</dd> <dt>

*pTranslation* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure, identifying the translation. If this argument is **NULL**, an identity Mₜ matrix is applied to the formula in Remarks.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure that contains the transformation matrix.

## Remarks

This function calculates the transformation matrix with the following formula, with matrix concatenation evaluated in left-to-right order:

M<sub>out</sub> = (M<sub>sc</sub>)⁻¹\* (M<sub>sr</sub>)⁻¹\* Mₛ \* M<sub>sr</sub> \* M<sub>sc</sub> \* (M<sub>rc</sub>)⁻¹\* M<sub>r</sub> \* M<sub>rc</sub> \* Mₜ

where:

M<sub>out</sub> = output matrix (*pOut*)

M<sub>sc</sub> = scaling center matrix (*pScalingCenter*)

M<sub>sr</sub> = scaling rotation matrix (*pScalingRotation*)

Mₛ = scaling matrix (*pScaling*)

M<sub>rc</sub> = center of rotation matrix (*pRotationCenter*)

M<sub>r</sub> = rotation matrix (*Rotation*)

Mₜ = translation matrix (*pTranslation*)

The return value for this function is the same value returned in the pOut parameter. In this way, the **D3DXMatrixTransformation2D** function can be used as a parameter for another function.

For 3D transformations, use [**D3DXMatrixTransformation**](d3dxmatrixtransformation.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXMatrixAffineTransformation2D**](d3dxmatrixaffinetransformation2d.md)
</dt> <dt>

[Transforms (Direct3D 9)](transforms.md)
</dt> </dl>

 

 
