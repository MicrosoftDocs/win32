---
title: dcl_uav_structured (sm5 - asm)
description: Declare an unordered access view (UAV) for use by a shader. | dcl_uav_structured (sm5 - asm)
ms.assetid: 40D6B8F7-8A41-4EFE-A8A3-44A646B4D43B
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_uav\_structured (sm5 - asm)

Declare an unordered access view (UAV) for use by a shader.



| dcl\_uav\_structured\[\_glc\] dstUAV, structByteStride |
|--------------------------------------------------------|



 



| Item                                                                                                                                   | Description                                           |
|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="dstUAV"></span><span id="dstuav"></span><span id="DSTUAV"></span>*dstUAV*<br/>                                         | \[in\] The UAV.<br/>                            |
| <span id="structByteStride"></span><span id="structbytestride"></span><span id="STRUCTBYTESTRIDE"></span>*structByteStride*<br/> | \[in\] The size of the structure in bytes.<br/> |



 

## Remarks

*dstUAV* is a u\# register declared as a reference to an UnorderedAccessView of a structured buffer with the specified stride that must be bound to UAV slot \# at the API.

The contents of the structure have no type; operations performed on the memory may implicitly interpret the data as having a type.

*structByteStride* is the size of the structure in bytes in the buffer being declared. This value must be greater than zero. *structByteStride* is of type uint, and must be a multiple of 4.

Instructions that reference a structured u\# take a 2D address, where the first component picks \[struct\], and the second component picks \[offset within struct, in aligned bytes\].

The \_glc flag means for"globally coherent". The absence of \_glc means the UAV is being declared only as "group coherent" in the compute shader, or "locally coherent" in a single pixel shader invocation.

The \_opc flag is the order preserving counter. It indicates that if a UAV is bound to slot \# (u\#), it must have been created with the COUNTER flag. This means that [imm\_atomic\_alloc](imm-atomic-alloc--sm5---asm-.md) or [imm\_atomic\_consume](imm-atomic-consume--sm5---asm-.md) operations in the shader manipulate a counter whose values can be used in the shader as a permanent reference to a location in the UAV. Data cannot be reordered after the shader is over.

The absence of the \_opc flag means that if the shader uses[imm\_atomic\_alloc](imm-atomic-alloc--sm5---asm-.md) or [imm\_atomic\_consume](imm-atomic-consume--sm5---asm-.md) instructions and a UAV is bound to slot \# (u), it must have been created with the APPEND flag, which provides a counter that does not guarantee order is preserved after the shader invocation.

If the \_opc flag is absent and the shader does not contain [imm\_atomic\_alloc](imm-atomic-alloc--sm5---asm-.md) or [imm\_atomic\_consume](imm-atomic-consume--sm5---asm-.md) instructions, a UAV bound to slot \# (u) is permitted to have been created with the COUNTER flag (the counter will go unused by this shader), no flag (no counter), but not with the APPEND flag.

> [!Note]  
> cs\_4\_0 and cs\_4\_1 supports **dcl\_tgsm\_structured**, but not [dcl\_tgsm\_raw](dcl-tgsm-raw--sm5---asm-.md).

 

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

 

 





