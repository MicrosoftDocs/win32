---
description: D3DXColorAdjustSaturation function (D3DX10Math.h) - Adjusts the saturation value of a color.
ms.assetid: a7ca64b4-2198-4116-8e9f-79d6c922fd09
title: D3DXColorAdjustSaturation function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXColorAdjustSaturation
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXColorAdjustSaturation function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Adjusts the saturation value of a color.

## Syntax


```C++
D3DXCOLOR* D3DXColorAdjustSaturation(
  _In_       D3DXCOLOR *pOut,
  _In_ const D3DXCOLOR *pC,
  _In_       FLOAT     s
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**D3DXCOLOR**](../direct3d9/d3dxcolor.md)\***

Pointer to a [**D3DXCOLOR**](d3d10-d3dxcolor.md) that is the result of the operation.

</dd> <dt>

*pC* \[in\]
</dt> <dd>

Type: **const [**D3DXCOLOR**](../direct3d9/d3dxcolor.md)\***

Pointer to a source D3DXCOLOR structure.

</dd> <dt>

*s* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Saturation value. This parameter linearly interpolates between the color converted to grayscale and the original color, pC. There are no limits on the value of s. If s is 0, the returned color is the grayscale color. If s is 1, the returned color is the original color.

</dd> </dl>

## Return value

Type: **[**D3DXCOLOR**](../direct3d9/d3dxcolor.md)\***

This function returns a pointer to a D3DXCOLOR structure that is the result of the saturation adjustment.

## Remarks

The input alpha channel is copied, unmodified, to the output alpha channel.

The return value for this function is the same value returned in the pOut parameter. In this way, this function can be used as a parameter for another function.

This function interpolates the red, green, and blue color components of a D3DXCOLOR structure between an unsaturated color and a color, as shown in the following example.


```
//Approximate values for each component's contribution to luminance.
//Based upon the NTSC standard described in ITU-R Recommendation BT.709.
FLOAT grey = pC->r * 0.2125f + pC->g * 0.7154f + pC->b * 0.0721f;

pOut->r = grey + s * (pC->r - grey);
```



If s is greater than 0 and less than 1, the saturation is decreased. If s is greater than 1, the saturation is increased.

The grayscale color is computed as:


```
r = g = b = 0.2125*r + 0.7154*g + 0.0721*b;
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

 

 
