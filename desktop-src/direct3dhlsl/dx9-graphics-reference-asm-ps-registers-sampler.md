---
title: Sampler (Direct3D 9 asm-ps)
description: A sampler is a input pseudo-register for a pixel shader, which is used to identify the sampling stage.
ms.assetid: 37cc28ae-fbd0-4f81-9e8e-f9609980d84e
keywords:
- Sampler, Type (Direct3D 9 asm-ps)
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Sampler (Direct3D 9 asm-ps)

A sampler is a input pseudo-register for a pixel shader, which is used to identify the sampling stage. There are 16 pixel shader sampling stage registers: s0 to s15. Therefore, up to 16 texture surfaces can be read in a single shader pass. The instructions that use a sampler register are texld and texldp.

Sampler must be declared before use with the [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md) instruction.



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|-------|------|------|-------|
| Sampler               |      |      |      |      | x    | x     | x    | x    | x     |



 

Samplers are pseudo registers because you cannot directly read or write to them.

A sampling unit corresponds to the texture sampling stage, encapsulating the sampling-specific state provided by [**SetSamplerState**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-setsamplerstate). Each sampler uniquely identifies a single texture surface, which is set to the corresponding sampler using the [**SetTexture**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture). However, the same texture surface can be set at multiple samplers.

At draw time, a texture cannot be simultaneously set as a render target and a texture at a stage.

A sampler might appear as the only argument in the texture load instruction: [texldl - ps](texldl---ps.md).

In ps\_3\_0, if a sampler is used, it needs to be declared at the beginning of the shader program using the [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md) instruction.

Sampling a texture with a higher dimension than is present in the texture coordinates is illegal. Sampling a texture with a lower dimension than is present in the texture coordinates will ignore the extra texture coordinates.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 