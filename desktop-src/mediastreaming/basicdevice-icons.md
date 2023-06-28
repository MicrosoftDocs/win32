---
title: BasicDevice.Icons property
description: Gets a vector of IDeviceIcon interfaces.
ms.assetid: 54933FD0-27A6-48D8-A49A-200AD9214B9A
keywords:
- Icons property Media Streaming API
- Icons property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , Icons property
topic_type:
- apiref
api_name:
- BasicDevice.Icons
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.Icons property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a vector of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interfaces.

This property is read-only.

## Syntax


```C++
HRESULT get_Icons(
  [out] IVector< IDeviceIcon > **value
);
```



## Property value

An enumerable collection of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interface pointers.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 