---
title: gather4 (sm4.1 - asm)
description: Gathers the four texels that would be used in a bi-linear filtering operation and packs them into a single register. | gather4 (sm4.1 - asm)
ms.assetid: 219B25AE-CBF9-4B68-B2DB-6D8C3C5B4CEA
ms.topic: reference
ms.date: 05/31/2018
---

# gather4 (sm4.1 - asm)

Gathers the four texels that would be used in a bi-linear filtering operation and packs them into a single register.



| gather4\[\_aoffimmi(u,v)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\] srcSampler.r |
|--------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the result of the operation.<br/>                                                                                                       |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] Contains the texture coordinates. <br/>                                                                                                                |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A resource register. <br/> The swizzle allows the returned values to be swizzled arbitrarily before they are written to *dest*. <br/>            |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>     | \[in\] A sampler register.<br/> This parameter must have a .r (red) swizzle, which indicates that the value of the R channel is copied to *dest*. <br/> |



 

## Remarks

This operation only works with single channel 2D or CubeMap textures. For 2D textures only the addressing modes of the sampler are used and the top level of any mip pyramid is used.

This instruction behaves like the [sample](sample--sm4---asm-.md) instruction, but a filtered sample is not generated. The four samples that would contribute to filtering are placed into xyzw in counter clockwise order starting with the sample to the lower left of the queried location. This is the same as point sampling with (u,v) texture coordinate deltas at the following locations: (-,+),(+,+),(+,-),(-,-), where the magnitude of the deltas are always half a texel.

For CubeMap textures when a bi-linear footprint spans an edge texels from the neighboring face are used. Corners use the same rules as the **sample** instruction; that is the unkown corner is considered the average of the three impinging face corners.

The texture format restrictions that apply to the **sample** instructions also apply to the **gather4** instruction.

For hardware implementations, optimizations in traditional bilinear filtering that detect samples directly on texels and skip reading of texels that would have weight 0 cannot be leveraged with **gather4**. **gather4** always returns all requested texels.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
| x             | x               | x            |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





