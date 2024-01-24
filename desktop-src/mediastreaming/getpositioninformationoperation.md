---
title: GetPositionInformationOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetPositionInformationAsync completes, and provides a method that returns the results of the operation.
ms.assetid: 57DDE3B2-EFA9-4FEB-B701-D987C58F5CEA
keywords:
- GetPositionInformationOperation class Media Streaming API
- GetPositionInformationOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- GetPositionInformationOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetPositionInformationOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when the asynchronous operation started by [**GetPositionInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getpositioninformationasync) completes, and provides a method that returns the results of the operation.

**GetPositionInformationOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **GetPositionInformationOperation** class has these methods.



| Method                                                           | Description                                                                                                                                                 |
|:-----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](getpositioninformationoperation-getresults.md) | Returns the results of the asynchronous operation started by [**GetPositionInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getpositioninformationasync). <br/> |



 

### Properties

The **GetPositionInformationOperation** class has these properties.



| Property                                                                  | Access type           | Description                                                                                                                                                                                          |
|:--------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](getpositioninformationoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetPositionInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getpositioninformationasync) is completed. <br/> |



 

 

