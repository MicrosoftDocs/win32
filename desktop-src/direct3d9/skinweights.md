---
description: This template is instantiated on a per-mesh basis.
ms.assetid: ac5289c6-989c-43b4-9190-ac8f831a05f0
title: SkinWeights
ms.topic: reference
ms.date: 05/31/2018
---

# SkinWeights

This template is instantiated on a per-mesh basis. Within a mesh, a sequence of n instances of this template will appear, where n is the number of bones (X file frames) that influence the vertices in the mesh. Each instance of the template basically defines the influence of a particular bone on the mesh. There is a list of vertex indices, and a corresponding list of weights.

``` syntax
template SkinWeights 
{ 
    < 6F0D123B-BAD2-4167-A0D0-80224F25FABB > 
    STRING transformNodeName; 
    DWORD nWeights; 
    array DWORD vertexIndices[nWeights]; 
    array float weights[nWeights]; 
    Matrix4x4 matrixOffset; 
} 
```

Where:

-   The name of the bone whose influence is being defined is transformNodeName, and nWeights is the number of vertices affected by this bone.
-   The vertices influenced by this bone are contained in vertexIndices, and the weights for each of the vertices influenced by this bone are contained in weights.
-   The matrix matrixOffset transforms the mesh vertices to the space of the bone. When concatenated to the bone's transform, this provides the world space coordinates of the mesh as affected by the bone. See [**Matrix4x4**](matrix4x4.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



