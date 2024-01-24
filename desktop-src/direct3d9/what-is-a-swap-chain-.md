---
description: A swap chain is a collection of buffers that are used for displaying frames to the user.
ms.assetid: aefc0680-cbe6-42eb-8c00-eaa343eee469
title: What Is a Swap Chain? (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# What Is a Swap Chain? (Direct3D 9)

A swap chain is a collection of buffers that are used for displaying frames to the user. Each time an application presents a new frame for display, the first buffer in the swap chain takes the place of the displayed buffer. This process is called swapping or flipping.

A graphics adapter holds a pointer to a surface that represents the image being displayed on the monitor, called a front buffer. As the monitor is refreshed, the graphics card sends the contents of the front buffer to the monitor to be displayed. However, this leads to a problem when rendering real-time graphics. The heart of the problem is that monitor refresh rates are very slow in comparison to the rest of the computer. Common refresh rates range from 60 Hz (60 times per second) to 100 Hz. If your application is updating the front buffer while the monitor is in the middle of a refresh, the image that is displayed will be cut in half with the upper half of the display containing the old image and the lower half containing the new image. This problem is referred to as tearing.

Direct3D implements two options to avoid tearing:

-   An option to only allow updates of the monitor on the vertical retrace (or vertical sync) operation. A monitor typically refreshes its image by moving a light pin horizontally, zigzagging from the top left of the monitor and ending at the bottom right. When the light pin reaches the bottom, the monitor recalibrates the light pin by moving it back to the upper left so that the process can start again. This recalibration is called a vertical sync. During a vertical sync, the monitor is not drawing anything, so any update to the front buffer will not be seen until the monitor starts to draw again. The vertical sync is relatively slow; however, not slow enough to render a complex scene while waiting. What is needed to avoid tearing and be able to render complex scenes is a process called back buffering.
-   An option to use a technique called back buffering. Back buffering is the process of drawing a scene to an off-screen surface, called a back buffer. Note that any surface other than the front buffer is called an off-screen surface because it is never directly viewed by the monitor. By using a back buffer, an application has the freedom to render a scene whenever the system is idle (that is, no windows messages are waiting) without having to consider the monitor's refresh rate. Back buffering brings in an additional complication of how and when to move the back buffer to the front buffer.

The process of moving the back buffer to the front buffer is called surface flipping. Because the graphics card simply uses a pointer to a surface to represent the front buffer, a simple pointer change is all that is needed to set the back buffer to the front buffer. When an application asks Direct3D to present the back buffer to the front buffer, Direct3D simply "flips" the two surface pointers. The result is that the back buffer is now the new front buffer, and the old front buffer is the new back buffer. A surface flip is invoked whenever an application asks the Direct3D device to present the back buffer; however, Direct3D can be set up to queue the requests until a vertical sync occurs. This option is referred to as the Direct3D device's presentation interval. Note that the data in the new back buffer may not be reusable, depending on how an application specifies how Direct3D should handle surface flipping. Surface flipping is key in multimedia, animation, and game software; it is equivalent to the way you can do animation with a pad of paper. On each page, the artist changes the figures slightly, so that when you flip rapidly between sheets, the drawing appears animated.

## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> <dt>

[Flipping Surfaces (Direct3D 9)](flipping-surfaces.md)
</dt> </dl>

 

 



