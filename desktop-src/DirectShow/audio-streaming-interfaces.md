---
Description: Audio Streaming Interfaces
ms.assetid: eaf510ef-a6a3-45e0-8f0a-281a44b0ff6f
title: Audio Streaming Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 



| Interface                                        | Description                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioMediaStream**](/windows/win32/austream/nn-austream-iaudiomediastream?branch=master)   | Controls audio media streams. This interface inherits from the [**IMediaStream**](/windows/win32/mmstream/nn-mmstream-imediastream?branch=master) interface and is used to create one or more [**IAudioStreamSample**](/windows/win32/austream/nn-austream-iaudiostreamsample?branch=master) objects. It is also used to set and retrieve the current format of the stream data.                                                                                                            |
| [**IAudioStreamSample**](/windows/win32/austream/nn-austream-iaudiostreamsample?branch=master) | Retrieves information from the underlying [**IAudioData**](/windows/win32/austream/nn-austream-iaudiodata?branch=master) data objects.                                                                                                                                                                                                                                                                                                        |
| [**IMemoryData**](/windows/win32/austream/nn-austream-imemorydata?branch=master)               | Contains methods that set and retrieve memory data on audio data objects. Audio data objects provide the underlying data that stream samples access. This interface provides a way to initialize memory buffers and to set actual amounts of audio data in the objects. Additionally, the [**IMemoryData::GetInfo**](/windows/win32/austream/nf-austream-imemorydata-getinfo?branch=master) method can be used to retrieve audio memory data. |
| [**IAudioData**](/windows/win32/austream/nn-austream-iaudiodata?branch=master)                 | Provides methods that enable applications to set and get the underlying audio data that audio streams will reference. The audio data format is set in the [**WAVEFORMATEX**](/windows/win32/mmreg/?branch=master) structure.                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[List of Multimedia Streaming Interfaces](list-of-multimedia-streaming-interfaces.md)
</dt> </dl>

 

 



