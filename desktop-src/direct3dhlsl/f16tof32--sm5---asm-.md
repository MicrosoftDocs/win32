---
title: f16tof32 (sm5 - asm)
description: Component-wise float16 to float32 conversion. | f16tof32 (sm5 - asm)
ms.assetid: CFAA1350-DA7F-4105-A90A-72052C5E2FB3
ms.topic: reference
ms.date: 05/31/2018
---

# f16tof32 (sm5 - asm)

Component-wise float16 to float32 conversion.



| f16tof32 dest\[.mask\], \[-\]src0\[.swizzle\] |
|----------------------------------------------|



 



| Item                                                            | Description                                          |
|-----------------------------------------------------------------|------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of the float32 result.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>    | \[in\] The float16 value to convert.<br/>      |



 

## Remarks

This operation performs a component-wise conversion of a float16 value from LSB bits to a float32 result.

This operation follows D3D rules for floating point conversion.

Use this instruction for shader-driven data decompression.

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

 

 





