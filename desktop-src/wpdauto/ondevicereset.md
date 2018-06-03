---
title: Device.onDeviceReset event
description: The onDeviceReset event occurs when the device is about to reset.
ms.assetid: d9cf8bbb-594c-4a41-a1f3-ff4ed21b6add
keywords:
- onDeviceReset event WPD Automation
- onDeviceReset event WPD Automation , Device object
- Device object WPD Automation , onDeviceReset event
topic_type:
- apiref
api_name:
- Device.onDeviceReset
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Device.onDeviceReset event

The **onDeviceReset** event occurs when the device is about to reset.

## Syntax


```JScript
Device.onDeviceReset()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples

The following JScript example shows how to set an event handler for the **onDeviceReset** event.


```JScript
// Event handler for onDeviceReset.
function HandleDeviceReset()
{
    Alert("onDeviceReset Event Handler: Device about to reset.");
}

// Set the event handler.
try
{
     deviceObject.onDeviceReset = HandleDeviceReset;
}
catch(e)
{
     Alert("Device object does not support onDeviceReset");
}

// 
// Reset device        
//

// Clear the event handler.
deviceObject.onDeviceReset = null;
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

 

 





