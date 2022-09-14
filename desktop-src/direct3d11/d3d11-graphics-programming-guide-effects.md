---
title: Effects (Direct3D 11)
description: Learn about Direct3D 11 effects. An effect is pipeline state, set by expressions written in HLSL and some syntax that is specific to the effect framework.
ms.assetid: d52a2cad-eac9-4442-9ee5-114bebe0f245
ms.topic: article
ms.date: 05/31/2018
---

# Effects (Direct3D 11)

A DirectX effect is a collection of pipeline state, set by expressions written in [HLSL](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-reference) and some syntax that is specific to the effect framework.

After compiling an effect, use the effect framework APIs to render. Effect functionality can range from something as simple as a vertex shader that transforms geometry and a pixel shader that outputs a solid color, to a rendering technique that requires multiple passes, uses every stage of the graphics pipeline, and manipulates shader state as well as the pipeline state not associated with the programmable shaders.

The first step is to organize the state you want to control in an effect. This includes shader state (vertex, hull, domain, geometry, pixel and compute shaders), texture and sampler state used by the shaders, and other non-programmable pipeline state. You can create an effect in memory as a text string, but typically, the size gets large enough that it is handy to store effect state in an effect file (a text file that ends in a .fx extension). To use an effect, you must compile it (to check HLSL syntax as well as effect framework syntax), initialize effect state through API calls, and modify your render loop to call the rendering APIs.

An effect encapsulates all of the render state required by a particular effect into a single rendering function called a technique. A pass is a sub-set of a technique, that contains render state. To implement a multiple pass rendering effect, implement one or more passes within a technique. For example, say you wanted to render some geometry with one set of depth/stencil buffers, and then draw some sprites on top of that. You could implement the geometry rendering in the first pass, and the sprite drawing in the second pass. To render the effect, you simply render both passes in your render loop. You can implement any number of techniques in an effect. Of course, the greater the number of techniques, the greater the compile time for the effect. One way to exploit this functionality is to create effects with techniques that are designed to run on different hardware. This allows an application to gracefully downgrade performance based on the hardware capabilities detected.

A set of techniques can be grouped in a group (which uses the syntax "fxgroup"). Techniques can be grouped in any way. For example, multiple groups could be created, one per material; each material could have a technique for each hardware level; each technique would have a set of passes which define the material on the particular hardware.

## In this section



| Topic                                                                                                                | Description                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Organizing State in an Effect](d3d11-graphics-programming-guide-effects-organize.md)<br/>                    | With Direct3D 11, effect state for certain pipeline stages is organized by structures.<br/>                                                                   |
| [Effect System Interfaces](d3d11-graphics-programming-guide-effects-interfaces.md)<br/>                       | The effect system defines several interfaces for managing effect state.<br/>                                                                                  |
| [Specializing Interfaces](d3d11-graphics-reference-effect-specializing.md)<br/>                               | [**ID3DX11EffectVariable**](id3dx11effectvariable.md) has a number of methods for casting the interface into the particular type of interface you need.<br/> |
| [Interfaces and Classes in Effects](d3d11-graphics-programming-guide-effects-interfaces-and-classes.md)<br/>  | There are many ways to use classes and interfaces in Effects 11.<br/>                                                                                         |
| [Rendering an Effect](d3d11-graphics-programming-guide-effects-render.md)<br/>                                | An effect can be used to store information, or to render using a group of state.<br/>                                                                         |
| [Cloning an Effect](d3d11-graphics-programming-guide-effects-cloning.md)<br/>                                 | Cloning an effect creates a second, almost identical copy of the effect.<br/>                                                                                 |
| [Stream Out Syntax](d3d11-graphics-reference-effect-streamout.md)<br/>                                        | A geometry shader with stream out is declared with a particular syntax.<br/>                                                                                  |
| [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md)<br/> | This topic shows the differences between Effects 10 and Effects 11.<br/>                                                                                      |



 

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 11](dx-graphics-overviews.md)
</dt> </dl>

 

