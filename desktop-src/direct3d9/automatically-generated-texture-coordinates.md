---
title: Auto-generated texture coordinates (Direct3D 9)
description: The system can use the transformed camera-space position or the normal from a vertex as texture coordinates, or it can compute the three element vectors used to address a cubic environment map.
ms.topic: article
ms.date: 05/31/2018
---

# Auto-generated texture coordinates (Direct3D 9)

The system can use the transformed camera-space position or the normal from a vertex as texture coordinates, or it can compute the three element vectors used to address a cubic environment map. Like texture coordinates that you explicitly specify in a vertex, you can use automatically generated texture coordinates as input for texture coordinate transformations.

Automatically generated texture coordinates can significantly reduce the bandwidth required for geometry data by eliminating the need for explicit texture coordinates in the vertex format. In many cases, the texture coordinates that the system generates can be used with transformations to produce special effects. Of course, this is a special-purpose feature, and you will use explicit texture coordinates for many occasions.

## Configuring Automatically Generated Texture Coordinates

In C++, the D3DTSS\_TEXCOORDINDEX texture-stage state (from the [**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md) enumerated type) controls how the system generates texture coordinates.

Normally, this state instructs the system to use a particular set of texture coordinates encoded in the vertex format. When you include the D3DTSS\_TCI\_CAMERASPACENORMAL, D3DTSS\_TCI\_CAMERASPACEPOSITION, or D3DTSS\_TCI\_CAMERASPACEREFLECTIONVECTOR flags in the value that you assign to this state, the system behavior is quite different. If any of these flags are present, the texture stage ignores the texture coordinates within the vertex format in favor of coordinates that the system generates. The meanings for each flag are shown in the following list.

-   D3DTSS\_TCI\_CAMERASPACENORMAL

    Use the vertex normal, transformed to camera space, as input texture coordinates.

-   D3DTSS\_TCI\_CAMERASPACEPOSITION

    Use the vertex position, transformed to camera space, as input texture coordinates.

-   D3DTSS\_TCI\_CAMERASPACEREFLECTIONVECTOR

    Use the reflection vector, transformed to camera space, as input texture coordinates. The reflection vector is computed from the input vertex position and normal vector.

The texture coordinate index flags are mutually exclusive. This example uses:

-   The vertex position (in camera-space) as the input texture coordinates for this texture stage
-   The wrap mode set in the D3DRENDERSTATE\_WRAP1 render state


```
// Assume d3dDevice is a valid pointer to an IDirect3DDevice9 interface
d3dDevice->SetTextureStageState(0, D3DTSS_TEXCOORDINDEX, 
                                   D3DTSS_TCI_CAMERASPACEPOSITION | 1);
```



Automatically generated texture coordinates are most useful as input values for a texture coordinate transformation, or to eliminate the need for your application to compute three-element vectors for cubic-environment maps.

Sphere-mapping uses a precomputed (at model time) texture map that contains the entire environment as reflected by a chrome sphere. Direct3D has a texture-coordinate generation feature using render state D3DTSS\_TCI\_CAMERASPACENORMAL, which takes the normal of the vertex in camera space and puts it through a texture transform to generate texture coordinates.

## Related topics

<dl> <dt>

[Texture Coordinate Processing](texture-coordinate-processing.md)
</dt> <dt>

[Texture Coordinate Transformations (Direct3D 9)](texture-coordinate-transformations.md)
</dt> <dt>

[Cubic Environment Mapping (Direct3D 9)](cubic-environment-mapping.md)
</dt> </dl>

 

 
