---
title: gather4_c (sm5 - asm)
description: Same as gather4, except this instrution performs comparison on texels, similar to sample\_c.
ms.assetid: 6265151A-36CE-4D31-B7B2-233CEEBDCF87
ms.topic: reference
ms.date: 05/31/2018
---

# gather4\_c (sm5 - asm)

Same as [**gather4**](gather4--sm5---asm-.md), except this instrution performs comparison on texels, similar to [**sample\_c**](sample-c--sm4---asm-.md).



| gather4\_c\[\_aoffimmi(u,v)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\], srcSampler\[.r\], srcReferenceValue |
|-----------------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                                       | Description                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                                            | \[in\] The address of the result of the operation<br/>                                    |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>                             | \[in\] A set of texture coordinates.<br/>                                                 |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/>                         | \[in\] A texture register.<br/>                                                           |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>                             | \[in\] A sampler register.<br/>                                                           |
| <span id="srcReferenceValue"></span><span id="srcreferencevalue"></span><span id="SRCREFERENCEVALUE"></span>*srcReferenceValue*<br/> | \[in\] A register with a single component selected, which is used in the comparison.<br/> |



 

## Remarks

See [**sample\_c**](sample-c--sm4---asm-.md) for a description of how *srcReferenceValue* gets compared against each fetched texel. Unlike **sample\_c**, **gather4\_c** returns each comparison result, rather than filtering them.

For TextureCube corners, where there are three real texels and a fourth must be synthesized, the synthesis must occur after the comparison step. This means the returned comparison result for the syntesized texel can be 0, 0.33 , 0.66 , or 1. Some implementations may only return either 0 or 1 for the synthesized texel. Aside from this listing of possible results, the method for synthesizing the texel is unspecified.

For formats with float32 components, if the value being fetched is normalized, or +-INF, it is used in the comparison operation untouched. NaN is used in the comparison operation as NaN, but the exact bit representation of the NaN may be changed. Denorms are flushed to zero going into the comparison. For TextureCubes, some synthesis of the missing 4th texel must occur at corners, so the notion of returning bits unchanged for the synthesized texel does not apply.

Formats supported for *gather4\_c* are same as those supported for *sample\_c*. These are single-component formats, thus the .R on *srcSampler*, rather than an arbitrary swizzle. **gather4\_c** on an unbound resource returns 0.

Use this instruction for custom shadow map filtering.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





