---
title: MediaRenderer.ActionInformation property
description: Gets information about which methods can currently be invoked on the DMR.
ms.assetid: 'c36d45cb-c01a-4418-8f21-906c95950d6f'
keywords:
- ActionInformation property Media Streaming API
- ActionInformation property Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , ActionInformation property
topic_type:
- apiref
api_name:
- MediaRenderer.ActionInformation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MediaRenderer.ActionInformation property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets information about which methods can currently be invoked on the DMR.

This property is read-only.

## Syntax


```C++
HRESULT get_ActionInformation(
  [out] IMediaRendererActionInformation **value
);
```



## Property value

A reference to an [**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation) interface.

## See also

<dl> <dt>

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 