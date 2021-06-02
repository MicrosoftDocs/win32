---
description: Modeling specular reflection requires that the system not only know in what direction light is traveling, but also the direction to the viewer's eye.
ms.assetid: 35da0ac3-4e68-4d37-a987-405fc15d0cbf
title: Specular Lighting (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Specular Lighting (Direct3D 9)

Modeling specular reflection requires that the system not only know in what direction light is traveling, but also the direction to the viewer's eye. The system uses a simplified version of the Phong specular-reflection model, which employs a halfway vector to approximate the intensity of specular reflection.

The default lighting state does not calculate specular highlights. To enable specular lighting, be sure to set D3DRS\_SPECULARENABLE to **TRUE**.

## Specular Lighting Equation

Specular Lighting is described by the following equation:

**Specular Lighting = Cₛ \* sum\[Lₛ \* (N · H)<sup>P</sup> \* Atten \* Spot\]**



 

The following table identifies the variables, their types, and their ranges.



| Parameter    | Default value | Type          | Description                                                                                                         |
|--------------|---------------|---------------|---------------------------------------------------------------------------------------------------------------------|
| Cₛ           | (0,0,0,0)     | D3DCOLORVALUE | Specular color.                                                                                                     |
| sum          | N/A           | N/A           | Summation of each light's specular component.                                                                       |
| N            | N/A           | D3DVECTOR     | Vertex normal.                                                                                                      |
| H            | N/A           | D3DVECTOR     | Half way vector. See the section on the halfway vector.                                                             |
| <sup>P</sup> | 0.0           | FLOAT         | Specular reflection power. Range is 0 to +infinity                                                                  |
| Lₛ           | (0,0,0,0)     | D3DCOLORVALUE | Light specular color.                                                                                               |
| Atten        | N/A           | FLOAT         | Light attenuation value. See [Attenuation and Spotlight Factor (Direct3D 9)](attenuation-and-spotlight-factor.md). |
| Spot         | N/A           | FLOAT         | Spotlight factor. See [Attenuation and Spotlight Factor (Direct3D 9)](attenuation-and-spotlight-factor.md).        |



 

The value for Cₛ is either:


```
if(SPECULARMATERIALSOURCE == D3DMCS_COLOR1)
  C = color1;
```



-   vertex color1, if the specular material source is D3DMCS\_COLOR1, and the first vertex color is supplied in the vertex declaration.
-   vertex color2, if specular material source is D3DMCS\_COLOR2, and the second vertex color is supplied in the vertex declaration.
-   material specular color

> [!Note]  
> If either specular material source option is used and the vertex color is not provided, then the material specular color is used.

 

Specular components are clamped to be from 0 to 255, after all lights are processed and interpolated separately.

## The Halfway Vector

The halfway vector (H) exists midway between two vectors: the vector from an object vertex to the light source, and the vector from an object vertex to the camera position. Direct3D provides two ways to compute the halfway vector. When D3DRS\_LOCALVIEWER is set to **TRUE**, the system calculates the halfway vector using the position of the camera and the position of the vertex, along with the light's direction vector. The following formula illustrates this.

**H = norm(norm(Cₚ - Vₚ) + L<sub>dir</sub>)**



 



| Parameter       | Default value | Type      | Description                                                  |
|-----------------|---------------|-----------|--------------------------------------------------------------|
| Cₚ              | N/A           | D3DVECTOR | Camera position.                                             |
| Vₚ              | N/A           | D3DVECTOR | Vertex position.                                             |
| L<sub>dir</sub> | N/A           | D3DVECTOR | Direction vector from vertex position to the light position. |



 

Determining the halfway vector in this manner can be computationally intensive. As an alternative, setting D3DRS\_LOCALVIEWER = **FALSE** instructs the system to act as though the viewpoint is infinitely distant on the z-axis. This is reflected in the following formula.

**H = norm((0,0,1) + L<sub>dir</sub>)**



 

This setting is less computationally intensive, but much less accurate, so it is best used by applications that use orthogonal projection.

## Example

In this example, the object is colored using the scene specular light color and a material specular color. The code is shown below.


```
D3DMATERIAL9 mtrl;
ZeroMemory( &mtrl, sizeof(mtrl) );

D3DLIGHT9 light;
ZeroMemory( &light, sizeof(light) );
light.Type = D3DLIGHT_DIRECTIONAL;

D3DXVECTOR3 vecDir;
vecDir = D3DXVECTOR3(0.5f, 0.0f, -0.5f);
D3DXVec3Normalize( (D3DXVECTOR3*)&light.Direction, &vecDir );

light.Specular.r = 1.0f;
light.Specular.g = 1.0f;
light.Specular.b = 1.0f;
light.Specular.a = 1.0f;

light.Range = 1000;
light.Falloff = 0;
light.Attenuation0 = 1;
light.Attenuation1 = 0;
light.Attenuation2 = 0;
m_pd3dDevice->SetLight( 0, &light );
m_pd3dDevice->LightEnable( 0, TRUE );
m_pd3dDevice->SetRenderState( D3DRS_SPECULARENABLE, TRUE );

mtrl.Specular.r = 0.5f;
mtrl.Specular.g = 0.5f;
mtrl.Specular.b = 0.5f;
mtrl.Specular.a = 0.5f;
mtrl.Power = 20;
m_pd3dDevice->SetMaterial( &mtrl );
m_pd3dDevice->SetRenderState(D3DRS_SPECULARMATERIALSOURCE, D3DMCS_MATERIAL);
```



According to the equation, the resulting color for the object vertices is a combination of the material color and the light color.

The following two illustration show the specular material color, which is gray, and the specular light color, which is white.

![illustration of a gray sphere](images/amb1.jpg)![illustration of a white sphere](images/lightwhite.jpg)

The resulting specular highlight is shown in the following illustration.

![illustration of the specular highlight](images/lights.jpg)

Combining the specular highlight with the ambient and diffuse lighting produces the following illustration. With all three types of lighting applied, this more clearly resembles a realistic object.

![illustration of combining the specular highlight, ambient lighting, and diffuse lighting](images/lightads.jpg)

Specular lighting is more intensive to calculate than diffuse lighting. It is typically used to provide visual clues about the surface material. The specular highlight varies in size and color with the material of the surface.

## Related topics

<dl> <dt>

[Mathematics of Lighting](mathematics-of-lighting.md)
</dt> </dl>

 

 



