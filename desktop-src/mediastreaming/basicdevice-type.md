---
title: BasicDevice.Type property
description: Gets an enumeration value indicating the device type of the DLNA device.
ms.assetid: 3689EA76-6876-463C-A6B3-8FBD5DB638A3
keywords:
- Type property Media Streaming API
- Type property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , Type property
topic_type:
- apiref
api_name:
- BasicDevice.Type
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.Type property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets an enumeration value indicating the device type of the DLNA device.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out] DeviceTypes *value
);
```



## Property value

A pointer to a [**DeviceTypes**](devicetypes.md) value.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 