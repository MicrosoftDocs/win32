---
description: To fully understand a shader that implements PRT, it is useful to derive the formula the shader uses to calculate exit radiance.
ms.assetid: 66876e9e-cde1-4d04-9b31-30be1c115e6b
title: PRT Equations (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# PRT Equations (Direct3D 9)

To fully understand a shader that implements PRT, it is useful to derive the formula the shader uses to calculate exit radiance.

To start off, the following equation is the general equation to calculate exit radiance resulting from direct lighting on a diffuse object with arbitrary distant lighting.

![equation of the exit radiance resulting from direct lighting on a diffuse object with arbitrary distant lighting](images/prt-theory-eq1.png)

where:



| Parameter     | Description                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------|
| Rₚ            | The exit radiance at vertex p. Evaluated at every vertex on the mesh.                                   |
| p<sub>d</sub> | The albedo of the surface.                                                                              |
| pi            | A constant, used as an energy conservation normalization factor.                                        |
| L(s)          | The lighting environment (source radiance).                                                             |
| Vₚ₍ₛ₎         | A binary visibility function for point p. It is 1 if the point can see the light, 0 if not.             |
| Hₙₚ₍ₛ₎        | The cosine term from Lambert's law. Equal to max((Nₚ· s), 0) where Nₚ is the surface normal at point p. |
| s             | The variable that integrates over the sphere.                                                           |



 

Using spherical basis functions, such as spherical harmonics, the following equation approximates the lighting environment.

![equation of the lighting environment](images/prt-theory-eq2.png)

where:



| Parameter        | Description                                              |
|------------------|----------------------------------------------------------|
| L(s)             | The lighting environment (source radiance).              |
| i                | An integer that sums over the number of basis functions. |
| O                | The order of spherical harmonics.                        |
| l<sub>i</sub>    | A coefficient.                                           |
| Y<sub>i(s)</sub> | Some basis function over the sphere.                     |



 

The collection of these coefficients, L', provides the optimal approximation for function L(s) with the basis functions Y(s). Substituting and distributing yields the following equation.

![equation of the exit radiance after substituting l(s) and distributing](images/prt-theory-eq3.png)

The integral of Y<sub>i(s)</sub>Vₚ₍ₛ₎Hₙₚ₍ₛ₎ is a transfer coefficient t<sub>pi</sub> that the simulator precomputes for every vertex on the mesh. Substituting this yields the following equation.

![equation of the exit radiance after substituting the transfer coefficient](images/prt-theory-eq4.png)

Changing this to vector notation yields the following uncompressed equation to calculate exit radiance for each channel.

![equation of the exit radiance after changing to vector notation](images/prt-theory-eq5.png)

where:



| Parameter     | Description                                                                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rₚ            | The exit radiance at vertex p.                                                                                                                                                      |
| p<sub>d</sub> | The albedo of the surface.                                                                                                                                                          |
| L'            | The vector of l<sub>i</sub>, and is the projection of the source radiance into the spherical harmonic basis functions. This is an order² vector of spherical harmonic coefficients. |
| Tₚ            | An order² transfer vector for vertex p. The simulator divides the transfer coefficients by p.                                                                                       |



 

Both of these vectors are an order² vector of spherical harmonic coefficients, so notice that this is simply a dot product. Depending on the order, the dot can be expensive so compression can be used. An algorithm called Clustered Principal Component Analysis (CPCA) efficiently compresses the data. This enables the use of a higher-order spherical harmonic approximation which results in sharper shadows.

CPCA provides the following equation to approximate the transfer vector.

![equation of the approximated transfer vector](images/prt-theory-eq6.png)

where:



| Parameter      | Description                                          |
|----------------|------------------------------------------------------|
| Tₚ             | The transfer vector for vertex p.                    |
| Mₖ             | The mean for cluster k.                              |
| j              | An integer that sums over the number of PCA vectors. |
| N              | The number of PCA vectors.                           |
| w<sub>pj</sub> | The jth PCA weight for point p.                      |
| B<sub>kj</sub> | The jth PCA basis vector for cluster k.              |



 

A cluster is simply some number of vertices that share the same mean vector. How to get the cluster mean, the PCA weights, the PCA basis vectors, and the cluster ids for the vertices is discussed below.

Substituting these two equations yields:

![equation of the exit radiance after substituting the transfer vector](images/prt-theory-eq7.png)

Then distributing the dot product yields the following equation.

![equation of the exit radiance after distributing the dot product](images/prt-theory-eq8.png)

Because both (Mₖ· L') and (B<sub>kj</sub>· L') are constant per vertex, the sample calculates these values with the CPU and passes them as constants into the vertex shader; because w<sub>pj</sub> changes for each vertex, the sample stores this per-vertex data in the vertex buffer.

## Related topics

<dl> <dt>

[Precomputed Radiance Transfer](precomputed-radiance-transfer.md)
</dt> </dl>

 

 



