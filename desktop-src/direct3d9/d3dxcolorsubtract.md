---
description: Subtracts two color values to create a new color value.
ms.assetid: c21f8402-c1c2-4909-896f-2872ef518537
title: D3DXColorSubtract function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXColorSubtract
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXColorSubtract function

Subtracts two color values to create a new color value.

## Syntax


```C++
D3DXCOLOR* D3DXColorSubtract(
  _Inout_       D3DXCOLOR *pOut,
  _In_    const D3DXCOLOR *pC1,
  _In_    const D3DXCOLOR *pC2
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXCOLOR**](d3dxcolor.md)\***

Pointer to a [**D3DXCOLOR**](d3dxcolor.md) structure that is the result of the operation.

</dd> <dt>

*pC1* \[in\]
</dt> <dd>

Type: **const [**D3DXCOLOR**](d3dxcolor.md)\***

Pointer to a source [**D3DXCOLOR**](d3dxcolor.md) structure.

</dd> <dt>

*pC2* \[in\]
</dt> <dd>

Type: **const [**D3DXCOLOR**](d3dxcolor.md)\***

Pointer to a source [**D3DXCOLOR**](d3dxcolor.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXCOLOR**](d3dxcolor.md)\***

This function returns a pointer to a [**D3DXCOLOR**](d3dxcolor.md) structure that is the difference between two color values.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the **D3DXColorSubtract** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXColorAdd**](d3dxcoloradd.md)
</dt> </dl>

 

 




