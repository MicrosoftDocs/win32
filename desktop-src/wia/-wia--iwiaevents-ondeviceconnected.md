---
description: Event that occurs when a new Windows Image Acquisition (WIA) hardware device is connected.
ms.assetid: 327a29b8-581c-41b5-bea7-068bec95e653
title: Wia.OnDeviceConnected event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Wia.OnDeviceConnected
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Wia.OnDeviceConnected event

Event that occurs when a new Windows Image Acquisition (WIA) hardware device is connected.

## Syntax


```JScript
Wia.OnDeviceConnected(
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

WIA notifies the script or application whenever a new hardware device is connected to the computer. Implement the **objWia**\_**OnDeviceConnected()** subroutine to allow the script or application to respond to the device connection.

For example, you might want a script to refresh the [**Devices**](-wia-iwia-devices.md) collection when a new device is installed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




