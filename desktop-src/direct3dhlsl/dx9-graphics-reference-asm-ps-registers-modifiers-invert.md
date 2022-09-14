---
title: Source Register Invert
description: Performs a (1 - value) calculation for each channel of the specified register.
ms.assetid: 387e409f-d76d-4d70-be0f-fb563f542482
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source Register Invert

Performs a (1 - value) calculation for each channel of the specified register.

## Syntax


```
1 - register
```



## Registers

Source Register. For more about register types, see [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## Remarks

The contents of the register are not changed. The modifier is applied only to the data read from the register. The invert operation is applied to all four color channels (RGBA).

This modifier can be used only with arithmetic instructions. In addition, this modifier cannot be combined with the other [Destination Register Write Mask](dx9-graphics-reference-asm-ps-registers-modifiers-write-mask.md).

## Example

This example uses inversion to generate the complement of register r1.


```
mul r0, r0, 1-r1;
```



## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> </dl>

 

 




