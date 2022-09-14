---
title: dmov (sm5 - asm)
description: Component-wise move. | dmov (sm5 - asm)
ms.assetid: 05DBB9E2-10EC-4324-BB8F-1A9E315DE90C
ms.topic: reference
ms.date: 05/31/2018
---

# dmov (sm5 - asm)

Component-wise move.



| dmov\[\_sat\] dest\[.mask\], \[-\]src0\[\_abs\]\[.swizzle\] |
|-------------------------------------------------------------|



 



| Item                                                            | Description                                              |
|-----------------------------------------------------------------|----------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The move destination. *dest* = *src0*.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The components to be moved.<br/>            |



 

## Remarks

The modifiers, other than swizzle, assume the data is floating point. The absence of modifiers moves data without altering bits.

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

 

 





