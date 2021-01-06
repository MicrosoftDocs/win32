---
description: Specifies the mesh data minus the position data.
ms.assetid: 30a95ca3-84ab-475d-9654-a3853263056b
title: FVFData
ms.topic: reference
ms.date: 05/31/2018
---

# FVFData

Specifies the mesh data minus the position data.

``` syntax
template FVFData
{
    < B6E70A0E-8EF9-4e83-94AD-ECC8B0C04897 >
    DWORD dwFVF;
    DWORD nDWords;
    array DWORD data[nDWords];
} 
```

Where:

-   dwFVF - A FVF code.
-   nDWords - Binary data. The number of DWORDS.
-   data\[nDWords\] - Array of DWORDS that contain the data in each vertex element.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



