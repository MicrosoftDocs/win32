---
title: dcl_resource_structured (sm5 - asm)
description: Declare a shader resource input and assign it to a t\ - a placeholder register for the resource. | dcl_resource_structured (sm5 - asm)
ms.assetid: 87FC8A56-9DB2-424B-889C-2AB59885DA13
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_resource structured (sm5 - asm)

Declare a shader resource input and assign it to a t\# - a placeholder register for the resource.



| dcl\_resource\_structured dstSRV, structByteStride |
|----------------------------------------------------|



 



| Item                                                                                                                                   | Description                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="dstSRV"></span><span id="dstsrv"></span><span id="DSTSRV"></span>*dstSRV*<br/>                                         | \[in\] A t\# register declared as a reference to a ShaderResourceView of a structured buffer with the specified stride that must be bound to SRV slot \# at the API. <br/> |
| <span id="structByteStride"></span><span id="structbytestride"></span><span id="STRUCTBYTESTRIDE"></span>*structByteStride*<br/> | \[in\] A uint that specifies the size of the structure in bytes in the buffer being declared. This value must be greater than zero.<br/>                                   |



 

## Remarks

The contents of the structure have no type; operations performed on the memory may implicitly interpret the data as having a type.

Instructions that reference a structured t\# take a 2D address, where the first component picks \[struct\], and the second component picks \[offset within struct, multiple of 32-bits\].

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

 

 





