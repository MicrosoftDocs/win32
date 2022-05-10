---
description: D3DXMatrixPerspectiveFovRH function (D3DX10Math.h) - Builds a right-handed perspective projection matrix based on a field of view.
ms.assetid: a75e6666-e6c0-4a54-bc88-835fa012542f
title: D3DXMatrixPerspectiveFovRH function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXMatrixPerspectiveFovRH
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixPerspectiveFovRH function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Builds a right-handed perspective projection matrix based on a field of view.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixPerspectiveFovRH(
  _Inout_ D3DXMATRIX *pOut,
  _In_    FLOAT      fovy,
  _In_    FLOAT      Aspect,
  _In_    FLOAT      zn,
  _In_    FLOAT      zf
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*fovy* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Field of view in the y direction, in radians.

</dd> <dt>

*Aspect* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Aspect ratio, defined as view space width divided by height.

</dd> <dt>

*zn* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Z-value of the near view-plane.

</dd> <dt>

*zf* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Z-value of the far view-plane.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a D3DXMATRIX structure that is a right-handed perspective projection matrix.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixPerspectiveFovRH function can be used as a parameter for another function.

This function computes the returned matrix as shown.


```
xScale     0          0              0
0        yScale       0              0
0          0      zf/(zn-zf)        -1
0          0      zn*zf/(zn-zf)      0
where:
yScale = cot(fovY/2)

xScale = yScale / aspect ratio
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

 

 
