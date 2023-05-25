---
title: BasicDevice.RemoteStreamingUrls property
description: Gets a vector of remote streaming URLs.
ms.assetid: E0F05E04-FED0-42E7-BC42-AFFA9780C366
keywords:
- RemoteStreamingUrls property Media Streaming API
- RemoteStreamingUrls property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , RemoteStreamingUrls property
topic_type:
- apiref
api_name:
- BasicDevice.RemoteStreamingUrls
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.RemoteStreamingUrls property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a vector of remote streaming URLs.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteStreamingUrls(
  [out] IVector< HSTRING > **value
);
```



## Property value

An enumerable collection of pointers to remote streaming URLs.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 