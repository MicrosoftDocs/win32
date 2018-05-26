---
Description: Using Multimedia Streams in Applications
ms.assetid: 73cfe89b-df46-445a-92c7-2f7323672441
title: Using Multimedia Streams in Applications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Multimedia Streams in Applications

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

The multimedia streaming interfaces greatly simplify the process of manipulating multimedia data by removing the dependency on specific characteristics of the hardware or software source and providing support for all Microsoft DirectX® media formats. Streams abstract the data to a very high level; applications can even move data from one stream to another without knowing anything about the data's format.

Perform the following steps to create a multimedia stream.

1.  Create the multimedia stream. The method of creation and initialization of the stream is architecture specific. DirectShow supports the [**IAMMultiMediaStream**](/windows/win32/amstream/nn-amstream-iammultimediastream?branch=master) interface, which is used to initialize the stream. Other in-process server implementations of [**IMultiMediaStream**](/windows/win32/mmstream/nn-mmstream-imultimediastream?branch=master) will be created and initialized using different mechanisms.
2.  After the multimedia stream object is initialized, the application will use **QueryInterface** to retrieve the **IMultiMediaStream** interface for the object. Use this interface to determine the stream's properties and enumerate the streams themselves. You can retrieve a specific stream by calling the [**IMultiMediaStream::GetMediaStream**](/windows/win32/mmstream/nf-mmstream-imultimediastream-getmediastream?branch=master) method with a specific purpose ID. MSPID\_PrimaryVideo and MSPID\_PrimaryAudio, which represent the primary video and audio streams, are the most commonly used purpose IDs.
3.  Call **IUnknown::QueryInterface** for an interface specific to the stream's media type. If you want to render a video stream, for example, retrieve its [**IDirectDrawMediaStream**](/windows/win32/ddstream/nn-ddstream-idirectdrawmediastream?branch=master) interface. Media-specific interfaces define additional methods necessary for taking full advantage of a format's capabilities.
4.  Create one or more samples from the stream data. Every media stream supports the [**IMediaStream::CreateSharedSample**](/windows/win32/mmstream/nf-mmstream-imediastream-createsharedsample?branch=master) method for sample creation. The resulting sample supports the [**IStreamSample**](/windows/win32/mmstream/nn-mmstream-istreamsample?branch=master) interface, which provides control over the sample and its characteristics. Typically, the media stream supports a format-specific method of sample creation that is more powerful than the aforementioned **IStreamSample** methods. **IDirectDrawMediaStream**, for example, can create samples attached to a desired DirectDraw surface and clipping rectangle. In some situations, however, you must handle data without knowing about its data format. If you want to stream data independent of its format, use the **IMediaStream::CreateSharedSample** method to create the data samples.
5.  After creating all desired stream samples, start the stream by calling the [**IMultiMediaStream::SetState**](/windows/win32/mmstream/nf-mmstream-imultimediastream-setstate?branch=master) method and pass in the STREAMSTATE\_RUN flag as its parameter.
6.  Call [**IStreamSample::Update**](/windows/win32/mmstream/nf-mmstream-istreamsample-update?branch=master) to update the stream sample. When the **IStreamSample::Update** method exits, you can access the sample's data. If you want a trigger a specific event or function call when the update returns, pass the appropriate pointers to the **IStreamSample::Update** method.

For more information on the multimedia streaming interfaces, see [Multimedia Streaming](multimedia-streaming.md).

 

 



