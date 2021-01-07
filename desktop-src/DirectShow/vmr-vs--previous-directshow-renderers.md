---
description: VMR vs.
ms.assetid: 45b3f964-6ec7-48b8-a66e-3c9883e6d780
title: VMR vs. Previous DirectShow Renderers
ms.topic: article
ms.date: 05/31/2018
---

# VMR vs. Previous DirectShow Renderers

With the old filters, different renderers would be required in the graph depending on the hardware configuration.

The [Video Renderer](video-renderer-filter.md) filter was used to render a single video stream in non-video port scenarios. It was based on graphics hardware technology which is now over five years old, and on an older version of DirectDraw. In certain scenarios, it uses GDI for rendering. This is done either to conserve video resources, which were much more limited five years ago, or else to overcome limitations in DirectDraw that were related to multi-monitor support. Neither the VMR-7 nor the VMR-9 ever uses GDI for rendering; the VMR-7 is based completely on DirectDraw 7 and the VMR-9 is based on Direct3D 9.

In scenarios involving either a video port or multiple video input streams, prior to the VMR the [Overlay Mixer](overlay-mixer-filter.md) filter was used for rendering. This filter only uses the hardware overlay on the graphics card, and so is generally limited to the one overlay surface provided by most cards. The Overlay Mixer performs destination color keying, but it is not capable of alpha blending. Because it does not have a window manager, it must use a second filter, the Video Renderer, for window management. The VMR is capable of true alpha blending, and can create multiple overlays in software in addition to the hardware overlays.

In video port scenarios where applications were overlaying closed captioning or other VBI data on the video, an additional filter, the [VBI Surface Allocator](vbi-surface-allocator.md), was required in order to allocate the additional video memory for the VBI text. For ISVs, the VMR-7 simplifies application development by combining allocation and rendering functionality into a single filter that is used in all scenarios. With the VMR, the VBI Surface Allocator is no longer needed. This filter is replaced in Windows XP by the new [Video Port Manager](video-port-manager.md) filter which performs all of the video port tasks previously performed by the Overlay Mixer.

> [!Note]  
> The VMR-9 does not support video ports.

 

The VMR is more robust than the earlier renderers, in part because it only uses DirectDraw 7 (or Direct3D 9 if you are using the VMR-9) interfaces, as opposed to the old renderers which used a mixture of interfaces from older and newer versions of DirectDraw. The VMR also employs a new image presentation mechanism which is designed for current and future generations of adapters, which have support for Direct3D, increased VRAM and video memory bandwidth, and hardware acceleration features. With the VMR, the focus is on front-end processing, and reduced dependence on video ports and overlays. But even with all its new functionality, the VMR is designed for maximum compatibility with existing applications.

The VMR is also extensible. Applications can provide their own sub-components to perform custom video effects and/or take control of the allocation and rendering process.

## Related topics

<dl> <dt>

[About the Video Mixing Render](about-the-video-mixing-render.md)
</dt> </dl>

 

 



