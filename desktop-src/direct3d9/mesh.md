---
description: Defines a simple mesh. The first array is a list of vertices, and the second array defines the faces of the mesh by indexing into the vertex array.
ms.assetid: 'vs|directx_sdk|~\mesh.htm'
title: Mesh
ms.topic: article
ms.date: 05/31/2018
---

# Mesh

Defines a simple mesh. The first array is a list of vertices, and the second array defines the faces of the mesh by indexing into the vertex array.

``` syntax
template Mesh
{
    <3D82AB44-62DA-11CF-AB39-0020AF71E433>
    DWORD nVertices;
    array Vector vertices[nVertices];
    DWORD nFaces;
    array MeshFace faces[nFaces];
    [...]
}
```

Where:

-   nVertices - Number of vertices.
-   array Vector vertices\[nVertices\] - Array of vertices, each of type Vector. See [**Vector**](vector.md).
-   nFaces - Number of faces.
-   array MeshFace faces\[nFaces\] - Array of faces, each of type MeshFace. See [**MeshFace**](meshface.md).
-   \[ ... \] - Any .x file template can be used here. This makes the architecture extensible. [**Material**](material.md) and [**TextureFilename**](texturefilename.md) templates are typically used.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



