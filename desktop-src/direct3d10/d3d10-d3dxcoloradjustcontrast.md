---
description: D3DXColorAdjustContrast function (D3DX10Math.h) - Adjusts the contrast value of a color.
ms.assetid: c111d3c7-19c6-4a6b-af0d-a9e1bc0bb7d9
title: D3DXColorAdjustContrast function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXColorAdjustContrast
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXColorAdjustContrast function (D3DX10Math.h)

Adjusts the contrast value of a color.

## Syntax


```C++
D3DXCOLOR* D3DXColorAdjustContrast(
  _In_       D3DXCOLOR *pOut,
  _In_ const D3DXCOLOR *pC,
  _In_       FLOAT     c
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**D3DXCOLOR**](../direct3d9/d3dxcolor.md)\***

\[in, out\] Pointer to a [**D3DXCOLOR**](d3d10-d3dxcolor.md) that is the result of the operation.

</dd> <dt>

*pC* \[in\]
</dt> <dd>

Type: **const [**D3DXCOLOR**](../direct3d9/d3dxcolor.md)\***

Pointer to a source D3DXCOLOR structure.

</dd> <dt>

*c* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Contrast value. This parameter linearly interpolates between fifty percent gray and the color, pC. There are no limits on the value of c. If this parameter is zero, then the returned color is fifty percent gray. If this parameter is 1, then the returned color is the original color.

</dd> </dl>

## Return value

Type: **[**D3DXCOLOR**](../direct3d9/d3dxcolor.md)\***

This function returns a pointer to a D3DXCOLOR structure that is the result of the contrast adjustment.

## Remarks

The input alpha channel is copied, unmodified, to the output alpha channel.

The return value for this function is the same value returned in the pOut parameter. In this way, this function can be used as a parameter for another function.

This function interpolates the red, green, and blue color components of a D3DXCOLOR structure between fifty percent gray and a specified contrast value, as shown in the following example.


```
pOut->r = 0.5f + c * (pC->r - 0.5f);
```



If c is greater than 0 and less than 1, the contrast is decreased. If c is greater than 1, the contrast is increased.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
