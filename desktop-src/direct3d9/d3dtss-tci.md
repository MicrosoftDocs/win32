---
description: Driver texture coordinate capability flags.
ms.assetid: b15509b4-7db1-429a-9468-be7a11dee505
title: D3DTSS_TCI
ms.topic: article
ms.date: 05/31/2018
---

# D3DTSS\_TCI

Driver texture coordinate capability flags.



| \#define                                 | Value       | Description                                                                                                                                                                                                          |
|------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DTSS\_TCI\_PASSTHRU                    | 0x00000000L | Use the specified texture coordinates contained within the vertex format. This value resolves to zero.                                                                                                               |
| D3DTSS\_TCI\_CAMERASPACENORMAL           | 0x00010000L | Use the vertex normal, transformed to camera space, as the input texture coordinates for this stage's texture transformation.                                                                                        |
| D3DTSS\_TCI\_CAMERASPACEPOSITION         | 0x00020000L | Use the vertex position, transformed to camera space, as the input texture coordinates for this stage's texture transformation.                                                                                      |
| D3DTSS\_TCI\_CAMERASPACEREFLECTIONVECTOR | 0x00030000L | Use the reflection vector, transformed to camera space, as the input texture coordinate for this stage's texture transformation. The reflection vector is computed from the input vertex position and normal vector. |
| D3DTSS\_TCI\_SPHEREMAP                   | 0x00040000L | Use the specified texture coordinates for sphere mapping.                                                                                                                                                            |



 

These constants are used by D3DTSS\_TEXCOORDINDEX.

## Constant Information



|  Requirement                        | Value           |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 



