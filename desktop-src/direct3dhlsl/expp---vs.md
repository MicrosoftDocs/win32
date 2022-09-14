---
title: expp - vs
description: Provides partial precision exponential 2x.
ms.assetid: ac080ac9-5dfd-49e4-92ea-50bb26844ff6
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# expp - vs

Provides partial precision exponential 2<sup>x</sup>.

## Syntax



| expp dst, src.{x\|y\|z\|w} |
|----------------------------|



 

Where:

-   dst is the destination register.
-   src is a source register. Source register requires explicit use of replicate swizzle, that is, exactly one of the .x, .y, .z, .w swizzle components (or the .r, .g, .b, .a equivalents) must be specified.
-   {x\|y\|z\|w} is the required replicate swizzle on source register.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| expp                   | x    | x    | x    | x     | x    | x     |



 

### vs\_1\_1

The [exp - vs](exp---vs.md) instruction operates differently depending on vertex shader versions.

In vs\_1\_1, the expp instruction gives the following results:


```
v = the scalar value from the source register with a replicate swizzle

dest.x = pow(2, floor(v))
dest.y = v - floor(v)
dest.z = pow(2, v) (partial-precision)
dest.w = 1
```



In vs\_2\_0 and up, the expp instruction gives the following results:


```
v = the scalar value from the source register with a replicate swizzle

dest.x = dest.y = dest.z = dest.y = pow(2, v) (partial-precision)
```



### vs\_2\_0

In vs\_2\_0 and up, the instruction works like this:


```
float V = the scalar value from the source register with a replicate swizzle

dest.x = dest.y = dest.z = dest.y = pow( 2, V ) (partial-precision)
```



The instruction provides at least 10 bits of precision.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




