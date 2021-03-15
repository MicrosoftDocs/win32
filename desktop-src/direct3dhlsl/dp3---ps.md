---
title: dp3 - ps
description: Computes the three-component dot product of the source registers. | dp3 - ps
ms.assetid: a365acd1-89c0-4340-8f51-8e478f84ddc0
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dp3 - ps

Computes the three-component dot product of the source registers.

## Syntax



| dp3 dst, src0, src1 |
|---------------------|



 

where

-   dst is the destination register.
-   src0 is a source register.
-   src1 is a source register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dp3                   | x    | x    | x    | x    | x    | x    | x     | x    | x     |



 

The following code snippet shows the operations performed:


```
dest.x = dest.y = dest.z = dest.w = 
  (src0.x * src1.x) + (src0.y * src1.y) + (src0.z * src1.z);
```



This instruction runs in the vector pipeline, always writing out to the color channels. For version 1\_4, this instruction still uses the vector pipeline but may write to any channel.

An instruction with a destination register .rgb (.xyz) write mask may be co-issued with dp3 As shown below.


```
dp3 r0.rgb, t0, v0            // Copy scalar result to color components
+mov r2.a, t0                 // Copy alpha component from t0 in parallel 
```



The dp3 instruction can be modified using the [Source Register Signed Scaling](dx9-graphics-reference-asm-ps-registers-modifiers-signed-scale.md) input argument modifier (\_bx2) applied to its input arguments if they are not already expanded to signed dynamic range. For a lighting shader, the saturate instruction modifier (\_sat) is often used to clamp the negative values to black, as shown in the following example.


```
dp3_sat r0, t0_bx2, v0_bx2    // t0 is a bump map, v0 contains the light direction
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




