---
description: In Direct3D, all two-dimensional (2D) images are represented by a linear range of memory called a surface.
ms.assetid: 33430f01-cd26-45f4-9ce8-ca2c17c7ae6b
title: Surface Formats (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Surface Formats (Direct3D 9)

In Direct3D, all two-dimensional (2D) images are represented by a linear range of memory called a surface. A surface can be thought of as a 2D array where each element holds a color value representing a small section of the image, called a pixel. An image's detail level is defined by both the number of pixels needed to represent the image, and the number of bits needed for the image's color spectrum. For example, an image that is 800 pixels wide by 600 pixels high with 32 bits of color for each pixel (written as 800x600x32) will be more detailed than an image that is 640 pixels wide by 480 pixels tall with 16 bits of color for each pixel (written as 640x480x16). Likewise, the more detailed image will require a larger surface to store the data. For an 800x600x32 image, the surface's array dimensions will be 800x600, and each element will hold a 32-bit value to represent its color.

All surfaces have a size and store a specific number of bits that represent color. The bits that represent color are separated into individual color elements: red, green, and blue. In Direct3D all color elements are defined by the [D3DFORMAT](d3dformat.md) enumerated type. A Direct3D color format is broken down into the number of byes reserved for each color. For example, a 16-bit color format in Direct3D is defined as D3DFMT\_R5G6B5, where 5 bits are reserved for red (R), 6 bits for green (G), and 5 bits for blue (B).

## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> </dl>

 

 



