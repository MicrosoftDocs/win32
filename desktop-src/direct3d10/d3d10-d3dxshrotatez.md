---
Description: Rotates the spherical harmonic (SH) vector in the z-axis by the given angle.
ms.assetid: 7c4bec55-4a4c-4f7e-8849-1cac373a2340
title: D3DXSHRotateZ function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXSHRotateZ function

Rotates the spherical harmonic (SH) vector in the z-axis by the given angle.

## Syntax


```C++
FLOAT* D3DXSHRotateZ(
  _In_       FLOAT *pOut,
  _In_       UINT  Order,
  _In_       FLOAT Angle,
  _In_ const FLOAT *pIn
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to Spherical harmonic (SH) output coefficients. The evaluation generates Order² coefficients. This pointer should not alias with pIn. See Remarks.

</dd> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Order of the SH evaluation. Must be in the range of D3DXSH\_MINORDER to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*Angle* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Rotation angle in radians. The rotation is performed around the z-axis.

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

Pointer to rotated SH coefficients.

</dd> </dl>

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)\***

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

 

 




