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
ms.topic: article
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

To handle notifications from this event, register a [**DeviceControllerFinderHandler**](https://msdn.microsoft.com/en-us/library/Hh828843(v=VS.85).aspx) event handler function using the [**add\_DeviceDeparture**](https://msdn.microsoft.com/en-us/library/Hh828904(v=VS.85).aspx) method. To unregister the event handler, use the [**remove\_DeviceDeparture**](https://msdn.microsoft.com/en-us/library/Hh828908(v=VS.85).aspx) method.

 

 




