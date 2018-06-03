---
Description: Multimedia Streaming Interfaces
ms.assetid: a94dbb64-dfca-4c24-8c11-761835faf8a8
title: Multimedia Streaming Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Multimedia Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This section contains reference entries for all the multimedia streaming interfaces and their methods, including those that Microsoft DirectShow supports.



| Interface                                                  | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAMMediaStream**](/windows/desktop/api/amstream/nn-amstream-iammediastream)                   | Handles the internal connections between DirectShow filters and filter graphs in applications that use multimedia streaming.                            |
| [**IAMMediaTypeSample**](/windows/desktop/api/amstream/nn-amstream-iammediatypesample)           | Contains methods for manipulating stream samples with arbitrary media types.                                                                            |
| [**IAMMediaTypeStream**](/windows/desktop/api/amstream/nn-amstream-iammediatypestream)           | Contains methods for creating multimedia streams with arbitrary media types.                                                                            |
| [**IAMMultiMediaStream**](/windows/desktop/api/amstream/nn-amstream-iammultimediastream)         | Exposes DirectShow functionality to multimedia stream developers.                                                                                       |
| [**IAudioData**](/windows/desktop/api/austream/nn-austream-iaudiodata)                           | Provides methods that enable applications to set and get the underlying audio data that audio streams will reference.                                   |
| [**IAudioMediaStream**](/windows/desktop/api/austream/nn-austream-iaudiomediastream)             | Controls audio media streams by providing methods that set and get the stream's format.                                                                 |
| [**IAudioStreamSample**](/windows/desktop/api/austream/nn-austream-iaudiostreamsample)           | Retrieves information from the underlying [**IAudioData**](/windows/desktop/api/austream/nn-austream-iaudiodata) data objects.                                                                |
| [**IDirectDrawMediaStream**](/windows/desktop/api/ddstream/nn-ddstream-idirectdrawmediastream)   | Controls media streams that appear on Microsoft® DirectDraw® surfaces.                                                                                  |
| [**IDirectDrawStreamSample**](/windows/desktop/api/ddstream/nn-ddstream-idirectdrawstreamsample) | Provides methods that set and retrieve pointers to the DirectDraw surface associated with the current stream sample.                                    |
| [**IMediaStream**](/windows/desktop/api/mmstream/nn-mmstream-imediastream)                       | Provides access to the characteristics of a media stream, such as the stream's media type and purpose ID. It also has methods that create data samples. |
| [**IMediaStreamFilter**](/windows/desktop/api/amstream/nn-amstream-imediastreamfilter)           | Supported by the Media Stream filter, which is used internally by the multimedia stream object. .                                                       |
| [**IMemoryData**](/windows/desktop/api/austream/nn-austream-imemorydata)                         | Contains methods that set and retrieve memory data on audio data objects.                                                                               |
| [**IMultiMediaStream**](/windows/desktop/api/mmstream/nn-mmstream-imultimediastream)             | Provides methods that control a multimedia stream and provide access to its underlying media streams.                                                   |
| [**IStreamSample**](/windows/desktop/api/mmstream/nn-mmstream-istreamsample)                     | Provides control over the behavior of stream samples.                                                                                                   |



 

 

 



