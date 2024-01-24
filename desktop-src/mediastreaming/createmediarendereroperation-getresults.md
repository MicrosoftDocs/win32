---
title: CreateMediaRendererOperation GetResults method
description: Gets the results of the asynchronous operation.
ms.assetid: 02C5DCB9-5C0F-4C0C-9443-B97168B5CEBB
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , CreateMediaRendererOperation interface
- CreateMediaRendererOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- CreateMediaRendererOperation.GetResults
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# CreateMediaRendererOperation::GetResults method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the results of the asynchronous operation.

## Syntax


```C++
MediaRenderer* GetResults();
```



## Parameters

This method has no parameters.

## Return value

The results of the operation. A pointer to the newly created [**MediaRenderer**](mediarenderer.md) object.

## See also

<dl> <dt>

[**CreateMediaRendererOperation**](createmediarendereroperation.md)
</dt> </dl>

 

 




