---
title: D3DX_FLOAT3_to_B8G8R8X8_UNORM function
description: Packs the given XMFLOAT3 into a DXGI\_FORMAT\_B8G8R8X8\_UNORM UINT.
ms.assetid: 9492578b-e3c3-4856-b6d2-49f776a21d77
keywords:
- D3DX_FLOAT3_to_B8G8R8X8_UNORM function HLSL
topic_type:
- apiref
api_name:
- D3DX_FLOAT3_to_B8G8R8X8_UNORM
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_FLOAT3\_to\_B8G8R8X8\_UNORM function

Packs the given XMFLOAT3 into a DXGI\_FORMAT\_B8G8R8X8\_UNORM UINT.

## Syntax

``` syntax
UINT D3DX_FLOAT3_to_B8G8R8X8_UNORM(
   hlsl_precise XMFLOAT3 unpackedInput
);
```

## Parameters

<dl> <dt>

*unpackedInput* 
</dt> <dd>

The unpacked shader data.

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

 

 





