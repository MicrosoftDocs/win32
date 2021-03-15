---
title: D3DX_FLOAT_to_UINT function
description: Converts a FLOAT value to UINT.
ms.assetid: 05c5de72-8915-4541-a82d-242e46bfa883
keywords:
- D3DX_FLOAT_to_UINT function HLSL
topic_type:
- apiref
api_name:
- D3DX_FLOAT_to_UINT
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_FLOAT\_to\_UINT function

Converts a FLOAT value to UINT.

## Syntax

``` syntax
UINT D3DX_FLOAT_to_UINT(
   FLOAT _V,
   FLOAT _Scale
);
```

## Parameters

<dl> <dt>

*\_V* 
</dt> <dd>

The v vector.

</dd> <dt>

*\_Scale* 
</dt> <dd>

The scale value.

</dd> </dl>

## Return value

The converted FLOAT value

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX\_DXGIFormatConvert.inl</dt> </dl> |



## See also

<dl> <dt>

[Functions](format-conversion-functions.md)
</dt> <dt>

[Unpacking and Packing DXGI\_FORMAT for In-Place Image Editing](dx-graphics-hlsl-unpacking-packing-dxgi-format.md)
</dt> </dl>

 

 





