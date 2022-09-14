---
title: ps_3_0
description: Learn about ps_3_0, a programmable pixel shader, which is made up of a set of instructions that operate on pixel data.
ms.assetid: 3eabf173-9d9d-45b2-bc30-de857428f3ee
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_3\_0

A programmable pixel shader is made up of a set of instructions that operate on pixel data. Registers transfer data in and out of the ALU. Additional control can be applied to modify the instruction, the results, or what data gets written out.

-   [ps\_3\_0 Instructions](dx9-graphics-reference-asm-ps-instructions-ps-3-0.md) contains a list of the available instructions.
-   [ps\_3\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-3-0.md) lists the different types of registers used by the pixel shader ALU.
-   [Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers.md) Are used to modify the way an instruction works.
-   [Destination Register Write Mask](dx9-graphics-reference-asm-ps-registers-modifiers-write-mask.md) determines what components of the destination register get written.
-   [Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md) alter the source register data before the instruction runs.
-   [Source Register Swizzling](dx9-graphics-reference-asm-ps-registers-modifiers-source-register-swizzling.md) gives additional control over which register components are read, copied, or written.

## New Features

Add a face register. Add a position register. Color registers (v\#) are now fully floating point and the texture coordinate registers (t\#) have been consolidated. Input declarations take the usage names, and multiple usages are permitted for components of a given register.

## Dynamic Flow Control

The device supports dynamic flow control ([if bool - ps](if-bool---ps.md), [break - ps](break---ps.md), and [break\_comp - ps](break-comp---ps.md)). The depth of nesting ranges from 0 to 24.

## Number of Temporary Registers

The number of temporary registers supported is 32.

## Static Flow Control Nesting Depth

The [call - ps](call---ps.md)/[callnz](callnz-bool---ps.md) /[call\_pred](callnz-pred---ps.md) can be nested to a maximum depth of 4. Independently, [loop - ps](loop---ps.md)/[rep - ps](rep---ps.md) instructions can be nested to a maximum depth of 4.

## Arbitrary Swizzle

Arbitrary swizzle is supported. See [Source Register Swizzling](dx9-graphics-reference-asm-ps-registers-modifiers-source-register-swizzling.md).

## Gradient Instructions

Gradient instructions are supported. See [dsx - ps](dsx---ps.md), [dsy - ps](dsy---ps.md), and [texldd - ps](texldd---ps.md).

## Predication

Instruction predication is supported. See [Predicate Register](dx9-graphics-reference-asm-ps-registers-predicate.md).

## Dependent Read Limit

There are no dependent read limits.

## Texture Instruction Limit

There is no limit on texture instructions.

## Instruction Count

Each pixel shader is allowed anywhere from 512 up to the number of slots in MaxPixelShader30InstructionSlots (not more than 32768). The number of instructions run can be much higher because of the looping support. MaxPShaderInstructionsExecuted should be at least 2^16.

## Sampler Count

The number of texture samplers available is 16.

## Device Caps

If ps\_3\_0 is supported, the following caps are supported in hardware (at a minimum):



| Cap                                                                                                          | Value                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MaxTextureWidth, MaxTextureHeight                                                                            | 4K each                                                                                                                                                                                                                                                                                               |
| MaxTextureRepeat                                                                                             | 8K                                                                                                                                                                                                                                                                                                    |
| MaxAnisotropy                                                                                                | 16                                                                                                                                                                                                                                                                                                    |
| PixelShaderVersion                                                                                           | 3\_0                                                                                                                                                                                                                                                                                                  |
| MaxPixelShader30InstructionSlots                                                                             | 512                                                                                                                                                                                                                                                                                                   |
| The following primitive caps are set:                                                                        | D3DPMISCCAPS\_BLENDOP, D3DPMISCCAPS\_CLIPPLANESCALEDPOINTS, D3DPMISCCAPS\_CLIPTLVERTS, D3DPMISCCAPS\_CULLCCW, D3DPMISCCAPS\_CULLCW, D3DPMISCCAPS\_CULLNONE, D3DPMISCCAPS\_FOGINFVF, D3DPMISCCAPS\_MASKZ                                                                                               |
| The following raster caps are set:                                                                           | D3DPRASTERCAPS\_MIPMAPLODBIAS, D3DPRASTERCAPS\_ANISOTROPY, D3DPRASTERCAPS\_COLORPERSPECTIVE, D3DPRASTERCAPS\_SCISSORTEST in D3DCAPS9                                                                                                                                                                  |
| Full support for depth bias including:                                                                       | D3DPRASTERCAPS\_SLOPESCALEDEPTHBIAS, D3DPRASTERCAPS\_DEPTHBIAS                                                                                                                                                                                                                                        |
| Full set of comparisons for depth and alpha test including:                                                  | All the D3DPCMPCAPS in D3DCAPS9.                                                                                                                                                                                                                                                                      |
| Source blending modes                                                                                        | All blending modes are supported as a source (except D3DPBLENDCAPS\_SRCALPHASAT, D3DPBLENDCAPS\_BOTHSRCALPHA, and D3DPBLENDCAPS\_BOTHINVSRCALPHA).                                                                                                                                                    |
| The following texture caps are supported:                                                                    | D3DPTEXTURECAPS\_CUBEMAP, D3DPTEXTURECAPS\_MIPCUBEMAP, D3DPTEXTURECAPS\_MIPMAP, D3DPTEXTURECAPS\_MIPVOLUMEMAP, D3DPTEXTURECAPS\_PERSPECTIVE, D3DPTEXTURECAPS\_PROJECTED, D3DPTEXTURECAPS\_TEXREPEATNOTSCALEDBYSIZE, D3DPTEXTURECAPS\_VOLUMEMAP                                                        |
| The following are supported on texture filter caps, volume texture filter caps and cube texture filter caps: | D3DPTFILTERCAPS\_MINFPOINT, D3DPTFILTERCAPS\_MINFLINEAR, D3DPTFILTERCAPS\_MINFANISOTROPIC (This is not required for VolumeTextureFilterCaps and CubeTextureFilterCaps ), D3DPTFILTERCAPS\_MIPFPOINT, D3DPTFILTERCAPS\_MIPFLINEAR, D3DPTFILTERCAPS\_MAGFPOINT, D3DPTFILTERCAPS\_MAGFLINEAR             |
| The following texture address modes are supported at vertex and pixel stages:                                | D3DPTADDRESSCAPS\_WRAP, D3DPTADDRESSCAPS\_MIRROR, D3DPTADDRESSCAPS\_CLAMP, D3DPTADDRESSCAPS\_BORDER, D3DPTADDRESSCAPS\_INDEPENDENTUV, D3DPTADDRESSCAPS\_MIRRORONCE                                                                                                                                    |
| All the pixel shader caps are supported.                                                                     | DynamicFlowControlDepth = 24, NumTemps = 32, StaticFlowControlDepth = 4, NumInstructionSlots = 512. The following features are supported: predication, arbitrary swizzles, and gradient instructions. There is no dependent-read limit, and no limit on the mixture of texture and math instructions. |
| All the stencil operations are supported. This includes two sided stencil.                                   | See [**D3DSTENCILOP**](/windows/desktop/direct3d9/d3dstencilop)                                                                                                                                                                                                                                                        |
| Device support point size per vertex                                                                         | D3DFVFCAPS\_PSIZE in D3DCAPS9                                                                                                                                                                                                                                                                         |
| Non-power of 2 texture support.                                                                              | Either full support or conditional non-pow-2 support; device should not have the square texture only limitation as in D3DPTEXTURECAPS\_SQUAREONLY.                                                                                                                                                    |
| If the device supports multiple rendertargets, the following caps are supported:                             | D3DPMISCCAPS\_INDEPENDENTWRITEMASKS, D3DPMISCCAPS\_MRTPOSTPIXELSHADERBLENDING                                                                                                                                                                                                                         |
| If vs\_3\_0 is supported                                                                                     | MaxUserClipPlanes in D3DCAPS9 is 6                                                                                                                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[Pixel Shaders](dx9-graphics-reference-asm-ps.md)
</dt> </dl>

 

 