---
description: Page flipping is key in multimedia, animation, and game software; it is analogous to the way you can do animation with a pad of paper.
ms.assetid: b6824962-c7cb-4e7f-8731-2971b0d9a2b0
title: Page Flipping and Back Buffering (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Page Flipping and Back Buffering (Direct3D 9)

Page flipping is key in multimedia, animation, and game software; it is analogous to the way you can do animation with a pad of paper. On each page, the artist changes the figure slightly, so that when you flip rapidly between sheets, the drawing appears animated.

Page flipping in software is similar to this process. Direct3D implements page flipping functionality through a swap chain, which is a property of the device. Initially, you set up a series of Direct3D buffers that flip to the screen in the way that the artist's paper flips to the next page. The first buffer is referred to as the color front buffer. The buffers behind it are called back buffers. Your application writes to a back buffer and then flips the color front buffer so that the back buffer appears on screen. While the system displays the image, your software is again writing to a back buffer. The process continues as long as you are animating, enabling you to animate images efficiently.

Direct3D makes it easy to set up page flipping schemes - from a simple double-buffered scheme (a color front buffer with one back buffer) to more sophisticated schemes with additional back buffers.

## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> <dt>

[What Is a Swap Chain? (Direct3D 9)](what-is-a-swap-chain-.md)
</dt> </dl>

 

 



