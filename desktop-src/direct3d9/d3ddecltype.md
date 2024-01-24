---
description: Defines a vertex declaration data type.
ms.assetid: 993fc7e4-4752-4bce-82d0-0a034fdc69c0
title: D3DDECLTYPE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DDECLTYPE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DDECLTYPE enumeration

Defines a vertex declaration data type.

## Syntax


```C++
typedef enum D3DDECLTYPE { 
  D3DDECLTYPE_FLOAT1     = 0,
  D3DDECLTYPE_FLOAT2     = 1,
  D3DDECLTYPE_FLOAT3     = 2,
  D3DDECLTYPE_FLOAT4     = 3,
  D3DDECLTYPE_D3DCOLOR   = 4,
  D3DDECLTYPE_UBYTE4     = 5,
  D3DDECLTYPE_SHORT2     = 6,
  D3DDECLTYPE_SHORT4     = 7,
  D3DDECLTYPE_UBYTE4N    = 8,
  D3DDECLTYPE_SHORT2N    = 9,
  D3DDECLTYPE_SHORT4N    = 10,
  D3DDECLTYPE_USHORT2N   = 11,
  D3DDECLTYPE_USHORT4N   = 12,
  D3DDECLTYPE_UDEC3      = 13,
  D3DDECLTYPE_DEC3N      = 14,
  D3DDECLTYPE_FLOAT16_2  = 15,
  D3DDECLTYPE_FLOAT16_4  = 16,
  D3DDECLTYPE_UNUSED     = 17
} D3DDECLTYPE, *LPD3DDECLTYPE;
```



## Constants

<dl> <dt>

<span id="D3DDECLTYPE_FLOAT1"></span><span id="d3ddecltype_float1"></span>**D3DDECLTYPE\_FLOAT1**
</dt> <dd>

One-component float expanded to (float, 0, 0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_FLOAT2"></span><span id="d3ddecltype_float2"></span>**D3DDECLTYPE\_FLOAT2**
</dt> <dd>

Two-component float expanded to (float, float, 0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_FLOAT3"></span><span id="d3ddecltype_float3"></span>**D3DDECLTYPE\_FLOAT3**
</dt> <dd>

Three-component float expanded to (float, float, float, 1).

</dd> <dt>

<span id="D3DDECLTYPE_FLOAT4"></span><span id="d3ddecltype_float4"></span>**D3DDECLTYPE\_FLOAT4**
</dt> <dd>

Four-component float expanded to (float, float, float, float).

</dd> <dt>

<span id="D3DDECLTYPE_D3DCOLOR"></span><span id="d3ddecltype_d3dcolor"></span>**D3DDECLTYPE\_D3DCOLOR**
</dt> <dd>

Four-component, packed, unsigned bytes mapped to 0 to 1 range. Input is a [**D3DCOLOR**](d3dcolor.md) and is expanded to RGBA order.

</dd> <dt>

<span id="D3DDECLTYPE_UBYTE4"></span><span id="d3ddecltype_ubyte4"></span>**D3DDECLTYPE\_UBYTE4**
</dt> <dd>

Four-component, unsigned byte.

</dd> <dt>

<span id="D3DDECLTYPE_SHORT2"></span><span id="d3ddecltype_short2"></span>**D3DDECLTYPE\_SHORT2**
</dt> <dd>

Two-component, signed short expanded to (value, value, 0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_SHORT4"></span><span id="d3ddecltype_short4"></span>**D3DDECLTYPE\_SHORT4**
</dt> <dd>

Four-component, signed short expanded to (value, value, value, value).

</dd> <dt>

<span id="D3DDECLTYPE_UBYTE4N"></span><span id="d3ddecltype_ubyte4n"></span>**D3DDECLTYPE\_UBYTE4N**
</dt> <dd>

Four-component byte with each byte normalized by dividing with 255.0f.

</dd> <dt>

<span id="D3DDECLTYPE_SHORT2N"></span><span id="d3ddecltype_short2n"></span>**D3DDECLTYPE\_SHORT2N**
</dt> <dd>

Normalized, two-component, signed short, expanded to (first short/32767.0, second short/32767.0, 0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_SHORT4N"></span><span id="d3ddecltype_short4n"></span>**D3DDECLTYPE\_SHORT4N**
</dt> <dd>

Normalized, four-component, signed short, expanded to (first short/32767.0, second short/32767.0, third short/32767.0, fourth short/32767.0).

</dd> <dt>

<span id="D3DDECLTYPE_USHORT2N"></span><span id="d3ddecltype_ushort2n"></span>**D3DDECLTYPE\_USHORT2N**
</dt> <dd>

Normalized, two-component, unsigned short, expanded to (first short/65535.0, short short/65535.0, 0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_USHORT4N"></span><span id="d3ddecltype_ushort4n"></span>**D3DDECLTYPE\_USHORT4N**
</dt> <dd>

Normalized, four-component, unsigned short, expanded to (first short/65535.0, second short/65535.0, third short/65535.0, fourth short/65535.0).

</dd> <dt>

<span id="D3DDECLTYPE_UDEC3"></span><span id="d3ddecltype_udec3"></span>**D3DDECLTYPE\_UDEC3**
</dt> <dd>

Three-component, unsigned, 10 10 10 format expanded to (value, value, value, 1).

</dd> <dt>

<span id="D3DDECLTYPE_DEC3N"></span><span id="d3ddecltype_dec3n"></span>**D3DDECLTYPE\_DEC3N**
</dt> <dd>

Three-component, signed, 10 10 10 format normalized and expanded to (v\[0\]/511.0, v\[1\]/511.0, v\[2\]/511.0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_FLOAT16_2"></span><span id="d3ddecltype_float16_2"></span>**D3DDECLTYPE\_FLOAT16\_2**
</dt> <dd>

Two-component, 16-bit, floating point expanded to (value, value, 0, 1).

</dd> <dt>

<span id="D3DDECLTYPE_FLOAT16_4"></span><span id="d3ddecltype_float16_4"></span>**D3DDECLTYPE\_FLOAT16\_4**
</dt> <dd>

Four-component, 16-bit, floating point expanded to (value, value, value, value).

</dd> <dt>

<span id="D3DDECLTYPE_UNUSED"></span><span id="d3ddecltype_unused"></span>**D3DDECLTYPE\_UNUSED**
</dt> <dd>

Type field in the declaration is unused. This is designed for use with D3DDECLMETHOD\_UV and D3DDECLMETHOD\_LOOKUPPRESAMPLED.

</dd> </dl>

## Remarks

Vertex data is declared with an array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) structures. Each element in the array contains a vertex declaration data type.

Use the DirectX Caps Viewer Tool (DXCapsViewer.exe) to see which types are supported on your device. You can get this tool and learn about it from the DirectX SDK. For info about the DirectX SDK, see [Where is the DirectX SDK?](../directx-sdk--august-2009-.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DDECLMETHOD**](./d3ddeclmethod.md)
</dt> </dl>

 

 
