---
description: Specifies vertex colors for a mesh, instead of applying a material per face or per mesh.
ms.assetid: 9ffd365f-11a5-420b-af5e-6a8be79a304c
title: MeshVertexColors
ms.topic: reference
ms.date: 05/31/2018
---

# MeshVertexColors

Specifies vertex colors for a mesh, instead of applying a material per face or per mesh.

``` syntax
template MeshVertexColors
{
    <1630B821-7842-11cf-8F52-0040333594A3>
    DWORD nVertexColors;
    array IndexColor vertexColors[nVertexColors];
} 
```

Where:

-   nVertexColors - Number of colors. This matches the number of vertices in the mesh.
-   array IndexColor vertexColors\[nVertexColors\] - Array of indexed colors. See [**IndexedColor**](indexedcolor.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



