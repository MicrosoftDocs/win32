---
title: GetVolumeOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by GetVolumeAsync is completed.
ms.assetid: 34100EE7-C4CB-4AE0-BD3E-9E23A643F87E
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , GetVolumeOperation interface
- GetVolumeOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- GetVolumeOperation.Completed
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetVolumeOperation.Completed property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetVolumeAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getvolumeasync) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  GetVolumeCompletedHandler *value
);

HRESULT get_Completed(
  [out] GetVolumeCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**GetVolumeOperation**](getvolumeoperation.md)
</dt> </dl>

 

 