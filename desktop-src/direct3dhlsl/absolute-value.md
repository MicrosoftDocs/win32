---
title: Absolute Value
description: Take the absolute value of a source operand used in an arithmetic operation.
ms.assetid: FD2ACE91-0AF6-43E8-80C5-849488E39BEF
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Absolute Value

Take the absolute value of a source operand used in an arithmetic operation.



| \_abs |
|-------|



 

This modifier is used for single and double precision floating point and instructions only. The **\_abs** modifier forces the sign of the number(s) on the source operand positive, including on INF values.

Applying **\_abs** on NaN preserves NaN, although the particular NaN bit pattern that results is not defined.

When \_abs is combined with the [negate](negate.md) modifier, the combination forces the sign to be negative, as if the **\_abs** modifier is applied first, then the **negate**.

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

 

 




