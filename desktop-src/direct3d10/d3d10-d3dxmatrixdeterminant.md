---
Description: Returns the determinant of a matrix.
ms.assetid: b0155c91-1554-42ef-b219-c6cdd2a905b5
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

Type: **const [**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to the source D3DXMATRIX structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)**

Returns the determinant of the matrix.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




