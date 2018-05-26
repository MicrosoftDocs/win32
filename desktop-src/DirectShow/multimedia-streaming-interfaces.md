---
Description: Multimedia Streaming Interfaces
ms.assetid: a94dbb64-dfca-4c24-8c11-761835faf8a8
title: Multimedia Streaming Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multimedia Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This section contains reference entries for all the multimedia streaming interfaces and their methods, including those that Microsoft DirectShow supports.



| Interface                                                  | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAMMediaStream**](/windows/win32/amstream/nn-amstream-iammediastream?branch=master)                   | Handles the internal connections between DirectShow filters and filter graphs in applications that use multimedia streaming.                            |
| [**IAMMediaTypeSample**](/windows/win32/amstream/nn-amstream-iammediatypesample?branch=master)           | Contains methods for manipulating stream samples with arbitrary media types.                                                                            |
| [**IAMMediaTypeStream**](/windows/win32/amstream/nn-amstream-iammediatypestream?branch=master)           | Contains methods for creating multimedia streams with arbitrary media types.                                                                            |
| [**IAMMultiMediaStream**](/windows/win32/amstream/nn-amstream-iammultimediastream?branch=master)         | Exposes DirectShow functionality to multimedia stream developers.                                                                                       |
| [**IAudioData**](/windows/win32/austream/nn-austream-iaudiodata?branch=master)                           | Provides methods that enable applications to set and get the underlying audio data that audio streams will reference.                                   |
| [**IAudioMediaStream**](/windows/win32/austream/nn-austream-iaudiomediastream?branch=master)             | Controls audio media streams by providing methods that set and get the stream's format.                                                                 |
| [**IAudioStreamSample**](/windows/win32/austream/nn-austream-iaudiostreamsample?branch=master)           | Retrieves information from the underlying [**IAudioData**](/windows/win32/austream/nn-austream-iaudiodata?branch=master) data objects.                                                                |
| [**IDirectDrawMediaStream**](/windows/win32/ddstream/nn-ddstream-idirectdrawmediastream?branch=master)   | Controls media streams that appear on Microsoft® DirectDraw® surfaces.                                                                                  |
| [**IDirectDrawStreamSample**](/windows/win32/ddstream/nn-ddstream-idirectdrawstreamsample?branch=master) | Provides methods that set and retrieve pointers to the DirectDraw surface associated with the current stream sample.                                    |
| [**IMediaStream**](/windows/win32/mmstream/nn-mmstream-imediastream?branch=master)                       | Provides access to the characteristics of a media stream, such as the stream's media type and purpose ID. It also has methods that create data samples. |
| [**IMediaStreamFilter**](/windows/win32/amstream/nn-amstream-imediastreamfilter?branch=master)           | Supported by the Media Stream filter, which is used internally by the multimedia stream object. .                                                       |
| [**IMemoryData**](/windows/win32/austream/nn-austream-imemorydata?branch=master)                         | Contains methods that set and retrieve memory data on audio data objects.                                                                               |
| [**IMultiMediaStream**](/windows/win32/mmstream/nn-mmstream-imultimediastream?branch=master)             | Provides methods that control a multimedia stream and provide access to its underlying media streams.                                                   |
| [**IStreamSample**](/windows/win32/mmstream/nn-mmstream-istreamsample?branch=master)                     | Provides control over the behavior of stream samples.                                                                                                   |



 

 

 



