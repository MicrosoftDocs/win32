---
description: The Direct3D Light Model covers ambient, diffuse, specular, and emissive lighting.
ms.assetid: cf870c89-4be0-4b95-92aa-ec7bcdc6d9dd
title: Mathematics of Lighting (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Mathematics of Lighting (Direct3D 9)

The Direct3D Light Model covers ambient, diffuse, specular, and emissive lighting. This is enough flexibility to solve a wide range of lighting situations. You refer to the total amount of light in a scene as the global illumination and compute it using the following equation.


```
Global Illumination = Ambient Light + Diffuse Light + Specular Light + Emissive Light 
```



[Ambient Lighting (Direct3D 9)](ambient-lighting.md) is constant lighting. It is constant in all directions and it colors all pixels of an object the same. It is fast to calculate but leaves objects looking flat and unrealistic. To see how ambient lighting is calculated by Direct3D, see Ambient Lighting (Direct3D 9).

[Diffuse Lighting (Direct3D 9)](diffuse-lighting.md) depends on both the light direction and the object surface normal. It varies across the surface of an object as a result of the changing light direction and the changing surface numeral vector. It takes longer to calculate diffuse lighting because it changes for each object vertex, however the benefit of using it is that it shades objects and gives them three-dimensional (3D) depth. To see how diffuse lighting is calculated in Direct3D, see Diffuse Lighting (Direct3D 9).

[Specular Lighting (Direct3D 9)](specular-lighting.md) identifies the bright specular highlights that occur when light hits an object surface and reflects back toward the camera. It is more intense than diffuse light and falls off more rapidly across the object surface. It takes longer to calculate specular lighting than diffuse lighting, however the benefit of using it is that it adds significant detail to a surface. To see how specular lighting is calculated in Direct3D, see Specular Lighting (Direct3D 9).

[Emissive Lighting (Direct3D 9)](emissive-lighting.md) is light that is emitted by an object; for example, a glow. To see how emissive lighting is calculated in Direct3D, see Emissive Lighting (Direct3D 9).

Realistic lighting can be accomplished by applying each of these types of lighting to a 3D scene. The values calculated for ambient, emissive, and diffuse components are output as the diffuse vertex color; the value for the specular lighting component is output as the specular vertex color. Ambient, diffuse, and specular light values can be affected by a given light's attenuation and spotlight factor. For more information about how attenuation works, see [Attenuation and Spotlight Factor (Direct3D 9)](attenuation-and-spotlight-factor.md).

To achieve a more realistic lighting effect, you add more lights; however, the scene takes longer to render. To achieve all the effects a designer wants, some games use more CPU power than is commonly available. In this case, it is typical to reduce the number of lighting calculations to a minimum by using lighting maps and environment maps to add lighting to a scene while using texture maps.

Lighting is computed in the camera space. To see how lighting transformations are calculated, see [Camera Space Transformations (Direct3D 9)](camera-space-transformations.md). Optimized lighting can be computed in model space, when special conditions exist: normal vectors are already normalized (D3DRS\_NORMALIZENORMALS is True), vertex blending is not needed, transformation matrices are orthogonal, and so forth.

## Related topics

<dl> <dt>

[Lights and Materials](lights-and-materials.md)
</dt> </dl>

 

 



