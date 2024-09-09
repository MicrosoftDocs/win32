---
title: dcl_stream (sm5 - asm)
description: Declare a geometry shader output stream.
ms.assetid: 0A8B8AB5-B7B0-46BB-91E8-B2E8E3D64B74
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_stream (sm5 - asm)

Declare a geometry shader output stream.



| dcl\_stream mN |
|-----------------|



 



| Item                                                       | Description                             |
|------------------------------------------------------------|-----------------------------------------|
| <span id="m_"></span><span id="M_"></span>*mN*<br/> | \[in\] Stream where *N* is 0..3 (m0..m3).<br/> |



 

## Remarks

A given stream can only be declared once.

If no streams are declared, output and output topology declarations are assumed to be for stream 0.

The first **dcl\_stream** cannot appear after any **dcl\_output** or **dcl\_outputTopology** statements.

Any **dcl\_output** or **dcl\_outputToplogy** statements after any **dcl\_stream** m\# statement define the outputs for stream m\#.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        | X        |       |         |



 

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

 

 





