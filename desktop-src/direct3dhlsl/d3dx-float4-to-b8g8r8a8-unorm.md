---
title: D3DX_FLOAT4_to_B8G8R8A8_UNORM function
description: Packs the given XMFLOAT4 back into a DXGI\_FORMAT\_B8G8R8A8\_UNORM.
ms.assetid: 5b7452ed-446a-4760-83e6-f3209ac8daf4
keywords:
- D3DX_FLOAT4_to_B8G8R8A8_UNORM function HLSL
topic_type:
- apiref
api_name:
- D3DX_FLOAT4_to_B8G8R8A8_UNORM
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_FLOAT4\_to\_B8G8R8A8\_UNORM function

Packs the given XMFLOAT4 back into a DXGI\_FORMAT\_B8G8R8A8\_UNORM.

## Syntax

``` syntax
UINT D3DX_FLOAT4_to_B8G8R8A8_UNORM(
   hlsl_precise XMFLOAT4 unpackedInput
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

 

 





