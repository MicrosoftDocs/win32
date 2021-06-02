---
description: Light properties describe a light source's type and color.
ms.assetid: b39f1287-c67b-4cbb-b599-4a1b2f4981ac
title: Light Properties (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Light Properties (Direct3D 9)

Light properties describe a light source's type and color. Depending on the type of light being used, a light can have properties for attenuation and range, or for spotlight effects. But, not all types of lights use all properties. Direct3D uses the [**D3DLIGHT9**](d3dlight9.md) structure to carry information about light properties for all types of light sources. This section contains information for all light properties. Information is divided into the following groups.

The position, range, and attenuation properties define a light's location in world space and how the light it emits behaves over distance. As with all light properties you use in C++, these are contained in a light's [**D3DLIGHT9**](d3dlight9.md) structure.

-   [Light Attenuation](#light-attenuation)
-   [Light Color](#light-color)
-   [Light Direction](#light-direction)
-   [Light Position](#light-position)
-   [Light Range](#light-range)

## Light Attenuation

Attenuation controls how a light's intensity decreases toward the maximum distance specified by the range property. Three [**D3DLIGHT9**](d3dlight9.md) structure members represent light attenuation: Attenuation0, Attenuation1, and Attenuation2. These members contain floating-point values ranging from 0.0 through infinity, controlling a light's attenuation. Some applications set the Attenuation1 member to 1.0 and the others to 0.0, resulting in light intensity that changes as 1 / D, where D is the distance from the light source to the vertex. The maximum light intensity is at the source, decreasing to 1 / (Light Range) at the light's range. Typically, an application sets Attenuation0 to 0.0, Attenuation1 to a constant value, and Attenuation2 to 0.0.

You can combine attenuation values to get more complex attenuation effects. Or, you might set them to values outside the normal range to create even stranger attenuation effects. Negative attenuation values, however, are not allowed. See [Attenuation and Spotlight Factor (Direct3D 9)](attenuation-and-spotlight-factor.md).

## Light Color

Lights in Direct3D emit three colors that are used independently in the system's lighting computations: a diffuse color, an ambient color, and a specular color. Each is incorporated by the Direct3D lighting module, interacting with a counterpart from the current material, to produce a final color used in rendering. The diffuse color interacts with the diffuse reflectance property of the current material, the specular color with the material's specular reflectance property, and so on. For specifics about how Direct3D applies these colors, see [Mathematics of Lighting (Direct3D 9)](mathematics-of-lighting.md).

In a C++ application, the [**D3DLIGHT9**](d3dlight9.md) structure includes three members for these colors - Diffuse, Ambient, and Specular - each one is a [**D3DCOLORVALUE**](d3dcolorvalue.md) structure that defines the color being emitted.

The type of color that applies most heavily to the system's computations is the diffuse color. The most common diffuse color is white (R:1.0 G:1.0 B:1.0), but you can create colors as needed to achieve desired effects. For example, you could use red light for a fireplace, or you could use green light for a traffic signal set to "Go."

Generally, you set the light color components to values between 0.0 and 1.0, inclusive, but this isn't a requirement. For example, you might set all the components to 2.0, creating a light that is "brighter than white." This type of setting can be especially useful when you use attenuation settings other than constant.

Note that although Direct3D uses RGBA values for lights, the alpha color component is not used.

Usually material colors are used for lighting. However, you can specify that material colors-emissive, ambient, diffuse, and specular-are to be overridden by diffuse or specular vertex colors. This is done by calling [**SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) and setting the device state variables listed in the following table.



| Device state variable         | Meaning                                       | Type                   | Default          |
|-------------------------------|-----------------------------------------------|------------------------|------------------|
| D3DRS\_AMBIENTMATERIALSOURCE  | Defines where to get ambient material color.  | D3DMATERIALCOLORSOURCE | D3DMCS\_MATERIAL |
| D3DRS\_DIFFUSEMATERIALSOURCE  | Defines where to get diffuse material color.  | D3DMATERIALCOLORSOURCE | D3DMCS\_COLOR1   |
| D3DRS\_SPECULARMATERIALSOURCE | Defines where to get specular material color. | D3DMATERIALCOLORSOURCE | D3DMCS\_COLOR2   |
| D3DRS\_EMISSIVEMATERIALSOURCE | Defines where to get emissive material color. | D3DMATERIALCOLORSOURCE | D3DMCS\_MATERIAL |
| D3DRS\_COLORVERTEX            | Disables or enables use of vertex colors.     | BOOL                   | TRUE             |



 

The alpha/transparency value always comes only from the diffuse color's alpha channel.

The fog value always comes only from the specular color's alpha channel.

D3DMATERIALCOLORSOURCE can have the following values.

-   D3DMCS\_MATERIAL - Material color is used as source.
-   D3DMCS\_COLOR1 - Diffuse vertex color is used as source.
-   D3DMCS\_COLOR2 - Specular vertex color is used as source.

## Light Direction

A light's direction property determines the direction that the light emitted by the object travels, in world space. Direction is used only by directional lights and spotlights, and is described with a vector.

Set the light direction in the Direction member of the light's [**D3DLIGHT9**](d3dlight9.md) structure. Direction member is of type [**D3DVECTOR**](d3dvector.md). Direction vectors are described as distances from a logical origin, regardless of the light's position in a scene. Therefore, a spotlight that points straight into a scene - along the positive z-axis - has a direction vector of <0,0,1> no matter where its position is defined to be. Similarly, you can simulate sunlight shining directly on a scene by using a directional light whose direction is <0,-1,0>. Obviously, you don't have to create lights that shine along the coordinate axes; you can mix and match values to create lights that shine at more interesting angles.

> [!Note]  
> Although you don't need to normalize a light's direction vector, always be sure that it has magnitude. In other words, don't use a <0,0,0> direction vector.

 

## Light Position

Light position is described using a [**D3DVECTOR**](d3dvector.md) structure in the Position member of the [**D3DLIGHT9**](d3dlight9.md) structure. The x-, y-, and z-coordinates are assumed to be in world space. Directional lights are the only type of light that don't use the position property.

## Light Range

A light's range property determines the distance, in world space, at which meshes in a scene no longer receive light emitted by that object. The Range member contains a floating-point value that represents the light's maximum range, in world space. Directional lights don't use the range property.

## Related topics

<dl> <dt>

[Lights and Materials](lights-and-materials.md)
</dt> </dl>

 

 
