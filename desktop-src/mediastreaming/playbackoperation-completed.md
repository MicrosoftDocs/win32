---
title: PlaybackOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by one of the MediaRenderer playback methods is completed.
ms.assetid: E8F8D3FC-C31F-485C-A30B-2457F4B1DE82
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , PlaybackOperation interface
- PlaybackOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- PlaybackOperation.Completed
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PlaybackOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  PlaybackOperationCompletedHandler *value
);

HRESULT get_Completed(
  [out] PlaybackOperationCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**PlaybackOperation**](playbackoperation.md)
</dt> </dl>

 

 




