---
title: StreamSelectOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetMuteAsync completes, and provides a method that returns the results of the operation. | StreamSelectOperation class
ms.assetid: 681142B4-AECD-42D0-A2D4-494E69A29025
keywords:
- StreamSelectOperation class Media Streaming API
- StreamSelectOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- StreamSelectOperation
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StreamSelectOperation class

Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getmuteasync) completes, and provides a method that returns the results of the operation.

**StreamSelectOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **StreamSelectOperation** class has these methods.



| Method                                                 | Description                                                                                                                                       |
|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](streamselectoperation-getresults.md) | Returns the results of the asynchronous operation started by [**SelectBestStreamAsync**](/previous-versions/windows/desktop/legacy/hh829001(v=vs.85)).<br/> |



 

### Properties

The **StreamSelectOperation** class has these properties.



| Property                                                        | Access type           | Description                                                                                                                                                                             |
|:----------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](streamselectoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**SelectBestStreamAsync**](/previous-versions/windows/desktop/legacy/hh829002(v=vs.85)) is completed.<br/> |



 

 

