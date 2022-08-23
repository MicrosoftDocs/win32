---
description: D3DXVec4CatmullRom function (D3DX10Math.h) - Performs a Catmull-Rom interpolation, using the specified 4D vectors.
ms.assetid: e3a10989-e25e-46fa-b72e-bade936cacf1
title: D3DXVec4CatmullRom function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec4CatmullRom
api_type:
- HeaderDef
api_location:
- D3DX10Math.h
---

# D3DXVec4CatmullRom function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Performs a Catmull-Rom interpolation, using the specified 4D vectors.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4CatmullRom(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR4 *pV0,
  _In_    const D3DXVECTOR4 *pV1,
  _In_    const D3DXVECTOR4 *pV2,
  _In_    const D3DXVECTOR4 *pV3,
  _In_          FLOAT       s
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) that is the result of the operation.

</dd> <dt>

*pV0* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a source D3DXVECTOR4 structure, a position vector.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a source D3DXVECTOR4 structure, a position vector.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a source D3DXVECTOR4 structure, a position vector.

</dd> <dt>

*pV3* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a source D3DXVECTOR4 structure, a position vector.

</dd> <dt>

*s* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Weighting factor. See Remarks.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a D3DXVECTOR4 structure that is the result of the Catmull-Rom interpolation.

## Remarks

Given four points (p1, p2, p3, p4), find a function Q(s) such that:


```
Q(s) is a cubic function.
Q(s) interpolates between p2 and p3 as s ranges from 0 to 1.
Q(s) is parallel to the line joining p1 to p3 when s is 0.
Q(s) is parallel to the line joining p2 to p4 when s is 1.
```



The Catmull-Rom spline can be derived from the Hermite spline by setting:


```
v1 = p2
v2 = p3
t1 = (p3 - p1) / 2
t2 = (p4 - p2) / 2
```



where:

v1 is the contents of pV0.

v2 in the contents of pV1.

p3 is the contents of pV2.

p4 is the contents of pV3.

Using the Hermite spline equation:


```
Q(s) = (2s3 - 3s2 + 1)v1 + (-2s3 + 3s2)v2 + (s3 - 2s2 + s)t1 + (s3 - s2)t2
```



and substituting for v1, v2, t1, t2 yields:


```
Q(s) = (2s3 - 3s2 + 1)p2 + (-2s3 + 3s2)p3 + (s3 - 2s2 + s)(p3 - p1) / 2 + (s3 - s2)(p4 - p2) / 2
```



This can be rearranged as:


```
Q(s) = [(-s3 + 2s2 - s)p1 + (3s3 - 5s2 + 2)p2 + (-3s3 + 4s2 + s)p3 + (s3 - s2)p4] / 2
```



## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
