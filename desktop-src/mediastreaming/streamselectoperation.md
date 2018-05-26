---
title: StreamSelectOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetMuteAsync completes, and provides a method that returns the results of the operation.
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
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StreamSelectOperation class

Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](imediarenderer-getmuteasync.md) completes, and provides a method that returns the results of the operation.

**StreamSelectOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **StreamSelectOperation** class has these methods.



| Method                                                 | Description                                                                                                                                       |
|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](streamselectoperation-getresults.md) | Returns the results of the asynchronous operation started by [**SelectBestStreamAsync**](streamselector-getstreampropertiesasync.md).<br/> |



 

### Properties

The **StreamSelectOperation** class has these properties.



| Property                                                        | Access type           | Description                                                                                                                                                                             |
|:----------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](streamselectoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**SelectBestStreamAsync**](streamselector-selectbeststreamasync.md) is completed.<br/> |



 

 

 





