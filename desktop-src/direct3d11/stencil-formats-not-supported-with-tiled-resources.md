---
title: Stencil formats not supported with tiled resources
description: Formats that contain stencil aren't supported with tiled resources.
ms.assetid: 1B675245-F21F-47B5-B3B4-C8307DAC575B
ms.topic: article
ms.date: 05/31/2018
---

# Stencil formats not supported with tiled resources

Formats that contain stencil aren't supported with tiled resources.

Formats that contain stencil include DXGI\_FORMAT\_D24\_UNORM\_S8\_UINT (and related formats in the R24G8 family) and DXGI\_FORMAT\_D32\_FLOAT\_S8X24\_UINT (and related formats in the R32G8X24 family).

Some implementations store depth and stencil in separate allocations while others store them together. Tile management for the two schemes would have to be different, and no single API can abstract or rationalize the differences. We recommend for future hardware to support independent depth and stencil surfaces, each independently tiled. 32 bit depth would have 128x128 tiles, and 8 bit stencil would have 256x256 tiles. Therefore, applications would have to live with tile shape misalignment between depth and stencil. But the same problem exists with different render target surface formats already.

## Related topics

<dl> <dt>

[Tiled resource cross process and device sharing](tiled-resource-cross-process-and-device-sharing.md)
</dt> </dl>

 

 




