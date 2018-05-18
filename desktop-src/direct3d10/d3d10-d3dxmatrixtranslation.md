---
Description: 'Create a translation matrix.'
ms.assetid: 'a3565a06-22af-4ded-8835-da4c7ae81805'
title: D3DXMatrixTranslation function
---

# D3DXMatrixTranslation function

Create a translation matrix.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixTranslation(
  _Inout_ D3DXMATRIX *pOut,
  _In_    FLOAT      x,
  _In_    FLOAT      y,
  _In_    FLOAT      z
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

The matrix that will become a translation matrix. See [**D3DXMATRIX**](d3d10-d3dxmatrix.md).

</dd> <dt>

*x* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The x-component of the translation.

</dd> <dt>

*y* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The y-component of the translation.

</dd> <dt>

*z* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The z-component of the translation.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

The translation matrix.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




