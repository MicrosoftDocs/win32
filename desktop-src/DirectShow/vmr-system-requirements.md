---
description: VMR System Requirements
ms.assetid: fd50b312-73f0-4c68-a8b1-3497d958bc8f
title: VMR System Requirements
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VMR System Requirements

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The VMR uses the graphics-processing capabilities of the computer's display card exclusively; the VMR does not perform any blending or rendering of video using the host processor, because to do so would greatly impact the frame rate and quality of the video being displayed. When taking advantage of the new features offered by the VMR, particularly blending of multiple video streams and/or application images, the overall performance obtained is highly dependent on the capabilities of the graphics card being used on the computer. Graphics cards that perform well with the VMR have the following hardware support built into them:

-   Support for YUV and "non-power of 2" Direct3D texture surfaces.
-   The ability to StretchBlt from YUV to RGB DirectDraw surfaces.
-   At least 16MB of video memory if multiple video streams are to be blended together. The actual amount of memory required is dependent on the image size of the video streams and resolution of the display mode being used.
-   Support for an RGB overlay or the ability to blend to a YUV overlay surface.
-   Hardware-accelerated video (support for DirectX Video Acceleration) decoding.
-   High pixel fill rates.

> [!Note]  
> The VMR requires that the system monitor be set for a color depth of at least 16 bits. The VMR cannot be put into a run state if the monitor is set for 256 colors. Also, some video cards cannot perform Direct3D operations when the display is set to 24 bits per pixel.

 

## Related topics

<dl> <dt>

[About the Video Mixing Render](about-the-video-mixing-render.md)
</dt> </dl>

 

 



