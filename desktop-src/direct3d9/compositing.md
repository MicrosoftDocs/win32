---
description: Your application can use the stencil buffer to composite 2D or 3D images onto a 3D scene.
ms.assetid: 9233d15d-fa99-41a2-a253-22f5ae5bf788
title: Compositing (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Compositing (Direct3D 9)

Your application can use the stencil buffer to composite 2D or 3D images onto a 3D scene. A mask in the stencil buffer is used to occlude an area of the rendering target surface. Stored 2D information, such as text or bitmaps, can then be written to the occluded area. Alternately, your application can render additional 3D primitives to the stencil-masked region of the rendering target surface. It can even render an entire scene.

Games often composite multiple 3D scenes together. For instance, driving games typically display a rear-view mirror. The mirror contains the view of the 3D scene behind the driver. It is essentially a second 3D scene composited with the driver's forward view.

## Related topics

<dl> <dt>

[Stencil Buffer Techniques](stencil-buffer-techniques.md)
</dt> </dl>

 

 



