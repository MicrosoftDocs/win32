---
description: FaceAdjacency - This template is instantiated on a per-mesh basis, holding information about which vertices in the mesh are duplicates of each other.
ms.assetid: dd30b3d6-767a-4d87-9b5c-1324738bcbb2
title: FaceAdjacency
ms.topic: reference
ms.date: 05/31/2018
---

# FaceAdjacency

This template is instantiated on a per-mesh basis, holding information about which vertices in the mesh are duplicates of each other. Duplicates result when a vertex sits on a smoothing group or material boundary. The purpose of this template is to allow the loader to determine which vertices exhibiting different peripheral parameters are actually the same vertexes in the model. Certain applications (mesh simplification, for example) can make use of this information.

``` syntax
template FaceAdjacency
{
    < A64C844A-E282-4756-8B80-250CDE04398C >
    DWORD nIndices;
    array DWORD indices[nIndices];
} 
```

Where:

-   nIndices - Number of indices in the mesh.
-   indices\[nIndices\] - Array of indices.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



