---
title: MediaRenderer.IsVideoSupported property
description: Gets a value that indicates whether the DMR is capable of playing video content.
ms.assetid: '09fee4e2-7ea4-45b6-944c-39bed030866d'
keywords:
- IsVideoSupported property Media Streaming API
- IsVideoSupported property Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , IsVideoSupported property
topic_type:
- apiref
api_name:
- MediaRenderer.IsVideoSupported
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MediaRenderer.IsVideoSupported property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a value that indicates whether the DMR is capable of playing video content.

This property is read-only.

## Syntax


```C++
HRESULT get_IsVideoSupported(
  [out] boolean *value
);
```



## Property value

A boolean value that is **True** if the DMR is capable of playing video content and **False** if it is not.

## See also

<dl> <dt>

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 




