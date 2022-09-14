---
title: texdepth - ps
description: Calculate depth values to be used in the depth buffer comparison test for this pixel.
ms.assetid: f7128dbb-a5f3-4e95-b53b-7432439ae0c4
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texdepth - ps

Calculate depth values to be used in the depth buffer comparison test for this pixel.

## Syntax



| texdepth dst |
|--------------|



 

where

-   dst is the destination register.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| texdepth              |      |      |      | x    |      |      |       |      |       |



 

This instruction uses r5.r / r5.g in the depth buffer comparison test for this pixel. The data in the blue and alpha channels is ignored. If r5.g = 0, the result of r5.r / r5.g = 1.0.

Temporary register r5 is the only register that this instruction can use.

After executing this instruction, temporary register r5 is unavailable for additional use in the shader.

When multisampling, using this instruction eliminates most of the benefit of the higher resolution depth buffer. Because the pixel shader runs once per pixel, the single depth value output by [texm3x2depth - ps](texm3x2depth---ps.md) or texdepth will be used for each of the subpixel depth comparison tests.

## Examples

Here is an example using texdepth.


```
ps_1_4              
texld  r0, t0        // Sample texture from texture stage 0 (dest 
                     //   register number) into r0
                     // Use texture coordinate data from t0
texcrd r1.rgb, t1    // Load a second set of texture coordinate data into r1
add    r5.rg, r0, r1 // Add the two sets of texture coordinate data
phase                // Phase marker, required when using texdepth instruction
texdepth  r5         // Calculate pixel depth as r5.r / r5.g
                     // Do other color calculations with shader output r0
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




