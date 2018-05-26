---
Description: Describes an individual vertex element in a vertex declaration.
ms.assetid: efe3e98b-938d-4d4c-b790-2b8c8aab0ded
title: VertexElement
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

-   Type - Vertex data type. See [**D3DDECLTYPE**](direct3d9.d3ddecltype).
-   Method - Tessellator processing method. See [**D3DDECLMETHOD**](direct3d9.d3ddeclmethod).
-   Usage - Intended use of the vertex data. See [**D3DDECLUSAGE**](direct3d9.d3ddeclusage).
-   UsageIndex - Modifies the usage data. See [**D3DDECLUSAGE**](direct3d9.d3ddeclusage).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> <dt>

[**D3DVERTEXELEMENT9**](d3dvertexelement9.md)
</dt> </dl>

 

 



