---
title: dcl_function_table (sm5 - asm)
description: Declare a function table.
ms.assetid: 3693A03F-5E4B-40E8-B436-2FE3462C8DB8
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_function\_table (sm5 - asm)

Declare a function table.



| dcl\_function\_table ft\# = {fb\#, fb\#, ...} |
|-----------------------------------------------|



 



| Item                                                      | Description                                   |
|-----------------------------------------------------------|-----------------------------------------------|
| <span id="ft"></span><span id="FT"></span>*ft*<br/> | \[in\] The function table entries.<br/> |



 

## Remarks

This function declares a function table as a set of function bodies that have been declared earlier.

This is like a C++ vtable except there is an entry per call site for an interface instead of per method.

There is no limit to how many function bodies can be listed in a function table.

It is valid for a given function body fb\# to be referenced multiple times in one or more function tables, as a way of sharing common code.

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

 

 





