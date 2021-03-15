---
description: Builds a left-handed perspective projection matrix
ms.assetid: 07bbbca8-ad1e-4177-97d4-601b33179b47
title: D3DXMatrixPerspectiveLH function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixPerspectiveLH
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXMatrixPerspectiveLH function (D3dx9math.h)

Builds a left-handed perspective projection matrix

## Syntax


```C++
D3DXMATRIX* D3DXMatrixPerspectiveLH(
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

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*w* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Width of the view volume at the near view-plane.

</dd> <dt>

*h* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Height of the view volume at the near view-plane.

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

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure that is a left-handed perspective projection matrix.

## Remarks

All the parameters of the **D3DXMatrixPerspectiveLH** function are distances in camera space. The parameters describe the dimensions of the view volume.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixPerspectiveLH** function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
2*zn/w  0       0              0
0       2*zn/h  0              0
0       0       zf/(zf-zn)     1
0       0       zn*zf/(zn-zf)  0
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

[**D3DXMatrixPerspectiveRH**](d3dxmatrixperspectiverh.md)
</dt> <dt>

[**D3DXMatrixPerspectiveFovRH**](d3dxmatrixperspectivefovrh.md)
</dt> <dt>

[**D3DXMatrixPerspectiveFovLH**](d3dxmatrixperspectivefovlh.md)
</dt> <dt>

[**D3DXMatrixPerspectiveOffCenterRH**](d3dxmatrixperspectiveoffcenterrh.md)
</dt> <dt>

[**D3DXMatrixPerspectiveOffCenterLH**](d3dxmatrixperspectiveoffcenterlh.md)
</dt> </dl>

 

 
