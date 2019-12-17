---
title: How to Clip with an Axis-Aligned Clip Rectangle
description: Shows how to clip a region with an axis-aligned clip rectangle.
ms.assetid: 4196653a-9177-4a41-9db9-4738a41313aa
ms.topic: article
ms.date: 05/31/2018
---

# How to Clip with an Axis-Aligned Clip Rectangle

This topic describes how to clip an image with an axis-aligned clip rectangle. This approach produces only rectangular clips, because the content bounds are aligned to the axis of the rectangle. This approach is more efficient than using layers with the content bounds. For more information, see[Layers Overview](direct2d-layers-overview.md).

**To clip with an axis-aligned clip rectangle**

1.  Load the original image from a resource. For information on how to load a bitmap, see [How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md).
2.  Call [**ID2D1RenderTarget::PushAxisAlignedClip**](https://msdn.microsoft.com/library/Dd316860(v=VS.85).aspx) to specify a rectangle. The rendering commands are clipped to the rectangle.

3.  Paint the original image.
4.  Call [**ID2D1RenderTarget::PopAxisAlignedClip**](https://msdn.microsoft.com/library/Dd316850(v=VS.85).aspx) to remove the last axis-aligned clip from the render target.

For example, in the following illustration, the original bitmap on the left is 200\*130 pixels. The bitmap on the right is the original bitmap clipped to the axis-aligned clip rectangle. The dimensions are (20, 20) to (100, 100).

![illustration of a goldfish bitmap before and after the bitmap is clipped](images/cliparegion-axisalignedclip.png)

To create the clipped image, create a rectangle structure as the clipping area. Call [**PushAxisAlignedClip**](https://msdn.microsoft.com/library/Dd316860(v=VS.85).aspx) with the clipping area and paint the original image. Call [**PopAxisAlignedClip**](https://msdn.microsoft.com/library/Dd316850(v=VS.85).aspx) to remove the clip from the render target. The following code shows how to do this.


```C++
pRT->PushAxisAlignedClip(
    D2D1::RectF(20, 20, 100, 100),
    D2D1_ANTIALIAS_MODE_PER_PRIMITIVE
    );

pRT->FillRectangle(D2D1::RectF(0, 0, 200, 133), m_pOriginalBitmapBrush);
pRT->PopAxisAlignedClip();
```



## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> </dl>

 

 




