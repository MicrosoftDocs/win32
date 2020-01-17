---
title: Negate
description: Flips the sign of the value of a source operand used in an arithmetic operation.
ms.assetid: '83ef3f61-7b0b-4033-8f7b-5345b205c441'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Negate

Flips the sign of the value of a source operand used in an arithmetic operation.



| \-  |
|-----|



 

For single and double precision floating point and instructions, the negate modifier flips the sign of the number(s) in the source operand, including on INF values. Applying **negate** on NaN preserves NaN, although the particular NaN bit pattern that results is not defined.

For integer instructions, the **negate** modifier takes the 2's complement of the number(s) in the source operand.

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

 

 




