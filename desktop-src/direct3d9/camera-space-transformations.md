---
description: Vertices in the camera space are computed by transforming the object vertices with the world view matrix.
ms.assetid: 889dd0d8-1933-4901-9bbc-06c3caa26d3e
title: Camera Space Transformations (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Camera Space Transformations (Direct3D 9)

Vertices in the camera space are computed by transforming the object vertices with the world view matrix.

V = V \* wvMatrix

Vertex normals, in camera space, are computed by transforming the object normals with the inverse transpose of the world view matrix. The world view matrix may or may not be orthogonal.

N = N \* (wvMatrix⁻¹)<sup>T</sup>

The matrix inversion and matrix transpose operate on a 4x4 matrix. The multiply combines the normal with the 3x3 portion of the resulting 4x4 matrix.

If the render state, D3DRENDERSTATE\_NORMALIZENORMALS is set to **TRUE**, vertex normal vectors are normalized after transformation to camera space as follows:

N = norm(N)

Light position in camera space is computed by transforming the light source position with the view matrix.

Lₚ = Lₚ \* vMatrix

The direction to the light in camera space for a directional light is computed by multiplying the light source direction by the view matrix, normalizing, and negating the result.

L<sub>dir</sub> = -norm(L<sub>dir</sub> \* wvMatrix)

For the D3DLIGHT\_POINT and D3DLIGHT\_SPOT the direction to light is computed as follows:

L<sub>dir</sub> = norm(V \* Lₚ), where the parameters are defined in the following table.



| Parameter       | Default value | Type      | Description                                               |
|-----------------|---------------|-----------|-----------------------------------------------------------|
| L<sub>dir</sub> | N/A           | D3DVECTOR | Direction vector from object vertex to the light          |
| V               | N/A           | D3DVECTOR | Vertex position in camera space                           |
| wvMatrix        | Identity      | D3DMATRIX | Composite matrix containing the world and view transforms |
| N               | N/A           | D3DVECTOR | Vertex normal                                             |
| Lₚ              | N/A           | D3DVECTOR | Light position in camera space                            |
| vMatrix         | Identity      | D3DMATRIX | Matrix containing the view transform                      |



 

## Related topics

<dl> <dt>

[Mathematics of Lighting](mathematics-of-lighting.md)
</dt> </dl>

 

 



