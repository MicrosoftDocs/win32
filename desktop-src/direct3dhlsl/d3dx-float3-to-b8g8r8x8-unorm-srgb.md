---
title: D3DX_FLOAT3_to_B8G8R8X8_UNORM_SRGB function
description: Packs the given XMFLOAT3 back into a DXGI\_FORMAT\_B8G8R8X8\_UNORM\_SRGB.
ms.assetid: 42d1e8f1-d1b7-4c93-a658-d25790e78830
keywords:
- D3DX_FLOAT3_to_B8G8R8X8_UNORM_SRGB function HLSL
topic_type:
- apiref
api_name:
- D3DX_FLOAT3_to_B8G8R8X8_UNORM_SRGB
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_FLOAT3\_to\_B8G8R8X8\_UNORM\_SRGB function

Packs the given XMFLOAT3 back into a DXGI\_FORMAT\_B8G8R8X8\_UNORM\_SRGB.

## Syntax

``` syntax
UINT D3DX_FLOAT3_to_B8G8R8X8_UNORM_SRGB(
   hlsl_precise XMFLOAT3 unpackedInput
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

 

 





