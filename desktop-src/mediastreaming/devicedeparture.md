---
title: DeviceDeparture event
description: Occurs when a new device is removed from the list of devices returned by the CachedDevices method.
ms.assetid: '10451878-e685-4042-9f92-ba3a408c4da0'
keywords:
- DeviceDeparture event Media Streaming API
topic_type:
- apiref
api_name:
- DeviceDeparture
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DeviceDeparture event

Occurs when a new device is removed from the list of devices returned by the [**CachedDevices**](idevicecontroller-cacheddevices.md) method.

## Syntax


```C++
void DeviceDeparture();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

To handle notifications from this event, register a [**DeviceControllerFinderHandler**](/previous-versions/windows/desktop/legacy/hh828843(v=vs.85)) event handler function using the [**add\_DeviceDeparture**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-idevicecontroller-add_devicedeparture) method. To unregister the event handler, use the [**remove\_DeviceDeparture**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-idevicecontroller-remove_devicedeparture) method.

 

 