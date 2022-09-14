---
title: ld (sm4 - asm)
description: Fetches data from the specified buffer or texture without any filtering (e.g. point sampling) using the provided integer address. The source data may come from any resource type, other than TextureCube.
ms.assetid: DEE9A55F-EDFE-478E-8169-5BF9C43E98AF
ms.topic: reference
ms.date: 05/31/2018
---

# ld (sm4 - asm)

Fetches data from the specified buffer or texture without any filtering (e.g. point sampling) using the provided integer address. The source data may come from any resource type, other than TextureCube.



| ld\[\_aoffimmi(u,v,w)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\] |
|----------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the result of the operation.<br/>                                                               |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>     | \[in\] The texture coordinates needed to perform the sample.<br/>                                                     |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A texture register (t\#) which must have been declared identifying which Texture or Buffer to fetch from.<br/> |



 

## Remarks

This instruction is a simplified alternative to the [sample](sample--sm4---asm-.md) instruction. Unlike **sample**, **ld** is also capable of fetching data from buffers. **ld** is can also fetch from multi-sample resources (on pixel shader only).

*srcAddress* provides the set of texture coordinates needed to perform the sample in the form of unsigned integers. If *srcAddress* is out of the range\[0...(\#texels in dimension -1)\], then out-of-bounds behavior is invoked, where **ld** returns 0 in all non-missing components of the format of the *srcResource*, and the default for missing components. An application wishing any more flexible control over out-of-range address behavior should use the **sample** instruction instead, as it honors address wrap/mirror/clamp/border behavior defined as sampler state.

*srcAddress.a* (POS-swizzle) always provides an unsigned integer mipmap level. If the value is out of the range \[0...(num miplevels in resource-1)\]), then out-of-bounds behavior is invoked. If the resource is a buffer, which can not have any mipmaps, then *srcAddress.a* is ignored

*srcAddress.gb* (POS-swizzle) is ignored for buffers and texture1D (non-Array). *srcAddress.b* (POS-swizzle) is ignored for texture1D arrays and texture2Ds.

For texture1D arrays, *srcAddress.g* (POS-swizzle) provides the array index as an unsigned integer. If the value is out of the range of available array indices \[0...(array size-1)\], then out-of-bounds behavior is invoked.

For texture2D arrays, *srcAddress.b* (POS-swizzle) provides the array index, otherwise with same semantics as for texture1D.

Fetching from *t\#* that has nothing bound to it returns 0 for all components.

### Address Offset

The optional \[\_aoffimmi(u,v,w)\] suffix (address offset by immediate integer) indicates that the texture coordinates for the **ld** are to be offset by a set of provided immediate texel space integer constant values. The literal values are a set of 4 bit 2's complement numbers, having integer range \[-8,7\]. This modifier is defined only for texture1D/2D/3D, including arrays, and not for buffers.

The offsets are added to the texture coordinates, in texel space, relative to the miplevel being accessed by the **ld**.

Address offsets are not applied along the array axis of texture1D/2D arrays.

The *\_aoffimmi v,w* components are ignored for texture1Ds.

The *\_aoffimmi w* component is ignored for texture2Ds.

Because the texture coordinates for **ld** are unsigned integers, if the offset causes the address to go below zero, it will wrap to a large address, and result in an out of bounds access.

### Return Type Control

The data format returned by **ld** to the destination register is determined in the same way as described for the **sample** instruction; it is based on the format bound to the *srcResource* parameter (*t\#*).

As with the **sample** instruction, returned values for **ld** are 4-vectors with format-specific defaults for components not present in the format. The swizzle on *srcResource* determines how to swizzle the 4-component result coming back from the texture load, after which .mask on *dest* determines which components in *dest* get updated.

When a 32-bit float value is read by *ld* into a 32-bit register, the bits are untouched; that is, denormal values remain denormal. This is unlike the **sample** instruction.

### Miscellaneous Details

As there is no filtering associated with the **ld** instruction, concepts like LOD bias do not apply to **ld**. Accordingly there is no sampler *s\#* parameter.

### Restrictions

-   *srcResource* must be a t\# register, and not a TextureCube. *srcResource* cannot be a constantbuffer either, which cannot be bound to t\# registers.
-   Relative addressing on *srcResource* is not permitted.
-   *srcAddress* must be a temp (r\#/x\#), constant (cb\#) or input (v\#) register.
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
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





