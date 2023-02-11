---
title: f32tof16 (sm5 - asm)
description: Component-wise float16 to float32 conversion. | f32tof16 (sm5 - asm)
ms.assetid: 36BCCFC5-722A-45EB-8A66-7544833BBBA5
ms.topic: reference
ms.date: 05/31/2018
---

# f32tof16 (sm5 - asm)

Component-wise float16 to float32 conversion.



| f32tof16 dest\[.mask\], \[-\]src0\[.swizzle\] |
|----------------------------------------------|



 



| Item                                                            | Description                                      |
|-----------------------------------------------------------------|--------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/> | \[in\] The address of float16 result.<br/> |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>    | \[in\] The float32 value to convert.<br/>  |



 

## Remarks

This instruction performs a component-wise conversion of a float32 value to a float16 value result placed in LSB 16 bits.

This instruction follows D3D rules for floating point conversion.

Use this instruction for shader-driven data compression.

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

 

 





