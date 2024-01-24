---
title: D3DX_IsNan function
description: Determines if the value is a NaN (Not a Number).
ms.assetid: 862d1d34-36ab-471e-b3ce-ce71896441e5
keywords:
- D3DX_IsNan function HLSL
topic_type:
- apiref
api_name:
- D3DX_IsNan
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_IsNan function

Determines if the value is a NaN (Not a Number).

## Syntax

``` syntax
bool D3DX_IsNan(
   FLOAT _V
);
```

## Parameters

<dl> <dt>

*\_V* 
</dt> <dd>

The specified value.

</dd> </dl>

## Return value

true if a NaN; otherwise false.

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

 

 





