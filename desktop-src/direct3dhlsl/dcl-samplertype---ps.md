---
title: dcl_samplerType (sm2, sm3 - ps asm)
description: Declare a pixel shader sampler.
ms.assetid: c90ff5b6-f89a-4993-8a5d-dbbc4a7896b0
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_samplerType (sm2, sm3 - ps asm)

Declare a pixel shader sampler.

## Syntax

dcl\_samplerType s\#



 

where:

-   \_samplerType defines the sampler data type. This determines how many coordinates are required by each texture coordinate when sampling. The following texture coordinate dimensions are defined.
    -   \_2d
    -   \_cube
    -   \_volume
-   s\# identifies a sampler where s is an abbreviation for the sampler, and \# is the sampler number. Samplers are pseudo registers because you cannot directly read or write to them.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| dcl\_samplerType      |      |      |      |      | x    | x    | x     | x    | x     |



 

All dcl\_samplerType instructions must appear before the first executable instruction.

## Example


```
dcl_cube t0.rgb;  // Define a 3D texture map.

add r0, r0, t0;   // Perturb texture coordinates. 
texld r0, s0, r0; // Load r0 with a color sampled from stage0
                  //   at perturbed texture coordinates r0.
                  // This is a dependent texture read.
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




