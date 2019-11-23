---
title: Saturate (HLSL reference)
description: Clamps the result of a single or double precision floating point arithmetic operation to \ 0.0f...1.0f\ range.
ms.assetid: 'ce3e79c7-c3e6-4a2c-910a-2cd568aece50'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Saturate (HLSL reference)

Clamps the result of a single or double precision floating point arithmetic operation to \[0.0f...1.0f\] range.



| \_sat |
|-------|



 

The **saturate** instruction result modifier performs the following operation on the result values(s) from a floating point arithmetic operation that has \_sat applied to it:

`min(1.0f, max(0.0f, value))`

where min() and max() in the above expression behave in the way [min](min--sm4---asm-.md), [max](max--sm4---asm-.md), [dmin](dmin--sm5---asm-.md), or [dmax](dmax--sm5---asm-.md) operate.

`_sat(NaN)` returns 0, by the rules for min and max.

## Minimum Shader Model

This modifier is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Instruction Modifiers](instruction-modifiers.md)
</dt> </dl>

 

 




