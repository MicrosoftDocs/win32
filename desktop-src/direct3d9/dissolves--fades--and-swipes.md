---
description: Increasingly, applications employ special effects that are commonly used in movies and video, such as dissolves, swipes, and fades.
ms.assetid: 6203922f-9594-4e5c-9baa-8b27ac30978f
title: Dissolves, Fades, and Swipes (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Dissolves, Fades, and Swipes (Direct3D 9)

Increasingly, applications employ special effects that are commonly used in movies and video, such as dissolves, swipes, and fades.

In a dissolve, one image is gradually replaced by another in a smooth sequence of frames. Although Direct3D provides methods of using multiple texture blending to achieve the same effect, applications that use the stencil buffer for dissolves can use texture-blending capabilities for other effects while they do a dissolve.

When your application performs a dissolve, it must render two different images. It uses the stencil buffer to control which pixels from each image are drawn to the rendering target surface. You can define a series of stencil masks and copy them into the stencil buffer on successive frames. Alternately, you can define a base stencil mask for the first frame and alter it incrementally.

At the beginning of the dissolve, your application sets the stencil function and stencil mask so that most of the pixels from the starting image pass the stencil test. Most of the pixels from the ending image should fail the stencil test. On successive frames, the stencil mask is updated so that fewer and fewer of the pixels in the starting image pass the test. As the frames progress, fewer and fewer of the pixels in the ending image fail the test. In this manner, your application can perform a dissolve using any arbitrary dissolve pattern.

Fading in or fading out is a special case of dissolving. When fading in, the stencil buffer is used to dissolve from a black or white image to a rendering of a 3D scene. Fading out is the opposite, your application starts with a rendering of a 3D scene and dissolves to black or white. The fade can be done using any arbitrary pattern you want to employ.

Direct3D applications use a similar technique for swipes. For example, when an application performs a left-to-right swipe, the ending image appears to slide gradually on top of the starting image from left to right. As in a dissolve, you must define a series of stencil masks that are loaded into the stencil buffer on successive frames, or successively modify the starting stencil mask. The stencil masks are used to disable the writing of pixels from the starting image and to enable the writing of pixels from the ending image.

A swipe is somewhat more complex than a dissolve in that your application must read pixels from the ending image in the reverse order of the swipe. That is, if the swipe is moving from left to right, your application must read pixels from the ending image from right to left.

## Related topics

<dl> <dt>

[Stencil Buffer Techniques](stencil-buffer-techniques.md)
</dt> </dl>

 

 



