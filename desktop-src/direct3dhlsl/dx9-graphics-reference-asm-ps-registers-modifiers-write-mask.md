---
title: Destination Register Write Mask
description: A write mask controls which components of a destination register are written after an instruction is completed.
ms.assetid: 376a28c8-8a88-4807-a8ab-f59448d965e8
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Destination Register Write Mask

A write mask controls which components of a destination register are written after an instruction is completed. An output write mask is allowed as long as the components are in the order of .rgba or .xyzw. That is, .rba and .xw are valid masks. Texture registers have one set of rules and non-texture registers have another set of rules.

## Syntax



| dst.writemask |
|---------------|



 

where

-   dst is a destination register.
-   writemask is a sequence of masks from either set: (x,y,z,w) or (red, green, blue, alpha).

## Remarks

The following destination write masks are available.



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| .xyzw (default)       | x    | x    | x    | x    | x    | x    | x     | x    | x     |
| .xyz                  | x    | x    | x    | x    | x    | x    | x     | x    | x     |
| .w                    | x    | x    | x    | x    | x    | x    | x     | x    | x     |
| arbitrary mask        |      |      |      | x    | x    | x    | x     | x    | x     |



 

The arbitrary mask allows any set of channels to be combined to produce a mask. The channels must be listed in the order r, g, b, a - for example, register.rba, which updates the red, blue, and alpha channels of the destination. The arbitrary mask is available in version 1\_4 or higher.

If no destination write mask is specified, the destination write mask defaults to the rgba case. In other words, all channels in the destination register are updated.

For versions 1\_0 to 1\_3, the [dp3 - ps](dp3---ps.md) dp3 arithmetic instruction can use only the .rgb or .rgba output write masks.

Destination register write masks are supported for arithmetic operations only. They cannot be used on texture addressing instructions, with the exception of the version 1\_4 instructions, [texcrd - ps](texcrd---ps.md) and [texld - ps\_2\_0 and up](texld---ps-2-0.md).

The default is to write all four color channels.


```
// All four color channels can be written by explicitly listing them.
mul r0.rgba, t0, v0

// Or, the default mask can be used to write all four channels.
mul r0, t0, v0
```



The alpha write mask is also referred to as the scalar write mask, because it uses the scalar pipeline.


```
add r0.a, t1, v1
```



So this instruction effectively puts the sum of the alpha component of t1 and the alpha component of v1 into r0.a.

The color write mask is used to control writing to the color channels.


```
// The color write mask is also referred to as the vector write mask, 
//   because it uses the vector pipeline.
mul r0.rgb, t0, v0
```



For version 1\_4, destination write masks can be used in any combination as long as the masks are ordered r,g,b,a.


```
// This example updates the red, blue, and alpha channels.
mov r0.rba, r1
```



A co-issued instruction allows two potentially different instructions to be issued simultaneously. This is accomplished by executing the instructions in the alpha pipeline and the RGB pipeline.


```
  mul r0.rgb, t0, v0
+ add r1.a,   t1, c1
```



The advantage of pairing instructions this way is that it allows different operations to be performed in the vector and scalar pipeline in parallel.

These vertex shader output registers are restricted to the following write masks:



| Register Type | Required Write Mask                                              |
|---------------|------------------------------------------------------------------|
| oFog          | no explicit write mask is allowed on this scalar register        |
| oPts          | no explicit write mask is allowed on this scalar register        |
| oPos          | .xyzw(which is the default)                                      |
| oT\#          | combined mask: .x \| .xy \| .xyz \| .xyzw (which is the default) |



 

## Related topics

<dl> <dt>

[Pixel Shader Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers.md)
</dt> </dl>

 

 




