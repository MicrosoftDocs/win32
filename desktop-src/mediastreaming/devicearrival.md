---
title: DeviceArrival event
description: Occurs when a new device is added to the list of devices returned by the CachedDevices method.
ms.assetid: C7CB49AE-C05F-4A2A-8A30-4B4BB7C7D9D2
keywords:
- DeviceArrival event Media Streaming API
topic_type:
- apiref
api_name:
- DeviceArrival
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DeviceArrival event

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Occurs when a new device is added to the list of devices returned by the [**CachedDevices**](idevicecontroller-cacheddevices.md) method.

## Syntax


```C++
void DeviceArrival();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

To handle notifications from this event, register a [**DeviceControllerFinderHandler**](/previous-versions/windows/desktop/legacy/hh828843(v=vs.85)) event handler function using the [**add\_DeviceArrival**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-idevicecontroller-add_devicearrival) method. To unregister the event handler, use the [**remove\_DeviceArrival**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-idevicecontroller-remove_devicearrival) method.

 

 