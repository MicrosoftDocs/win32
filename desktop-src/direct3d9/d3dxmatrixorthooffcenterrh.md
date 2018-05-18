---
Description: 'Builds a customized, right-handed orthographic projection matrix.'
ms.assetid: 'd6171e28-b138-4ccf-9f12-fb977a30aca1'
title: D3DXMatrixOrthoOffCenterRH function
---

# D3DXMatrixOrthoOffCenterRH function

Builds a customized, right-handed orthographic projection matrix.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixOrthoOffCenterRH(
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

Pointer to the resulting [**D3DXMATRIX**](direct3d10.d3d10_d3dxmatrix).

</dd> <dt>

*l* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Minimum x-value of view volume.

</dd> <dt>

*r* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Maximum x-value of view volume.

</dd> <dt>

*b* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Minimum y-value of view volume.

</dd> <dt>

*t* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Maximum y-value of view volume.

</dd> <dt>

*zn* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Minimum z-value of the view volume.

</dd> <dt>

*zf* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Maximum z-value of the view volume.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the resulting [**D3DXMATRIX**](direct3d10.d3d10_d3dxmatrix).

## Remarks

The [**D3DXMatrixOrthoRH**](d3dxmatrixorthorh.md) function is a special case of the **D3DXMatrixOrthoOffCenterRH** function. To create the same projection using **D3DXMatrixOrthoOffCenterRH**, use the following values: l = -w/2, r = w/2, b = -h/2, and t = h/2.

All the parameters of the **D3DXMatrixOrthoOffCenterRH** function are distances in camera space. The parameters describe the dimensions of the view volume.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixOrthoOffCenterRH** function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
2/(r-l)      0            0           0
0            2/(t-b)      0           0
0            0            1/(zn-zf)   0
(l+r)/(l-r)  (t+b)/(b-t)  zn/(zn-zf)  1
```



## Requirements



|                    |                                                                                        |
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

[**D3DXMatrixOrthoOffCenterLH**](d3dxmatrixorthooffcenterlh.md)
</dt> </dl>

 

 




