---
description: About Video Rendering in DirectShow
ms.assetid: 3b064758-2ae5-4441-801c-5400e4ef3790
title: About Video Rendering in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Video Rendering in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow provides several filters that render video:

-   [Video Renderer](video-renderer-filter.md) filter. This filter is available for all platforms that support DirectX, and has no particular system requirements. The Video Renderer uses DirectDraw whenever possible to render the video; otherwise, it uses GDI. This filter is the default video renderer on platforms earlier than Windows XP.
-   [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7). The VMR-7 is available on Windows XP, where it is the default video renderer. The VMR-7 always uses DirectDraw 7 for rendering. It provides many powerful features not available in the older Video Renderer filter, including a plug-in model where the application controls the DirectDraw surfaces used for rendering.
-   [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9). The VMR-9 is a newer version of the Video Mixing Renderer that uses Direct3D 9 for rendering. It is available for all platforms that support DirectX. It is not the default renderer, however, because it has higher system requirements than the Video Renderer filter.
-   The [Overlay Mixer](overlay-mixer-filter.md) filter is designed specifically for DVD playback and broadcast video. It also supports Video Port Extensions (VPEs), enabling it to work with hardware MPEG-2 decoders or analog TV tuners that send video directly to the graphics card.
-   The [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) filter is available starting in Windows Vista. It offers improved video performance compared with earlier video renderers, especially when Windows Vista desktop composition is enabled.

Generally, the EVR is preferred for applications that target Windows Vista or later, and the VMR-9 is preferred for applications running on earlier versions of Windows. For more information about using the VMR-7 and VMR-9 filters, see [Using the Video Mixing Renderer](using-the-video-mixing-renderer.md).

Windowed Mode and Windowless Mode

A DirectShow video renderer can operate in either *windowed* mode or *windowless* mode.

-   In windowed mode, the renderer creates its own window to display the video. Typically you will make this window the child of an application window. For more information, see [Using Windowed Mode](using-windowed-mode.md).
-   In windowless mode, the renderer draws the video directly onto an application window. It does not create its own window. For more information about this mode, see [Using Windowless Mode](using-windowless-mode.md).

The Video Renderer filter supports windowed mode only. The VMR-7 and VMR-9 filters support both modes. They default to windowed mode for backward compatibility, but windowless mode is preferred. The EVR supports windowless mode only.

## Related topics

<dl> <dt>

[Video Rendering](video-rendering.md)
</dt> </dl>

 

 



