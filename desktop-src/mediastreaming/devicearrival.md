---
title: DeviceArrival event
description: Occurs when a new device is added to the list of devices returned by the CachedDevices method.
ms.assetid: 'C7CB49AE-C05F-4A2A-8A30-4B4BB7C7D9D2'
keywords: ["DeviceArrival event Media Streaming API"]
topic_type:
- apiref
api_name:
- DeviceArrival
api_type:
- COM
---

# DeviceArrival event

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

To handle notifications from this event, register a [**DeviceControllerFinderHandler**](devicecontrollerfinderhandler.md) event handler function using the [**add\_DeviceArrival**](idevicecontroller-add-devicearrival.md) method. To unregister the event handler, use the [**remove\_DeviceArrival**](idevicecontroller-remove-devicearrival.md) method.

 

 




