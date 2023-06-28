---
title: PlaybackOperation class
description: Registers an event handler that is invoked when an asynchronous operation started by one of the MediaRenderer playback methods completes, and provides a method that returns the results of the operation.
ms.assetid: 4899254A-C393-4D03-970F-CF272F4761B6
keywords:
- PlaybackOperation class Media Streaming API
- PlaybackOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- PlaybackOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PlaybackOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when an asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods completes, and provides a method that returns the results of the operation.

**PlaybackOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **PlaybackOperation** class has these methods.



| Method                                             | Description                                                                                                                                |
|:---------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](playbackoperation-getresults.md) | Returns the results of an asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods.<br/> |



 

### Properties

The **PlaybackOperation** class has these properties.



| Property                                                    | Access type           | Description                                                                                                                                                                           |
|:------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](playbackoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods is completed. <br/> |



 

 

 





