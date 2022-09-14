---
description: Video Encoding with Temporal Compression
ms.assetid: df363017-97c5-45b0-b8a5-44ac73b7a0e7
title: Video Encoding with Temporal Compression (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Video Encoding with Temporal Compression (Microsoft Media Foundation)

To achieve the highest compression ratios possible, the Windows Media Video codecs use *temporal compression*. Temporal compression is a technique of reducing compressed video size by not encoding each frame as a complete image. The frames that are encoded completely (like a static image) are called *key frames*. All other frames in the video are represented by data specifying the change since the last frame. These frames are called *delta frames*.

The amount of compression that can be achieved using temporal compression depends upon the content. If the video is static, without a lot of motion or other changes in image, many delta frames can be created for each key frame. The more delta frames that are used, the smaller the encoded video stream. However, if the video is dynamic, with lots of motion or changing colors, the benefit of using temporal compression is smaller.

## Related topics

<dl> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



