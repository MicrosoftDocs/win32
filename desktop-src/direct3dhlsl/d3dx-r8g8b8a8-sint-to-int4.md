---
title: D3DX_R8G8B8A8_SINT_to_INT4 function
description: Unpacks DXGI\_FORMAT\_R8G8B8A8\_SINT shader data to an XMINT4.
ms.assetid: 144bd296-02b5-4307-b785-860680db2d52
keywords:
- D3DX_R8G8B8A8_SINT_to_INT4 function HLSL
topic_type:
- apiref
api_name:
- D3DX_R8G8B8A8_SINT_to_INT4
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_R8G8B8A8\_SINT\_to\_INT4 function

Unpacks DXGI\_FORMAT\_R8G8B8A8\_SINT shader data to an XMINT4.

## Syntax

``` syntax
XMINT4 D3DX_R8G8B8A8_SINT_to_INT4(
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

 

 





