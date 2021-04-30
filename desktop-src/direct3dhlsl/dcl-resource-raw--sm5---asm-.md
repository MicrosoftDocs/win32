---
title: dcl_resource raw (sm5 - asm)
description: Declare a shader resource input and assign it to a t\ - a placeholder register for the resource. | dcl_resource raw (sm5 - asm)
ms.assetid: ECBA9DAB-F217-47FB-9588-F35866004E72
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_resource raw (sm5 - asm)

Declare a shader resource input and assign it to a t\# - a placeholder register for the resource.



| dcl\_resource\_raw dstSRV |
|---------------------------|



 



| Item                                                                                           | Description                                                                                       |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="dstSRV"></span><span id="dstsrv"></span><span id="DSTSRV"></span>*dstSRV*<br/> | \[in\] A t\# register declared as a reference to a ShaderResourceView of a raw buffer.<br/> |



 

## Remarks

The contents of the structure have no type; operations performed on the memory may implicitly interpret the data as having a type.

Instructions that reference a raw t\# take a 1D address, an unsigned 32-bit value specifying the byte offset to a 32-bit aligned location in the Buffer. The address must be a multiple of 4 (bytes).

Views bound to t\# declared as raw must have RAW specified on their creation; otherwise behavior when accessed from a shader is undefined.

cs\_4\_0 and cs\_4\_1 support this instruction.

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

 

 





