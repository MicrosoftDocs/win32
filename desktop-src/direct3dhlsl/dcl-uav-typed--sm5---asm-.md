---
title: dcl_uav_typed (sm5 - asm)
description: Declare an unordered access view (UAV) for use by a shader. | dcl_uav_typed (sm5 - asm)
ms.assetid: F9F5583F-E3D0-447F-9227-BBB1B4E71934
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_uav\_typed (sm5 - asm)

Declare an unordered access view (UAV) for use by a shader.



| dcl\_uav\_typed\[\_glc\] dstUAV, dimension, type |
|--------------------------------------------------|



 



| Item                                                                                           | Description                                                                                       |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="dstUAV"></span><span id="dstuav"></span><span id="DSTUAV"></span>*dstUAV*<br/> | \[in\] The UAV.<br/>                                                                        |
| <span id="dimension"></span><span id="DIMENSION"></span>*dimension*<br/>                 | \[in\] Specifies how many dimensions the instructions accessing the UAV are providing.<br/> |
| <span id="type"></span><span id="TYPE"></span>*type*<br/>                                | \[in\] The type of the UAV.<br/>                                                            |



 

## Remarks

*dstUAV* is a u\# register being declared as a reference to an UnorderedAccessView that must be bound to UAV slot \# at the API.

The dimension must be buffer, Texture1D, Texture1DArray, Texture2D, Texture2DArray, or Texture3D. This indicates how many dimensions any instructions accessing the UAV are providing: 1 (Texture1D, Buffer), 2 (Texture1DArray, Texture2D) or 3 (Texture2DArray, Texture3D).

Type is {UNORM,SNORM,UINT,SINT,FLOAT}. Operations done with the declared u\# must be compatible with the type declared here, and the UAV bound to slot \# must also have the same type.

The \_glc flag stands for "globally coherent". The absence of \_glc means the UAV is being declared only as "group coherent" in the compute shader, or "locally coherent" in a single pixel shader invocation.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | X     | X       |



 

Because UAVs are available at all shader stages for Direct3D 11.1, this instruction applies to all shader stages for the Direct3D 11.1 runtime, which is available starting with Windows 8.



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

> [!Note]  
> This instruction is not supported in compute shader 4.x.

 

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

 

 





