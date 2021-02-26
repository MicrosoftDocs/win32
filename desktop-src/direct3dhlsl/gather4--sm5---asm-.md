---
title: gather4 (sm5 - asm)
description: Gathers the four texels that would be used in a bi-linear filtering operation and packs them into a single register. | gather4 (sm5 - asm)
ms.assetid: 5F93BB70-7696-48E4-BCD3-91D5D42FF63E
ms.topic: reference
ms.date: 05/31/2018
---

# gather4 (sm5 - asm)

Gathers the four texels that would be used in a bi-linear filtering operation and packs them into a single register. This instruction only works with 2D or CubeMap textures, including arrays. Only the addressing modes of the sampler are used and the top level of any mip pyramid is used.



| gather4\[\_aoffimmi(u,v)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\], srcSampler\[.select\_component\] |
|-----------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                    |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the results of the operation.<br/> |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] A set of texture coordinates.<br/>                |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A texture register.<br/>                          |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>     | \[in\] A sampler register.<br/>                          |



 

## Remarks

This instruction behaves like the [**sample**](sample--sm4---asm-.md) instruction, but a filtered sample is not generated. The four samples that would contribute to filtering are placed into xyzw in counter clockwise order starting with the sample to the lower left of the queried location. This is the same as point sampling with (u,v) texture coordinate deltas at the following locations: (-,+),(+,+),(+,-),(-,-), where the magnitude of the deltas are always half a texel.

For CubeMap textures, when a bi-linear footprint spans an edge, texels from the neighboring face are used. Corners use the same rules as the [**sample**](sample--sm4---asm-.md) instruction; that is, the unknown corner is considered the average of the three impinging face corners.

There are texture format restrictions that apply to **gather4** which are expressed in the format list.

The swizzle on *srcResource* allows the returned values to be swizzled arbitrarily before they are written to the destination.

The .select\_component on *srcSampler* chooses which component of the source texture (r/g/b/a) to read 4 texels from.

For formats with float32 components, if the value being fetched is normalized, denormalized, +-0 or +-INF, it is returned to the shader unaltered. NaN is returned as NaN, but the exact bit representation of the NaN may be changed. For TextureCubes, some synthesis of the missing 4th texel must occur at corners, so returning bits unchanged for the synthesized texel does not apply, and denorms could be flushed.

For hardware implementations, optimizations in traditional bilinear filtering that detect samples directly on texels and skip reading of texels that would have weight 0 cannot be leveraged with this instruction. *gather4* always returns all requested texels.

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

 

 





