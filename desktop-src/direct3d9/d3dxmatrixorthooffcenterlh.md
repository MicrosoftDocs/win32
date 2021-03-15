---
description: Builds a customized, left-handed orthographic projection matrix.
ms.assetid: e4f087e5-63d9-49ca-9d8e-3a25070e1a51
title: D3DXMatrixOrthoOffCenterLH function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixOrthoOffCenterLH
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXMatrixOrthoOffCenterLH function (D3dx9math.h)

Builds a customized, left-handed orthographic projection matrix.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixOrthoOffCenterLH(
  _Inout_ D3DXMATRIX *pOut,
  _In_    FLOAT      l,
  _In_    FLOAT      r,
  _In_    FLOAT      b,
  _In_    FLOAT      t,
  _In_    FLOAT      zn,
  _In_    FLOAT      zf
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the resulting [**D3DXMATRIX**](../direct3d10/d3d10-d3dxmatrix.md).

</dd> <dt>

*l* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Minimum x-value of view volume.

</dd> <dt>

*r* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Maximum x-value of view volume.

</dd> <dt>

*b* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Minimum y-value of view volume.

</dd> <dt>

*t* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Maximum y-value of view volume.

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

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the resulting [**D3DXMATRIX**](../direct3d10/d3d10-d3dxmatrix.md).

## Remarks

The [**D3DXMatrixOrthoLH**](d3dxmatrixortholh.md) function is a special case of the **D3DXMatrixOrthoOffCenterLH** function. To create the same projection using **D3DXMatrixOrthoOffCenterLH**, use the following values: l = -w/2, r = w/2, b = -h/2, and t = h/2.

All the parameters of the **D3DXMatrixOrthoOffCenterLH** function are distances in camera space. The parameters describe the dimensions of the view volume.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixOrthoOffCenterLH** function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
2/(r-l)      0            0           0
0            2/(t-b)      0           0
0            0            1/(zf-zn)   0
(l+r)/(l-r)  (t+b)/(b-t)  zn/(zn-zf)  1
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXMatrixOrthoRH**](d3dxmatrixorthorh.md)
</dt> <dt>

[**D3DXMatrixOrthoLH**](d3dxmatrixortholh.md)
</dt> <dt>

[**D3DXMatrixOrthoOffCenterRH**](d3dxmatrixorthooffcenterrh.md)
</dt> </dl>

 

 
