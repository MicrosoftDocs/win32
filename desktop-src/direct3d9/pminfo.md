---
description: PMInfo - Not supported. Used internally by DirectX.
ms.assetid: 8a07357f-d4e8-4104-9d21-51c3e8b8d6d2
title: PMInfo
ms.topic: reference
ms.date: 05/31/2018
---

# PMInfo

Not supported. Used internally by DirectX.

``` syntax
template PMInfo 
{ 
    < B6C3E656-EC8B-4b92-9B62-681659522947 > 
    DWORD nAttributes; 
    array PMAttributeRange attributeRanges[nAttributes]; 
    DWORD nMaxValence; 
    DWORD nMinLogicalVertices; 
    DWORD nMaxLogicalVertices; 
    DWORD nVSplits; 
    array PMVSplitRecord splitRecords[nVSplits]; 
    DWORD nAttributeMispredicts; 
    array DWORD attributeMispredicts[nAttributeMispredicts]; 
}
```

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



