---
title: dcl_tessellator_output_primitive (sm5 - asm)
description: Declare the tessellator output primitive type in a hull shader declaration section.
ms.assetid: 95F074C5-6012-4160-B78E-440C33C1ECC3
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_tessellator\_output\_primitive (sm5 - asm)

Declare the tessellator output primitive type in a hull shader declaration section.



| dcl\_tessellator\_output\_primitive type |
|------------------------------------------|



 



| Item | Description                                  |
|------|----------------------------------------------|
| <span id="output_point___output_line_____________________________________triangloutput_e_cw___output_triangle_ccw"></span><span id="OUTPUT_POINT___OUTPUT_LINE_____________________________________TRIANGLOUTPUT_E_CW___OUTPUT_TRIANGLE_CCW"></span>*type*<br/> | \[in\] The output primitive type. One of:<br/><ul><li>output\_point</li><li>output\_line</li><li>output\_triangle\_cw</li><li>output\_triangle\_ccw</ul><br/> |



 

## Remarks

This instruction applies to the following shader stages:



| Vertex | Hull                 | Domain | Geometry | Pixel | Compute |
|--------|----------------------|--------|----------|-------|---------|
|        | Declarations Section |        |          |       |         |



 

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

 

 





