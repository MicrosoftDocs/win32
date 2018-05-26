---
title: Device.onDeviceUpdated event
description: The onDeviceUpdated event occurs when the device has been updated, such as when a device property has been changed.
ms.assetid: 9b0e82d1-7fc4-40f8-9ec5-ef88ffb56731
keywords:
- onDeviceUpdated event WPD Automation
- onDeviceUpdated event WPD Automation , Device object
- Device object WPD Automation , onDeviceUpdated event
topic_type:
- apiref
api_name:
- Device.onDeviceUpdated
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device.onDeviceUpdated event

The **onDeviceUpdated** event occurs when the device has been updated, such as when a device property has been changed.

## Syntax


```JScript
Device.onDeviceUpdated()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples

The following JScript example shows how to set and trigger an event handler for the **onDeviceUpdated** event.


```JScript
// Event handler for onDeviceUpdated.
function HandleDeviceUpdated()
{
    Alert("onDeviceUpdated Event Handler: Device updated successfully.");
}

// Set the event handler.
try
{
    deviceObject.onDeviceUpdated = HandleDeviceUpdated;
}
catch(e)
{
    Alert("Device object does not support the onDeviceUpdated event.");
}

// Trigger the event handler by updating the DeviceFriendlyName
// property.
var oldName = deviceObject.DeviceFriendlyName; 
var newName = "DeviceUpdated-Event-Name";
deviceObject.DeviceFriendlyName = newName;

// Clear the event handler object and restore the DeviceFriendlyName.
deviceObject.onDeviceUpdated = null;
deviceObject.DeviceFriendlyName = oldName;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Device Object**](device-object.md)
</dt> </dl>

 

 





