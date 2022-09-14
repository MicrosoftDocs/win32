---
title: Texture Coordinate Register (HLSL VS reference)
description: This vertex shader output register contains per-vertex texture coordinates.
ms.assetid: d42c8e4c-8227-4fe8-9432-90c592011024
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Texture Coordinate Register (HLSL VS reference)

This vertex shader output register contains per-vertex texture coordinates.

A register consists of properties that determine how each register behaves.



| Property        | Description   |
|-----------------|---------------|
| Name            | oT0 - oT7     |
| Count           | Eight vectors |
| I/O permissions | Write-only    |



 

The output texture coordinates registers are an array of output data registers. The register data is iterated and used as texture coordinates by the texture sampling stages to supply data to the pixel shader.

When writing to a texture coordinate register, it is recommended that you pass only as many floating point values as the dimension of the corresponding texture map. Control the values that are passed with a modifier. For example, use .xy for a 2D texture map.

The fixed function vertex pipeline flags, [**D3DTEXTURETRANSFORMFLAGS**](/windows/desktop/direct3d9/d3dtexturetransformflags) (D3DTTFF\_COUNT1, D3DTTFF\_COUNT2, D3DTTFF\_COUNT3, D3DTTFF\_COUNT4), should be set to zero if you are using a programmable vertex shader.

Object vertex data supplies input texture coordinates. Objects that do not use tiled textures commonly have texture coordinates in the range \[0,1\]. Objects that use tiled textures, such as terrain, typically have texture coordinates that range from \[-n,+n\] where n can be any floating point number.

Texture coordinate interpolation is performed on vertex data for rasterization. During rasterization, texture coordinates are interpolated between object vertices, modified by texture wrapping, and scaled by the texture size (also taking into account texture addressing modes) to produce an integer index. The index is then used to perform a texture lookup. Use the MaxTextureRepeat value in [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9) to determine how many times a texture can be tiled.

## Example

Declare the texture coordinate register.


```
dcl_texcoord v7
```



Copy the per-vertex texture coordinates to the output register.


```
mov oT0, v7
```





| Vertex shader versions      | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------------|------|------|-------|------|------|-------|
| Texture Coordinate Register | x    | x    | x     | x    | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 