---
title: store_uav_typed (sm5 - asm)
description: Random-access write of an element into a typed unordered access view (UAV).
ms.assetid: AD8E035B-DACD-4241-A05B-7D6DC8E3222C
ms.topic: reference
ms.date: 05/31/2018
---

# store\_uav\_typed (sm5 - asm)

Random-access write of an element into a typed unordered access view (UAV).



| store\_uav\_typed dstUAV.xyzw, dstAddress\[.swizzle\], src0\[.swizzle\] |
|-------------------------------------------------------------------------|



 



| Item                                                                                                           | Description                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="dstUAV"></span><span id="dstuav"></span><span id="DSTUAV"></span>*dstUAV*<br/>                 | \[in\] Contains the result of the operation.<br/> |
| <span id="dstAddress"></span><span id="dstaddress"></span><span id="DSTADDRESS"></span>*dstAddress*<br/> | \[in\] The address at which to write.<br/>        |
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/>                                                | \[in\] The components to write.<br/>              |



 

## Remarks

This instruction performs a 4 component \*32-bit element written from *src0* to *dstUAV* at the address in *dstAddress*. *dstUAV* is a typed UAV (u\#).

The format of the UAV determines format conversion.

The number of 32-bit unsigned integer components taken from the address are determined by the dimensionality of the resource declared at *dstUAV*. This address is in elements.

Out of bounds addressing means nothing gets written to memory.

*dstUAV* always has a .xyzw write mask. All components must be written.

It is invalid and undefined to use this instruction on a UAV that is not declared as typed. That is, doing this on a structured or typeless UAV is invalid.

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



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





