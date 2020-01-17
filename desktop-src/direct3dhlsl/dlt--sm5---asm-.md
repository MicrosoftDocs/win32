---
title: dlt (sm5 - asm)
description: Component-wise double-precision less-than comparison.
ms.assetid: A9DE5007-4ADD-403D-A2B7-EAE475E9DCCB
ms.topic: reference
ms.date: 05/31/2018
---

# dlt (sm5 - asm)

Component-wise double-precision less-than comparison.



| dlt\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\], \[-\]src1\[\_abs\]\[.swizzle\] |
|--------------------------------------------------------------------------------------------|



 



| Item                                                            | Description                                                    |
|-----------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the results of the operation.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to compare to *src1*.<br/>         |
| <span id="src1"></span><span id="SRC1"></span>*src1*<br/> | \[in\] The components to compare to *src0*.<br/>         |



 

## Remarks

This instruction performs the double-precision floating-point comparison (*src0* < *src1*) for each component and writes the result to *dest*.

If the comparison is true, then 32-bit 0xFFFFFFFF is returned for that component. Otherwise 32-bit 0x00000000 is returned.

Comparison with NaN returns false.

The valid *dest* masks are any one or two components. That is: .x, .y, .z, .w, .xy, .xz, .xw, .yz, .yw, .zw The first *dest* component in the mask receives the 32-bit result for the first double comparison. The second component in the mask (if present) receives the 32-bit result for the second double comparison.

The valid swizzles for the source parameters are .xyzw, .xyxy, .zwxy, .zwzw. The following *src* mappings are post-swizzle:

-   *src0* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).
-   *src1* is a double vec2 across (x 32LSB, y 32MSB) and (z 32LSB, w 32MSB).

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

 

 





