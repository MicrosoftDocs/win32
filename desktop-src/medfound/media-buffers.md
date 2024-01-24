---
description: Media Buffers
ms.assetid: 3ee073ea-7bac-4971-9167-93a4e541ab77
title: Media Buffers
ms.topic: article
ms.date: 05/31/2018
---

# Media Buffers

A media buffer is a COM object that manages a block of memory, typically to hold media data. Media buffers are used to move data from one pipeline component to the next. Most applications do not use media buffers directly, because the Media Session handles all of the data flow between pipeline objects. You must use media buffers if you are writing your own pipeline component, or if you are using a pipeline component directly without the Media Session.

Media buffers exposes the [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface. This interface is designed for reading or writing any type of data. Uncompressed video frames require special handling, because they might be stored in Direct3D surfaces located in video memory.

This section contains the following topics.



| Topic                                                        | Description                                                          |
|--------------------------------------------------------------|----------------------------------------------------------------------|
| [Working with Media Buffers](working-with-media-buffers.md) | Describes the general behavior of media buffers for all media types. |
| [Uncompressed Video Buffers](uncompressed-video-buffers.md) | How work with media buffers that contain uncompressed video frames.  |
| [DirectX Surface Buffer](directx-surface-buffer.md)         | Describes how to store a Direct3D surface in a media buffer.         |



 

## Related topics

<dl> <dt>

[Media Foundation Primitives](media-foundation-primitives.md)
</dt> </dl>

 

 



