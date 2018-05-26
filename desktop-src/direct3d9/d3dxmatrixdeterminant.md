---
Description: Returns the determinant of a matrix.
ms.assetid: 711ba616-4c90-41d1-b9d5-0893b3e47284
title: D3DXMatrixDeterminant function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXMatrixDeterminant function

Returns the determinant of a matrix.

## Syntax


```C++
FLOAT D3DXMatrixDeterminant(
  _In_ const D3DXMATRIX *pM
);
```



## Parameters

<dl> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the source [**D3DXMATRIX**](d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)**

Returns the determinant of the matrix.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 




