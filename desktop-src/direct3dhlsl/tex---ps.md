---
title: tex - ps
description: Loads the destination register with color data (RGBA) sampled from a texture. The texture must be bound to a particular texture stage (n) using SetTexture. Texture sampling is controlled by SetSamplerState.
ms.assetid: 'vs|directx_sdk|~\tex___ps.htm'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# tex - ps

Loads the destination register with color data (RGBA) sampled from a texture. The texture must be bound to a particular texture stage (n) using [**SetTexture**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture). Texture sampling is controlled by [**SetSamplerState**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-setsamplerstate).

## Syntax



| tex dst |
|---------|



 

where

-   dst is the destination register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| tex                   | x    | x    | x    |      |      |      |       |      |       |



 

The destination register number specifies the texture stage number.

Texture sampling uses texture coordinates to look up, or sample, a color value at the specified (u,v,w,q) coordinates while taking into account the texture stage state attributes.

The texture coordinate data is interpolated from the vertex texture coordinate data and is associated with a specific texture stage. The default association is a one-to-one mapping between texture stage number and texture coordinate declaration order. This means that the first set of texture coordinates defined in the vertex format are by default associated with texture stage 0.

Texture coordinates may be associated with any stage using two techniques. When using a fixed function vertex shader or the fixed function pipeline, the texture stage state flag TSS\_TEXCOORDINDEX can be used in [**SetTextureStageState**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate) to associate coordinates to a stage. Otherwise, the texture coordinates are output by the vertex shader oTₙ registers when using a programmable vertex shader.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 