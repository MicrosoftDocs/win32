---
title: BasicDevice.SerialNumber property
description: Gets the serial number of the device.
ms.assetid: 3B290778-F3AE-4390-B90F-ED727649AF80
keywords:
- SerialNumber property Media Streaming API
- SerialNumber property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , SerialNumber property
topic_type:
- apiref
api_name:
- BasicDevice.SerialNumber
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.SerialNumber property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the serial number of the device.

This property is read-only.

## Syntax


```C++
HRESULT get_SerialNumber(
  [out] HSTRING *value
);
```



## Property value

A pointer to the device’s serial number.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 