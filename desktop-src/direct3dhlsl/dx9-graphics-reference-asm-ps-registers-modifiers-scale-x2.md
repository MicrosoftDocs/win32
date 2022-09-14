---
title: Source Register Scale x 2
description: Multiply the value by two before using it in the instruction.
ms.assetid: a02c9572-e03d-410b-8b65-7ea1a0bfaa0f
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source Register Scale x 2

Multiply the value by two before using it in the instruction.

## Syntax


```
register_x2
```



## Register

Source register. For more about register types, see [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## Remarks

The contents of the register are not changed. The modifier is applied only to the data read from the register.

This modifier is mutually exclusive with [Source Register Invert](dx9-graphics-reference-asm-ps-registers-modifiers-invert.md), so it cannot be applied to the same register.

This modifier is only available to arithmetic instructions in version 1\_4.

## Example

This example samples a texture, converts data to the range of -1 to +1, and calculates a dot product.


```
mul r0, r0, r1_x2;
```



## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> </dl>

 

 




