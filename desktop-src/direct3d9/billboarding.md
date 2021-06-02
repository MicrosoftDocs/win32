---
description: When creating 3D scenes, an application can sometimes gain performance advantages by rendering 2D objects in a way that makes them appear to be 3D objects. This is the basic idea behind the technique of billboarding.
ms.assetid: 6637a9ce-6731-4f60-8b76-854e86b10bdd
title: Billboarding (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Billboarding (Direct3D 9)

When creating 3D scenes, an application can sometimes gain performance advantages by rendering 2D objects in a way that makes them appear to be 3D objects. This is the basic idea behind the technique of billboarding.

A billboard in the normal sense of the word is a sign along a roadway. Microsoft Direct3D applications can create and render this type of billboard by defining a rectangular solid and applying a texture to it. Billboarding in the more specialized sense of 3D graphics is an extension of this. The goal is to make 2D objects appear to be 3D. The technique is to apply a texture that contains the object's image to a rectangular primitive. The primitive is rotated so that it always faces the user. It doesn't matter if the object's image is not rectangular. Portions of the billboard can be made transparent, so the parts of the billboard image that you don't want seen are not visible.

Many games employ billboarding for animated sprites. For instance, when the user is moving through a 3D maze, he or she may see weapons or rewards that can be picked up. These are typically 2D images textured on a rectangular primitive. Billboarding is often used in games to render images of trees, bushes, and clouds.

When an image is applied to a billboard, the rectangular primitive must first be rotated so that the resulting image faces the user. Your application must then translate it into position. The application can then apply a texture to the primitive.

Billboarding works best for symmetrical objects, especially objects that are symmetrical along the vertical axis. It also requires that the altitude of the viewpoint doesn't increase too much. If the user is allowed to view the billboarded from above, it becomes readily apparent that the object is 2D rather than 3D.

## Related topics

<dl> <dt>

[Alpha Examples](alpha-examples.md)
</dt> </dl>

 

 



