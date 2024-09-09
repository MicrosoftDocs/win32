---
description: Computes the product of two functions represented using SH (f and g).
ms.assetid: 632400a4-2ac9-438d-85f7-869101f350c8
title: D3DXSHMultiply2 function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXSHMultiply2
- D3DXSHMultiply3
- D3DXSHMultiply4
- D3DXSHMultiply5
- D3DXSHMultiply6
api_type:
- HeaderDef
api_location:
- d3dx9math.h
---

# D3DXSHMultiply2 function (D3dx9math.h)

> [!Note]
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated and is not supported for Windows Store apps.

> [!Note]
> Instead of using this function, we recommend that you use the [Spherical Harmonics Math](https://github.com/Microsoft/DirectXMath/tree/main/SHMath) library function **XMSHMultiply2**, **XMSHMultiply3**, **XMSHMultiply4**, **XMSHMultiply5**, or **XMSHMultiply6**.

Computes the product of two functions represented using SH (f and g).

## Syntax


```C++
FLOAT* D3DXSHMultiply2(
  _In_       FLOAT *pOut,
  _In_ const FLOAT *pF,
  _In_ const FLOAT *pG
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to the output SH coefficients - basis function Ylm is stored at l\*l + m+l.

</dd> <dt>

*pF* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Input SH coeffs for first function.

</dd> <dt>

*pG* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Second set of input SH coeffs.

</dd> </dl>

## Return value

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to SH output coefficients.

## Remarks

The order is a number between 2 and 6 inclusive. So this page actually documents several functions: D3DXSHMultiply2, D3DXSHMultiply3, ... D3DXSHMultiply6.

Computes the product of two functions represented using SH (f and g), where *pOut*\[i\] = int(y\_i(s) \* f(s) \* g(s)), where y\_i(s) is the ith SH basis function, f(s) and g(s) are SH functions (sum\_i(y\_i(s)\*c\_i)). The order O determines the lengths of the arrays, where there should always be O^2 coefficients. In general the product of two SH functions of order O generates an SH function of order 2\*O - 1, but the results are truncated. This means that the product commutes (f\*g == g\*f) but doesn't associate (f\*(g\*h) != (f\*g)\*h.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
