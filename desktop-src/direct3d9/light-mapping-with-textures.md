---
description: For an application to realistically render a 3D scene, it must take into account the effect that light sources have on the appearance of the scene.
ms.assetid: ff2037e4-2cf6-4247-b93f-13f0078f3b58
title: Light Mapping with Textures (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Light Mapping with Textures (Direct3D 9)

For an application to realistically render a 3D scene, it must take into account the effect that light sources have on the appearance of the scene. Although techniques such as flat and Gouraud shading are valuable tools in this respect, they can be insufficient for your needs. Direct3D supports multipass and multiple texture blending. These capabilities enable your application to render scenes with a more realistic appearance than scenes rendered with shading techniques alone. By applying one or more light maps, your application can map areas of light and shadow onto its primitives.

A light map is a texture or group of textures that contains information about lighting in a 3D scene. You can store the lighting information in the alpha values of the light map, in the color values, or in both.

If you implement light mapping using multipass texture blending, your application should render the light map onto its primitives on the first pass. It should use a second pass to render the base texture. The exception to this is specular light mapping. In that case, render the base texture first; then add the light map.

Multiple texture blending enables your application to render the light map and the base texture in one pass. If the user's hardware provides for multiple texture blending, your application should take advantage of it when performing light mapping. This significantly improves your application's performance.

Using light maps, a Direct3D application can achieve a variety of lighting effects when it renders primitives. It can map not only monochrome and colored lights in a scene, but it can also add details such as specular highlights and diffuse lighting.

Information on using Direct3D texture blending to perform light mapping is presented in the following topics.

-   [Monochrome Light Maps (Direct3D 9)](monochrome-light-maps.md)
-   [Color Light Maps (Direct3D 9)](color-light-maps.md)
-   [Specular Light Maps (Direct3D 9)](specular-light-maps.md)
-   [Diffuse Light Maps (Direct3D 9)](diffuse-light-maps.md)

## Related topics

<dl> <dt>

[Texture Blending](texture-blending.md)
</dt> </dl>

 

 



