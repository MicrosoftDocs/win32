---
title: Using the Stream Buffer Engine
description: Using the Stream Buffer Engine
ms.assetid: aa19d268-fbeb-4dc4-a8f5-8bc31a85367f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Stream Buffer Engine

This topic applies to Windows XP Service Pack 1 or later.

The Stream Buffer Engine enables an application to seek, pause, and record a live video stream without interrupting the stream. Transitions between live and recorded content are seamless. Currently, the Stream Buffer Engine supports MPEG-2 video and digital video (DV) sources, at capture rates up to 20 megabits per second (Mbps).

Applications can use the Stream Buffer Engine to provide VCR-like functions, such as pause, seek, and multi-speed play ("trick mode"), while rendering a live video stream. Applications can also use the Stream Buffer Engine to record video for later playback.

You can use the Stream Buffer Engine directly in your application, or indirectly through the Video Control. The Video Control automatically encrypts the content using the TV Ratings Components.

To learn about using the Stream Buffer Engine with the Video Control, see the following topic:

-   [Using the Stream Buffer Engine with the Video Control](using-the-stream-buffer-engine-with-the-video-control.md).

To learn about using the Stream Buffer Engine directly in a DirectShow-based application, see the following topics:

-   [About the Stream Buffer Engine](about-the-stream-buffer-engine.md)
-   [Creating Stream Buffer Graphs](creating-stream-buffer-graphs.md)
-   [Creating Stream Buffer Recordings](creating-stream-buffer-recordings.md)
-   [Buffering in the Stream Buffer Engine](buffering-in-the-stream-buffer-engine.md)
-   [About the dvr-ms File Format](about-the-dvr-ms-file-format.md)
-   [Receiving Spanning Events in the Stream Buffer Engine](receiving-spanning-events-in-the-stream-buffer-engine.md)
-   [Stream Buffer Source Filter Enhancements in Windows 7](stream-buffer-source-filter-enhancements-in-windows-7.md)
-   [Stream Buffer Engine Reference](stream-buffer-engine-reference.md)

## Related topics

<dl> <dt>

[Stream Buffer Engine](stream-buffer-engine.md)
</dt> </dl>

 

 




