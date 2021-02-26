---
title: D3DX_SRGB_to_FLOAT_inexact function
description: Converts an SRGB value to FLOAT. | D3DX_SRGB_to_FLOAT_inexact function
ms.assetid: 6eadda6d-ff99-4a8e-9e30-ae455732438e
keywords:
- D3DX_SRGB_to_FLOAT_inexact function HLSL
topic_type:
- apiref
api_name:
- D3DX_SRGB_to_FLOAT_inexact
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_SRGB\_to\_FLOAT\_inexact function

Converts an SRGB value to FLOAT.

## Syntax

``` syntax
FLOAT D3DX_SRGB_to_FLOAT_inexact(
   hlsl_precise FLOAT val
);
```

## Parameters

<dl> <dt>

*val* 
</dt> <dd>

SRGB value to convert.

</dd> </dl>

## Return value

The converted SRGB value.

## Remarks

This function doesn't have a high enough precision to give the exact answer. The alternative function [**D3DX\_SRGB\_to\_FLOAT**](d3dx-srgb-to-float.md) uses a lookup table to give an exact SRGB to float conversion.

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX\_DXGIFormatConvert.inl</dt> </dl> |



## See also

<dl> <dt>

[Functions](format-conversion-functions.md)
</dt> <dt>

[Unpacking and Packing DXGI\_FORMAT for In-Place Image Editing](dx-graphics-hlsl-unpacking-packing-dxgi-format.md)
</dt> </dl>

 

 





