---
title: sgn - vs
description: Computes the sign of the input.
ms.assetid: b03530d1-c621-483e-bd94-31abafeb2e6e
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# sgn - vs

Computes the sign of the input.

## Syntax



| sgn dst, src0, src1, src2 |
|---------------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a temporary register that holds intermediate results. Following execution, contents are undefined.
-   src2 is a temporary register that holds intermediate results. Following execution, contents are undefined.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| sgn                    |      | x    | x    | x     | x    | x     |



 

This instruction works as shown below.


```
for each component in src0
{
   if (src0.component < 0) 
       dest.component = -1; 
   else
       if (src0.component == 0) 
           dest.component = 0; 
       else 
           dest.component = 1;
}
```



src1 and src2 must be different [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md)s.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




