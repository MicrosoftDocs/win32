---
description: VertexDuplicationIndices - This template is instantiated on a per-mesh basis, holding information about which vertices in the mesh are duplicates of each other.
ms.assetid: 43417389-69c1-4af6-92c2-75b621f9c165
title: VertexDuplicationIndices
ms.topic: reference
ms.date: 05/31/2018
---

# VertexDuplicationIndices

This template is instantiated on a per-mesh basis, holding information about which vertices in the mesh are duplicates of each other. Duplicates result when a vertex sits on a smoothing group or material boundary. The purpose of this template is to allow the loader to determine which vertices exhibiting different peripheral parameters are actually the same vertexes in the model. Certain applications (mesh simplification, for example) can make use of this information.

``` syntax
template VertexDuplicationIndices 
{ 
    < B8D65549-D7C9-4995-89CF-53A9A8B031E3 > 
    DWORD nIndices; 
    DWORD nOriginalVertices; 
    array DWORD indices[nIndices]; 
}
```

Where:

-   nIndices - Number of vertex indices. This is the number of vertices in the mesh.
-   nOriginalVertices - Number of vertices in the mesh before any duplication occurs.
-   The value indices\[n\] holds the vertex index that vertex\[n\] in the vertex array for the mesh would have had if no duplication had occurred. Indices in this array that are the same, therefore, indicate duplicate vertices.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



