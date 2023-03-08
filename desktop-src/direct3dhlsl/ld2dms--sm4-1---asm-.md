---
title: ld2dms (sm4.1 - asm)
description: Reads individual samples out of 2-dimensional multi-sample textures.
ms.assetid: 8D92BFA8-4B22-46F3-876D-8D84BB3A96E7
ms.topic: reference
ms.date: 05/31/2018
---

# ld2dms (sm4.1 - asm)

Reads individual samples out of 2-dimensional multi-sample textures.



| ld2dms\[\_aoffimmi(u,v)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\], sampleIndex |
|------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of result of the operation. <br/>                                                                 |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] The texture coordinates needed to perform the sample.<br/>                                                    |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A texture register (t\#) which must have been declared identifying which Texture or Buffer to fetch from<br/> |
| <span id="sampleIndex"></span><span id="sampleindex"></span><span id="SAMPLEINDEX"></span>*sampleIndex*<br/> | \[in\] Idendifies the samples to read from *srcResource* (scalar operand).<br/>                                                       |



 

## Remarks

This instruction is a simplified alternative to the [sample](sample--sm4---asm-.md) instruction. It fetches data from the specified Texture without any filtering (e.g. point sampling) using the provided integer *srcAddress* and *sampleIndex*.

*srcAddress* provides the set of texture coordinates needed to perform the sample in the form of unsigned integers. If *srcAddress* is out of the range\[0...(\#texels in dimension -1)\], **ld2dms** always returns 0 in all components present in the format of the resource, and defaults (0,0,0,1.0f/0x00000001) for missing components.

*sampleIndex* does not have to be a literal. The multi-sample count does not have to be specified on the texture resource, and it works with depth or stencil views.

An application wishing any more flexible control over out-of-range address behavior should use the **sample** instruction instead, as it honors address wrap/mirror/clamp/border behavior defined as sampler state.

*srcAddress.b* (post-swizzle) is ignored for Texture2Ds. If the value is out of the range of available array indices \[0...(array size-1)\], then **ld2dms** always returns 0 in all components present in the format of the resource, and defaults (0,0,0,1.0f/0x00000001) for missing components.

For Texture2D Arrays, *srcAddress.b* (post-swizzle) provides the array index. Oherwise it has the same behavior as Texture2D.

*srcAddress.a* (post-swizzle) is always ignored. The HLSL compiler will never output anything there.

*srcResource* is a texture register (t\#) which must have been declared(22.3.11), identifying which Texture to fetch from.

Fetching from t\# that has nothing bound to it returns 0 for all components.

### Address Offset

The optional \[\_aoffimmi(u,v,w)\] suffix (address offset by immediate integer) indicates that the texture coordinates for the **ld2dms** are to be offset by a set of provided immediate texel space integer constant values. The literal values are a set of 4 bit 2's complement numbers, having integer range \[-8,7\].

The offsets are added to the texture coordinates, in texel space.

Address offsets are not applied along the array axis of Texture1D/2D Arrays.

The *\_aoffimmi v,w* components are ignored for Texture1Ds.

The *\_aoffimmi w* component is ignored for Texture2Ds.

Because the texture coordinates for **ld2dms** are unsigned integers, if the offset causes the address to go below zero, it will wrap to a large address, and result in an out of bounds access, which like **ld** returns 0 in all components present in the format of the resource, and the defaults (0,0,0,1.0f/0x00000001) for missing components.

### Sample Number

**ld2dms** is available for use on any resource. **ld2dms** operates identically to **ld** except on 2D multsample resources, by using the additional (0-based) *sampleIndex* operand to identify which sample to read from the resource.

The result of specifying a *sampleIndex* that exceeds the number of samples in the resource is undefined, but cannot return data outside of the address space of the device context.

### Return Type Control

The data format returned by **ld2dms** to the destination register is determined in the same way as described for the **sample** instruction. It is based on the format bound to the *srcResource* parameter (t\#).

As with the **sample** instruction, returned values for **ld2dms** are 4-vectors with format-specific defaults for components not present in the format. The swizzle on *srcResource* determines how to swizzle the 4-component result coming back from the texture load, after which .mask on *dest* determines which components in *dest* get updated.

When a 32-bit float value is read by **ld2dms** into a 32-bit register, the bits are untouched; that is, denormal values remain denormal. This is unlike the **sample** instruction.

### Miscellaneous Details

As there is no filtering associated with this instruction, concepts like LOD bias do not apply. Accordingly there is no *sampler s\#* parameter.

### Restrictions

-   *srcResource* must be a t\# register, and not a TextureCube, Texture1D or Texture1DArray. *srcResource* cannot be a ConstantBuffer, which cannot be bound to t\# registers.
-   Relative addressing on *srcResource* is not permitted.
-   *srcAddress* and *sampleIndex* must be a temp (r\#/x\#), constant (cb\#) or input (v\#) register.
-   *dest* must be a temp (r\#/x\#) or output (o\*\#) register.

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

 

 





