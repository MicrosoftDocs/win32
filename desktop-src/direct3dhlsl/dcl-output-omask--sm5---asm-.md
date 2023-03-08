---
title: dcl_output oMask (sm5 - asm)
description: Declare an output register to be written by the shader.
ms.assetid: 23FC5FA3-F550-4CD1-9AA9-86738818686F
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_output oMask (sm5 - asm)

Declare an output register to be written by the shader.



| dcl\_output o\#\[.mask\] |
|--------------------------|



 



| Item                                                   | Description                            |
|--------------------------------------------------------|----------------------------------------|
| <span id="o#"></span><span id="O#"></span>*o#*<br/> | \[in\] The output register.<br/><ul><li><em>#</em> is an name that identifies the register.</li><li><em>[.mask]</em> is an optional component mask (.xyzw) that specifies which of the register components to use.</li></ul> |



 

## Remarks


```
Example:
                dcl_output oMask[3].xyz
```



### Restrictions

-   The component mask can be any subset of \[xyzw\]. However, leaving gaps between components wastes space.
-   It is legal to declare a superset of the component mask declared for input by the next stage. However mutually exclusive masks are not allowed. The vertex shader outputting o3.xy, means the pixel shader inputting v3.z is invalid, but inputting v3.x or v3.y or v3.xy is valid.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     |         |



 

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

 

 





