---
title: D3DX_R10G10B10A2_UINT_to_UINT4 function
description: Unpacks DXGI\_FORMAT\_R10G10B10A2\_UINT shader data to an XMINT4.
ms.assetid: 47c4f11f-936a-46d5-9533-1a4f9fce6168
keywords:
- D3DX_R10G10B10A2_UINT_to_UINT4 function HLSL
topic_type:
- apiref
api_name:
- D3DX_R10G10B10A2_UINT_to_UINT4
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_R10G10B10A2\_UINT\_to\_UINT4 function

Unpacks DXGI\_FORMAT\_R10G10B10A2\_UINT shader data to an XMINT4.

## Syntax

``` syntax
XMINT4 D3DX_R10G10B10A2_UINT_to_UINT4(
   UINT packedInput
);
```

## Parameters

<dl> <dt>

*packedInput* 
</dt> <dd>

The packed shader data.

</dd> </dl>

## Return value

The unpacked shader data.

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

 

 





