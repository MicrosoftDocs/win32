---
Description: Computes the dot product of two spherical harmonic (SH) vectors.
ms.assetid: 71b7480d-ddac-4b02-bca7-d9318823d03e
title: D3DXSHDot function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXSHDot function

Computes the dot product of two spherical harmonic (SH) vectors.

## Syntax


```C++
FLOAT D3DXSHDot(
  _In_       UINT  Order,
  _In_ const FLOAT *pA,
  _In_ const FLOAT *pB
);
```



## Parameters

<dl> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Order of the spherical harmonic (SH) evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*pA* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

Pointer to the first SH vector.

</dd> <dt>

*pB* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

Pointer to the second SH vector.

</dd> </dl>

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)**

SH output coefficients.

## Remarks

Each coefficient of the basis function Yₗₘ is stored at memory location l² + m + l, where:

-   l is the degree of the basis function.
-   m is the basis function index for the given l value and ranges from -l to l, inclusive.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[Precomputed Radiance Transfer (Direct3D 9)](precomputed-radiance-transfer.md)
</dt> </dl>

 

 




