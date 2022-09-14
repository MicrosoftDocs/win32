---
title: D3DX_B8G8R8A8_UNORM_to_FLOAT4 function
description: Unpacks DXGI\_FORMAT\_B8G8R8A8\_UNORM shader data to an XMFLOAT4.
ms.assetid: 1a52058c-825d-4607-b67d-8226dccdee54
keywords:
- D3DX_B8G8R8A8_UNORM_to_FLOAT4 function HLSL
topic_type:
- apiref
api_name:
- D3DX_B8G8R8A8_UNORM_to_FLOAT4
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX\_B8G8R8A8\_UNORM\_to\_FLOAT4 function

Unpacks DXGI\_FORMAT\_B8G8R8A8\_UNORM shader data to an XMFLOAT4.

## Syntax

``` syntax
XMFLOAT4 D3DX_B8G8R8A8_UNORM_to_FLOAT4(
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

 

 





