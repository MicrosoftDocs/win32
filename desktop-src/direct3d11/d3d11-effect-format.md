---
title: Effect Format (Direct3D 11)
ms.assetid: c425f57b-fc14-46a5-bb65-a0a2305bd406
description: "Learn more about: Effect Format (Direct3D 11)"
ms.topic: reference
ms.date: 05/31/2018
---

# Effect Format (Direct3D 11)

An effect (which is often stored in a file with a .fx file extension) declares the pipeline state set by an effect. Effect state can be roughly broken down into three categories:

-   [Variables](d3d11-effect-variable-syntax.md), which are usually declared at the top of an effect.
-   [Functions](d3d11-effect-function-syntax.md), which implement shader code, or are used as helper functions by other functions.
-   [Techniques](d3d11-effect-technique-syntax.md), which can be arranged in effect groups, and implement rendering sequences using one or more effect passes. Each pass sets one or more [state groups](d3d11-effect-states.md) and calls shader functions.

![diagram of the categories of declarations for effects, including variables at the top, functions in the middle, and techniques at the bottom](images/d3d10-effect-intro.png)

The preceding diagram shows the categories of effect state.

The definition of the effect binary format can be found in Binary\\EffectBinaryFormat.h in the effects source code.


## In this section



| Topic                                                                   | Description                                                                                                          |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Effect Variable Syntax](d3d11-effect-variable-syntax.md)<br/>   | An effect variable is declared with the syntax described in this section.<br/>                                 |
| [Annotation Syntax](d3d11-effect-annotation-syntax.md)<br/>      | An annotation is a user-defined piece of information, declared with the syntax described in this section.<br/> |
| [Effect Function Syntax](d3d11-effect-function-syntax.md)<br/>   | An effect function is written in HLSL and is declared with the syntax described in this section.<br/>          |
| [Effect Technique Syntax](d3d11-effect-technique-syntax.md)<br/> | An effect technique is declared with the syntax described in this section.<br/>                                |
| [Effect State Groups](d3d11-effect-states.md)<br/>               | Effect states are name value pairs in the form of an expression.<br/>                                          |
| [Effect Group Syntax](d3d11-effect-group-syntax.md)<br/>         | An effect group is declared with the syntax described in this section.<br/>                                    |



 

## Related topics

<dl> <dt>

[Effects 11 Reference](d3d11-graphics-reference-effects11.md)
</dt> </dl>

 

 





