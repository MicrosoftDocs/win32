---
title: GetTransportInformationOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetTransportInformationAsync completes, and provides a method that returns the results of the operation.
ms.assetid: EDB7E338-94E9-47DA-A95E-E49123655505
keywords:
- GetTransportInformationOperation class Media Streaming API
- GetTransportInformationOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- GetTransportInformationOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetTransportInformationOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when the asynchronous operation started by [**GetTransportInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-gettransportinformationasync) completes, and provides a method that returns the results of the operation.

**GetTransportInformationOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **GetTransportInformationOperation** class has these methods.



| Method                                                            | Description                                                                                                                                                  |
|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](gettransportinformationoperation-getresults.md) | Returns the results of the asynchronous operation started by [**GetTransportInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-gettransportinformationasync).<br/> |



 

### Properties

The **GetTransportInformationOperation** class has these properties.



| Property                                                                   | Access type           | Description                                                                                                                                                                                            |
|:---------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](gettransportinformationoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetTransportInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-gettransportinformationasync) is completed. <br/> |



 

 

