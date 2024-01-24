---
title: BasicDevice.PresentationUrl property
description: Gets the presentation URL of the device.
ms.assetid: 106892F9-2F2D-4B44-A6A0-D0CC36E21117
keywords:
- PresentationUrl property Media Streaming API
- PresentationUrl property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , PresentationUrl property
topic_type:
- apiref
api_name:
- BasicDevice.PresentationUrl
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.PresentationUrl property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the presentation URL of the device.

This property is read-only.

## Syntax


```C++
HRESULT get_PresentationUrl(
  [out] HSTRING *value
);
```



## Property value

A pointer to the device’s presentation URL.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 