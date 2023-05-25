---
description: Features of the VMR
ms.assetid: a809045b-b60d-4092-bc4d-0e70e17d2913
title: Features of the VMR
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Features of the VMR

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Video Mixing Renderer 7 (VMR-7) supports the following new features:

-   Real mixing of multiple video streams, using the alpha-blending capabilities of Direct3D hardware devices.
-   The ability to plug in your own compositing component to implement effects and transitions between multiple video streams entering the VMR.
-   True windowless rendering. It is no longer necessary to make the video playback window a child of the application's window in order to contain video playback. The VMR's new windowless rendering mode allows applications to easily host video playback within any window without having to forward window messages to the renderer for renderer-specific processing.
-   A new renderless playback mode where applications can supply their own allocator component to get access to the decoded video image prior to it being displayed on the screen.
-   Improved support for PCs equipped with multiple monitors.
-   Support for Microsoft's new DirectX Video Acceleration architecture.
-   Support for high-quality video playback concurrently on multiple windows.
-   Support for DirectDraw Exclusive Mode
-   100% backward-compatibility with existing applications.
-   Support for frame stepping and a reliable way to capture the current image being displayed.
-   The ability for applications to easily alpha-blend their own static image data (such as channel logos or UI components) with the video in a smooth flicker-free way.

The VMR-9 supports all the features listed above, plus:

-   The ability to process video data directly with Direct3D APIs such as pixel shaders.
-   Improved support for interlaced video content.
-   Support on any platform supported by DirectX.

## Related topics

<dl> <dt>

[About the Video Mixing Render](about-the-video-mixing-render.md)
</dt> </dl>

 

 



