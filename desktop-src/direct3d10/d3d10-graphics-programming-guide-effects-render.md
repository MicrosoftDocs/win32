---
description: Learn about rendering an effect for Direct3D 10. An effect can be used to store information, or to render using a group of state.
ms.assetid: c5654335-ad80-4a5b-bf1f-5f32b2cc8ea2
title: Rendering an Effect (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Rendering an Effect (Direct3D 10)

An effect can be used to store information, or to render using a group of state. Each technique specifies vertex shaders, geometry shaders, pixel shaders, shader state, sampler and texture state and other pipeline state. So once you have organized state into an effect, you can encapsulate the rendering effect that results from that state by creating and rendering the effect.

There are a few steps for preparing an effect for rendering. The first is compiling, which checks the HLSL like code against the HLSL language syntax and the effect framework rules. You can compile an effect from your application using API calls or you can compile an effect offline using the effect compiler utility. Once your effect has successfully compiled, create it by calling a different (but very similar) set of APIs.

After the effect is created, there are two remaining steps for using it. First, you must initialize the effect state values (the values of the effect variables) using a number of methods for setting state. For some variables this can be done once when an effect is created; others must be updated each time your application calls the render loop. Once the effect variables are set, you tell the runtime to render the affect by applying a technique. These topics are all discussed in further detail below.

-   [Compile an Effect (Direct3D 10)](d3d10-graphics-programming-guide-effects-compile.md)
-   [Create an Effect (Direct3D 10)](d3d10-graphics-programming-guide-effects-create.md)
-   [Set Effect State (Direct3D 10)](d3d10-graphics-programming-guide-effects-set-state.md)
-   [Apply a Technique (Direct3D 10)](d3d10-graphics-programming-guide-effects-apply-technique.md)

Naturally there are [performance considerations](d3d10-graphics-programming-guide-effects-performance.md) for using effects. These considerations are largely the same if you are not using an effect. Things like, minimizing the amount of state changes, or organizing the variables that need to be updated by frequency. These tactics are used to minimize the amount of data that needs to be sent from the CPU to the GPU, and therefore minimize potential synchronization problems.

## Related topics

<dl> <dt>

[Effects (Direct3D 10)](d3d10-graphics-programming-guide-effects.md)
</dt> </dl>

 

 



