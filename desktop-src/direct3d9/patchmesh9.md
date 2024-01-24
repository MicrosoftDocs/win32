---
description: PatchMesh9 defines a mesh defined by Bézier patches, including a list of vertices and the patches for the mesh by indexing into the vertex array.
ms.assetid: 642ca513-c83e-4c6d-845c-0eaecc232728
title: PatchMesh9
ms.topic: reference
ms.date: 05/31/2018
---

# PatchMesh9

Defines a mesh defined by Bézier patches. The first array is a list of vertices, and the second array defines the patches for the mesh by indexing into the vertex array.

``` syntax
template PatchMesh9
{
    < B9EC94E1-B9A6-4251-BA18-94893F02C0EA >
    DWORD Type;
    DWORD Degree;
    DWORD Basis;
    DWORD nVertices;
    array Vector vertices[nVertices];
    DWORD nPatches;
    array Patch patches[nPatches];
    [ ... ]
} 
```

Where:

-   Type - Patch mesh type: rectangle, triangle, or N-patch.
-   Degree - Degree of the variables in the curve equation.
-   Basis - Basis type of a high-order patch surface.
-   nVertices - Number of vertices.
-   vertices\[nVertices\] - Array of vertices. See [**Vector**](vector.md).
-   nPatches - Number of patches.
-   patches\[nPatches\] - Array of patches. See [**Patch**](patch.md).
-   \[ ... \] - Any .x file template can be used here. This makes the architecture extensible.

The patches use the vertices in the array of vertices as the control points for each patch.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



