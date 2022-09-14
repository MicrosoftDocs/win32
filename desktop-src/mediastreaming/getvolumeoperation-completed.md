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
ms.date: 05/31/2018
api_location: 
---

# GetVolumeOperation.Completed property

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

 

 