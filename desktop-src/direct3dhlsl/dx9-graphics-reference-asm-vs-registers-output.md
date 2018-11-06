---
title: Output Registers
description: Output Registers
ms.assetid: 44148185-1051-44b9-afde-a2ecd76c829f
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Output Registers

-   Vertex Color Register
-   Fog Register
-   Position\_Register
-   Point\_Size\_Register
-   Texture\_Coordinate\_Register

Register names are preceded by a lowercase letter o, indicating that the output registers are write-only.

## Vertex Color Register - oD0, oD1

oD0 is the diffuse color register. oD1 is the specular color register. The oD0 value is interpolated and is written to the input color register 0 (v0) of the pixel shader. The oD1 value is interpolated and written to the input color register 1 (v1) of the pixel shader. For more information about pixel shader color registers, see Registers.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Vertex Color Register  | x    | x    | x     | x    |      |       |



 

## Fog Register - oFog

The output fog value registers. The value is the fog factor to be interpolated and then routed to the fog table. Only the scalar x-component of the fog is used. Values are clamped between zero and one before passing to the rasterizer.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Fog Register           | x    | x    | x     | x    |      |       |



 

## Position Register - oPos

The output position registers. The value is the position in homogeneous clipping space. This value must be written by the vertex shader.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Position Register      | x    | x    | x     | x    |      |       |



 

## Point Size Register - oPts

The output point-size registers. Only the scalar x-component of the point size is used.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Point Size Register    | x    | x    | x     | x    |      |       |



 

## Texture Coordinate Register - oT0 to oT7

The output texture coordinates registers. Specifically, these are an array of output data registers that are iterated and used as texture coordinates by the texture sampling stages routing data to the pixel shader.



| Vertex shader versions      | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------------|------|------|-------|------|------|-------|
| Texture Coordinate Register | x    | x    | x     | x    |      |       |



 

When writing to a texture coordinate register, it is recommended to pass only as many floating point values as the dimension of the corresponding texture map. Control the values passed with a modifier. For example, use .xy for a 2D texture map.

When texture projection is enabled for a texture stage, all four floating point values must be written to the corresponding texture register.

Any of the D3DTTFF\* texture transform flags should be zero when the programmable pipeline is being used.

### Texture Coordinate Range

Object vertex data supplies input texture coordinates. Objects that do not used tiled textures commonly have texture coordinates in the range \[0,1\]. Objects that use tiled textures, such as terrain, typically have texture coordinates that range from \[-?,+?\] where ? can be a large floating point number.

Texture coordinate interpolation is performed on vertex data for rasterization. During rasterization, texture coordinates are interpolated between object vertices, modified by texture wrapping and scaled by the texture size (also taking into account texture address mode) to produce an integer index. The index is then used to perform a texture lookup. MaxTextureRepeat can be used to determine how many times a texture can be tiled.

If texture coordinates are read directly into a pixel shader (using texcoord or texcrd), the texture coordinate range depends on the instruction and the pixel shader version.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




