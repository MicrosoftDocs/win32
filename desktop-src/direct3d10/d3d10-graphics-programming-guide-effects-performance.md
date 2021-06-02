---
description: Performance Considerations (Direct3D 10)
ms.assetid: 9f029be5-4ce0-46ca-909b-adaa980398e7
title: Performance Considerations (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Performance Considerations (Direct3D 10)

## Using Effect Pools

It is common for rendering pipelines to use many shaders to render different object types and special effects. The shader are a mixture of states that a common among all the shaders such as a world matrix or a light position, and other state that is specific to each shader such as an object's diffuse color, or specular highlight calculation. An effect pool is a place in memory to store state that is used across many shaders, as well as common device objects such as shaders, render state objects and constant buffers. The performance improvement results from updating the common state once for all the shaders that need that state.

An effect pool is a shared memory location for effect state. A pool is created similarly to an effect; it can be created from memory (or a file or a resource). This leads to two different types of effects: a global effect that does not depend on state in other effect versus a child effect which depends on state in another effect.

You specify whether an effect is a global effect (the default case) or a child effect (by supplying the [D3D10\_EFFECT\_COMPILE\_CHILD\_EFFECT](d3d10-effect.md) flag) when the effect is created. A global effect can serve as an effect pool; a child effect cannot be an effect pool.

## Related topics

<dl> <dt>

[Rendering an Effect](d3d10-graphics-programming-guide-effects-render.md)
</dt> <dt>

[Effects (Direct3D 10)](d3d10-graphics-programming-guide-effects.md)
</dt> </dl>

 

 



