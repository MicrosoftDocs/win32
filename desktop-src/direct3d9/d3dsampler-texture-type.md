---
description: Defines the sampler texture types for vertex shaders.
ms.assetid: 8e9923f9-6f30-45e5-a557-f26d441a534d
title: D3DSAMPLER_TEXTURE_TYPE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DSAMPLER_TEXTURE_TYPE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DSAMPLER\_TEXTURE\_TYPE enumeration

Defines the sampler texture types for vertex shaders.

## Syntax


```C++
typedef enum D3DSAMPLER_TEXTURE_TYPE { 
  D3DSTT_UNKNOWN,
  D3DSTT_2D,
  D3DSTT_CUBE,
  D3DSTT_VOLUME,
  D3DSTT_FORCE_DWORD
} D3DSAMPLER_TEXTURE_TYPE, *LPD3DSAMPLER_TEXTURE_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DSTT_UNKNOWN"></span><span id="d3dstt_unknown"></span>**D3DSTT\_UNKNOWN**
</dt> <dd>

Uninitialized value. The value of this element is 0 &lt;&lt; D3DSP\_TEXTURETYPE\_SHIFT.

</dd> <dt>

<span id="D3DSTT_2D"></span><span id="d3dstt_2d"></span>**D3DSTT\_2D**
</dt> <dd>

Declaring a 2D texture. The value of this element is 2 &lt;&lt; D3DSP\_TEXTURETYPE\_SHIFT.

</dd> <dt>

<span id="D3DSTT_CUBE"></span><span id="d3dstt_cube"></span>**D3DSTT\_CUBE**
</dt> <dd>

Declaring a cube texture. The value of this element is 3 &lt;&lt; D3DSP\_TEXTURETYPE\_SHIFT.

</dd> <dt>

<span id="D3DSTT_VOLUME"></span><span id="d3dstt_volume"></span>**D3DSTT\_VOLUME**
</dt> <dd>

Declaring a volume texture. The value of this element is 4 &lt;&lt; D3DSP\_TEXTURETYPE\_SHIFT.

</dd> <dt>

<span id="D3DSTT_FORCE_DWORD"></span><span id="d3dstt_force_dword"></span>**D3DSTT\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> </dl>

 

 




