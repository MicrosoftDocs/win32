---
description: This template is instantiated on a per-mesh basis only in meshes that contain exported skinning information. The purpose of this template is to provide information about the nature of the skinning information that was exported.
ms.assetid: 95a4fa45-63d1-4931-9c91-b26807d2b043
title: XSkinMeshHeader
ms.topic: reference
ms.date: 05/31/2018
---

# XSkinMeshHeader

This template is instantiated on a per-mesh basis only in meshes that contain exported skinning information. The purpose of this template is to provide information about the nature of the skinning information that was exported.

``` syntax
template XSkinMeshHeader 
{ 
    < 3CF169CE-FF7C-44ab-93C0-F78F62D172E2 >  
    WORD nMaxSkinWeightsPerVertex; 
    WORD nMaxSkinWeightsPerFace; 
    WORD nBones; 
}
```

Where:

-   nMaxSkinWeightsPerVertex - Maximum number of transforms that affect a vertex in the mesh.
-   nMaxSkinWeightsPerFace - Maximum number of unique transforms that affect the three vertices of any face.
-   nBones - Number of bones that affect vertices in this mesh.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



