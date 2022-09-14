---
description: PatchMesh defines a mesh defined by Bézier patches, including a list of vertices and the patches for the mesh by indexing into the vertex array.
ms.assetid: 'vs|directx_sdk|~\patchmesh.htm'
title: PatchMesh
ms.topic: article
ms.date: 05/31/2018
---

# PatchMesh

Defines a mesh defined by Bézier patches. The first array is a list of vertices, and the second array defines the patches for the mesh by indexing into the vertex array.

``` syntax
template PatchMesh
{
    < D02C95CC-EDBA-4305-9B5D-1820D7704BBF >
    DWORD nVertices;
    array Vector vertices[nVertices];
    DWORD nPatches;
    array Patch patches[nPatches];
    [ ... ]
}
```

Where:

-   nVertices - Number of vertices.
-   vertices\[nVertices\] - Array of vertices. See [**Vector**](vector.md).
-   nPatches - Number of patches.
-   patches\[nPatches\] - Array of patches. See [**Patch**](patch.md).
-   \[ ... \] - Any .x file template can be used here. This makes the architecture extensible.

The patches use the vertices in the array of vertices as the control points for each patch. This is a legacy template. The latest patch mesh template is [**PatchMesh9**](patchmesh9.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



