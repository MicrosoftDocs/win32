---
title: dcl_tessellator_domain (sm5 - asm)
description: Declare the tessellator domain in a hull shader declaration section, and the domain shader.
ms.assetid: 11A1D9D0-D848-4750-875B-7060CE1CF42A
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_tessellator\_domain (sm5 - asm)

Declare the tessellator domain in a hull shader declaration section, and the domain shader.



| dcl\_tessellator\_domain domain |
|---------------------------------------------------------------------------|



 



| Item                                                                                                                                                                                | Description                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="domain_isoline___domain_tri___domain_quad"></span><span id="DOMAIN_ISOLINE___DOMAIN_TRI___DOMAIN_QUAD"></span>*domain*<br/> | \[in\] The domain. One of:<br/><ul><li>domain\_isoline</li><li>domain\_tri</li><li>domain\_quad</li></ul> |



 

## Remarks

Behavior is undefined if the hull shader and domain shader provide mismatching domains or any other conflicting decalarations.

This instruction applies to the following shader stages:



| Vertex | Hull                 | Domain | Geometry | Pixel | Compute |
|--------|----------------------|--------|----------|-------|---------|
|        | Declarations Section | X      |          |       |         |



 

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

 

 





