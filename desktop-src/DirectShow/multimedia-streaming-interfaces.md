---
description: Multimedia Streaming Interfaces
ms.assetid: '53d639e2-8717-4552-b0d3-b8c500bd38a8'
title: Multimedia Streaming Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Multimedia Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This section contains reference entries for all the multimedia streaming interfaces and their methods, including those that Microsoft DirectShow supports.



| Interface                                                  | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAMMediaStream**](/previous-versions/windows/desktop/api/amstream/nn-amstream-iammediastream)                   | Handles the internal connections between DirectShow filters and filter graphs in applications that use multimedia streaming.                            |
| [**IAMMediaTypeSample**](/previous-versions/windows/desktop/api/amstream/nn-amstream-iammediatypesample)           | Contains methods for manipulating stream samples with arbitrary media types.                                                                            |
| [**IAMMediaTypeStream**](/previous-versions/windows/desktop/api/amstream/nn-amstream-iammediatypestream)           | Contains methods for creating multimedia streams with arbitrary media types.                                                                            |
| [**IAMMultiMediaStream**](/previous-versions/windows/desktop/api/amstream/nn-amstream-iammultimediastream)         | Exposes DirectShow functionality to multimedia stream developers.                                                                                       |
| [**IAudioData**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiodata)                           | Provides methods that enable applications to set and get the underlying audio data that audio streams will reference.                                   |
| [**IAudioMediaStream**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiomediastream)             | Controls audio media streams by providing methods that set and get the stream's format.                                                                 |
| [**IAudioStreamSample**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiostreamsample)           | Retrieves information from the underlying [**IAudioData**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiodata) data objects.                                                                |
| [**IDirectDrawMediaStream**](/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawmediastream)   | Controls media streams that appear on Microsoft® DirectDraw® surfaces.                                                                                  |
| [**IDirectDrawStreamSample**](/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawstreamsample) | Provides methods that set and retrieve pointers to the DirectDraw surface associated with the current stream sample.                                    |
| [**IMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream)                       | Provides access to the characteristics of a media stream, such as the stream's media type and purpose ID. It also has methods that create data samples. |
| [**IMediaStreamFilter**](/previous-versions/windows/desktop/api/amstream/nn-amstream-imediastreamfilter)           | Supported by the Media Stream filter, which is used internally by the multimedia stream object. .                                                       |
| [**IMemoryData**](/previous-versions/windows/desktop/api/austream/nn-austream-imemorydata)                         | Contains methods that set and retrieve memory data on audio data objects.                                                                               |
| [**IMultiMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imultimediastream)             | Provides methods that control a multimedia stream and provide access to its underlying media streams.                                                   |
| [**IStreamSample**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-istreamsample)                     | Provides control over the behavior of stream samples.                                                                                                   |



 

 

 



