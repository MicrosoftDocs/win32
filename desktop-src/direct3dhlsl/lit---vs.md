---
title: lit - vs
description: Provides partial support for lighting by calculating lighting coefficients from two dot products and an exponent.
ms.assetid: e0ed1a75-6682-4d05-b0e5-dc65e201de98
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# lit - vs

Provides partial support for lighting by calculating lighting coefficients from two dot products and an exponent.

## Syntax



| lit dst, src |
|--------------|



 

where

-   dst is the destination register.
-   src is a source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| lit                    | x    | x    | x    | x     | x    | x     |



 

The source vector is assumed to contain the values shown in the following pseudocode.


```
src.x = N*L        ; The dot product between normal and direction to light
src.y = N*H        ; The dot product between normal and half vector
src.z = ignored    ; This value is ignored
src.w = exponent   ; The value must be between -128.0 and 128.0
```



The following code fragment shows the operations performed.


```
dest.x = 1;
dest.y = 0;
dest.z = 0;
dest.w = 1;

float power = src.w;
const float MAXPOWER = 127.9961f;
if (power < -MAXPOWER)
    power = -MAXPOWER;          // Fits into 8.8 fixed point format
else if (power > MAXPOWER)
    power = MAXPOWER;          // Fits into 8.8 fixed point format

if (src.x > 0)
{
    dest.y = src.x;
    if (src.y > 0)
    {
        // Allowed approximation is EXP(power * LOG(src.y))
        dest.z = (float)(pow(src.y, power));
    }
}
```



Reduced precision arithmetic is acceptable in evaluating the destination y component (dest.y). An implementation must support at least eight fraction bits in the power argument. Dot products are calculated with normalized vectors, and clamp limits are -128 to 128.

Error should correspond to a [logp - vs](logp---vs.md) and [exp - vs](exp---vs.md) combination, or no more than approximately one significant bit for an 8-bit color component.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




