---
description: Base Multimedia Streaming Interfaces
ms.assetid: a94dbb64-dfca-4c24-8c11-761835faf8a8
title: Base Multimedia Streaming Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Base Multimedia Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

The base multimedia streaming interfaces provide a programmatic way to access multimedia streams. However, using a base interface to access a specific type of data can limit the amount of control you have over the data, so media developers should create derived versions of these interfaces that provide more powerful control over the unique capabilities of their media type.



| Interface                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream) | Defines how to access the highest-level multimedia stream object; this object contains and provides access to other stream objects. [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream) has methods that enumerate or retrieve specific streams, as well as checking the stream's total time duration and seeking within the stream.                                                                                                       |
| [**IMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream)           | Defines a generic stream object. Use its methods to retrieve a pointer to the stream, get information about the stream, and create samples from the stream data. You can also create shared stream samples, which multiple streams can access without duplicating the sample's data.                                                                                                                                                  |
| [**IStreamSample**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-istreamsample)         | Controls the behavior of a specific stream sample. You can retrieve the stream that created the sample, check the sample's start and end times and completion status, and perform a user-defined function on the sample itself (through the [**Update**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-istreamsample-update) method). Typically, the Update method processes the sample data in an appropriate manner, such as rendering video data or playing back audio data. |



 

## Related topics

<dl> <dt>

[List of Multimedia Streaming Interfaces](list-of-multimedia-streaming-interfaces.md)
</dt> </dl>

 

 



