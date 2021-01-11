---
description: Lights are used to illuminate objects in a scene.
ms.assetid: 0751bb76-611a-41c4-aab2-aa6f68b61b0e
title: Lights and Materials (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Lights and Materials (Direct3D 9)

Lights are used to illuminate objects in a scene. When lighting is enabled, Direct3D calculates the color of each object vertex based on a combination of:

> [!Note]  
> This section is only for the fixed-function pipeline. Programmable shaders perform all lighting explicitly.

 

-   The current material color and the texels in an associated texture map.
-   The diffuse and specular colors at the vertex, if specified.
-   The color and intensity of light produced by light sources in the scene or the scene's ambient light level.

When you use Direct3D lighting and materials, you allow Direct3D to handle the details of illumination for you. Advanced users can perform lighting on their own, if desired.

How you work with lighting and materials makes a big difference in the appearance of the rendered scene. Materials define how light reflects off a surface. Direct light and ambient light levels define the light that is reflected. You must use materials to render a scene if lighting is enabled. Lights are not required to render a scene, but details in a scene rendered without light are not visible. At best, rendering an unlit scene results in a silhouette of the objects in the scene. This is not enough detail for most purposes.

## Direct Light vs. Ambient Light

Although both direct and ambient light illuminate objects in a scene, they are independent of one another, they have very different effects, and they require that you work with them in completely different ways.

Direct light is just that: direct. Direct light always has direction and color, and it is a factor for shading algorithms, such as Gouraud shading. Different types of lights emit direct light in different ways, creating special attenuation effects. You create a set of light parameters for direct light by calling the [**IDirect3DDevice9::SetLight**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setlight) method.

Ambient light is effectively everywhere in a scene. You can think of it as a general level of light that fills an entire scene, regardless of the objects and their locations in that scene. Ambient light has no position or direction, only color and intensity. Each light adds to the overall ambient light in a scene. Set the ambient light level with a call to the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method, specifying D3DRS\_AMBIENT as the *State* parameter, and the desired RGBA color as the Value parameter.

Ambient light color takes the form of an RGBA value, where each component is an integer value from 0 to 255. This is unlike most color values in Direct3D.

You can use the [**D3DCOLOR\_RGBA**](d3dcolor-rgba.md) macro to generate RGBA values. The red, green, and blue components combine to make the final color of the ambient light. The alpha component controls the transparency of the color. When using hardware acceleration or RGB emulation, the alpha component is ignored.

## Direct3D Light Model vs. Nature

In nature, when light is emitted from a source, it is reflected off of hundreds, if not thousands or millions of objects before reaching the user's eye. Each time it is reflected, some light is absorbed by a surface, some is scattered in random directions, and the rest goes on to another surface or to the user's eye. This process continues until the light is reduced to nothing or a user perceives the light.

Obviously, the calculations required to perfectly simulate the natural behavior of light are too time-consuming to use for real-time Direct3D graphics. Therefore, with speed in mind, the Direct3D light model approximates the way light works in the natural world. Direct3D describes light in terms of red, green, and blue components that combine to create a final color.

In Direct3D, when light reflects off a surface, the light color interacts mathematically with the surface itself to create the color eventually displayed on the screen. For specific information about the algorithms Direct3D uses, see [Mathematics of Lighting (Direct3D 9)](mathematics-of-lighting.md).

The Direct3D light model generalizes light into two types: ambient light and direct light. Each has different attributes, and each interacts with the material of a surface in different ways. Ambient light is light that has been scattered so much that its direction and source are indeterminate: it maintains a low level of intensity everywhere. The indirect lighting used by photographers is a good example of ambient light. Ambient light in Direct3D, as in nature, has no real direction or source, only a color and intensity. In fact, the ambient light level is completely independent of any objects in a scene that generate light. Ambient light does not contribute to specular reflection.

Direct light is the light generated by a source within a scene; it always has color and intensity, and it travels in a specified direction. Direct light interacts with the material of a surface to create specular highlights, and its direction is used as a factor in shading algorithms, including Gouraud shading. When direct light is reflected, it does not contribute to the ambient light level in a scene. The sources in a scene that generate direct light have different characteristics that affect how they illuminate a scene.

Additionally, a polygon's material has properties that affect how that polygon reflects the light it receives. You set a single reflectance trait that describes how the material reflects ambient light, and you set individual traits to determine the material's specular and diffuse reflectance. For more information, see [Materials (Direct3D 9)](materials.md).

## Color Values for Lights and Materials

Direct3D describes color in terms of four components-red, green, blue, and alpha-that combine to make a final color. The [**D3DCOLORVALUE**](d3dcolorvalue.md) C++ structure is defined to contain values for each component. Each member is a floating-point value that typically ranges from 0.0 to 1.0, inclusive. Although both lights and materials use the same structure to describe color, the values in the structure are used a little differently by each.

Color values for light sources represent the amount of a particular light component it emits. Because lights don't use an alpha component, only the red, green, and blue components of the color are relevant. You can visualize the three components as the red, green, and blue lenses on a projection television. Each lens might be off (a 0.0 value in the appropriate member), it might be as bright as possible (a 1.0 value), or it might be some level in between. The colors coming through the lenses combine to make the light's final color. A combination like R(1.0), G(1.0), B(1.0) creates a white light, where R(0.0), G(0.0), B(0.0) doesn't emit light at all. You can make a light that emits only one component, resulting in a pure red, green, or blue light; or, the light could use combinations to emit colors like yellow or purple. You can even set negative color component values to create a "dark light" that actually removes light from a scene. Or, you might set the components to some value larger than 1.0 to create an extremely bright light.

With materials, on the other hand, color values represent how much of a light component is reflected by a surface that is rendered with that material. A material whose color components are R(1.0), G(1.0), B(1.0), A(1.0) reflects all the light that comes its way. Likewise, a material with R(0.0), G(1.0), B(0.0), A(1.0) reflects all the green light that is directed at it. Materials have multiple reflectance values to create various types of effects.

Additional information is contained in: [Light Types (Direct3D 9)](light-types.md), and [Light Properties (Direct3D 9)](light-properties.md).

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> </dl>

 

 
