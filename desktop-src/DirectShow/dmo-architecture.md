---
description: DMO Architecture
ms.assetid: f74b2d0f-b40c-4598-97a4-9c1dc71bbb1a
title: DMO Architecture
ms.topic: article
ms.date: 05/31/2018
---

# DMO Architecture

This section describes the overall architecture of a DMO.

**Streams**

A DMO is an object that takes *m* inputs and produces *n* outputs. The inputs and outputs are called *streams*. Every DMO has at least one stream. Streams are not objects; they are simply referenced on the DMO by index number. The number of streams is fixed at design time.

**Media Types**

All data is typed using a *media type*, which defines how to interpret the contents of the data. For example, 320 x 240 24-bit RGB video is one type; 44.1-kilohertz (kHz) 16-bit stereo PCM audio is another type. Media types are described using the [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) structure. Before the client can process any data, it must set the media type for each stream on the DMO.

Typically, a stream can accept a range of media types. Some DMOs support a wider range of types than others. The DMO interfaces define methods for the client to discover the supported types. For example, one DMO might support RGB video at any bit depth, while another might support only 24-bit RGB. Also, a DMO might be limited to certain combinations of inputs and outputs. For example, if the input type is 16-bit video, the output stream might require the same bit depth. The client can enumerate each stream's preferred types and then test specific combinations.

**Buffers**

In the default DMO model, the client allocates separate input buffers and output buffers. It fills the input buffers with data and delivers them to the DMO, and the DMO writes new data into the output buffers.

Optionally, a DMO can support "in-place" processing. With in-place processing, the DMO writes the output directly into the input buffer, over the original data. In-place processing eliminates the need for separate buffers. On the other hand, it alters the original data, which may not be acceptable for some applications.

The default (non-in-place) buffering model is supported through the [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface. All DMOs must implement this interface. If a DMO supports in-place processing, it also exposes the [**IMediaObjectInPlace**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobjectinplace) interface. The client is responsible for allocating all buffers, both input and output.

## Related topics

<dl> <dt>

[About DMOs](about-dmos.md)
</dt> </dl>

 

 



