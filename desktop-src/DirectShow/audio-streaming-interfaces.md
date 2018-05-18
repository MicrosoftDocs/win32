---
Description: Audio Streaming Interfaces
ms.assetid: 'eaf510ef-a6a3-45e0-8f0a-281a44b0ff6f'
title: Audio Streaming Interfaces
---

# Audio Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 



| Interface                                        | Description                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAudioMediaStream**](iaudiomediastream.md)   | Controls audio media streams. This interface inherits from the [**IMediaStream**](imediastream.md) interface and is used to create one or more [**IAudioStreamSample**](iaudiostreamsample.md) objects. It is also used to set and retrieve the current format of the stream data.                                                                                                            |
| [**IAudioStreamSample**](iaudiostreamsample.md) | Retrieves information from the underlying [**IAudioData**](iaudiodata.md) data objects.                                                                                                                                                                                                                                                                                                        |
| [**IMemoryData**](imemorydata.md)               | Contains methods that set and retrieve memory data on audio data objects. Audio data objects provide the underlying data that stream samples access. This interface provides a way to initialize memory buffers and to set actual amounts of audio data in the objects. Additionally, the [**IMemoryData::GetInfo**](imemorydata-getinfo.md) method can be used to retrieve audio memory data. |
| [**IAudioData**](iaudiodata.md)                 | Provides methods that enable applications to set and get the underlying audio data that audio streams will reference. The audio data format is set in the [**WAVEFORMATEX**](waveformatex.md) structure.                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[List of Multimedia Streaming Interfaces](list-of-multimedia-streaming-interfaces.md)
</dt> </dl>

 

 



