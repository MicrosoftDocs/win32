---
description: Creates the negative color value of a color value.
ms.assetid: 74143126-93f8-49fa-abe3-fd730b644d87
title: D3DXColorNegative function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXColorNegative
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXColorNegative function

Creates the negative color value of a color value.

## Syntax


```C++
D3DXCOLOR* D3DXColorNegative(
  _Inout_       D3DXCOLOR *pOut,
  _In_    const D3DXCOLOR *pC
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXCOLOR**](d3dxcolor.md)\***

Pointer to a [**D3DXCOLOR**](d3dxcolor.md) structure that is the result of the operation.

</dd> <dt>

*pC* \[in\]
</dt> <dd>

Type: **const [**D3DXCOLOR**](d3dxcolor.md)\***

Pointer to a source [**D3DXCOLOR**](d3dxcolor.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXCOLOR**](d3dxcolor.md)\***

This function returns a pointer to a [**D3DXCOLOR**](d3dxcolor.md) structure that is the negative color value of the color value.

## Remarks

The input alpha channel is copied, unmodified, to the output alpha channel.

The return value for this function is the same value returned in the pOut parameter. In this way, the **D3DXColorNegative** function can be used as a parameter for another function.

This function returns the negative color value by subtracting 1.0 from the color components of the [**D3DXCOLOR**](d3dxcolor.md) structure, as shown in the following example.


```
pOut->r = 1.0f - pC->r;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXColorLerp**](d3dxcolorlerp.md)
</dt> <dt>

[**D3DXColorModulate**](d3dxcolormodulate.md)
</dt> <dt>

[**D3DXColorScale**](d3dxcolorscale.md)
</dt> </dl>

 

 




