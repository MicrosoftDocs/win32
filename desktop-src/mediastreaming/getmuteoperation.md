---
title: GetMuteOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetMuteAsync completes, and provides a method that returns the results of the operation. | GetMuteOperation class
ms.assetid: 691D4936-604A-496F-B62E-FB36B406F0DD
keywords:
- GetMuteOperation class Media Streaming API
- GetMuteOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- GetMuteOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetMuteOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getmuteasync) completes, and provides a method that returns the results of the operation.

**GetMuteOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **GetMuteOperation** class has these methods.



| Method                                            | Description                                                                                                                   |
|:--------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](getmuteoperation-getresults.md) | Returns the results of the asynchronous operation started by [**GetMuteAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getmuteasync). <br/> |



 

### Properties

The **GetMuteOperation** class has these properties.



| Property                                                   | Access type           | Description                                                                                                                                                            |
|:-----------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](getmuteoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getmuteasync) is completed. <br/> |



 

 

