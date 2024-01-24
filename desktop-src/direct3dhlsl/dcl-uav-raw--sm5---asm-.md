---
title: dcl_uav_raw (sm5 - asm)
description: Declare an unordered access view (UAV) for use by a shader. | dcl_uav_raw (sm5 - asm)
ms.assetid: D0F43FF8-FF1C-4E42-AF42-F528C98FD680
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_uav\_raw (sm5 - asm)

Declare an unordered access view (UAV) for use by a shader.



| dcl\_uav\_raw\[\_glc\] dstUAV |
|-------------------------------|



 



| Item                                                                                           | Description                |
|------------------------------------------------------------------------------------------------|----------------------------|
| <span id="dstUAV"></span><span id="dstuav"></span><span id="DSTUAV"></span>*dstUAV*<br/> | \[in\] The UAV.<br/> |



 

## Remarks

*dstUAV* is a u\# register declared as a reference to an UnorderedAccessView of a Buffer, where the buffer appears as a simple 1D array of 32-bit untyped entries.

Operations performed on the memory may implicitly interpret the data as having a type.

The \_glc flag means "globally coherent". The absence of \_glc means the UAV is being declared only as "group coherent" in the compute shader, or "locally coherent" in a single pixel shader invocation.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | X     | X       |



 

Because UAVs are available at all shader stages for Direct3D 11.1, this instruction applies to all shader stages for the Direct3D 11.1 runtime, which is available starting with Windows 8.



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



 

> [!Note]  
> This instruction is supported in cs\_4\_0 and cs\_4\_1.

 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





