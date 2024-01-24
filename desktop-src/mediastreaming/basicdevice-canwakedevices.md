---
title: BasicDevice.CanWakeDevices property
description: Gets a value that indicates if the device can wake.
ms.assetid: 0BF0B2CD-E09E-4A0B-9D48-A980CBFE4233
keywords:
- CanWakeDevices property Media Streaming API
- CanWakeDevices property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , CanWakeDevices property
topic_type:
- apiref
api_name:
- BasicDevice.CanWakeDevices
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.CanWakeDevices property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a value that indicates if the device can wake.

This property is read-only.

## Syntax


```C++
HRESULT get_CanWakeDevices(
  [out] boolean *value
);
```



## Property value

A pointer to a boolean value that is **True** if the device can wake.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 