---
description: Sampler states define texture sampling operations such as texture addressing and texture filtering.
ms.assetid: 03a6a5f1-5e4f-4ba8-be4a-74d78fbc85d0
title: D3DSAMPLERSTATETYPE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DSAMPLERSTATETYPE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DSAMPLERSTATETYPE enumeration

Sampler states define texture sampling operations such as texture addressing and texture filtering. Some sampler states set-up vertex processing, and some set-up pixel processing. Sampler states can be saved and restored using stateblocks (see [State Blocks Save and Restore State (Direct3D 9)](state-blocks-save-and-restore-state.md)).

## Syntax


```C++
typedef enum D3DSAMPLERSTATETYPE { 
  D3DSAMP_ADDRESSU       = 1,
  D3DSAMP_ADDRESSV       = 2,
  D3DSAMP_ADDRESSW       = 3,
  D3DSAMP_BORDERCOLOR    = 4,
  D3DSAMP_MAGFILTER      = 5,
  D3DSAMP_MINFILTER      = 6,
  D3DSAMP_MIPFILTER      = 7,
  D3DSAMP_MIPMAPLODBIAS  = 8,
  D3DSAMP_MAXMIPLEVEL    = 9,
  D3DSAMP_MAXANISOTROPY  = 10,
  D3DSAMP_SRGBTEXTURE    = 11,
  D3DSAMP_ELEMENTINDEX   = 12,
  D3DSAMP_DMAPOFFSET     = 13,
  D3DSAMP_FORCE_DWORD    = 0x7fffffff
} D3DSAMPLERSTATETYPE, *LPD3DSAMPLERSTATETYPE;
```



## Constants

<dl> <dt>

<span id="D3DSAMP_ADDRESSU"></span><span id="d3dsamp_addressu"></span>**D3DSAMP\_ADDRESSU**
</dt> <dd>

Texture-address mode for the u coordinate. The default is D3DTADDRESS\_WRAP. For more information, see [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md).

</dd> <dt>

<span id="D3DSAMP_ADDRESSV"></span><span id="d3dsamp_addressv"></span>**D3DSAMP\_ADDRESSV**
</dt> <dd>

Texture-address mode for the v coordinate. The default is D3DTADDRESS\_WRAP. For more information, see [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md).

</dd> <dt>

<span id="D3DSAMP_ADDRESSW"></span><span id="d3dsamp_addressw"></span>**D3DSAMP\_ADDRESSW**
</dt> <dd>

Texture-address mode for the w coordinate. The default is D3DTADDRESS\_WRAP. For more information, see [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md).

</dd> <dt>

<span id="D3DSAMP_BORDERCOLOR"></span><span id="d3dsamp_bordercolor"></span>**D3DSAMP\_BORDERCOLOR**
</dt> <dd>

Border color or type [**D3DCOLOR**](d3dcolor.md). The default color is 0x00000000.

</dd> <dt>

<span id="D3DSAMP_MAGFILTER"></span><span id="d3dsamp_magfilter"></span>**D3DSAMP\_MAGFILTER**
</dt> <dd>

Magnification filter of type [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md). The default value is D3DTEXF\_POINT.

</dd> <dt>

<span id="D3DSAMP_MINFILTER"></span><span id="d3dsamp_minfilter"></span>**D3DSAMP\_MINFILTER**
</dt> <dd>

Minification filter of type [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md). The default value is D3DTEXF\_POINT.

</dd> <dt>

<span id="D3DSAMP_MIPFILTER"></span><span id="d3dsamp_mipfilter"></span>**D3DSAMP\_MIPFILTER**
</dt> <dd>

Mipmap filter to use during minification. See [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md). The default value is D3DTEXF\_NONE.

</dd> <dt>

<span id="D3DSAMP_MIPMAPLODBIAS"></span><span id="d3dsamp_mipmaplodbias"></span>**D3DSAMP\_MIPMAPLODBIAS**
</dt> <dd>

Mipmap level-of-detail bias. The default value is zero.

</dd> <dt>

<span id="D3DSAMP_MAXMIPLEVEL"></span><span id="d3dsamp_maxmiplevel"></span>**D3DSAMP\_MAXMIPLEVEL**
</dt> <dd>

level-of-detail index of largest map to use. Values range from 0 to (n - 1) where 0 is the largest. The default value is zero.

</dd> <dt>

<span id="D3DSAMP_MAXANISOTROPY"></span><span id="d3dsamp_maxanisotropy"></span>**D3DSAMP\_MAXANISOTROPY**
</dt> <dd>

DWORD maximum anisotropy. Values range from 1 to the value that is specified in the **MaxAnisotropy** member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure. The default value is 1.

</dd> <dt>

<span id="D3DSAMP_SRGBTEXTURE"></span><span id="d3dsamp_srgbtexture"></span>**D3DSAMP\_SRGBTEXTURE**
</dt> <dd>

Gamma correction value. The default value is 0, which means gamma is 1.0 and no correction is required. Otherwise, this value means that the sampler should assume gamma of 2.2 on the content and convert it to linear (gamma 1.0) before presenting it to the pixel shader.

</dd> <dt>

<span id="D3DSAMP_ELEMENTINDEX"></span><span id="d3dsamp_elementindex"></span>**D3DSAMP\_ELEMENTINDEX**
</dt> <dd>

When a multielement texture is assigned to the sampler, this indicates which element index to use. The default value is 0.

</dd> <dt>

<span id="D3DSAMP_DMAPOFFSET"></span><span id="d3dsamp_dmapoffset"></span>**D3DSAMP\_DMAPOFFSET**
</dt> <dd>

Vertex offset in the presampled displacement map. This is a constant used by the tessellator, its default value is 0.

</dd> <dt>

<span id="D3DSAMP_FORCE_DWORD"></span><span id="d3dsamp_force_dword"></span>**D3DSAMP\_FORCE\_DWORD**
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

 

 
