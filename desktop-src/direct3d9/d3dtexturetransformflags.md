---
description: Defines texture coordinate transformation values.
ms.assetid: a91f33ce-2db5-437a-ac29-402b26b0d4e1
title: D3DTEXTURETRANSFORMFLAGS enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DTEXTURETRANSFORMFLAGS
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DTEXTURETRANSFORMFLAGS enumeration

Defines texture coordinate transformation values.

## Syntax


```C++
typedef enum D3DTEXTURETRANSFORMFLAGS { 
  D3DTTFF_DISABLE      = 0,
  D3DTTFF_COUNT1       = 1,
  D3DTTFF_COUNT2       = 2,
  D3DTTFF_COUNT3       = 3,
  D3DTTFF_COUNT4       = 4,
  D3DTTFF_PROJECTED    = 256,
  D3DTTFF_FORCE_DWORD  = 0x7fffffff
} D3DTEXTURETRANSFORMFLAGS, *LPD3DTEXTURETRANSFORMFLAGS;
```



## Constants

<dl> <dt>

<span id="D3DTTFF_DISABLE"></span><span id="d3dttff_disable"></span>**D3DTTFF\_DISABLE**
</dt> <dd>

Texture coordinates are passed directly to the rasterizer.

</dd> <dt>

<span id="D3DTTFF_COUNT1"></span><span id="d3dttff_count1"></span>**D3DTTFF\_COUNT1**
</dt> <dd>

The rasterizer should expect 1D texture coordinates. This value is used by fixed function vertex processing; it should be set to 0 when using a programmable vertex shader.

</dd> <dt>

<span id="D3DTTFF_COUNT2"></span><span id="d3dttff_count2"></span>**D3DTTFF\_COUNT2**
</dt> <dd>

The rasterizer should expect 2D texture coordinates. This value is used by fixed function vertex processing; it should be set to 0 when using a programmable vertex shader.

</dd> <dt>

<span id="D3DTTFF_COUNT3"></span><span id="d3dttff_count3"></span>**D3DTTFF\_COUNT3**
</dt> <dd>

The rasterizer should expect 3D texture coordinates. This value is used by fixed function vertex processing; it should be set to 0 when using a programmable vertex shader.

</dd> <dt>

<span id="D3DTTFF_COUNT4"></span><span id="d3dttff_count4"></span>**D3DTTFF\_COUNT4**
</dt> <dd>

The rasterizer should expect 4D texture coordinates. This value is used by fixed function vertex processing; it should be set to 0 when using a programmable vertex shader.

</dd> <dt>

<span id="D3DTTFF_PROJECTED"></span><span id="d3dttff_projected"></span>**D3DTTFF\_PROJECTED**
</dt> <dd>

This flag is honored by the fixed function pixel pipeline, as well as the programmable pixel pipeline in versions ps\_1\_1 to ps\_1\_3. When texture projection is enabled for a texture stage, all four floating point values must be written to the corresponding texture register. Each texture coordinate is divided by the last element before being passed to the rasterizer. For example, if this flag is specified with the D3DTTFF\_COUNT3 flag, the first and second texture coordinates are divided by the third coordinate before being passed to the rasterizer.

</dd> <dt>

<span id="D3DTTFF_FORCE_DWORD"></span><span id="d3dttff_force_dword"></span>**D3DTTFF\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Texture coordinates can be transformed using a 4 x 4 matrix before the results are passed to the rasterizer. The texture coordinate transforms are set by calling [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api), and by passing in the D3DTSS\_TEXTURETRANSFORMFLAGS texture stage state and one of the values from **D3DTEXTURETRANSFORMFLAGS**. For more information about texture transforms, see [Texture Coordinate Transformations (Direct3D 9)](texture-coordinate-transformations.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md)
</dt> </dl>

 

 
