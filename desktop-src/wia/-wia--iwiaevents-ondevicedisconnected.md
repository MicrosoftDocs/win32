---
description: Event that occurs when a new Windows Image Acquisition (WIA) hardware device is disconnected.
ms.assetid: 9c3ccdba-288c-4bdd-b257-b03999bc6fd9
title: Wia.OnDeviceDisconnected event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Wia.OnDeviceDisconnected
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Wia.OnDeviceDisconnected event

Event that occurs when a new Windows Image Acquisition (WIA) hardware device is disconnected.

## Syntax


```JScript
Wia.OnDeviceDisconnected(
  Id
)
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

A string that contains the ID of the connected device.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

WIA notifies the script or application whenever a hardware device is disconnected from the computer. Implement the **objWia**\_**OnDeviceDisconnected()** subroutine to allow the script or application to respond to the device disconnection.

For example, you might want a script to refresh the [**Devices**](-wia-iwia-devices.md) collection when a device is removed from the computer.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




