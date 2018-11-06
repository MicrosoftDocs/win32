---
title: Flow Control Limitations
description: Pixel shader flow control instructions have limits affecting how many levels of nesting can be included in the instructions. In addition, there are some limitations for implementing per-pixel flow control with gradient instructions.
ms.assetid: 17a902cd-16a4-4065-9249-01f9b1f40506
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Flow Control Limitations

Pixel shader flow control instructions have limits affecting how many levels of nesting can be included in the instructions. In addition, there are some limitations for implementing per-pixel flow control with gradient instructions.

> [!Note]  
> When you use the \*\_4\_0\_level\_9\_x HLSL shader profiles, you implicitly use of the [Shader Model 2.x](dx-graphics-hlsl-sm2.md) profiles to support Direct3D 9 capable hardware. Shader Model 2.x profiles support more limited flow control behavior than the [Shader Model 4.x](dx-graphics-hlsl-sm4.md) and later profiles.

 

-   [Pixel Shader Instruction Depth Counts](#pixel-shader-instruction-depth-counts)
-   [Interaction of Per-Pixel Flow Control With Screen Gradients](#interaction-of-per-pixel-flow-control-with-screen-gradients)

## Pixel Shader Instruction Depth Counts

ps\_2\_0 does not support flow control. The limitations for the other pixel shader versions are listed below.

### Instruction Depth Count for ps\_2\_x

Each instruction counts against one or more nesting depth limits. The following table lists the depth count that each instruction adds or subtracts from the existing depth.



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|
| [if bool - ps](if-bool---ps.md)         | 1                                    | 0                                                                         | 0                | 0            |
| [if\_comp - ps](if-comp---ps.md)        | 0                                    | 1                                                                         | 0                | 0            |
| [if pred - ps](if-pred---ps.md)         | 0                                    | 1                                                                         | 0                | 0            |
| [else - ps](else---ps.md)               | 0                                    | 0                                                                         | 0                | 0            |
| [endif - ps](endif---ps.md)             | -1([if bool - ps](if-bool---ps.md)) | -1([if pred - ps](if-pred---ps.md) or [if\_comp - ps](if-comp---ps.md)) | 0                | 0            |
| [rep - ps](rep---ps.md)                 | 0                                    | 0                                                                         | 1                | 0            |
| [endrep - ps](endrep---ps.md)           | 0                                    | 0                                                                         | -1               | 0            |
| [break - ps](break---ps.md)             | 0                                    | 0                                                                         | 0                | 0            |
| [break\_comp - ps](break-comp---ps.md)  | 0                                    | 1, -1                                                                     | 0                | 0            |
| [breakp - ps](break-p---ps.md)          | 0                                    | 0                                                                         | 0                | 0            |
| [call - ps](call---ps.md)               | 0                                    | 0                                                                         | 0                | 1            |
| [callnz bool - ps](callnz-bool---ps.md) | 0                                    | 0                                                                         | 0                | 1            |
| [callnz pred - ps](callnz-pred---ps.md) | 0                                    | 1                                                                         | 0                | 1            |
| [ret - ps](ret---ps.md)                 | 0                                    | -1([callnz pred - ps](callnz-pred---ps.md))                              | 0                | -1           |
| [setp\_comp - ps](setp-comp---ps.md)    | 0                                    | 0                                                                         | 0                | 0            |



 

### Nesting Depth

Nesting depth defines the number of instructions can be called from inside of each other. Each type of instruction has one or more nesting limits as indicated in the following table.



| Instruction Type | Maximum                                                                                   |
|------------------|-------------------------------------------------------------------------------------------|
| Static nesting   | 24 if (D3DCAPS9.D3DPSHADERCAPS2\_0.StaticFlowControlDepth > 0); 0 otherwise            |
| Dynamic nesting  | 0 to 24, see D3DCAPS9.D3DPSHADERCAPS2\_0.DynamicFlowControlDepth                          |
| rep nesting      | 0 to 4, see D3DCAPS9.D3DPSHADERCAPS2\_0.StaticFlowControlDepth                            |
| call nesting     | 0 to 4, see D3DCAPS9.D3DPSHADERCAPS2\_0.StaticFlowControlDepth (independent of rep limit) |



 

### Instruction Depth Count for ps\_2\_sw

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth.



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|
| [if bool - ps](if-bool---ps.md)         | 1                                    | 0                                                                         | 0                | 0            |
| [if pred - ps](if-pred---ps.md)         | 0                                    | 1                                                                         | 0                | 0            |
| [if\_comp - ps](if-comp---ps.md)        | 0                                    | 1                                                                         | 0                | 0            |
| [else - ps](else---ps.md)               | 0                                    | 0                                                                         | 0                | 0            |
| [endif - ps](endif---ps.md)             | -1([if bool - ps](if-bool---ps.md)) | -1([if pred - ps](if-pred---ps.md) or [if\_comp - ps](if-comp---ps.md)) | 0                | 0            |
| [rep - ps](rep---ps.md)                 | 0                                    | 0                                                                         | 1                | 0            |
| [endrep - ps](endrep---ps.md)           | 0                                    | 0                                                                         | -1               | 0            |
| [loop - ps](loop---ps.md)               | n/a                                  | n/a                                                                       | n/a              | n/a          |
| [endloop - ps](endloop---ps.md)         | n/a                                  | n/a                                                                       | n/a              | n/a          |
| [break - ps](break---ps.md)             | 0                                    | 0                                                                         | 0                | 0            |
| [break\_comp - ps](break-comp---ps.md)  | 0                                    | 1, -1                                                                     | 0                | 0            |
| [breakp - ps](break-p---ps.md)          | 0                                    | 0                                                                         | 0                | 0            |
| [call - ps](call---ps.md)               | 0                                    | 0                                                                         | 0                | 1            |
| [callnz bool - ps](callnz-bool---ps.md) | 0                                    | 0                                                                         | 0                | 1            |
| [callnz pred - ps](callnz-pred---ps.md) | 0                                    | 1                                                                         | 0                | 1            |
| [ret - ps](ret---ps.md)                 | 0                                    | -1([callnz pred - ps](callnz-pred---ps.md))                              | 0                | -1           |
| [setp\_comp - ps](setp-comp---ps.md)    | 0                                    | 0                                                                         | 0                | 0            |



 

### Nesting Depth

Nesting depth defines the number of instructions that can be called from inside of each other. Each type of instruction has one or more nesting limits as indicated in the following table.



| Instruction Type | Maximum |
|------------------|---------|
| Static nesting   | 24      |
| Dynamic nesting  | 24      |
| rep nesting      | 4       |
| call nesting     | 4       |



 

### Instruction Depth Count for ps\_3\_0

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth.



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|
| [if bool - ps](if-bool---ps.md)         | 1                                    | 0                                                                         | 0                | 0            |
| [if pred - ps](if-pred---ps.md)         | 0                                    | 1                                                                         | 0                | 0            |
| [if\_comp - ps](if-comp---ps.md)        | 0                                    | 1                                                                         | 0                | 0            |
| [else - ps](else---ps.md)               | 0                                    | 0                                                                         | 0                | 0            |
| [endif - ps](endif---ps.md)             | -1([if bool - ps](if-bool---ps.md)) | -1([if pred - ps](if-pred---ps.md) or [if\_comp - ps](if-comp---ps.md)) | 0                | 0            |
| [rep - ps](rep---ps.md)                 | 0                                    | 0                                                                         | 1                | 0            |
| [endrep - ps](endrep---ps.md)           | 0                                    | 0                                                                         | -1               | 0            |
| [loop - ps](loop---ps.md)               | 0                                    | 0                                                                         | 1                | 0            |
| [endloop - ps](endloop---ps.md)         | 0                                    | 0                                                                         | -1               | 0            |
| [break - ps](break---ps.md)             | 0                                    | 0                                                                         | 0                | 0            |
| [break\_comp - ps](break-comp---ps.md)  | 0                                    | 1, -1                                                                     | 0                | 0            |
| [breakp - ps](break-p---ps.md)          | 0                                    | 0                                                                         | 0                | 0            |
| [call - ps](call---ps.md)               | 0                                    | 0                                                                         | 0                | 1            |
| [callnz bool - ps](callnz-bool---ps.md) | 0                                    | 0                                                                         | 0                | 1            |
| [callnz pred - ps](callnz-pred---ps.md) | 0                                    | 1                                                                         | 0                | 1            |
| [ret - ps](ret---ps.md)                 | 0                                    | -1([callnz pred - ps](callnz-pred---ps.md))                              | 0                | -1           |
| [setp\_comp - ps](setp-comp---ps.md)    | 0                                    | 0                                                                         | 0                | 0            |



 

### Nesting Depth

Nesting depth defines the number of instructions that can be called from inside of each other. Each type of instruction has one or more nesting limits as indicated in the following table.



| Instruction Type | Maximum |
|------------------|---------|
| Static nesting   | 24      |
| Dynamic nesting  | 24      |
| loop/rep nesting | 4       |
| call nesting     | 4       |



 

### Instruction Depth Count for ps\_3\_sw

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth.



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|
| [if bool - ps](if-bool---ps.md)         | 1                                    | 0                                                                         | 0                | 0            |
| [if pred - ps](if-pred---ps.md)         | 0                                    | 1                                                                         | 0                | 0            |
| [if\_comp - ps](if-comp---ps.md)        | 0                                    | 1                                                                         | 0                | 0            |
| [else - ps](else---ps.md)               | 0                                    | 0                                                                         | 0                | 0            |
| [endif - ps](endif---ps.md)             | -1([if bool - ps](if-bool---ps.md)) | -1([if pred - ps](if-pred---ps.md) or [if\_comp - ps](if-comp---ps.md)) | 0                | 0            |
| [rep - ps](rep---ps.md)                 | 0                                    | 0                                                                         | 1                | 0            |
| [endrep - ps](endrep---ps.md)           | 0                                    | 0                                                                         | -1               | 0            |
| [loop - ps](loop---ps.md)               | 0                                    | 0                                                                         | 1                | 0            |
| [endloop - ps](endloop---ps.md)         | 0                                    | 0                                                                         | -1               | 0            |
| [break - ps](break---ps.md)             | 0                                    | 0                                                                         | 0                | 0            |
| [break\_comp - ps](break-comp---ps.md)  | 0                                    | 1, -1                                                                     | 0                | 0            |
| [breakp - ps](break-p---ps.md)          | 0                                    | 0                                                                         | 0                | 0            |
| [call - ps](call---ps.md)               | 0                                    | 0                                                                         | 0                | 1            |
| [callnz bool - ps](callnz-bool---ps.md) | 0                                    | 0                                                                         | 0                | 1            |
| [callnz pred - ps](callnz-pred---ps.md) | 0                                    | 1                                                                         | 0                | 1            |
| [ret - ps](ret---ps.md)                 | 0                                    | -1([callnz pred - ps](callnz-pred---ps.md))                              | 0                | -1           |
| [setp\_comp - ps](setp-comp---ps.md)    | 0                                    | 0                                                                         | 0                | 0            |



 

### Nesting Depth

Nesting depth defines the number of instructions that can be called from inside of each other. Each type of instruction has one or more nesting limits as indicated in the following table.



| Instruction Type | Maximum |
|------------------|---------|
| Static nesting   | 24      |
| Dynamic nesting  | 24      |
| loop/rep nesting | 4       |
| call nesting     | 4       |



 

## Interaction of Per-Pixel Flow Control With Screen Gradients

The pixel shader instruction set includes several instructions that produce or use gradients of quantities with respect to screen space x and y. The most common use for gradients is to compute level-of-detail calculations for texture sampling, and in the case of anisotropic filtering, selecting samples along the axis of anisotropy. Typically, hardware implementations run the pixel shader on multiple pixels simultaneously (such as a 2x2 grid), so that gradients of quantities computed in the shader can be reasonably approximated as deltas of the values at the same point of execution in adjacent pixels.

When flow control is present in a shader, the result of a gradient calculation requested inside a given branch path is ambiguous when adjacent pixels may execute separate flow control paths. Therefore, it is deemed illegal to use any pixel shader operation that requests a gradient calculation to occur at a location that is inside a flow control construct which could vary across pixels for a given primitive being rasterized.

All pixel shader instructions are partitioned into those operations that are permitted and into those that are not permitted inside of flow control:

-   Scenario A: Operations that are not permitted inside flow control that could vary across the pixels in a primitive. These include the operations listed in the following table. 

    | Instruction                                                                                                      | Is Permitted in Flow Control when:                       |
    |------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
    | [texld - ps\_2\_0 and up](texld---ps-2-0.md), [texldb - ps](texldb---ps.md) and [texldp - ps](texldp---ps.md) | A temporary register is used for the texture coordinate. |
    | [dsx - ps](dsx---ps.md) and [dsy - ps](dsy---ps.md)                                                            | A temporary register is used for the operand.            |

    

     

-   Scenario B: Operations that are permitted anywhere. These include the operations listed in the following table. 

    | Instruction                                                                                                      | Is Permitted Anywhere when:                                                                                             |
    |------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
    | [texld - ps\_2\_0 and up](texld---ps-2-0.md), [texldb - ps](texldb---ps.md) and [texldp - ps](texldp---ps.md) | A read-only quantity is used for the texture coordinate (may vary per-pixel, such as interpolated texture coordinates). |
    | [dsx - ps](dsx---ps.md) and [dsy - ps](dsy---ps.md)                                                            | A read-only quantity is used for the input operand (may vary per-pixel, such as interpolated texture coordinates).      |
    | [texldl - ps](texldl---ps.md)                                                                                   | The user provides level-of-detail as an argument, so there are no gradients, and thus no issue with flow control.       |
    | [texldd - ps](texldd---ps.md)                                                                                   | The user provides gradients as input arguments, so there is no issue with flow control.                                 |

    

     

These restrictions are strictly enforced in shader validation. Scenarios having a branch condition that looks like it would branch consistently across a primitive, even though an operand in the condition expression is a pixel-shader-computed quantity, nevertheless still fall into scenario A and are not permitted. Similarly, scenarios where gradients are requested on some shader-computed quantity x from inside dynamic flow control, yet where it appears that x is not modified across any of the branches, nevertheless still fall into scenario A and are not permitted.

Predication is included in these restrictions on flow control, so that implementations remain free to trivially interchange the implementation of branch instructions with predicated instructions.

The user can use instructions from scenarios A and B together. For example, suppose the user needs an anisotropic texture sample given a shader computed texture coordinate; however, the texture load is only needed for pixels satisfying some per-pixel condition. To meet these requirements, the user can compute the texture coordinate for all pixels, outside per-pixel varying flow control, immediately computing gradients using [dsx - ps](dsx---ps.md) and [dsy - ps](dsy---ps.md) instructions. Then, within a per-pixel [if bool - ps](if-bool---ps.md)/[endif - ps](endif---ps.md) block, the user can use [texldd - ps](texldd---ps.md) (texture load with user provided gradients), passing the precalculated gradients. Another way to describe this usage pattern is that, while all pixels in the primitive had to compute the texture coordinates and be involved with gradient calculation, only the pixels that needed to sample a texture actually did so.

Regardless of these rules, the burden is still on the user to ensure that before computing any gradient (or performing a texture sample that implicitly computes a gradient), the register containing the source data must have been initialized for all execution paths beforehand. Initialization of temporary registers is not validated or enforced in general.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




