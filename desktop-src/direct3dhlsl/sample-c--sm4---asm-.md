---
title: sample_c (sm4 - asm)
description: Performs a comparison filter.
ms.assetid: 59786ED2-48FB-494E-A5A4-F732D63BF01B
ms.topic: reference
ms.date: 05/31/2018
---

# sample\_c (sm4 - asm)

Performs a comparison filter.



| sample\_c\[\_aoffimmi(u,v,w)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource.r, // must be .r swizzle srcSampler, srcReferenceValue // single component selected |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                                       | Description                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                                            | \[in\] The address of the results of the operation.<br/>                                                             |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>                             | \[in\] A set of texture coordinates. For more information see the [sample](sample--sm4---asm-.md) instruction.<br/> |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/>                         | \[in\] A texture register. For more information see the **sample** instruction.<br/>                                 |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>                             | \[in\] A sampler register. For more information see the **sample** instruction.<br/>                                 |
| <span id="srcReferenceValue"></span><span id="srcreferencevalue"></span><span id="SRCREFERENCEVALUE"></span>*srcReferenceValue*<br/> | \[in\] A register with a single component selected, which is used in the comparison.<br/>                            |



 

## Remarks

The primary purpose for this instruction is to provide a building-block for Percentage-Closer Depth filtering. The "c" in **sample\_c** stands for Comparison.

The operands to **sample\_c** are identical to the [sample](sample--sm4---asm-.md) instruction, except that there is an additional float32 source operand, *srcReferenceValue*, which must be a register with single-component selected, or a scalar literal.

The *srcResource* parameter must have a .r (red) swizzle. **sample\_c** operates exclusively on the red component, and returns a single value. The .r swizzle on *srcResource* indicates that the scalar result is replicated to all components.

When a Depth Buffer is set as an input texture, the depth value shows up in the red component.

If this instruction is used with a Resource that is not a Texture1D/2D/2DArray/Cube/CubeArray, it produces undefined results.

When this instruction is executed, the sampling hardware uses the current Sampler's ComparisonFunction to compare *srcReferenceValue* against the Red component value for the source Resource at each filter "tap" location (texel) that the currently configured texture filter covers, based on the provided coordinates in *srcAddress*.

The comparison occurs after *srcReferenceValue* has been quantized to the precision of the texture format, in exactly the same way that z is quantized to depth buffer precision before Depth Comparison at the Output Merger visibility test. This includes a clamp to the format range (e.g. \[0..1\] for a UNORM format).

The source texel's Red component is compared against the quantized *srcReferenceValue*. For texels that fall off the Resource, the Red component value is determined by applying the Address Modes (and BorderColorR if in Border mode) from the Sampler. The comparison honors all D3D11 floating point comparison rules, in the case the texture format is floating point.

Each comparison that passes returns 1.0f as the Red component value for the texel, and each comparison that fails returns 0.0f as the Red value for the texture. Filtering then occurs exactly as specified by the Sampler states, operating only in the Red component, and returning a single scalar filter result back to the Shader, replicated to all masked *dest* components.

The use of **sample\_c** is orthogonal to all other general purpose filtering controls. **sample\_c** works seamlessly with the other general purpose filter modes. **sample\_c** changes the behavior of the general purpose filters such that the values being filtered all become 1.0f or 0.0f due to comparison results.

Fetching from an input slot that has nothing bound to it returns 0 for all components.

For more information, see the [sample](sample--sm4---asm-.md) instruction.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               |                 | x            |



 

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

 

 





