---
title: Pixel Shader Source Register Modifiers
description: Use source register modifiers to change the value read from a register before an instruction runs.
ms.assetid: b45d0919-7878-4184-ad4a-5623aae9d1f1
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Pixel Shader Source Register Modifiers

Use source register modifiers to change the value read from a register before an instruction runs. The contents of a source register are left unchanged. Modifiers are useful for adjusting the range of register data in preparation for the instruction. A set of modifiers called selectors copies or replicates the data from a single channel (r,g,b,a) into the other channels.

## ps\_1\_1 - ps\_1\_4

This table identifies the versions that support each modifier:



| Source register modifiers                                                                                    | Syntax         | Version 1\_1 | Version 1\_2     | Version 1\_3     | Version 1\_4     |
|--------------------------------------------------------------------------------------------------------------|----------------|---------|------|------|------|
| [bias](dx9-graphics-reference-asm-ps-registers-modifiers-bias.md)                                           | register\_bias | X       | X    | X    | X    |
| [invert](dx9-graphics-reference-asm-ps-registers-modifiers-invert.md)                                       | 1 - register   | X       | X    | X    | X    |
| [negate](dx9-graphics-reference-asm-ps-registers-modifiers-negate.md)                                       | \- register    | X       | X    | X    | X    |
| [scale by 2](dx9-graphics-reference-asm-ps-registers-modifiers-scale-x2.md)                                 | register\_x2   |         |      |      | X    |
| [signed scaling](dx9-graphics-reference-asm-ps-registers-modifiers-signed-scale.md)                         | register\_bx2  | X       | X    | X    | X    |
| [texld and texcrd modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-ps-1-4.md)                   | register\_d\*  | X       | X    | X    | X    |
| [source register swizzling](dx9-graphics-reference-asm-ps-registers-modifiers-source-register-swizzling.md) | register.xyzw  | X       | X    | X    | X    |



 

Source register modifiers can be used only on arithmetic instructions. They cannot be used on texture address instructions. The exception to this is the [scale by 2](dx9-graphics-reference-asm-ps-registers-modifiers-scale-x2.md) modifier. For version 1\_1, signed scale can be used on the source argument of any texm\* instruction. For version 1\_2 or 1\_3, signed scale can be used on the source argument of any texture address instruction.

Some modifier specific restrictions:

-   Negate can be combined with either the bias, signed scaling, or scalex2 modifier. When combined, negate is run last.
-   Invert cannot be combined with any other modifier.
-   Invert, negate, bias, signed scaling, and scalex2 can be combined with any of the selectors.
-   Source register modifiers should not be used on constant registers because they will cause undefined results. For version 1\_4, modifiers on constants are not allowed and will fail validation.

## ps\_2\_0 and Above

For version ps\_2\_0 and up, the number of modifiers has been simplified.

### Negate

Negate the contents of the source register.



| Component modifier | Description     |
|--------------------|-----------------|
| \- r               | Source negation |



 

The negate modifier cannot be used on second source register of these instructions: [m3x2 - ps](m3x2---ps.md), [m3x3 - ps](m3x3---ps.md), [m3x4 - ps](m3x4---ps.md), [m4x3 - ps](m4x3---ps.md), and [m4x4 - ps](m4x4---ps.md).



| Pixel shader versions | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|-------|------|-------|
| \-                    | x    | x    | x     | x    | x     |



 

### Absolute Value

Take the absolute value of the register.



| Pixel shader versions | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|-------|------|-------|
| abs                   |      |      |       | x    | x     |



 

If any version 3 shader reads from one or more constant float registers (c\#), one of the following must be true.

-   All of the constant floating-point registers must use the abs modifier.
-   None of the constant floating-point registers can use the abs modifier.

## Related topics

<dl> <dt>

[Pixel Shader Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers.md)
</dt> </dl>

 

 




