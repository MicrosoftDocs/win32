---
title: tex - ps
description: Loads the destination register with color data (RGBA) sampled from a texture. The texture must be bound to a particular texture stage (n) using SetTexture. Texture sampling is controlled by SetSamplerState.
ms.assetid: 33f04a99-c5dc-48c1-a221-f12acb36e7f5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# tex - ps

Loads the destination register with color data (RGBA) sampled from a texture. The texture must be bound to a particular texture stage (n) using [**SetTexture**](https://msdn.microsoft.com/library/windows/desktop/bb174461). Texture sampling is controlled by [**SetSamplerState**](https://msdn.microsoft.com/library/windows/desktop/bb174456).

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

Texture coordinates may be associated with any stage using two techniques. When using a fixed function vertex shader or the fixed function pipeline, the texture stage state flag TSS\_TEXCOORDINDEX can be used in [**SetTextureStageState**](https://msdn.microsoft.com/library/windows/desktop/bb174462) to associate coordinates to a stage. Otherwise, the texture coordinates are output by the vertex shader oTₙ registers when using a programmable vertex shader.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




