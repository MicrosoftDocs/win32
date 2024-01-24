---
title: Rendering an Effect (Direct3D 11)
description: Learn about rendering an effect for Direct3D 11. An effect can be used to store information, or to render using a group of state.
ms.assetid: 7af239de-812d-4295-b599-b9deb371b01b
ms.topic: article
ms.date: 05/31/2018
---

# Rendering an Effect (Direct3D 11)

An effect can be used to store information, or to render using a group of state. Each technique specifies some set of vertex shaders, hull shaders, domain shaders, geometry shaders, pixel shaders, compute shaders, shader state, sampler and texture state, unordered access view state and other pipeline state. So once you have organized state into an effect, you can encapsulate the rendering effect that results from that state by creating and rendering the effect.

There are a few steps for preparing an effect for rendering. The first is compiling, which checks the HLSL like code against the HLSL language syntax and the effect framework rules. You can compile an effect from your application using API calls or you can compile an effect offline using the effect compiler utility [fxc.exe](/windows/desktop/direct3dtools/fxc). Once your effect has successfully compiled, create it by calling a different (but very similar) set of APIs.

After the effect is created, there are two remaining steps for using it. First, you must initialize the effect state values (the values of the effect variables) using a number of methods for setting state if they are not initialized in HLSL. For some variables this can be done once when an effect is created; others must be updated each time your application calls the render loop. Once the effect variables are set, you tell the runtime to render the effect by applying a technique. These topics are all discussed in further detail below.

Naturally there are performance considerations for using effects. These considerations are largely the same if you are not using an effect. Things like minimizing the amount of state changes and organizing the variables by frequency of update. These tactics are used to minimize the amount of data that needs to be sent from the CPU to the GPU, and therefore minimize potential synchronization problems.

## In this section



| Topic                                                                                        | Description                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Compile an Effect](d3d11-graphics-programming-guide-effects-compile.md)<br/>         | After an effect has been authored, the next step is to compile the code to check for syntax problems.<br/>                                                                                                                                                                                                          |
| [Create an Effect](d3d11-graphics-programming-guide-effects-create.md)<br/>           | An effect is created by loading the compiled effect bytecode into the effects framework. Unlike Effects 10, the effect must be compiled before creating the effect. Effects loaded into memory can be created by calling [**D3DX11CreateEffectFromMemory**](d3dx11createeffectfrommemory.md).<br/>                 |
| [Set Effect State](d3d11-graphics-programming-guide-effects-set-state.md)<br/>        | Some effect constants only need to be initialized. Once initialized, the effect state is set to the device for the entire render loop. Other variables need to be updated each time the render loop is called. The basic code for setting effect variables is shown below, for each of the types of variables.<br/> |
| [Apply a Technique](d3d11-graphics-programming-guide-effects-apply-technique.md)<br/> | With the constants, textures, and shader state declared and initialized, the only thing left to do is to set the effect state in the device.<br/>                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

