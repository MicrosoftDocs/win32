---
description: Defines normals for a mesh.
ms.assetid: 05f17128-dfc9-4a78-b23c-0420a1c3d1bd
title: MeshNormals
ms.topic: reference
ms.date: 05/31/2018
---

# MeshNormals

Defines normals for a mesh. The first array of vectors is the normal vectors themselves, and the second array is an array of indexes specifying which normals should be applied to a given face. The value of the nFaceNormals member should be equal to the number of faces in a mesh.

``` syntax
template MeshNormals
{
    < F6F23F43-7686-11cf-8F52-0040333594A3 >
    DWORD nNormals;
    array Vector normals[nNormals];
    DWORD nFaceNormals;
    array MeshFace faceNormals[nFaceNormals];
} 
```

Where:

-   nNormals - Number of normals.
-   array Vector normals\[nNormals\] - Array of normals. See [**Vector**](vector.md).
-   nFaceNormals - Number of face normals.
-   array MeshFace faceNormals\[nFaceNormals\] - Array of mesh face normals. See [**MeshFace**](meshface.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



