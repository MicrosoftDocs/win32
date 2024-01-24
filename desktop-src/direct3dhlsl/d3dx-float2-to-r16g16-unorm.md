---
title: D3DX_FLOAT2_to_R16G16_UNORM function
description: Packs the given XMFLOAT2 back into a DXGI\_FORMAT\_R16G16\_UNORM.
ms.assetid: 5a1bd034-262f-4f55-8f38-d2fda42bb13b
keywords:
- D3DX_FLOAT2_to_R16G16_UNORM function HLSL
topic_type:
- apiref
api_name:
- D3DX_FLOAT2_to_R16G16_UNORM
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_FLOAT2\_to\_R16G16\_UNORM function

Packs the given XMFLOAT2 back into a DXGI\_FORMAT\_R16G16\_UNORM.

## Syntax

``` syntax
UINT D3DX_FLOAT2_to_R16G16_UNORM(
   XMFLOAT2 unpackedInput
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

 

 





