---
description: Requirements for Decoders
ms.assetid: 149aea20-0d37-4b1c-a098-8446c4088ce1
title: Requirements for Decoders
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Decoders

Decoders that deliver samples to the VMR must observe the following rules:

-   There should be one subpicture frame delivered to the VMR for each video frame. The two frames should have the same time stamps.
-   If the subpicture has not changed, use the AM\_GBF\_NOTASYNCPOINT flag in the [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer) method to force the allocator to return a buffer containing the last frame delivered to the VMR. Just put a new time stamp on the sample and deliver it to the VMR again. If the subpicture fame is blank, you should still deliver it. The VMR will detect the empty frame and not blend it with the video. This test is performed by the VGA chip and does not affect the playback performance.
-   All samples, except for live streams, must have valid start and stop time stamps attached. (DVD is not a live stream.)
-   The media sample time stamps must be contiguous
-   The decoder must identify itself as VMR-capable for use by graph builders.
-   The subpicture stream should now contain embedded per-pixel alpha values. The ARGB4444 surface type is ideal for subpictures.
-   Do not assume that the stride of the subpicture is the same as the surface width. This is not always the case with the VMR.

## Related topics

<dl> <dt>

[About DirectX Video Acceleration](about-directx-video-acceleration.md)
</dt> </dl>

 

 



