---
description: D3DXVec3ProjectArray function (D3DX10Math.h) - Projects an array (x, y, z, 0) from object space into screen space.
ms.assetid: 33f0f65a-c027-4a31-83a7-f5f6b2a2f72f
title: D3DXVec3ProjectArray function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec3ProjectArray
api_type:
- HeaderDef
api_location:
- D3DX10Math.h
---

# D3DXVec3ProjectArray function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Projects an array (x, y, z, 0) from object space into screen space.

## Syntax


```C++
D3DXVECTOR3* D3DXVec3ProjectArray(
  _Inout_       D3DXVECTOR3    *pOut,
  _In_          UINT           OutStride,
  _In_    const D3DXVECTOR3    *pV,
  _In_          UINT           VStride,
  _In_    const D3D10_VIEWPORT *pViewport,
  _In_    const D3DXMATRIX     *pProjection,
  _In_    const D3DXMATRIX     *pView,
  _In_    const D3DXMATRIX     *pWorld,
  _In_          UINT           n
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3d10-d3dxvector3.md) that is the result of the operation.

</dd> <dt>

*OutStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Stride between vectors in the output data stream.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to the source D3DXVECTOR3 structure.

</dd> <dt>

*VStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Stride between vectors in the input data stream.

</dd> <dt>

*pViewport* \[in\]
</dt> <dd>

Type: **const [**D3D10\_VIEWPORT**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_viewport)\***

Pointer to a [**D3D10\_VIEWPORT**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_viewport), representing the viewport.

</dd> <dt>

*pProjection* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure, representing the projection matrix.

</dd> <dt>

*pView* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a D3DXMATRIX structure, representing the view matrix.

</dd> <dt>

*pWorld* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a D3DXMATRIX structure, representing the world matrix.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of elements in the array.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure that is the array projected from object space to screen space.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec3ProjectArray function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
