---
description: Defines a B&\#233;zier control patch. The array defines the control points for the patch.
ms.assetid: 'vs|directx_sdk|~\patch.htm'
title: Patch
ms.topic: article
ms.date: 05/31/2018
---

# Patch

Defines a Bézier control patch. The array defines the control points for the patch.

``` syntax
template Patch
{
    < A3EB5D44-FC22-429D-9AFB-3221CB9719A6 >
    DWORD nControlIndices;
    array DWORD controlIndices[nControlIndices];
} 
```

Where:

-   nControlIndices - Number of control point indices.
-   array DWORD controlIndices\[nControlIndices\] - Array of control point indices.

The type of patch is defined by the number of control points, as shown in the following table.



| Number of control points | Type                              |
|--------------------------|-----------------------------------|
| 10                       | Cubic Bézier triangular patch     |
| 15                       | Quartic Bézier triangular patch   |
| 16                       | Cubic Bézier quad rectangle patch |



 

The order of the control points are given in a spiral pattern, as shown in the following diagrams for triangular and rectangular patches.

Triangular patches use the following pattern.

![diagram of the pattern for triangular patches](images/tripatch.png)

Rectangular patches use the following pattern.

![diagram of the pattern for rectangular patches](images/quadpatch.png)

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



