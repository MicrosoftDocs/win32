---
description: Used in a mesh object to specify which material applies to which faces. The nMaterials member specifies how many materials are present, and materials specify which material to apply.
ms.assetid: b38fd445-1a31-41ed-abbe-084abfe1c221
title: MeshMaterialList
ms.topic: reference
ms.date: 05/31/2018
---

# MeshMaterialList

Used in a mesh object to specify which material applies to which faces. The nMaterials member specifies how many materials are present, and materials specify which material to apply.

``` syntax
template MeshMaterialList
{
    < F6F23F42-7686-11CF-8F52-0040333594A3 >
    DWORD nMaterials;
    DWORD nFaceIndexes;
    array DWORD faceIndexes[nFaceIndexes];
    [Material <3D82AB4D-62DA-11CF-AB39-0020AF71E433>]
} 
```

Where:

-   nMaterials - A DWORD. The number of materials.
-   nFaceIndexes - A DWORD. The number of indices.
-   faceIndexes\[nFaceIndexes\] - An array of DWORDs containing the face indices.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



