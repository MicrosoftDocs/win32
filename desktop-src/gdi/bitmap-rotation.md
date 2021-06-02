---
description: To copy a bitmap into a parallelogram; use the PlgBlt function, which performs a bit-block transfer from a rectangle in a source device context into a parallelogram in a destination device context.
ms.assetid: fd5b3d9f-fdce-485e-bff8-464d96b8db34
title: Bitmap Rotation
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Rotation

To copy a bitmap into a parallelogram; use the [**PlgBlt**](/windows/desktop/api/Wingdi/nf-wingdi-plgblt) function, which performs a bit-block transfer from a rectangle in a source device context into a parallelogram in a destination device context. To rotate the bitmap, an application must provide the coordinates, in world units, to be used for the corners of the parallelogram. (For more information about rotation and world units, see [Coordinate Spaces and Transformations](coordinate-spaces-and-transformations.md).)

 

 



