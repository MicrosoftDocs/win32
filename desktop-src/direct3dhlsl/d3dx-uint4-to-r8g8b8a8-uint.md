---
title: D3DX_UINT4_to_R8G8B8A8_UINT function
description: Packs the given XMUINT4 back into a DXGI\_FORMAT\_R8G8B8A8\_UINT.
ms.assetid: d4770dfc-1387-40c3-a4f8-365a1421fa3c
keywords:
- D3DX_UINT4_to_R8G8B8A8_UINT function HLSL
topic_type:
- apiref
api_name:
- D3DX_UINT4_to_R8G8B8A8_UINT
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_UINT4\_to\_R8G8B8A8\_UINT function

Packs the given XMUINT4 back into a DXGI\_FORMAT\_R8G8B8A8\_UINT.

## Syntax

``` syntax
UINT D3DX_UINT4_to_R8G8B8A8_UINT(
   hlsl_precise XMUINT4 unpackedInput
);
```

## Parameters

<dl> <dt>

*unpackedInput* 
</dt> <dd>

The shader data to pack.

</dd> </dl>

## Return value

The packed shader data.

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

 

 





