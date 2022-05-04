---
description: D3DXPlaneFromPoints function (D3DX10Math.h) - Constructs a plane from three points.
ms.assetid: 0e77af1b-cedf-482c-8398-10becb398a2c
title: D3DXPlaneFromPoints function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXPlaneFromPoints
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXPlaneFromPoints function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Constructs a plane from three points.

## Syntax


```C++
D3DXPLANE* D3DXPlaneFromPoints(
  _Inout_       D3DXPLANE   *pOut,
  _In_    const D3DXVECTOR3 *pV1,
  _In_    const D3DXVECTOR3 *pV2,
  _In_    const D3DXVECTOR3 *pV3
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to the [**D3DXPLANE**](d3d10-d3dxplane.md) that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md), defining one of the points used to construct the plane.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure, defining one of the points used to construct the plane.

</dd> <dt>

*pV3* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure, defining one of the points used to construct the plane.

</dd> </dl>

## Return value

Type: **[**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to the D3DXPLANE structure constructed from the given points.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXPlaneFromPoints function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
