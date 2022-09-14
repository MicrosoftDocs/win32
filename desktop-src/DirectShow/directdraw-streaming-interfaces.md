---
description: DirectDraw Streaming Interfaces
ms.assetid: 8f91d90d-0b9f-4d04-bc10-4b82c1b0e062
title: DirectDraw Streaming Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# DirectDraw Streaming Interfaces

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

If you use DirectDraw-supported video formats in your streams, the following interfaces give you more powerful control over the data than the more generic base interfaces.



| Interface                                                  | Description                                                                                                                                                                                                                 |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDirectDrawMediaStream**](/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawmediastream)   | Sets and retrieves the stream format and the DirectDraw object associated with the media stream; this interface derives from [**IMediaStream**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-imediastream). You can also use this interface to create video samples. |
| [**IDirectDrawStreamSample**](/previous-versions/windows/desktop/api/ddstream/nn-ddstream-idirectdrawstreamsample) | Enables you to attach video samples to DirectDraw surfaces; this interface derives from the [**IStreamSample**](/previous-versions/windows/desktop/api/mmstream/nn-mmstream-istreamsample) interface. Each attached surface includes a clipping rectangle to make rendering easier. |



 

## Related topics

<dl> <dt>

[List of Multimedia Streaming Interfaces](list-of-multimedia-streaming-interfaces.md)
</dt> </dl>

 

 



