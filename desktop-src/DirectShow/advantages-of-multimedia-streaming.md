---
description: Advantages of Multimedia Streaming
ms.assetid: 01020ad5-430d-4b4d-8de3-bcc81270e132
title: Advantages of Multimedia Streaming
ms.topic: article
ms.date: 05/31/2018
---

# Advantages of Multimedia Streaming

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

When developers use multimedia streaming in their applications, it greatly reduces the amount of format-specific programming needed. Typically, an application that must obtain media data from a file or hardware source must know everything about the data format and the hardware device. The application must handle the connection, transfer of data, any necessary data conversion, and the actual data rendering or file storage. Because each format and device is slightly different, this process is often complex and cumbersome. Multimedia streaming, on the other hand, automatically negotiates the transfer and conversion of data from the source to the application. The streaming interfaces provide a uniform and predictable method of data access and control, which makes it easy for an application to play back the data, regardless of its original source or format.

The following steps show how to implement streaming, from hardware device to rendered playback.

1.  A source of video data, such as DirectShow, exposes the streaming interfaces.
2.  The application developer uses the multimedia streaming interfaces to handle data format conversion.
3.  The application developer uses the DirectDraw interfaces to render the resulting data.

The specification for multimedia streams comprises several interfaces; each interface includes methods that control a certain aspect of the streaming process or handle a certain type of data. See [List of Multimedia Streaming Interfaces](list-of-multimedia-streaming-interfaces.md) for additional information.

## Related topics

<dl> <dt>

[About the Multimedia Streaming Architecture](about-the-multimedia-streaming-architecture.md)
</dt> </dl>

 

 



