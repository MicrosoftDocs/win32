---
description: Used by the Mesh template to define a mesh's faces. Each element of the nFaceVertexIndices array references a mesh vertex used to build the face.
ms.assetid: 38c40ebe-eca2-4dd9-95b8-b396225e3050
title: MeshFace
ms.topic: reference
ms.date: 05/31/2018
---

# MeshFace

Used by the [**Mesh**](mesh.md) template to define a mesh's faces. Each element of the nFaceVertexIndices array references a mesh vertex used to build the face.

``` syntax
template MeshFace
{
    < 3D82AB5F-62DA-11cf-AB39-0020AF71E433 >
    DWORD nFaceVertexIndices;
    array DWORD faceVertexIndices[nFaceVertexIndices];
} 
```

Where:

-   nFaceVertexIndices - Number of indices.
-   array DWORD faceVertexIndices\[nFaceVertexIndices\] - Array of indices.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



