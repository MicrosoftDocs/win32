---
title: Sampler (Direct3D 9 asm-vs)
description: A sampler is a input pseudo-register for a vertex shader, which is used to identify the sampling stage. There are four vertex shader samplers s0 to s3. Four texture surfaces can be read in a single shader pass.
ms.assetid: a4588ced-24e2-4d4e-93e4-35a985bafaa4
keywords:
- Sampler, Type (Direct3D 9 asm-vs)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sampler (Direct3D 9 asm-vs)

A sampler is a input pseudo-register for a vertex shader, which is used to identify the sampling stage. There are four vertex shader samplers: s0 to s3. Four texture surfaces can be read in a single shader pass.

Sampler (Direct3D 9 asm-vs)s are pseudo registers because you cannot directly read or write to them.

A sampling unit corresponds to the texture sampling stage, encapsulating the sampling-specific state provided by [**SetSamplerState**](https://msdn.microsoft.com/library/windows/desktop/bb174456). Each sampler uniquely identifies a single texture surface, which is set to the corresponding sampler using the [**SetTexture**](https://msdn.microsoft.com/library/windows/desktop/bb174461). However, the same texture surface can be set at multiple samplers.

At draw time, a texture cannot be simultaneously set as a render target and a texture at a stage.

Because there are four samplers, up to four texture surfaces can be read from in a single shader pass. A sampler might appear as the only argument in the texture load instruction: [texldl - vs](texldl---vs.md).

In vs\_3\_0, if a sampler is used, it needs to be declared at the beginning of the shader program using the [dcl\_samplerType (sm3 - vs asm)](dcl-samplertype---vs.md) instruction.



| Vertex shader versions | 1\_1 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|------------------------|------|------|-------|------|------|-------|
| Sampler                |      |      |       |      | x    | x     |



 

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> <dt>

[Vertex Textures in vs\_3\_0 (DirectX HLSL)](https://msdn.microsoft.com/library/windows/desktop/bb206339)
</dt> </dl>

 

 




