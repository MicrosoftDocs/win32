---
title: BasicDevice.FriendlyName property
description: Gets the friendly name of the device.
ms.assetid: C17143AD-845B-4665-B765-A1FB0D135F84
keywords:
- FriendlyName property Media Streaming API
- FriendlyName property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , FriendlyName property
topic_type:
- apiref
api_name:
- BasicDevice.FriendlyName
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.FriendlyName property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the friendly name of the device.

This property is read-only.

## Syntax


```C++
HRESULT get_FriendlyName(
  [out] HSTRING *value
);
```



## Property value

A pointer to the device’s friendly name.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 