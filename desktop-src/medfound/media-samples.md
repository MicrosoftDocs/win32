---
description: Learn about media samples in Microsoft Media Foundation. A media sample is an object that contains an ordered list of zero or more buffers.
ms.assetid: 14389eea-8091-4c10-849e-53db3e98a7c8
title: Media Samples (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Media Samples (Microsoft Media Foundation)

A media sample is an object that contains an ordered list of zero or more buffers. Media samples expose the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface. The amount of data contained in one sample depends on the component that creates the sample and on the type of data in the buffers. For uncompressed video, a sample usually holds a single video frame. For uncompressed audio, the amount of data can vary, but usually an audio frame does not span two samples. For compressed data, these guidelines might not apply.

A single sample might contain multiple buffers for reasons of efficiency. For example, in an ASF file, a video frame is often spread out among multiple ASF packets. The media source might read the packets into multiple buffers. Instead of copying each fragment into one buffer, the source simply puts all of the buffers into one sample. Downstream components can then decide whether to copy the smaller buffers into one contiguous buffer. Generally, if you are writing a pipeline component, you should assume that any sample might contain more than one buffer.

This section contains the following topics.



| Topic                                                        | Description                                                                                                              |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [Working with Media Samples](working-with-media-samples.md) | Describes the general behavior of media samples.                                                                         |
| [Video Samples](video-samples.md)                           | Describes a specialized implementation of [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) designed for holding uncompressed video frames. |



 

## Related topics

<dl> <dt>

[Media Buffers](media-buffers.md)
</dt> <dt>

[Media Foundation Primitives](media-foundation-primitives.md)
</dt> </dl>

 

 



