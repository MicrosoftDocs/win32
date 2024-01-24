---
title: GetVolumeOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetVolumeAsync completes, and provides a method that returns the results of the operation.
ms.assetid: F7BCE2AB-89B5-44CE-8BDF-347F2E3FD6C9
keywords:
- GetVolumeOperation class Media Streaming API
- GetVolumeOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- GetVolumeOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetVolumeOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when the asynchronous operation started by [**GetVolumeAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getvolumeasync) completes, and provides a method that returns the results of the operation.

**GetVolumeOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **GetVolumeOperation** class has these methods.



| Method                                              | Description                                                                                                                      |
|:----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](getvolumeoperation-getresults.md) | Returns the results of the asynchronous operation started by [**GetVolumeAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getvolumeasync).<br/> |



 

### Properties

The **GetVolumeOperation** class has these properties.



| Property                                                     | Access type           | Description                                                                                                                                                                |
|:-------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](getvolumeoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetVolumeAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getvolumeasync) is completed. <br/> |



 

 

