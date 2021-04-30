---
description: Synchronizing the VMR to the Monitor's Refresh Rate
ms.assetid: 73e73821-fb08-488a-956e-ef33f6651a26
title: Synchronizing the VMR to the Monitor's Refresh Rate
ms.topic: article
ms.date: 05/31/2018
---

# Synchronizing the VMR to the Monitor's Refresh Rate

In rare scenarios, you may wish to precisely synchronize video rendering with the monitor's refresh rate, so that exactly one new frame is presented each time the monitor refreshes. The most reliable way to do this is to create a custom allocator-presenter that uses a flip operation instead of a blit operation to write the video bits into the primary surface. "Flip" is called each time the monitor refreshes, so if your video stream contains no time stamps, the VMR will render as fast as possible to the primary surface, but the surface will block the stream until the Flip operation completes. This means that, as long as the CPU is not overburdened, the next frame will always be waiting in the primary surface each time the monitor refreshes. However, if some other CPU-intensive process is running, it could possibly starve your DirectShow streaming thread so that it cannot deliver video frames fast enough to the primary surface.

## Related topics

<dl> <dt>

[VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
</dt> </dl>

 

 



