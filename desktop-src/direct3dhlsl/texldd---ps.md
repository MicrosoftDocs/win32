---
title: texldd - ps
description: Samples a texture with additional gradient inputs.
ms.assetid: 6d6b3180-d82e-4be4-929b-e5a6431bec38
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texldd - ps

Samples a texture with additional gradient inputs.

## Syntax



| texldd, dst, src0, src1, src2, src3 |
|-------------------------------------|



 

Where:

-   dst is a destination register.
-   src0 is a source register that provides the texture coordinates for the texture sample. See [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md).
-   src1 identifies the source sampler register (s\#), where \# specifies which texture sampler number to sample. The sampler has associated with it a texture and a control state defined by the [**D3DSAMPLERSTATETYPE**](/windows/desktop/direct3d9/d3dsamplerstatetype) enumeration (ex. D3DSAMP\_MINFILTER).
-   src2 is an input source register that specifies the x gradient.
-   src3 is an input source register that specifies the y gradient.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texldd                |      |      |      |      |      | x \* | x     | x    | x     |



 

\* This instruction is only supported by ps\_2\_a. It is not supported by ps\_2\_b. For more information about profiles, see [**D3DXGetPixelShaderProfile**](/windows/desktop/direct3d9/d3dxgetpixelshaderprofile).

This instruction samples a texture using the texture coordinates at src0, the sampler specified by src1, and the gradients DSX and DSY coming from src2 and src3. The x and y gradient values are used to select the appropriate mipmap level of the texture for sampling.

All sources support arbitrary swizzles.

All write masks are valid on the destination.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 