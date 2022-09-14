---
title: sample_c_lz (sm4 - asm)
description: Performs a comparison filter. This instruction behaves like sample\_c, except LOD is 0, and derivatives are ignored.
ms.assetid: 5F11F091-AF2F-4293-88C7-824F11FE01E4
ms.topic: reference
ms.date: 05/31/2018
---

# sample\_c\_lz (sm4 - asm)

Performs a comparison filter. This instruction behaves like [sample\_c](sample-c--sm4---asm-.md), except LOD is 0, and derivatives are ignored.



| sample\_c\_lz\[\_aoffimmi(u,v,w)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource.r, // must be .r swizzle srcSampler, srcReferenceValue // single component selected |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                                       | Description                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                                            | \[in\] The address of the results of the operation.<br/>                                                             |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>                             | \[in\] A set of texture coordinates. For more information see the [sample](sample--sm4---asm-.md) instruction.<br/> |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/>                         | \[in\] A texture register. For more information see the **sample** instruction.<br/>                                 |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>                             | \[in\] A sampler register. For more information see the **sample** instruction.<br/>                                 |
| <span id="srcReferenceValue"></span><span id="srcreferencevalue"></span><span id="SRCREFERENCEVALUE"></span>*srcReferenceValue*<br/> | \[in\] A register with a single component selected, which is used in the comparison.<br/>                            |



 

## Remarks

The "lz" stands for level-zero. Because derivatives are ignored, this instruction is available in shaders other than the Pixel Shader.

If this instruction is used with a mipmapped texture, LOD 0 gets sampled, unless the sampler has an LOD clamp which places the LOD somewhere else, or if there is an LOD Bias, which would simply bias starting from 0. Because derivatives are ignored, anisotropic filtering behaves as isotropic filtering.

In Pixel Shaders, this instruction can be used inside varying flow control when the texture coordinates are derived in the shader, unlike **sample\_c**.

Fetching from an input slot that has nothing bound to it returns 0 for all components.

This instruction is available in all shaders, not just the Pixel Shader, for consistency.



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| X             | X               | x            |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





