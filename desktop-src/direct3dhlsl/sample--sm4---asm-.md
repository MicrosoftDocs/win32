---
title: sample (sm4 - asm)
description: Samples data from the specified Element/texture using the specified address and the filtering mode identified by the given sampler. | sample (sm4 - asm)
ms.assetid: 9055D3EE-FD4A-418C-A743-D12E8BDF69FF
ms.topic: reference
ms.date: 05/31/2018
---

# sample (sm4 - asm)

Samples data from the specified Element/texture using the specified address and the filtering mode identified by the given sampler.



| sample\[\_aoffimmi(u,v,w)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\], srcSampler |
|--------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                                                        |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the result of the operation.<br/>                                      |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] A set of texture coordinates. For more information, see the **Remarks** section.<br/> |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A texture register. For more information, see the **Remarks** section.<br/>           |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>     | \[in\] A sampler register. For more information, see the **Remarks** section.<br/>           |



 

## Remarks

The source data may come from any Resource Type, other than Buffers.

*srcAddress* provides the set of texture coordinates needed to perform the sample, as floating point values referencing normalized space in the texture. Address wrapping modes (wrap/mirror/clamp/border etc.) are applied for texture coordinates outside \[0...1\] range, taken from the sampler state (s\#), and applied after any address offset is applied to texture coordinates.

*srcResource* is a texture register (t\#). This is simply a placeholder for a texture, including the return data type of the resource being sampled. All of this information is declared in the Shader preamble. The actual resource to be sampled is bound to the Shader externally at slot \# (for t\#).

*srcSampler* is a sampler register (s). This is simply a placeholder for a collection of filtering controls such as point vs. linear, mipmapping and address wrapping controls.

The set of information required for the hardware to perform sampling is split into two orthogonal pieces. First, the texture register provides source data type information including, for example, information about whether the texture contains SRGB data. It also references the actual memory being sampled. Second, the sampler register defines the filtering mode to apply.

### Array Resources

For Texture1D Arrays, the *srcAddress* g component (POS-swizzle) selects which Array Slice to fetch from. This is always treated as a scaled float value, rather than the normalized space for standard texture coordinates, and a round-to-nearest even is applied on the value, followed by a clamp to the available BufferArray range.

For Texture2D Arrays, the *srcAddress* b component (POS-swizzle) selects which Array Slice to fetch from, otherwise using the same semantics described for Texture1D Arrays .

### Address Offset

The optional \[\_aoffimmi(u,v,w)\] suffix (address offset by immediate integer) indicates that the texture coordinates for the sample are to be offset by a set of provided immediate texel space integer constant values. The literal values are a set of 4 bit 2's complement numbers, having integer range \[-8,7\]. This modifier is defined for all Resources, including Texture1D/2D Arrays and Texture3D, but it is undefined for TextureCube.

Hardware can take advantage of immediate knowledge that a traversal over some footprint of texels about a common location is being performed by a set of sample instructions. This can be conveyed using \_aoffimmi(u,v,w).

The offsets are added to the texture coordinates, in texel space, relative to each miplevel being accessed. So even though texture coordinates are provided as normalized float values, the offset applies a texel-space integer offset.

Address offsets are not applied along the array axis of Texture1D/2D Arrays.

\_aoffimmi v,w components are ignored for Texture1Ds.

\_aoffimmi w component is ignored for Texture2Ds.

Address wrapping modes (wrap/mirror/clamp/border etc.) from the sampler state (s\#) are applied after any address offset is applied to texture coordinates.

### Return Type Control

The data format returned by the sample to the destination register is determined by the resource format (DXGI\_FORMAT\*) bound to the *srcResource* parameter (t\#). For example, if the specified t\# was bound with a resource with format DXGI\_FORMAT\_A8B8G8R8\_UNORM\_SRGB, then the sampling operation will convert sampled texels from gamma 2.0 to 1.0, apply filtering, and the result will written to the destination register as floating point values in the range \[0..1\].

Returned values are 4-vectors (with format-specific defaults for components not present in the format). The swizzle on *srcResource* determines how to swizzle the 4-component result coming back from the texture sample/filter, after which .mask on *dest* determines which components in *dest* get updated.

When **sample** reads a 32-bit float value into a 32-bit register, with point sampling (no filtering), it may or may not flush denormal values, but otherwise numbers are unmodified. If the uncertainty with point sampling denormal values is an issue for an application,use the [ld](ld--sm4---asm-.md) instruction, which guarantees that 32-bit float values are read unmodified.

### LOD Calculation

For details on how derivatives are calculated in the process of determining LOD for filtering, see [deriv\_rtx](deriv-rtx--sm4---asm-.md) and [deriv\_rty](deriv-rty--sm4---asm-.md). The **sample** instruction implicitly computes derivatives on the texture coordinates using the same definition that the **deriv** Shader instructions use. This does not apply to [sample\_l](sample-l--sm4---asm-.md) or [sample\_d](sample-d--sm4---asm-.md) instructions. For those instructions, LOD or derivatives are provided directly by the application.

For the **sample** instruction, implementations can choose to share the same LOD calculation across all 4 pixels in a 2x2 stamp (but no larger area), or perform per-pixel LOD calculations.

### Miscellaneous Details

For Buffer & Texture1D, *srcAddress* .gba components (POS-swizzle) are ignored. For Texture1D Arrays, *srcAddress* .ba components (POS-swizzle) are ignored. For Texture2Ds, *srcAddress* .a component (POS-swizzle) is ignored.

Fetching from an input slot that has nothing bound to it returns 0 for all components.

### Restrictions

-   *srcResource* must be a t\# register. *srcResource* cannot be a ConstantBuffer, which cannot be bound to t\# registers.
-   *srcSampler* must be an s\# register.
-   Relative addressing on *srcResource* or *srcSampler* is not permitted.
-   *srcAddress* must be a temp (r\#/x\#), constantBuffer (cb\#), input (v\#) register or immediate value(s).
-   *dest* must be a temp (r\#/x\#) or output (o\*\#) register.
-   \_aoffimmi(u,v,w) is not permitted for TextureCubes.

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

 

 





