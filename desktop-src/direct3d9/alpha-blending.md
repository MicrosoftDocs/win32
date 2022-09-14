---
description: Learn about alpha blending. Alpha blending is used to display an image that has transparent or semi-transparent pixels.
ms.assetid: 553b0bc8-1bd8-4282-9260-cdc5f2b8788d
title: Alpha Blending (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Blending (Direct3D 9)

Alpha blending is used to display an image that has transparent or semi-transparent pixels. In addition to a red, green, and blue color channel, each pixel in an alpha bitmap has a transparency component known as its alpha channel. The alpha channel typically contains as many bits as a color channel. For example, an 8-bit alpha channel can represent 256 levels of transparency, from 0 (the entire pixel is transparent) to 255 (the entire pixel is opaque). The list below shows some special effects you can create using alpha blending.

Color can be defined with or without alpha values. Color without alpha is RGB color with alpha is stored as ARGB. Vertex data, material data and texture data can be used to give object's transparency. The frame buffer can also be used to generate transparency effects.

-   [Vertex Alpha (Direct3D 9)](vertex-alpha.md)
-   [Material Alpha (Direct3D 9)](material-alpha.md)
-   [Texture Alpha (Direct3D 9)](texture-alpha.md)
-   [Frame Buffer Alpha (Direct3D 9)](frame-buffer-alpha.md)
-   [Render Target Alpha (Direct3D 9)](render-target-alpha.md)

Samples that demonstrate alpha include:

-   [Billboarding (Direct3D 9)](billboarding.md)
-   [Clouds, Smoke, and Vapor Trails (Direct3D 9)](clouds--smoke--and-vapor-trails.md)
-   [Fire, Flares, and Explosions (Direct3D 9)](fire--flares--and-explosions.md)

## Related topics

<dl> <dt>

[Direct3D Rendering](direct3d-rendering.md)
</dt> </dl>

 

 



