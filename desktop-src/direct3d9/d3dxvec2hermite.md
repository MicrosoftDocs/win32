---
description: D3DXVec2Hermite function (D3dx9math.h) - Performs a Hermite spline interpolation, using the specified 2D vectors.
ms.assetid: 30eb9490-bc01-4449-adfb-1c552e8ad3e7
title: D3DXVec2Hermite function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec2Hermite
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec2Hermite function (D3dx9math.h)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Performs a Hermite spline interpolation, using the specified 2D vectors.

## Syntax


```C++
D3DXVECTOR2* D3DXVec2Hermite(
  _Inout_       D3DXVECTOR2 *pOut,
  _In_    const D3DXVECTOR2 *pV1,
  _In_    const D3DXVECTOR2 *pT1,
  _In_    const D3DXVECTOR2 *pV2,
  _In_    const D3DXVECTOR2 *pT2,
  _In_          FLOAT       s
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the [**D3DXVECTOR2**](d3dxvector2.md) structure that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure, a position vector.

</dd> <dt>

*pT1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure, a tangent vector.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure, a position vector.

</dd> <dt>

*pT2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure, a tangent vector.

</dd> <dt>

*s* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Weighting factor. See Remarks.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure that is the result of the Hermite spline interpolation.

## Remarks

The **D3DXVec2Hermite** function interpolates from (positionA, tangentA) to (positionB, tangentB) using Hermite spline interpolation.

The spline interpolation is a generalization of the ease-in, ease-out spline. The ramp is a function of Q(s) with the following properties.

Q(s) = As³ + Bs² + Cs + D (and therefore, Q'(s) = 3As² + 2Bs + C)

a) Q(0) = v1, so Q'(0) = t1

b) Q(1) = v2, so Q'(1) = t2

v1 is the contents of pV1, v2 in the contents of pV2, t1 is the contents of pT1, and t2 is the contents of pT2.

These properties are used to solve for A, B, C, D.

``` syntax
D = v1  (from a)
C = t1  (from a)
3A + 2B = t2 - t-1 (substituting for C)
A + B = v2 - v1 - t1 (substituting for C and D)
```

Plug in the solutions for A,B,C and D to generate Q(s).

``` syntax
A = 2v1 - 2v2 + t2 + t1
B = 3v2 - 3v1 - 2t1 - t2
C = t1
D = v1
```

This yields:

Q(s) = (2v1 - 2v2 + t2 + t1)s³ + (3v2 - 3v1 - 2t1 - t2)s² + t1s + v1

Which can be rearranged as:

Q(s) = (2s³ - 3s² + 1)v1 + (-2s³ + 3s²)v2 + (s³ - 2s² + s)t1 + (s³ - s²)t2

Hermite splines are useful for controlling animation because the curve runs through all the control points. Also, because the position and tangent are explicitly specified at the ends of each segment, it is easy to create a C2 continuous curve as long as you make sure that your starting position and tangent match the ending values of the last segment.

The return value for this function is the same value returned in the pOut parameter. In this way, the **D3DXVec2Hermite** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
