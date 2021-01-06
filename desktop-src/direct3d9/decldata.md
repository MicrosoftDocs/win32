---
description: Describes a vertex declaration.
ms.assetid: 6a95bdf6-8767-4ad3-bcec-b32858d25571
title: DeclData
ms.topic: reference
ms.date: 05/31/2018
---

# DeclData

Describes a vertex declaration.

``` syntax
template DeclData
{
    < BF22E553-292C-4781-9FEA-62BD554BDD93 >
    DWORD nElements;
    array VertexElement Elements[nElements];
    DWORD nDWords;
    array DWORD data[nDWords];
} 
```

Where:

-   nElements - Number of vertex declaration elements.
-   Elements\[nElements\] - Array of vertex declaration elements.
-   nDWords - Number of DWORDS.
-   data\[nDWords\] - Array of DWORDS that contain the data in each vertex element.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



