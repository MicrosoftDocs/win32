---
description: You can use Microsoft Direct3D to simulate natural phenomena involving energy releases.
ms.assetid: a16af13d-3a38-42b5-900b-ff58a0c917b2
title: Fire, Flares, and Explosions (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Fire, Flares, and Explosions (Direct3D 9)

You can use Microsoft Direct3D to simulate natural phenomena involving energy releases. For instance, an application can generate the appearance of fire by applying flame-like textures to a set of billboards. This is especially effective if the application uses a sequence of fire textures to animate the flames on each billboard in the fire. Varying the speed of the animation playback from billboard to billboard increases the appearance of real flames. The semblance of intermingled 3D flames can be achieved by layering the billboards and the textures on the billboards.

You can simulate flares and flashes by applying successively brighter light maps to all primitives in a scene. Although this is a computationally high-overhead technique, it allows your application to simulate a localized flare or flash. That is, the portion of the scene where the flare or flash originates can brighten first.

Another technique is to position a billboard in front of the scene so that the entire render-target area is covered. The application applies successively whiter textures to the billboard and decreases the transparency over time. The entire scene fades to white as time passes. This is a low overhead method of creating a flare. However, using this technique, it can be difficult to generate the appearance of a bright flash from a single point light source.

Explosions can be displayed in a 3D scene procedure similar to those used for fire, flashes, and flares. For instance, your application might use a billboard to display a shock wave and rising plume of smoke when the explosion occurs. At the same time, your application can use a set of billboards to simulate flames. In addition, it can position a single billboard in front of the scene to add a flare of light to the entire scene.

Energy beams can be simulated using billboards. Your application can also display them using primitives that are defined as line lists or line strips. For details, see [Line Lists](line-lists.md) and [Line Strips](line-strips.md).

Your application can create force fields using billboards or primitives defined as triangle lists. To create a force field from triangle lists, define a set of disjoint triangles in a triangle list equally spaced over the region covered by the force field. The gaps between the triangles allow the user to see the scene behind the triangles, as you might expect when looking at a force field. Apply a texture to the triangle list that gives the triangles the appearance of glowing with energy. For further information, see [Triangle Lists](triangle-lists.md).

## Related topics

<dl> <dt>

[Alpha Examples](alpha-examples.md)
</dt> </dl>

 

 



