---
title: MediaRenderer.IsImageSupported property
description: Gets a value that indicates whether the DMR is capable of displaying images.
ms.assetid: '3e356ccc-1165-4eaa-9f6e-3332ea84a133'
keywords:
- IsImageSupported property Media Streaming API
- IsImageSupported property Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , IsImageSupported property
topic_type:
- apiref
api_name:
- MediaRenderer.IsImageSupported
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MediaRenderer.IsImageSupported property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a value that indicates whether the DMR is capable of displaying images.

This property is read-only.

## Syntax


```C++
HRESULT get_IsImageSupported(
  [out] boolean *value
);
```



## Property value

A boolean value that is **True** if the DMR is capable of displaying images and **False** if it is not.

## See also

<dl> <dt>

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 




