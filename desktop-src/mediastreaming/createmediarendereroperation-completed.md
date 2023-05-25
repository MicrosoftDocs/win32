---
title: CreateMediaRendererOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by CreateMediaRendererAsync or CreateMediaRendererFromBasicDeviceAsync is completed.
ms.assetid: B62CF929-13D0-4665-89E4-DEC48A38DDF7
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , CreateMediaRendererOperation interface
- CreateMediaRendererOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- CreateMediaRendererOperation.Completed
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# CreateMediaRendererOperation.Completed property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets or sets an event handler that is invoked when the asynchronous operation started by [**CreateMediaRendererAsync**](imediarendererfactory-createmediarendererasync.md) or [**CreateMediaRendererFromBasicDeviceAsync**](imediarendererfactory-createmediarendererfrombasicdeviceasync.md) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  ICreateMediaRendererCompletedHandler value
);

HRESULT get_Completed(
  [out] ICreateMediaRendererCompletedHandler *value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**CreateMediaRendererOperation**](createmediarendereroperation.md)
</dt> </dl>

 

 




