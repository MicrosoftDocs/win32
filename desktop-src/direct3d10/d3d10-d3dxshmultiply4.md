---
description: Computes the product of two spherical harmonics functions (f and g). Both functions are of order N = 4.
ms.assetid: 05427a18-447e-45d7-a851-e580298c9a1f
title: D3DXSHMultiply4 function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXSHMultiply4
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXSHMultiply4 function

> [!Note]
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated and is not supported for Windows Store apps.

> [!Note]
> Instead of using this function, we recommend that you use the [Spherical Harmonics Math](https://github.com/Microsoft/DirectXMath/tree/main/SHMath) library function **XMSHMultiply4**.

Computes the product of two spherical harmonics functions (*f* and *g*). Both functions are of order N = 4.

## Syntax


```C++
FLOAT* D3DXSHMultiply4(
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

Pointer to the output SH coefficients — basis function *Y*ₗₘ is stored at l² + *m* + l. The order *N* determines the length of the array, where there should always be *N*² coefficients.

</dd> <dt>

*pF* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Input SH coefficients for first function.

</dd> <dt>

*pG* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Second set of input SH coefficients.

</dd> </dl>

## Return value

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to SH output coefficients.

## Remarks

The product of two SH functions of order N = 4 generates an SH function of order 2 × *N* - 1 = 7, but the results are truncated. This means that the product commutes ( *f* × *g* = *g* × *f* ) but doesn't associate ( *f* × ( *g* × *h* ) ≠ ( *f* × *g* ) × *h* ).

This function uses the following equation:


```
pOut[i] = int(y_i(s) * f(s) * g(s))
```



where y\_i(s) is the ith SH basis function, and where f(s) and g(s) use the following SH function:


```
sum_i(y_i(s)*c_i)
```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
