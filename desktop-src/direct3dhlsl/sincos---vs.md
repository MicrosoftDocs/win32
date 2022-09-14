---
title: sincos - vs
description: Computes sine and cosine, in radians. | sincos - vs
ms.assetid: 733a3980-ceaf-43dc-a862-923c369e4a65
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# sincos - vs

Computes sine and cosine, in radians.

## Syntax

### vs\_2\_0 and vs\_2\_x



| sincos dst.{x\|y\|xy}, src0.{x\|y\|z\|w}, src1, src2 |
|------------------------------------------------------|



 

Where:

-   dst is the destination register and has to be a [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md) (r\#). The destination register must have exactly one of the following three masks: .x \| .y \| .xy.
-   src0 is a source register that provides the input angle, which must be within \[-pi, +pi\]. {x\|y\|z\|w} is the required replicate swizzle.
-   src1 and src2 are source registers and must be two different [Constant Float Register](dx9-graphics-reference-asm-vs-registers-constant-float.md) (c\#). The values of src1 and src2 must be that of the macros [**D3DSINCOSCONST1**](/windows/desktop/direct3d9/d3dsincosconst1) and [**D3DSINCOSCONST2**](/windows/desktop/direct3d9/d3dsincosconst2) respectively.

### vs\_3\_0



| sincos dst.{x\|y\|xy}, src0.{x\|y\|z\|w} |
|------------------------------------------|



 

Where:

-   dst is a destination register and has to be a [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md) (r\#). The destination register must have exactly one of the following three masks: .x \| .y \| .xy.
-   src0 is a source register that provides the input angle, which must be within \[-pi, +pi\]. {x\|y\|z\|w} is the required replicate swizzle.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| sincos                 |      | x    | x    | x     | x    | x     |



 

### vs\_2\_0 and vs\_2\_x Remarks

For vs\_2\_0 and vs\_2\_x, sincos can be used with predication, but with one restriction to the swizzle of the [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md) (p0): only replicate swizzle (.x \| .y \| .z \| .w) is allowed.

For vs\_2\_0 and vs\_2\_x, the instruction operates as follows: (V = the scalar value from src0 with a replicate swizzle):

-   If the write mask is .x:
    ```
    dest.x = cos( V )
    dest.y is undefined when the instruction completes
    dest.z is undefined when the instruction completes
    dest.w is not touched by the instruction
    ```

    

-   If the write mask is .y:
    ```
    dest.x is undefined when the instruction completes
    dest.y = sin( V )
    dest.z is undefined when the instruction completes
    dest.w is not touched by the instruction
    ```

    

-   If the write mask is .xy:
    ```
    dest.x = cos( V )
    dest.y = sin( V )
    dest.z is undefined when the instruction completes
    dest.w is not touched by the instruction
    ```

    

### vs\_3\_0 Remarks

For vs\_3\_0, sincos can be used with predication without any restriction. See [Predicate Register](dx9-graphics-reference-asm-vs-registers-predicate.md).

For vs\_3\_0, the instruction operates as follows: (V = the scalar value from src0 with a replicate swizzle)

-   If the write mask is .x:
    ```
    dest.x = cos( V )
    dest.y is not touched by the instruction
    dest.z is not touched by the instruction
    dest.w is not touched by the instruction
    ```

    

-   If the write mask is .y:
    ```
    dest.x is not touched by the instruction
    dest.y = sin( V )
    dest.z is not touched by the instruction
    dest.w is not touched by the instruction
    ```

    

-   If the write mask is .xy:
    ```
    dest.x = cos( V )
    dest.y = sin( V )
    dest.z is not touched by the instruction
    dest.w is not touched by the instruction
    ```

    

The application can map an arbitrary angle (in radians) to the range \[-pi, +pi\] using the following shader pseudocode:


```
def c0, pi, 0.5, 2*pi, 1/(2*pi)
mad r0.x, input_angle, c0.w, c0.y
frc r0.x, r0.x
mad r0.x, r0.x, c0.z, -c0.x
```



## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 
