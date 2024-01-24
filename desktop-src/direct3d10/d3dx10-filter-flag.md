---
description: Texture filtering flags.
ms.assetid: bc73d916-fe18-4b15-b507-7954e157ab9a
title: D3DX10_FILTER_FLAG enumeration (D3DX10Tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10_FILTER_FLAG
api_type: 
- HeaderDef
api_location: 
- D3DX10Tex.h
---

# D3DX10\_FILTER\_FLAG enumeration

Texture filtering flags.

## Syntax


```C++
typedef enum D3DX10_FILTER_FLAG { 
  D3DX10_FILTER_NONE              = (1 << 0),
  D3DX10_FILTER_POINT             = (2 << 0),
  D3DX10_FILTER_LINEAR            = (3 << 0),
  D3DX10_FILTER_TRIANGLE          = (4 << 0),
  D3DX10_FILTER_BOX               = (5 << 0),
  D3DX10_FILTER_MIRROR_U          = (1 << 16),
  D3DX10_FILTER_MIRROR_V          = (2 << 16),
  D3DX10_FILTER_MIRROR_W          = (4 << 16),
  D3DX10_FILTER_MIRROR            = (7 << 16),
  D3DX10_FILTER_DITHER            = (1 << 19),
  D3DX10_FILTER_DITHER_DIFFUSION  = (2 << 19),
  D3DX10_FILTER_SRGB_IN           = (1 << 21),
  D3DX10_FILTER_SRGB_OUT          = (2 << 21),
  D3DX10_FILTER_SRGB              = (3 << 21)
} D3DX10_FILTER_FLAG, *LPD3DX10_FILTER_FLAG;
```



## Constants

<dl> <dt>

<span id="D3DX10_FILTER_NONE"></span><span id="d3dx10_filter_none"></span>**D3DX10\_FILTER\_NONE**
</dt> <dd>

No scaling or filtering will take place. Pixels outside the bounds of the source image are assumed to be transparent black.

</dd> <dt>

<span id="D3DX10_FILTER_POINT"></span><span id="d3dx10_filter_point"></span>**D3DX10\_FILTER\_POINT**
</dt> <dd>

Each destination pixel is computed by sampling the nearest pixel from the source image.

</dd> <dt>

<span id="D3DX10_FILTER_LINEAR"></span><span id="d3dx10_filter_linear"></span>**D3DX10\_FILTER\_LINEAR**
</dt> <dd>

Each destination pixel is computed by sampling the four nearest pixels from the source image. This filter works best when the scale on both axes is less than two.

</dd> <dt>

<span id="D3DX10_FILTER_TRIANGLE"></span><span id="d3dx10_filter_triangle"></span>**D3DX10\_FILTER\_TRIANGLE**
</dt> <dd>

Every pixel in the source image contributes equally to the destination image. This is the slowest of the filters.

</dd> <dt>

<span id="D3DX10_FILTER_BOX"></span><span id="d3dx10_filter_box"></span>**D3DX10\_FILTER\_BOX**
</dt> <dd>

Each pixel is computed by averaging a 2x2(x2) box of pixels from the source image. This filter works only when the dimensions of the destination are half those of the source, as is the case with mipmaps.

</dd> <dt>

<span id="D3DX10_FILTER_MIRROR_U"></span><span id="d3dx10_filter_mirror_u"></span>**D3DX10\_FILTER\_MIRROR\_U**
</dt> <dd>

Pixels off the edge of the texture on the u-axis should be mirrored, not wrapped.

</dd> <dt>

<span id="D3DX10_FILTER_MIRROR_V"></span><span id="d3dx10_filter_mirror_v"></span>**D3DX10\_FILTER\_MIRROR\_V**
</dt> <dd>

Pixels off the edge of the texture on the v-axis should be mirrored, not wrapped.

</dd> <dt>

<span id="D3DX10_FILTER_MIRROR_W"></span><span id="d3dx10_filter_mirror_w"></span>**D3DX10\_FILTER\_MIRROR\_W**
</dt> <dd>

Pixels off the edge of the texture on the w-axis should be mirrored, not wrapped.

</dd> <dt>

<span id="D3DX10_FILTER_MIRROR"></span><span id="d3dx10_filter_mirror"></span>**D3DX10\_FILTER\_MIRROR**
</dt> <dd>

Specifying this flag is the same as specifying the D3DX\_FILTER\_MIRROR\_U, D3DX\_FILTER\_MIRROR\_V, and D3DX\_FILTER\_MIRROR\_W flags.

</dd> <dt>

<span id="D3DX10_FILTER_DITHER"></span><span id="d3dx10_filter_dither"></span>**D3DX10\_FILTER\_DITHER**
</dt> <dd>

The resulting image must be dithered using a 4x4 ordered dither algorithm. This happens when converting from one format to another.

</dd> <dt>

<span id="D3DX10_FILTER_DITHER_DIFFUSION"></span><span id="d3dx10_filter_dither_diffusion"></span>**D3DX10\_FILTER\_DITHER\_DIFFUSION**
</dt> <dd>

Do diffuse dithering on the image when changing from one format to another.

</dd> <dt>

<span id="D3DX10_FILTER_SRGB_IN"></span><span id="d3dx10_filter_srgb_in"></span>**D3DX10\_FILTER\_SRGB\_IN**
</dt> <dd>

Input data is in standard RGB (sRGB) color space. See remarks.

</dd> <dt>

<span id="D3DX10_FILTER_SRGB_OUT"></span><span id="d3dx10_filter_srgb_out"></span>**D3DX10\_FILTER\_SRGB\_OUT**
</dt> <dd>

Output data is in standard RGB (sRGB) color space. See remarks.

</dd> <dt>

<span id="D3DX10_FILTER_SRGB"></span><span id="d3dx10_filter_srgb"></span>**D3DX10\_FILTER\_SRGB**
</dt> <dd>

Same as specifying D3DX\_FILTER\_SRGB\_IN \| D3DX\_FILTER\_SRGB\_OUT. See remarks.

</dd> </dl>

## Remarks

D3DX10 automatically performs gamma correction (to convert color data from RGB space to standard RGB space) when loading texture data. This is automatically done for instance when RGB data is loaded from a .png file into an sRGB texture. Use the SRGB filter flags to indicate if the data does not need to be converted into sRGB space.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Tex.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](d3d10-graphics-reference-d3dx10-enums.md)
</dt> </dl>

 

 




