---
title: DeviceDeparture event
description: Occurs when a new device is removed from the list of devices returned by the CachedDevices method.
ms.assetid: '3ABA1C74-228C-46AF-9743-CC5F4345A974'
keywords: ["DeviceDeparture event Media Streaming API"]
topic_type:
- apiref
api_name:
- DeviceDeparture
api_type:
- COM
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

To handle notifications from this event, register a [**DeviceControllerFinderHandler**](devicecontrollerfinderhandler.md) event handler function using the [**add\_DeviceDeparture**](idevicecontroller-add-devicedeparture.md) method. To unregister the event handler, use the [**remove\_DeviceDeparture**](idevicecontroller-remove-devicedeparture.md) method.

 

 




