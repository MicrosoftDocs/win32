---
description: Defines stencil-buffer operations.
ms.assetid: 338a3b7f-236a-484f-96b8-1e6bfb014484
title: D3DSTENCILOP enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DSTENCILOP
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DSTENCILOP enumeration

Defines stencil-buffer operations.

## Syntax


```C++
typedef enum D3DSTENCILOP { 
  D3DSTENCILOP_KEEP         = 1,
  D3DSTENCILOP_ZERO         = 2,
  D3DSTENCILOP_REPLACE      = 3,
  D3DSTENCILOP_INCRSAT      = 4,
  D3DSTENCILOP_DECRSAT      = 5,
  D3DSTENCILOP_INVERT       = 6,
  D3DSTENCILOP_INCR         = 7,
  D3DSTENCILOP_DECR         = 8,
  D3DSTENCILOP_FORCE_DWORD  = 0x7fffffff
} D3DSTENCILOP, *LPD3DSTENCILOP;
```



## Constants

<dl> <dt>

<span id="D3DSTENCILOP_KEEP"></span><span id="d3dstencilop_keep"></span>**D3DSTENCILOP\_KEEP**
</dt> <dd>

Do not update the entry in the stencil buffer. This is the default value.

</dd> <dt>

<span id="D3DSTENCILOP_ZERO"></span><span id="d3dstencilop_zero"></span>**D3DSTENCILOP\_ZERO**
</dt> <dd>

Set the stencil-buffer entry to 0.

</dd> <dt>

<span id="D3DSTENCILOP_REPLACE"></span><span id="d3dstencilop_replace"></span>**D3DSTENCILOP\_REPLACE**
</dt> <dd>

Replace the stencil-buffer entry with a reference value.

</dd> <dt>

<span id="D3DSTENCILOP_INCRSAT"></span><span id="d3dstencilop_incrsat"></span>**D3DSTENCILOP\_INCRSAT**
</dt> <dd>

Increment the stencil-buffer entry, clamping to the maximum value.

</dd> <dt>

<span id="D3DSTENCILOP_DECRSAT"></span><span id="d3dstencilop_decrsat"></span>**D3DSTENCILOP\_DECRSAT**
</dt> <dd>

Decrement the stencil-buffer entry, clamping to zero.

</dd> <dt>

<span id="D3DSTENCILOP_INVERT"></span><span id="d3dstencilop_invert"></span>**D3DSTENCILOP\_INVERT**
</dt> <dd>

Invert the bits in the stencil-buffer entry.

</dd> <dt>

<span id="D3DSTENCILOP_INCR"></span><span id="d3dstencilop_incr"></span>**D3DSTENCILOP\_INCR**
</dt> <dd>

Increment the stencil-buffer entry, wrapping to zero if the new value exceeds the maximum value.

</dd> <dt>

<span id="D3DSTENCILOP_DECR"></span><span id="d3dstencilop_decr"></span>**D3DSTENCILOP\_DECR**
</dt> <dd>

Decrement the stencil-buffer entry, wrapping to the maximum value if the new value is less than zero.

</dd> <dt>

<span id="D3DSTENCILOP_FORCE_DWORD"></span><span id="d3dstencilop_force_dword"></span>**D3DSTENCILOP\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Stencil-buffer entries are integer values ranging from 0 through 2ⁿ - 1, where n is the bit depth of the stencil buffer.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> </dl>

 

 




