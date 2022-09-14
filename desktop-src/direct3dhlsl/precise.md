---
title: Precise
description: Per-instruction disabling of arithmetic refactoring.
ms.assetid: A26E569A-32EA-4AED-83C2-4F937AD3829E
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Precise

Per-instruction disabling of arithmetic refactoring.



| precise (component mask) |
|--------------------------|



 

This modifier requires the global shader flag "REFACTORING\_ALLOWED". When REFACTORING\_ALLOWED is present, individual component results of individual instructions can be forced to remain precise or not-refactorable by compilers or drivers. If components of a [**mad**](mad--sm4---asm-.md) instruction are tagged as **precise**, the hardware must execute a **mad** instruction or the exact equivalent, and it cannot split it into a multiply followed by an add. Conversely, a multiply followed by an add, where either or both are flagged as **precise**, cannot be merged into a fused **mad**.

If REFACTORING\_ALLOWED has not been specified, the **precise** modifier is not allowed. It is not needed because everything is precise. The **precise** modifier affects any operation, not just arithmetic.

## Minimum Shader Model

This modifier is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Instruction Modifiers](shader-model-5-instruction-modifiers.md)
</dt> </dl>

 

 




