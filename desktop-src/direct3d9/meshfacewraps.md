---
description: Used to define the texture topology of each face in a wrap. The value of the nFaceWrapValues member should be equal to the number of faces in a mesh.
ms.assetid: f4aa356c-8f91-462f-9fc7-869b186b6c27
title: MeshFaceWraps
ms.topic: reference
ms.date: 05/31/2018
---

# MeshFaceWraps

Used to define the texture topology of each face in a wrap. The value of the nFaceWrapValues member should be equal to the number of faces in a mesh.

``` syntax
template MeshFaceWraps
{
    < ED1EC5C0-C0A8-11D0-941C-0080C80CFA7B >
    DWORD nFaceWrapValues;
    array Boolean2d faceWrapValues[nFaceWrapValues];
} 
```

This template is no longer used.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



