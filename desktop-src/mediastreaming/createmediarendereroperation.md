---
title: CreateMediaRendererOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by CreateMediaRendererAsync or CreateMediaRendererFromBasicDeviceAsync completes, and provides a method that returns the results of the operation.
ms.assetid: 0BC87D9E-5285-4F98-96B4-C841DDECBBE0
keywords:
- CreateMediaRendererOperation class Media Streaming API
- CreateMediaRendererOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- CreateMediaRendererOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# CreateMediaRendererOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when the asynchronous operation started by [**CreateMediaRendererAsync**](imediarendererfactory-createmediarendererasync.md) or [**CreateMediaRendererFromBasicDeviceAsync**](imediarendererfactory-createmediarendererfrombasicdeviceasync.md) completes, and provides a method that returns the results of the operation.

**CreateMediaRendererOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CreateMediaRendererOperation** class has these methods.



| Method                                                        | Description                                                 |
|:--------------------------------------------------------------|:------------------------------------------------------------|
| [**GetResults**](createmediarendereroperation-getresults.md) | Gets the results of the asynchronous operation. <br/> |



 

### Properties

The **CreateMediaRendererOperation** class has these properties.



| Property                                                               | Access type           | Description                                                                                                                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](createmediarendereroperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**CreateMediaRendererAsync**](imediarendererfactory-createmediarendererasync.md) or [**CreateMediaRendererFromBasicDeviceAsync**](imediarendererfactory-createmediarendererfrombasicdeviceasync.md) is completed. <br/> |



 

 

 





