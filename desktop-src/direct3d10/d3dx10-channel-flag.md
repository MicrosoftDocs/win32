---
description: These flags are used by functions which operate on one or more channels in a texture.
ms.assetid: 54ecb39a-a36e-43bb-bb51-78b7375716d8
title: D3DX10_CHANNEL_FLAG enumeration (D3DX10Tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10_CHANNEL_FLAG
api_type: 
- HeaderDef
api_location: 
- D3DX10Tex.h
---

# D3DX10\_CHANNEL\_FLAG enumeration

These flags are used by functions which operate on one or more channels in a texture.

## Syntax


```C++
typedef enum D3DX10_CHANNEL_FLAG { 
  D3DX10_CHANNEL_RED        = (1 << 0),
  D3DX10_CHANNEL_BLUE       = (1 << 1),
  D3DX10_CHANNEL_GREEN      = (1 << 2),
  D3DX10_CHANNEL_ALPHA      = (1 << 3),
  D3DX10_CHANNEL_LUMINANCE  = (1 << 4)
} D3DX10_CHANNEL_FLAG, *LPD3DX10_CHANNEL_FLAG;
```



## Constants

<dl> <dt>

<span id="D3DX10_CHANNEL_RED"></span><span id="d3dx10_channel_red"></span>**D3DX10\_CHANNEL\_RED**
</dt> <dd>

Indicates the red channel should be used.

</dd> <dt>

<span id="D3DX10_CHANNEL_BLUE"></span><span id="d3dx10_channel_blue"></span>**D3DX10\_CHANNEL\_BLUE**
</dt> <dd>

Indicates the blue channel should be used.

</dd> <dt>

<span id="D3DX10_CHANNEL_GREEN"></span><span id="d3dx10_channel_green"></span>**D3DX10\_CHANNEL\_GREEN**
</dt> <dd>

Indicates the green channel should be used.

</dd> <dt>

<span id="D3DX10_CHANNEL_ALPHA"></span><span id="d3dx10_channel_alpha"></span>**D3DX10\_CHANNEL\_ALPHA**
</dt> <dd>

Indicates the alpha channel should be used.

</dd> <dt>

<span id="D3DX10_CHANNEL_LUMINANCE"></span><span id="d3dx10_channel_luminance"></span>**D3DX10\_CHANNEL\_LUMINANCE**
</dt> <dd>

Indicates the luminaces of the red, green, and blue channels should be used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Tex.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](d3d10-graphics-reference-d3dx10-enums.md)
</dt> </dl>

 

 




