---
title: gather4_po (sm5 - asm)
description: A variant of gather4, but instead of supporting an immediate offset \ -8..7\ , the offset comes as a parameter to the instruction, and also has larger range of \ -32..31\ .
ms.assetid: A77A32B4-BD4F-46E7-9999-13EAA8A26974
ms.topic: reference
ms.date: 05/31/2018
---

# gather4\_po (sm5 - asm)

A variant of [gather4](gather4--sm5---asm-.md), but instead of supporting an immediate offset \[-8..7\], the offset comes as a parameter to the instruction, and also has larger range of \[-32..31\].



| gather4\_po dest\[.mask\], srcAddress\[.swizzle\], srcOffset\[.swizzle\], srcResource\[.swizzle\], srcSampler\[.select\_component\] |
|-------------------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                   |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the result of the operation.<br/> |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] A set of texture coordinates.<br/>               |
| <span id="srcOffset"></span><span id="srcoffset"></span><span id="SRCOFFSET"></span>*srcOffset*<br/>         | \[in\] The offset.<br/>                                 |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A texture register.<br/>                         |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>     | \[in\] A sampler register.<br/>                         |



 

## Remarks

The first two components of the 4-vector offset parameter supply 32-bit integer offsets. The other components of this parameter are ignored.

The 6 least significant bits of each offset value is honored as a signed value, yielding \[-32..31\] range.

This instruction only works with 2D textures, unlike **gather4**, which also works with TextureCubes.

The only modes honored in the sampler are the addressing modes. Only the most detailed mip in the resource view is used.

If the address falls on a texel center, this does not mean the other texels can be zeroed out.

The *srcSampler* parameter includes \[.select\_component\], allowing any single component of a texture to be retrieved, including returning defaults for missing components.

For formats with float32 components, if the value being fetched is normalized, denormalized, +-0 or +-INF, it is returned to the shader unaltered. NaN is returned as NaN, but the exact bit representation of the NaN may be changed. For TextureCubes, some synthesis of the missing 4th texel must occur at corners, so the notion of returning bits unchanged for the synthesized texel does not apply, and denorms could be flushed.

Use this instruction to extend offset range of **gather4** to be larger and programmable. The "po" suffix on the name means "programmable offset".

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

 

 





