---
description: Defines a mesh's texture coordinates.
ms.assetid: c87eb176-b502-49b6-bc73-401cc46e8412
title: MeshTextureCoords
ms.topic: reference
ms.date: 05/31/2018
---

# MeshTextureCoords

Defines a mesh's texture coordinates.

``` syntax
template MeshTextureCoords
{
    < F6F23F40-7686-11cf-8F52-0040333594A3 >
    DWORD nTextureCoords;
    array Coords2d textureCoords[nTextureCoords] ;
} 
```

Where:

-   nTextureCoords - Number of texture coordinates.
-   array Coords2d textureCoords\[nTextureCoords\] - Array of 2D texture coordinates. See [**Coords2d**](coords2d.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



