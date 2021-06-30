---
title: Modifiers for ps_1_X
description: Instruction modifiers affect the result of the instruction before it is written into the destination register. Learn about modifiers for ps_1_X.
ms.assetid: 15b892da-b6fd-4bd5-8889-bc48035e7819
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Modifiers for ps\_1\_X

Instruction modifiers affect the result of the instruction before it is written into the destination register. For instance, use them to multiply or divide the result by a factor of two, or to clamp the result between zero and one. Instruction modifiers are applied after the instruction runs but before writing the result to the destination register.

A list of the modifiers is shown below.



| Modifier | Description                   | Syntax           | Version 1\_1 | Version 1\_2     |Version  1\_3    | Version 1\_4    |
|----------|-------------------------------|------------------|---------|------|------|------|
| \_x2     | Multiply by 2                 | instruction\_x2  | X       | X    | X    | X    |
| \_x4     | Multiply by 4                 | instruction\_x4  | X       | X    | X    | X    |
| \_x8     | Multiply by 8                 | instruction\_x8  |         |      |      | X    |
| \_d2     | Divide by 2                   | instruction\_d2  | X       | X    | X    | X    |
| \_d4     | Divide by 4                   | instruction\_d4  |         |      |      | X    |
| \_d8     | Divide by 8                   | instruction\_d8  |         |      |      | X    |
| \_sat    | Saturate (clamp from 0 and 1) | instruction\_sat | X       | X    | X    | X    |



 

-   The multiply modifier multiplies the register data by a power of two after it is read. This is the same as a shift left.
-   The divide modifier divides the register data by a power of two after it is read. This is the same as a shift right.
-   The saturate modifier clamps the range of register values from zero to one.

Instruction modifiers can be used on arithmetic instructions. They may not be used on texture address instructions.

Multiply modifier

This example loads the destination register (dest) with the sum of the two colors in the source operands (src0 and src1) and multiplies the result by two.


```
add_x2 dest, src0, src1
```



This example combines two instruction modifiers. First, two colors in the source operands (src0 and src1) are added. The result is then multiplied by two, and clamped between 0.0 to 1.0 for each component. The result is saved in the destination register.


```
add_x2_sat dest, src0, src1
```



Divide modifier

This example loads the destination register (dest) with the sum of the two colors in the source operands (src0 and src1) and divides the result by two.


```
add_d2 dest, src0, src1
```



Saturate modifier

For arithmetic instructions, the saturation modifier clamps the result of this instruction into the range 0.0 to 1.0 for each component. The following example shows how to use this instruction modifier.


```
dp3_sat r0, t0_bx2, v0_bx2    ; t0 is bump, v0 is light direction
```



This operation occurs after any multiply or divide instruction modifier. \_sat is most often used to clamp dot product results. However, it also enables consistent emulation of multipass methods where the frame buffer is always in the range 0 to 1, and of DirectX 6 and 7.0 multitexture syntax, in which saturation is defined to occur at every stage.

This example loads the destination register (dest) with the sum of the two colors in the source operands (src0 and src1), and clamps the result into the range 0.0 to 1.0 for each component.


```
add_sat dest, src0, src1
```



This example combines two instruction modifiers. First, two colors in the source operands (src0 and src1) are added. The result is multiplied by two and clamped between 0.0 to 1.0 for each component. The result is saved in the destination register.


```
add_x2_sat dest, src0, src1
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




