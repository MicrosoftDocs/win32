---
title: resinfo (sm4 - asm)
description: Query the dimensions of a given input resource.
ms.assetid: 5D549AC6-E0CB-4395-953C-5E5ECEEE234D
ms.topic: reference
ms.date: 05/31/2018
---

# resinfo (sm4 - asm)

Query the dimensions of a given input resource.



| resinfo\[\_uint\|\_rcpFloat\] dest\[.mask\], srcMipLevel.select\_component, srcResource\[.swizzle\] |
|-----------------------------------------------------------------------------------------------------|



 



| Item                                                                                                               | Description                                                                               |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the result of the operation.<br/>                             |
| <span id="srcMipLevel"></span><span id="srcmiplevel"></span><span id="SRCMIPLEVEL"></span>*srcMipLevel*<br/> | \[in\] The mip level.<br/>                                                          |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] A t\# or u\# input texture for which the dimensions are being queried. <br/> |



 

## Remarks

*srcMipLevel* is read as an unsigned integer scalar so a single component selector is required for the source register, if it is not a scalar immediate value.

*dest* receives \[width, height, depth or array size, total-mip-count\], selected by the write mask.

The returned width, height and depth values are for the mip-level selected by the *srcMipLevel* parameter, and are in number of texels, independent of texel data size. For multisample resources (texture2D\[Array\]MS\#), width and height are also returned in texels, not samples.

The total mip count returned in *dest.w* is unaffected by the *srcMipLevel* parameter.

For UAVs (u\#), the number of mip levels is always 1.

All aspects of this instruction are based on the characteristics of the resource view bound at the t\#/u\#, not the underlying base resource.

Returned values are all floating point, unless the \_uint modifier is used, in which case the returned values are all integers. If the \_rcpFloat modifier is used, all returned values are floating point, and the width, height and depth are returned as reciprocals (1.0f/width, 1.0f/height, 1.0f/depth), including INF if width/height/depth are 0 from out-of-range *srcMipLevel* behavior. The \_rcpFloat modifier only applies to width, height, and depth returned values and does not apply to values that are set to 0 and thus not returned, and also does not apply to array size returns.

The swizzle on *srcResource* allows the returned values to be swizzled arbitrarily before they are written to the destination.

If *srcResource* is a Texture1D, then width is returned in *dest.x*, and *dest.yz* are set to 0.

If *srcResource* is a Texture1DArray, then width is returned in *dest.x*, the array size is returned in *dest.y*, and *dest.z* is set to 0.

If *srcResource* is a Texture2D, then width and height are returned in *dest.xy*, and *dest.z* is set to 0.

If *srcResource* is a Texture2DArray, then width and height are returned in *dest.xy*, and the array size is returned in *dest.z*.

If *srcResource* is a Texture3D, then width, height and depth are returned in *dest.xyz*.

If *srcResource* is a TextureCube, then the width and height of the individual cube face dimensions are returned in *dest.xy*, and *dest.z* is set to 0.

If *srcResource* is a TextureCubeArray, then the width and height the individual cube face dimensions are returned in *dest.xy*. *dest.z* is set to an undefined value.

If the a per-resource mip clamp has been specified on *srcResource*, resinfo always returns the total number of mipmaps in the view for the mip count, regardless of the clamp. However, if the dimensions of a given miplevel are requested by resinfo and the miplevel has been clamped off (e.g. a clamp of 2.2 means that mips 0 and 1 have been clamped off), the dimensions returned are undefined. Some implementations will return the out of bounds behavior specified for resinfo when the miplevel is out of range. Other implementations will return the dimensions of the mip as if it had not been clamped.

### Restrictions

-   *srcResource* must be a t\# or u\# register that is not a Buffer, but is a Texture\*.
-   Relative addressing of *srcResource* is not permitted.
-   *srcMipLevel* must use a single component selector if it is not a scalar immediate.
-   Fetching from t\# or u\# that has nothing bound to it returns 0 for width, height, depth or arraysize, and total-mip-count. The \_rcpFloat modifier is still honored in this case, thus returning INF for the applicable returned values.
-   If *srcMipLevel* is out of the range of the available number of miplevels in the resource, the behavior for the size return (*dest.xyz*) is identical to that of an unbound t\# or u\# resource. The total mip count is still returned in *dest.w* for this case.

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

 

 





