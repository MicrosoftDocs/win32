---
title: Source Register Signed Scaling
description: Subtracts 0.5 from each channel and scales the result by 2.0. The name bx2 comes from bias and scale-times-two, which is the operation it performs.
ms.assetid: ad94145a-2687-4c20-b3ed-70270a0c53bf
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source Register Signed Scaling

Subtracts 0.5 from each channel and scales the result by 2.0. The name bx2 comes from bias and scale-times-two, which is the operation it performs.

## Syntax


```
source register_bx2
```



## Register

Source Register. For more about register types, see [ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).

## Remarks

This operation is commonly used to expand data from \[0.0 to 1.0\] to \[-1.0 to 1.0\]. This modifier is designed for use with the arithmetic instructions. This modifier is commonly used on inputs to the dot product instruction ([dp3 - ps](dp3---ps.md)). Using \_bx2 on data outside the range 0 to 1 may produce undefined results.

The signed scaling operation is applied to the data read from the register before the next instruction is run. The operation is applied to all four color channels (RGBA) as follows:


```
y = 2(x - 0.5)
```



The contents of the register are not changed. The modifier is applied only to the data read from the register.

This modifier is mutually exclusive with [Source Register Invert](dx9-graphics-reference-asm-ps-registers-modifiers-invert.md) so it cannot be applied to the same register.

Version information:

-   For ps\_1\_0 and ps\_1\_1, you can use \_bx2 on any source register for texture instructions of the form texm3x2\* and texm3x3\*. \_bx2 cannot be used on any of the other texture instructions such as [texreg2ar - ps](texreg2ar---ps.md) or [texreg2gb - ps](texreg2gb---ps.md).
-   For ps\_1\_2 and ps\_1\_3, you can use \_bx2 on any source register for any tex\* instruction except: [texreg2ar - ps](texreg2ar---ps.md), [texreg2gb - ps](texreg2gb---ps.md), [texbem - ps](texbem---ps.md) or [texbeml - ps](texbeml---ps.md).

## Example

This example samples a texture, converts data to the range of -1 to +1, and calculates a dot product.


```
tex t0                        ; Read a texture color.
dp3_sat r0, t0_bx2, v0_bx2    ; Calculate a dot product.
```



## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> </dl>

 

 




