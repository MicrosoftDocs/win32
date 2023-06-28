---
title: MediaRenderer.PauseAsync method
description: Instructs the DMR asynchronously to pause playing the current content. | MediaRenderer.PauseAsync method
ms.assetid: '1bd36349-0551-44e8-9550-3fd80900de9a'
keywords:
- PauseAsync method Media Streaming API
- PauseAsync method Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , PauseAsync method
topic_type:
- apiref
api_name:
- MediaRenderer.PauseAsync
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MediaRenderer.PauseAsync method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Instructs the DMR asynchronously to pause playing the current content.

## Syntax


```C++
HRESULT PauseAsync(
  [out] PlaybackOperation **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a reference to a [**PlaybackOperation**](playbackoperation.md) object that is used to get results from the asynchronous operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 





