---
description: Computes the product of two spherical harmonics functions (f and g). Both functions are of order N = 2.
ms.assetid: 9e0942ce-e39d-4147-9472-cda8a97fd390
title: D3DXSHMultiply2 function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHMultiply2
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXSHMultiply2 function (D3DX10Math.h)

Computes the product of two spherical harmonics functions (*f* and *g*). Both functions are of order N = 2.

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

Pointer to the output SH coefficients — the basis function *Y*ₗₘ is stored at l² + *m* + l. The order *N* determines the length of the array, where there should always be *N*² coefficients.

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

The product of two SH functions of order N = 2 generates an SH function of order 2 × *N* - 1 = 3, but the results are truncated. This means that the product commutes ( *f* × *g* = *g* × *f* ) but doesn't associate ( *f* × (*g* × *h*) ≠ ( *f* × *g*) × *h* ).

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

 

 
