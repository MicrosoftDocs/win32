---
title: texld - ps_2_0 and up
description: Sample a texture at a particular sampler, using provided texture coordinates. This instruction is different from the texld - ps\_1\_4 instruction used in pixel shader version 1\_4.
ms.assetid: 2b0d02b4-d9dd-4388-aa86-03b27bc4fdc8
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texld - ps\_2\_0 and up

Sample a texture at a particular sampler, using provided texture coordinates. This instruction is different from the [texld - ps\_1\_4](texld---ps-1-4.md) instruction used in pixel shader version 1\_4.

## Syntax



| texld dst, src0, src1 |
|-----------------------|



 

Where:

-   dst is a destination register.
-   src0 is a source register that provides the texture coordinates for the texture sample.
-   src1 identifies the [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), where \# specifies which texture sampler number to sample. The sampler has associated with it a texture and a sampler state defined by [**D3DSAMPLERSTATETYPE**](/windows/desktop/direct3d9/d3dsamplerstatetype).

### ps\_2\_0 and ps\_2\_x

dst must be a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) and only .xyzw mask (default mask) is allowed.

src0 must be either a [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md) (t\#) or a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#), with no modifier or swizzle.

src1 must be a [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), with no modifier or swizzle.

If the D3DD3DPSHADERCAPS2\_0\_NODEPENDENTREADLIMIT cap bit is not set (in D3DPSHADERCAPS2\_0), a given texture instruction ([texld](texld---ps-1-4.md), [texldp](texldp---ps.md), [texldb - ps](texldb---ps.md), [texldd](texldd---ps.md) ) may be dependent upon, at most, third order. A first-order dependent texture instruction is a texture instruction in which either:

-   src0 is a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#).
-   dst was previously written, now being written again.

A second-order dependent texture instruction is defined as a texture instruction that reads or writes to a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) whose contents, before executing the texture instruction, depend (perhaps indirectly) on the outcome of a first-order dependent texture instruction. An (n)<sup>th</sup>-order dependent texture instruction derives from an (n - 1)<sup>th</sup>-order texture instruction.

### ps\_3\_0

src1 must be a [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), with no modifier. Swizzle is allowed on src0 or src1. The swizzle is applied to the texture coordinates before texture lookup.

## Remarks

This instruction is supported in the following versions:



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texld                 |      |      |      |      | x    | x    | x     | x    | x     |



 

The number of coordinates required for src0 to perform the texture sample depends on how src1 was declared, plus the .w component. Sampler types are declared with [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md). If src1 is declared as a 2D sampler, then src0 must contain .xy coordinates; if src1 is declared as either a cube sampler or a volume sampler, then src0 must contain .xyz coordinates. Sampling a texture with fewer dimensions than are present in the texture coordinate is allowed since the extra texture coordinate component(s) are ignored.

If the source texture contains fewer than four components, defaults are placed in the missing components. Defaults depend on the texture format as shown in the following table:



| Texture Format                                                                                          | Default Values       |
|---------------------------------------------------------------------------------------------------------|----------------------|
| D3DFMT\_R5G6B5, D3DFMT\_R8G8B8, D3DFMT\_L8, D3DFMT\_L16, D3DFMT\_R3G3B2, D3DFMT\_CxV8U8, D3DFMT\_L6V5U5 | A = 1.0              |
| D3DFMT\_V8U8, D3DFMT\_V16U16, D3DFMT\_G16R16, D3DFMT\_G16R16F, D3DFMT\_G32R32F                          | B = A = 1.0          |
| D3DFMT\_A8                                                                                              | R = G = B = 0.0      |
| D3DFMT\_R16F, D3DFMT\_R32F                                                                              | G = B = A = 1.0      |
| All depth/stencil formats                                                                               | R = B = 0.0, A = 1.0 |



 

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 
