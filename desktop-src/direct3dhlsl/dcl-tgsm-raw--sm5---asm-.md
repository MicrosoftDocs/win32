---
title: dcl_tgsm_raw (sm5 - asm)
description: Declare a reference to a region of shared memory space available to the compute shader s thread group.
ms.assetid: 8EA6931C-5B13-431F-A886-04F8C73CD22D
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_tgsm\_raw (sm5 - asm)

Declare a reference to a region of shared memory space available to the compute shader s thread group.



| dcl\_tgsm\_raw g\#, byteCount |
|-------------------------------|



 



| Item                                                                                                       | Description                                                                             |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span id="g_"></span><span id="G_"></span>*g\#*<br/>                                                 | \[in\] A reference to a block of size *byteCount* of untyped shared memory. <br/> |
| <span id="byteCount"></span><span id="bytecount"></span><span id="BYTECOUNT"></span>*byteCount*<br/> | \[in\] Must be a multiple of 4. <br/>                                             |



 

## Remarks

The total storage for all g\# must be <= the amount of shared memory available per thread group, which is 32kB.

In an extreme case, you can declare 8192 total g\# s, each with a *byteCount* of 4.

In the opposite extreme, you can declare a single g\# with a *byteCount* of 32768.

> [!Note]  
> cs\_4\_0 and cs\_4\_1 supports [dcl\_tgsm\_structured](dcl-tgsm-structured--sm5---asm-.md), but not **dcl\_tgsm\_raw**.

 

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          |       | X       |



 

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

 

 





