---
title: D3DX_R16G16_SINT_to_INT2 function
description: Unpacks DXGI\_FORMAT\_R16G16\_SINT shader data to an XMINT2.
ms.assetid: 0aad1581-5fd8-43c0-828d-51ef9eb82a74
keywords:
- D3DX_R16G16_SINT_to_INT2 function HLSL
topic_type:
- apiref
api_name:
- D3DX_R16G16_SINT_to_INT2
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_R16G16\_SINT\_to\_INT2 function

Unpacks DXGI\_FORMAT\_R16G16\_SINT shader data to an XMINT2.

## Syntax

``` syntax
XMINT2 D3DX_R16G16_SINT_to_INT2(
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

 

 





