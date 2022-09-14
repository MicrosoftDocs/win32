---
description: You can use the stencil buffer for more abstract effects, such as outlining and silhouetting.
ms.assetid: 8b9cd2b3-c1bf-4ac9-aae5-7fc0c9e049ff
title: Outlines and Silhouettes (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Outlines and Silhouettes (Direct3D 9)

You can use the stencil buffer for more abstract effects, such as outlining and silhouetting.

If your application applies a stencil mask to the image of a primitive that is the same shape but slightly smaller, the resulting image contains only the primitive's outline. The application can then fill the stencil-masked area of the image with a solid color, giving the primitive an embossed look.

If the stencil mask is the same size and shape as the primitive you are rendering, the resulting image contains a hole where the primitive should be. Your application can then fill the hole with black to produce a silhouette of the primitive.

## Related topics

<dl> <dt>

[Stencil Buffer Techniques](stencil-buffer-techniques.md)
</dt> </dl>

 

 



