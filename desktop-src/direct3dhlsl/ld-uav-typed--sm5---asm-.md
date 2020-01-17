---
title: ld_uav_typed (sm5 - asm)
description: Random-access read of an element from a typed unordered access view (UAV).
ms.assetid: E5E03311-3596-4497-9271-FE6445DBFC62
ms.topic: reference
ms.date: 05/31/2018
---

# ld\_uav\_typed (sm5 - asm)

Random-access read of an element from a typed unordered access view (UAV).



| ld\_uav\_typed dst0\[.mask\], srcAddress\[.swizzle\], srcUAV\[.swizzle\] |
|--------------------------------------------------------------------------|



 



| Item                                                                                                           | Description                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="dst0"></span><span id="DST0"></span>*dst0*<br/>                                                | \[in\] The address of the results of the operation.<br/> |
| <span id="srcAddress"></span><span id="srcaddress"></span><span id="SRCADDRESS"></span>*srcAddress*<br/> | \[in\] Specifies the address to read from.<br/>          |
| <span id="srcUAV"></span><span id="srcuav"></span><span id="SRCUAV"></span>*srcUAV*<br/>                 | \[in\] The source to read from. <br/>                    |



 

## Remarks

This instruction performs a 4-component element read from *srcUAV* at the unsigned integer address in *srcAddress*, converted to 32bit per component based on the format, then written to *dst0* in the shader.

*srcUAV* is a UAV (u\#) declared as typed. However, the type of the bound resource must be R32\_UINT/SINT/FLOAT.

The number of 32-bit unsigned integer components taken from the address are determined by the dimensionality of the resource declared at *srcUAV*. Addressing is the same as the [ld](ld--sm4---asm-.md) instruction.

Out of bounds addressing is the same as the **ld** instruction.

The behavior of this instruction is identical to the **ld** instruction if called as **ld dst0\[.mask\], srcAddress\[.swizzle\], srcUAV\[.swizzle\]**

It is invalid and undefined to use this instruction on a UAV that is not declared as typed. Doing this on a structured or typeless UAV is invalid.

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



 

cs\_4\_0 and cs\_4\_1 support this instruction for UAV, SRV and TGSM.

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





