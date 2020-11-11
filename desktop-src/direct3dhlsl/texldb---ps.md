---
title: texldb - ps
description: Biased texture load instruction. This instruction uses the fourth element (.a or .w) to bias the texture-sampling level-of-detail just before sampling.
ms.assetid: cafd72c9-b7bb-4e3f-8a8c-de26a4446864
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texldb - ps

Biased texture load instruction. This instruction uses the fourth element (.a or .w) to bias the texture-sampling level-of-detail just before sampling.

## Syntax



| texldb dst, src0, src1 |
|------------------------|



 

Where:

-   dst is the destination register.
-   src0 is a source register that provides the texture coordinates for the texture sample. See [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md).
-   src1 identifies the [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), where \# specifies which texture sampler number to sample. The sampler has associated with it a texture and a sampler state defined by [**D3DSAMPLERSTATETYPE**](/windows/desktop/direct3d9/d3dsamplerstatetype).

For the restrictions when using texldb, see the [texld - ps\_2\_0 and up](texld---ps-2-0.md) instruction.

### ps\_2\_0 and ps\_2\_x

dst must be a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) and only .xyzw mask (default mask) is allowed.

src0 must be either a [Texture Coordinate Register](dx9-graphics-reference-asm-ps-registers-texture-coordinate.md) (t\#) or a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#), with no modifier or swizzle.

src1 must be a [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), with no modifier or swizzle.

If the D3DD3DPSHADERCAPS2\_0\_NODEPENDENTREADLIMIT cap bit is not set (in D3DPSHADERCAPS2\_0), a given texture instruction (texld, texldp, texldb, texldd) may be dependent upon, at most, third order. A first-order dependent texture instruction is a texture instruction in which either:

-   src0 is a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#).
-   dst was previously written, now being written again.

A second-order dependent texture instruction is defined as a texture instruction that reads or writes to a [Temporary Register](dx9-graphics-reference-asm-ps-registers-temporary.md) (r\#) whose contents, before executing the texture instruction, depend (perhaps indirectly) on the outcome of a first-order dependent texture instruction. An (n)<sup>th</sup>-order dependent texture instruction derives from an (n - 1)<sup>th</sup>-order texture instruction.

### ps\_3\_0

src1 must be a [Sampler (Direct3D 9 asm-ps)](dx9-graphics-reference-asm-ps-registers-sampler.md) (s\#), with no modifier. Swizzle is allowed on src1, and when applied, the texture lookup results are pre-swizzled before written to dst.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texldb                |      |      |      |      | x    | x    | x     | x    | x     |



 

texldb biases the mipmap level-of-detail, computed normally as part of the sample process by the (signed) value in src0.w. Positive bias values will result in smaller mipmaps being selected and vice versa. For ps\_2\_0 and ps\_2\_x, bias values can be within the range \[-3.0, +3.0\]. For ps\_3\_0, bias values can be within the range \[-16.0, +15.0\]. Bias values outside these ranges produce undefined results. The sampler state D3DSAMP\_MIPMAPLODBIAS is still honored, and the texldb bias is added to this, but on a per-pixel basis. After the biased level-of-detail is computed, D3DSAMP\_MAXMIPLEVEL is still honored and the texture sample occurs. After texldb, the contents of src0 are unaffected (unless dst is the same register).

The number of coordinates required for src0 to perform the texture sample depends on how src1 was declared, plus the .w component. Sampler types are declared with [dcl\_samplerType (sm2, sm3 - ps asm)](dcl-samplertype---ps.md). If src1 is declared as a 2D sampler, then src0 must contain .xyw coordinates; if src1 is declared as either a cube sampler or a volume sampler, then src0 must contain .xyzw coordinates. Sampling a 2D texture with .xyzw coordinates is allowed (the .z coordinate is ignored).

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

 

 