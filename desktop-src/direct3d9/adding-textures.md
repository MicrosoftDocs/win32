---
description: To add textures, use the hierarchical nature of the file format and add an optional TextureFilename data object to the Material data objects.
ms.assetid: 741f4c05-49f8-4c76-be5c-ce5b496124bb
title: Adding Textures (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Adding Textures (Direct3D 9)

To add textures, use the hierarchical nature of the file format and add an optional [**TextureFilename**](texturefilename.md) data object to the [**Material**](material.md) data objects. The **Material** objects now read as follows:


```
Material RedMaterial {
1.000000;0.000000;0.000000;1.000000;;    // R = 1.0, G = 0.0, B = 0.0
0.000000;
0.000000;0.000000;0.000000;;
0.000000;0.000000;0.000000;;
TextureFilename { "tex1.ppm"; }
}

Material GreenMaterial {
0.000000;1.000000;0.000000;1.000000;;     // R = 0.0, G = 1.0, B = 0.0
0.000000;
0.000000;0.000000;0.000000;;
0.000000;0.000000;0.000000;;
TextureFilename { "win95.ppm"; }
}
```



## Related topics

<dl> <dt>

[X Files (Legacy)](x-files--legacy-.md)
</dt> </dl>

 

 



