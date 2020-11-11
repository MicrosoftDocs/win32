---
title: Buffer tiling
description: A Buffer resource is divided into 64KB tiles, with some empty space in the last tile if the size is not a multiple of 64KB.
ms.assetid: 979EFCF3-1FE1-412A-A19D-F1B1CF86423B
ms.topic: article
ms.date: 05/31/2018
---

# Buffer tiling

A [Buffer](overviews-direct3d-11-resources-buffers.md) resource is divided into 64KB tiles, with some empty space in the last tile if the size is not a multiple of 64KB.

Structured buffers must have no constraint on the stride to be tiled. But possible performance optimizations in hardware for using [**StructuredBuffers**](/windows/desktop/direct3dhlsl/sm5-object-structuredbuffer) can be sacrificed by making them tiled in the first place.

## Related topics

<dl> <dt>

[How a tiled resource's area is tiled](how-a-tiled-resource-s-area-is-tiled.md)
</dt> </dl>

 

 