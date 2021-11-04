---
description: Learn about Direct3D 10 effects. An effect is pipeline state, set by expressions written in HLSL and some syntax that is specific to the effect framework.
ms.assetid: db4c7651-b6a1-4bc3-bcf8-a5cb56c7563e
title: Effects (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Effects (Direct3D 10)

A DirectX effect is a collection of pipeline state, set by expressions written in [HLSL](../direct3dhlsl/dx-graphics-hlsl-reference.md) and some syntax that is specific to the effect framework. After compiling an effect, use the effect framework APIs to render. Effect functionality can range from something as simple as a vertex shader that transforms geometry and a pixel shader that outputs a solid color, to a rendering technique that requires multiple passes, uses every stage of the graphics pipeline, and manipulates shader state as well as the pipeline state not associated with the programmable shaders.

The first step is to organize the state you want to control in an effect. This includes shader state (vertex, geometry and pixel shaders), texture and sampler state used by the shaders, and other non-programmable pipeline state. You can create an effect in memory as a text string, but typically, the size gets large enough that it is handy to store effect state in an effect file (a text file that ends in a .fx extension). To use an effect, you must compile it (to check HLSL syntax as well as effect framework syntax), initialize effect state through API calls, and modify your render loop to call the rendering APIs.

-   [Organizing State in an Effect](d3d10-graphics-programming-guide-effects-organize.md)
-   [Effect System Interfaces](d3d10-graphics-programming-guide-effects-interfaces.md)
-   [Specializing Interfaces](d3d10-graphics-reference-effect-specializing.md)
-   [Rendering an Effect](d3d10-graphics-programming-guide-effects-render.md)

An effect encapsulates all of the render state required by a particular effect into a single rendering function called a technique. A pass is a sub-set of a technique, that contains render state. To implement a multiple pass rendering effect, implement one or more passes within a technique. For example, say you wanted to render some geometry with one set of depth/stencil buffers, and then draw some sprites on top of that. You could implement the geometry rendering in the first pass, and the sprite drawing in the second pass. To render the effect, you simply render both passes in your render loop. You can implement any number of techniques in an effect. Of course, the greater the number of techniques, the greater the compile time for the effect. One way to exploit this functionality is to create effects with techniques that are designed to run on different hardware. This allows an application to gracefully downgrade performance based on the hardware capabilities detected.

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 
