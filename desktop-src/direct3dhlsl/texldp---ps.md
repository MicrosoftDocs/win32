---
title: texldp - ps
description: Projected texture load instruction. This instruction divides the input texture coordinate by the fourth element (.a or .w) just before sampling.
ms.assetid: 82e62ba3-a9f5-4afb-8dca-4c54a00843eb
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texldp - ps

Projected texture load instruction. This instruction divides the input texture coordinate by the fourth element (.a or .w) just before sampling.

## Syntax



| texldp dst, src0, src1 |
|------------------------|



 

where

-   dst is the destination register.
-   src0 is a source register that provides the texture coordinates for the texture sample. See [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md).
-   src1 identifies the [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), where \# specifies which texture sampler number to sample. The sampler has associated with it a texture and a sampler state defined by [**D3DSAMPLERSTATETYPE**](/windows/desktop/direct3d9/d3dsamplerstatetype).

For the set of restrictions when using texldp, see [texld](texld---ps-2-0.md).

## Remarks

texldp performs projection on the coordinates read from src0 before performing the sample. Each texture coordinate is divided by src0.w, then the texture is sampled. When texldp completes, the contents of src0 are unaffected (unless dst is the same register). An alternative to using texldp is to manually perform the projection division in the shader. However, performing the division in shader code is usually slower than when performed by the texldp instruction, so avoid such additional math when possible.

The number of coordinates required for src0 to perform the texture sample depends on how src1 was declared, plus the .w component. Sampler types are declared with [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md). If src1 is declared as a 2D sampler, then src0 must contain .xyw coordinates; if src1 is declared as either a cube sampler or a volume sampler, then src0 must contain .xyzw coordinates. Sampling a 2D texture with .xyzw coordinates is allowed (the .z coordinate is ignored).

If the source texture contains fewer than four components, defaults are placed in the missing components. Defaults depend on the texture format as shown in the following table.



| Texture Format                                                                                          | Default Values for missing components |
|---------------------------------------------------------------------------------------------------------|---------------------------------------|
| D3DFMT\_R5G6B5, D3DFMT\_R8G8B8, D3DFMT\_L8, D3DFMT\_L16, D3DFMT\_R3G3B2, D3DFMT\_CxV8U8, D3DFMT\_L6V5U5 | A = 1.0                               |
| D3DFMT\_V8U8, D3DFMT\_V16U16, D3DFMT\_G16R16, D3DFMT\_G16R16F, D3DFMT\_G32R32F                          | B = A = 1.0                           |
| D3DFMT\_A8                                                                                              | R = G = B = 0.0                       |
| D3DFMT\_R16F, D3DFMT\_R32F                                                                              | G = B = A = 1.0                       |
| All depth/stencil formats                                                                               | R = B = 0.0, A = 1.0                  |



 

This instruction is supported in the following versions:



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texldp                |      |      |      |      | x    | x    | x     | x    | x     |



 

### ps\_2\_0 and ps\_2\_x

dst must be a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) and only .xyzw mask (default mask) is allowed.

src0 must be either a [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md) (t\#) or a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#), with no modifier or swizzle.

src1 must be a [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), with no modifier or swizzle.

If the D3DD3DPSHADERCAPS2\_0\_NODEPENDENTREADLIMIT cap bit is not set (in D3DPSHADERCAPS2\_0), a given texture instruction ([texld](texld---ps-1-4.md), texldp, [texldb - ps](texldb---ps.md), [texldd](texldd---ps.md) ) may be dependent upon, at most, third order. A first-order dependent texture instruction is a texture instruction in which either:

-   src0 is a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#)
-   dst was previously written, now being written again.

A second-order dependent texture instruction is defined as a texture instruction that reads or writes to a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) whose contents, before executing the texture instruction, depend (perhaps indirectly) on the outcome of a first-order dependent texture instruction. An (n)<sup>th</sup>-order dependent texture instruction derives from an (n - 1)<sup>th</sup>-order texture instruction.

### ps\_3\_0

For ps\_3\_0, src1 must be a [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), with no modifier. Swizzle is allowed on src1, and when applied, the texture lookup results are pre-swizzled before written to dst.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 