---
Description: Defines a basic material color that can be applied to either a complete mesh or a mesh's individual faces. The power is the specular exponent of the material.
ms.assetid: dfa021ba-61d8-4f99-9bbb-0cfbe11b787d
title: Material
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Material

Defines a basic material color that can be applied to either a complete mesh or a mesh's individual faces. The power is the specular exponent of the material.

``` syntax
template Material
{
    < 3D82AB4D-62DA-11CF-AB39-0020AF71E433 >
    ColorRGBA faceColor;
    FLOAT power;
    ColorRGB specularColor;
    ColorRGB emissiveColor;
    [...]
} 
```

Where:

-   faceColor - Face color. A ColorRGBA template. See [**ColorRGBA**](colorrgba.md).
-   power - Material specular color exponent.
-   specularColor - Material specular color. A ColorRGB template. See [**ColorRGB**](colorrgb.md).
-   emissiveColor - Material emissive color. A ColorRGB template. See [**ColorRGB**](colorrgb.md).

> [!Note]  
> The ambient color requires an alpha component.

 

[**TextureFilename**](texturefilename.md) is an optional data object. If this object is not present, the face is untextured.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



