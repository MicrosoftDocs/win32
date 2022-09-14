---
title: Source Register Negate
description: Performs a negate (y -x), on all register components.
ms.assetid: fe11f7a7-81be-4237-8194-15704f6fe43c
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source Register Negate

Performs a negate (y = -x), on all register components.

## Syntax


```
- register
```



## Registers

Source Register. For more about register types, see [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## Remarks

The contents of the register are not changed. The modifier is applied only to the data read from the register. The negate operation is applied to all four color channels (RGBA).

This operation is performed after any other modifiers present on the same argument.

This modifier is mutually exclusive with [Source Register Invert](dx9-graphics-reference-asm-ps-registers-modifiers-invert.md) so it cannot be applied to the same register.

This modifier is for use only with arithmetic instructions.

## Example

The following example shows how to use this modifier.


```
mul r0, r0, -v1;
```



## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> </dl>

 

 




