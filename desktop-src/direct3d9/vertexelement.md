---
Description: Describes an individual vertex element in a vertex declaration.
ms.assetid: efe3e98b-938d-4d4c-b790-2b8c8aab0ded
title: VertexElement
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VertexElement

Describes an individual vertex element in a vertex declaration.

``` syntax
template VertexElement 
{ 
    < F752461C-1E23-48f6-B9F8-8350850F336F > 
    DWORD Type; 
    DWORD Method; 
    DWORD Usage; 
    DWORD UsageIndex; 
} 
```

Where:

-   Type - Vertex data type. See [**D3DDECLTYPE**](https://msdn.microsoft.com/en-us/library/Bb172533(v=VS.85).aspx).
-   Method - Tessellator processing method. See [**D3DDECLMETHOD**](https://msdn.microsoft.com/en-us/library/Bb172532(v=VS.85).aspx).
-   Usage - Intended use of the vertex data. See [**D3DDECLUSAGE**](https://msdn.microsoft.com/en-us/library/Bb172534(v=VS.85).aspx).
-   UsageIndex - Modifies the usage data. See [**D3DDECLUSAGE**](https://msdn.microsoft.com/en-us/library/Bb172534(v=VS.85).aspx).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> <dt>

[**D3DVERTEXELEMENT9**](d3dvertexelement9.md)
</dt> </dl>

 

 



