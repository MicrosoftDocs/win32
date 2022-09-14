---
title: D3DX_FLOAT2_to_R16G16_FLOAT function
description: Packs the given XMFLOAT2 back into a DXGI\_FORMAT\_R16G16\_FLOAT.
ms.assetid: 8d03fac3-68f0-4c85-afaa-ff2cb76f1b73
keywords:
- D3DX_FLOAT2_to_R16G16_FLOAT function HLSL
topic_type:
- apiref
api_name:
- D3DX_FLOAT2_to_R16G16_FLOAT
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_FLOAT2\_to\_R16G16\_FLOAT function

Packs the given XMFLOAT2 back into a DXGI\_FORMAT\_R16G16\_FLOAT.

## Syntax

``` syntax
UINT D3DX_FLOAT2_to_R16G16_FLOAT(
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

 

 





