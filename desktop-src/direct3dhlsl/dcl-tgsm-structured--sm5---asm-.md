---
title: dcl_tgsm_structured (sm5 - asm)
description: Declare a reference to a region of shared memory space available to the compute shader s thread group. The memory is viewed as an array of structures.
ms.assetid: C42CD506-58EB-4740-8403-3F9BF29F0CAE
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_tgsm\_structured (sm5 - asm)

Declare a reference to a region of shared memory space available to the compute shader s thread group. The memory is viewed as an array of structures.



| dcl\_tgsm\_structured g\#, structByteStride, structCount |
|----------------------------------------------------------|



 



| Item                                                                                                                                   | Description                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <span id="g_"></span><span id="G_"></span>*g\#*<br/>                                                                             | \[in\] A reference to a block of shared memory of size *structByteStride* \* *structCount* bytes. <br/> |
| <span id="structByteStride"></span><span id="structbytestride"></span><span id="STRUCTBYTESTRIDE"></span>*structByteStride*<br/> | \[in\] The structure stride. This value is a uint in bytes and must be a multiple of 4. <br/>           |
| <span id="structCount"></span><span id="structcount"></span><span id="STRUCTCOUNT"></span>*structCount*<br/>                     | \[in\] The number of structures.<br/>                                                                   |



 

## Remarks

The total storage for all g\# must be <= the amount of shared memory available per thread group, which is 32kB, or 8192 32-bit scalars.

In an extreme case, you can declare 8192 total g\# s, if each has a *structByteStride* of 4 and a *structCount* of 1.

In the opposite extreme, you can declare a single g\# with a structure stride of 32kB and a structure count of 1.

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

 

 





