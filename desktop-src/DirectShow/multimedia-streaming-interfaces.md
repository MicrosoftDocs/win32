---
Description: Multimedia Streaming Interfaces
ms.assetid: 'a94dbb64-dfca-4c24-8c11-761835faf8a8'
title: Multimedia Streaming Interfaces
---

# Multimedia Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This section contains reference entries for all the multimedia streaming interfaces and their methods, including those that Microsoft DirectShow supports.



| Interface                                                  | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAMMediaStream**](iammediastream.md)                   | Handles the internal connections between DirectShow filters and filter graphs in applications that use multimedia streaming.                            |
| [**IAMMediaTypeSample**](iammediatypesample.md)           | Contains methods for manipulating stream samples with arbitrary media types.                                                                            |
| [**IAMMediaTypeStream**](iammediatypestream.md)           | Contains methods for creating multimedia streams with arbitrary media types.                                                                            |
| [**IAMMultiMediaStream**](iammultimediastream.md)         | Exposes DirectShow functionality to multimedia stream developers.                                                                                       |
| [**IAudioData**](iaudiodata.md)                           | Provides methods that enable applications to set and get the underlying audio data that audio streams will reference.                                   |
| [**IAudioMediaStream**](iaudiomediastream.md)             | Controls audio media streams by providing methods that set and get the stream's format.                                                                 |
| [**IAudioStreamSample**](iaudiostreamsample.md)           | Retrieves information from the underlying [**IAudioData**](iaudiodata.md) data objects.                                                                |
| [**IDirectDrawMediaStream**](idirectdrawmediastream.md)   | Controls media streams that appear on Microsoft® DirectDraw® surfaces.                                                                                  |
| [**IDirectDrawStreamSample**](idirectdrawstreamsample.md) | Provides methods that set and retrieve pointers to the DirectDraw surface associated with the current stream sample.                                    |
| [**IMediaStream**](imediastream.md)                       | Provides access to the characteristics of a media stream, such as the stream's media type and purpose ID. It also has methods that create data samples. |
| [**IMediaStreamFilter**](imediastreamfilter.md)           | Supported by the Media Stream filter, which is used internally by the multimedia stream object. .                                                       |
| [**IMemoryData**](imemorydata.md)                         | Contains methods that set and retrieve memory data on audio data objects.                                                                               |
| [**IMultiMediaStream**](imultimediastream.md)             | Provides methods that control a multimedia stream and provide access to its underlying media streams.                                                   |
| [**IStreamSample**](istreamsample.md)                     | Provides control over the behavior of stream samples.                                                                                                   |



 

 

 



