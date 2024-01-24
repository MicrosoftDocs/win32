---
title: GetStreamPropertiesOperation class
description: Registers an event handler that is invoked when the asynchronous operation started by GetStreamPropertiesAsync completes, and provides a method that returns the results of the operation.
ms.assetid: 1D1C9B73-9D7B-4886-AFA4-D35DF10367CD
keywords:
- GetStreamPropertiesOperation class Media Streaming API
- GetStreamPropertiesOperation class Media Streaming API , described
topic_type:
- apiref
api_name:
- GetStreamPropertiesOperation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetStreamPropertiesOperation class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Registers an event handler that is invoked when the asynchronous operation started by [**GetStreamPropertiesAsync**](/previous-versions/windows/desktop/legacy/hh829001(v=vs.85)) completes, and provides a method that returns the results of the operation.

**GetStreamPropertiesOperation** has these types of members:

-   [Methods](#methods)
-   [Properties](#getstreampropertiesoperation-class)

### Methods

The **GetStreamPropertiesOperation** class has these methods.



| Method                                                        | Description                                                                                                                                          |
|:--------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetResults**](getstreampropertiesoperation-getresults.md) | Returns the results of the asynchronous operation started by [**GetStreamPropertiesAsync**](/previous-versions/windows/desktop/legacy/hh829001(v=vs.85)).<br/> |



 

### Properties

The **GetStreamPropertiesOperation** class has these properties.



| Property                                                               | Access type           | Description                                                                                                                                                                                   |
|:-----------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Completed**](getstreampropertiesoperation-completed.md)<br/> | Read/write<br/> | Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetStreamPropertiesAsync**](/previous-versions/windows/desktop/legacy/hh829001(v=vs.85)) is completed.<br/> |



 

 

