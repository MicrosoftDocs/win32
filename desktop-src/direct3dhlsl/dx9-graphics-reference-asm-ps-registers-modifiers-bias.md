---
title: Source Register Bias
description: Subtract 0.5 from all components.
ms.assetid: 6e1e96b0-e265-4b43-a9cb-8435e1fe891c
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source Register Bias

Subtract 0.5 from all components.

## Registers

Source register. For more about register types, see [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## Remarks

The contents of the register are not changed. The modifier is applied only to the data read from the register. The bias is applied to all four color channels (RGBA) as follows:


```
output = (input - 0.5)
```



The effect is to modify data that was in the range 0 to 1 to be in the range -0.5 to 0.5. Applying bias to data outside this range may produce undefined results.

> [!Note]  
> This modifier is mutually exclusive with [Source Register Invert](dx9-graphics-reference-asm-ps-registers-modifiers-invert.md), so it cannot be applied to the same register.

 

This modifier is for use with the arithmetic instructions.

## Example

This example performs the same operation as D3DTOP\_ADDSIGNED in DirectX 6.0 and 7.0 multiple texture syntax.


```
add r0, r0, t0_bias; Shift down by 0.5.
```



## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> </dl>

 

 




