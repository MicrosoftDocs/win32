---
description: D3DXMatrixTransformation function (D3DX10Math.h) - Builds a transformation matrix. NULL arguments are treated as identity transformations.
ms.assetid: 99c75ce9-3683-4753-b635-760eb8aaf46e
title: D3DXMatrixTransformation function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXMatrixTransformation
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixTransformation function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Builds a transformation matrix. **NULL** arguments are treated as identity transformations.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixTransformation(
  _Inout_       D3DXMATRIX     *pOut,
  _In_    const D3DXVECTOR3    *pScalingCenter,
  _In_    const D3DXQUATERNION *pScalingRotation,
  _In_    const D3DXVECTOR3    *pScaling,
  _In_    const D3DXVECTOR3    *pRotationCenter,
  _In_    const D3DXQUATERNION *pRotation,
  _In_    const D3DXVECTOR3    *pTranslation
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pScalingCenter* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md), identifying the scaling center point. If this argument is **NULL**, an identity M<sub>sc</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*pScalingRotation* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a [**D3DXQUATERNION**](d3d10-d3dxquaternion.md) that specifies the scaling rotation. If this argument is **NULL**, an identity M<sub>sr</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*pScaling* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure, the scaling vector. If this argument is **NULL**, an identity Mₛ matrix is applied to the formula in Remarks.

</dd> <dt>

*pRotationCenter* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure, a point that identifies the center of rotation. If this argument is **NULL**, an identity M<sub>rc</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*pRotation* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a D3DXQUATERNION structure that specifies the rotation. If this argument is **NULL**, an identity M<sub>r</sub> matrix is applied to the formula in Remarks.

</dd> <dt>

*pTranslation* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure, representing the translation. If this argument is **NULL**, an identity Mₜ matrix is applied to the formula in Remarks.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a D3DXMATRIX structure that is the transformation matrix.

## Remarks

This function calculates the transformation matrix with the following formula, with matrix concatenation evaluated in left-to-right order:

M<sub>out</sub> = (M<sub>sc</sub>)⁻¹ \* (M<sub>sr</sub>)⁻¹\* Mₛ \* M<sub>sr</sub> \* M<sub>sc</sub> \* (M<sub>rc</sub>)⁻¹\* M<sub>r</sub> \* M<sub>rc</sub> \* Mt

where:

M<sub>out</sub> = output matrix (pOut)

M<sub>sc</sub> = scaling center matrix (pScalingCenter)

M<sub>sr</sub> = scaling rotation matrix (pScalingRotation)

Mₛ = scaling matrix (pScaling)

M<sub>rc</sub> = center of rotation matrix (pRotationCenter)

M<sub>r</sub> = rotation matrix (pRotation)

Mₜ = translation matrix (pTranslation)

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixTransformation function can be used as a parameter for another function.

For 2D transformations, use [**D3DXMatrixTransformation2D**](d3d10-d3dxmatrixtransformation2d.md).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
