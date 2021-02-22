---
description: Creating Multimedia Stream Objects and Stream Samples
ms.assetid: 1aecdd39-f1b3-490b-b092-86d51439be02
title: Creating Multimedia Stream Objects and Stream Samples
ms.topic: article
ms.date: 05/31/2018
---

# Creating Multimedia Stream Objects and Stream Samples

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

Objects that support the [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream) interface are the basic containers for multimedia data streams. The **IMultiMediaStream** interface includes methods that enumerate the object's data streams; these streams are typically video and audio data, but can include data of any format, such as closed-captioning, plain text, or SMPTE timecode. The **IMultiMediaStream** interface is a generic container, however; developers can create other versions of the interface that support specific data formats. Objects that implement the [**IAMMultiMediaStream**](/previous-versions/windows/desktop/api/amstream/nn-amstream-iammultimediastream) interface, for example, can enumerate and control streams of any DirectShow data format. Because individual data streams are format specific, they support at least two different interfaces: one generic and one data-specific. Every stream supports the [**IMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream) interface, which provides methods to retrieve its format and a pointer to the stream itself. The [**IDirectDrawMediaStream**](/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawmediastream) interface, on the other hand, has methods that deal specifically with rendering video data. Any interface derived from **IMultiMediaStream** also supports the creation of stream samples, the basic units of streaming data.

A multimedia sample is a reference to an object containing the media data. For a video image, this is a DirectDraw surface. The sample's exact content varies, depending on the type of media (sound, text, and so on). Because a sample is only a reference to the data object, any number of stream samples can refer to the same object. The [**IStreamSample**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-istreamsample) interface provides methods that get and set a sample's characteristics, such as its start and stop time, status, and stream association. The [**IStreamSample::Update**](/previous-versions/windows/desktop/api/mmstream/nf-mmstream-istreamsample-update) method refreshes the sample's data in the case of readable streams. For writable streams, it will write the sample's data to the stream. Typically, you use the **Update** method in a loop that renders, transfers, or stores streaming data.

## Related topics

<dl> <dt>

[About the Multimedia Streaming Architecture](about-the-multimedia-streaming-architecture.md)
</dt> </dl>

 

 



