---
title: sample_d (sm4 - asm)
description: Samples data from the specified Element/texture using the specified address and the filtering mode identified by the given sampler. | sample_d (sm4 - asm)
ms.assetid: 9CF57C4A-C0D1-4D57-A5EE-62BBBB291438
ms.topic: reference
ms.date: 05/31/2018
---

# sample\_d (sm4 - asm)

Samples data from the specified Element/texture using the specified address and the filtering mode identified by the given sampler.



| sample\_d\[\_aoffimmi(u,v,w)\] dest\[.mask\], srcAddress\[.swizzle\], srcResource\[.swizzle\], srcSampler, srcXDerivatives\[.swizzle\], srcYDerivatives\[.swizzle\] |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|



 



| Item                                                                                                                               | Description                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                                    | \[in\] The address of the results of the operation.<br/>                                                                  |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/>                     | \[in\] A set of texture coordinates. For more information see the [sample](sample--sm4---asm-.md) instruction.<br/>      |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/>                 | \[in\] A texture register. For more information see the **sample** instruction.<br/>                                      |
| <span id="srcSampler"></span><span id="srcsampler"></span><span id="SRCSAMPLER"></span>*srcSampler*<br/>                     | \[in\] A sampler register. For more information see the **sample** instruction.<br/>                                      |
| <span id="srcXDerivatives"></span><span id="srcxderivatives"></span><span id="SRCXDERIVATIVES"></span>*srcXDerivatives*<br/> | \[in\] The derivatives for the source address in the x direction. For more information, see the **Remarks** section.<br/> |
| <span id="srcYDerivatives"></span><span id="srcyderivatives"></span><span id="SRCYDERIVATIVES"></span>*srcYDerivatives*<br/> | \[in\] The derivatives for the source address in the y direction. For more information, see the **Remarks** section.<br/> |



 

## Remarks

This instruction behaves like the [sample](sample--sm4---asm-.md) instruction, except that derivatives for the source address in the x direction and the y direction are provided by extra parameters, *srcXDerivatives* and *srcYDerivatives*, respectively. These derivatives are in normalized texture coordinate space.

The r, g and b components of *srcXDerivatives* (POS-swizzle) provide du/dx, dv/dx and dw/dx. The 'a' component (POS-swizzle) is ignored.

The r, g and b components of *srcYDerivatives* (POS-swizzle) provide du/dy, dv/dy and dw/dy. The 'a' component (POS-swizzle) is ignored.

Unlike the **sample** instruction, which is permitted to share a single LOD calculation across a 2x2 stamp, **sample\_d** must calculate LOD completely independently, per-pixel when used in the Pixel Shader.

If the derivative inputs to **sample\_d** came from derivative calculation instructions in the Pixel Shader and the values include INF/NaN, the behavior of **sample\_d** may not match the **sample** instruction, which implicitly computes the derivative. The INF/NaN values may affect the LOD calculation differently.

Fetching from an input slot that has nothing bound to it returns 0 for all components.

### Restrictions

-   **sample\_d** inherits the same restrictions as the **sample** instruction, plus additional an restriction below for its additional parameters.
-   *srcXDerivatives* and *srcYDerivatives* must be temp (r\#/x\#), constantBuffer (cb\#), input (v\#) registers or immediate value(s).

This instruction applies to the following shader stages:



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

 

 





