---
title: Source register swizzling (HLSL PS reference)
description: Swizzling refers to the ability to copy any source register component to any temporary register component. Swizzling does not affect the source register data. Before an instruction runs, the data in a source register is copied to a temporary register.
ms.assetid: 27aee6a8-5185-4236-b3e4-44addf230c34
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Source register swizzling (HLSL PS reference)

Swizzling refers to the ability to copy any source register component to any temporary register component. Swizzling does not affect the source register data. Before an instruction runs, the data in a source register is copied to a temporary register.

## Source Swizzling

Source swizzle allows individual component of a source register to take on the value of any of the four components of the same source register before the register is read for computation.

For example, the .zxxy swizzle means:

-   .x component will take on the value of .z component
-   .y component will take on the value of .x component
-   .z component will take on the value of .x component
-   .w component will take on the value of .y component

The components can appear in any order. If fewer than four components are specified, the last component is repeated. For example:


```
.xy  = .xyyy
.wzx = .wzxx
.z   = .zzzz
```



If no component is specified, no swizzling is applied.

Some instructions have restrictions for source swizzle. They are listed in the respected instruction reference pages.



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| .x                    |      |      |      | x    | x    | x    | x     | x    | x     |
| .y                    |      |      |      | x    | x    | x    | x     | x    | x     |
| .z                    | x\*  | x\*  | x\*  | x    | x    | x    | x     | x    | x     |
| .w                    | x    | x    | x    | x    | x    | x    | x     | x    | x     |
| .xyzw (default)       | x    | x    | x    | x    | x    | x    | x     | x    | x     |
| .yzxw                 |      |      |      |      | x    | x    | x     | x    | x     |
| .zxyw                 |      |      |      |      | x    | x    | x     | x    | x     |
| .wzyx                 |      |      |      |      | x    | x    | x     | x    | x     |
| arbitrary swizzle     |      |      |      |      |      | x    | x     | x    | x     |



 

\* Only available if destination write mask is .w (.a).

## Arbitrary Swizzle

Swizzles can be applied to source registers in an arbitrary order; that is, any source register can take any component mask, in any order.

## Replicate Swizzle

Replicate swizzle copies one component to another. This is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.

## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> <dt>

[ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers](dx9-graphics-reference-asm-ps-registers-ps-1-x.md)
</dt> <dt>

[ps\_2\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-2-0.md)
</dt> <dt>

[ps\_2\_x Registers](dx9-graphics-reference-asm-ps-registers-ps-2-x.md)
</dt> <dt>

[ps\_3\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-3-0.md)
</dt> </dl>

 

 




