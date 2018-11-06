---
Description: Rotates the spherical harmonic (SH) vector by the given matrix.
ms.assetid: 22ed379a-ce08-46df-9cc1-8d5fde87c179
title: D3DXSHRotate function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHRotate
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXSHRotate function

Rotates the spherical harmonic (SH) vector by the given matrix.

## Syntax


```C++
FLOAT* D3DXSHRotate(
  _In_       FLOAT      *pOut,
  _In_       UINT       Order,
  _In_ const D3DXMATRIX *pMatrix,
  _In_ const FLOAT      *pIn
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to Spherical harmonic (SH) output coefficients. The evaluation generates Order² coefficients. This pointer should not alias with pIn. See Remarks.

</dd> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Order of the SH evaluation. Must be in the range of D3DXSH\_MINORDER to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*pMatrix* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](https://msdn.microsoft.com/en-us/library/Bb172912(v=VS.85).aspx)\***

Pointer to the rotation matrix. The rotation sub-matrix must be orthogonal, with a unit determinant.

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to rotated SH coefficients.

</dd> </dl>

## Return value

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to SH output coefficients.

## Remarks

Each coefficient of the basis function Yₗₘ is stored at memory location l² + m + l, where:

-   l is the degree of the basis function.
-   m is the basis function index for the given l value and ranges from -l to l, inclusive.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




