---
description: The Create method of the DeviceInfo object makes a connection to the Windows Image Acquisition (WIA) device specified by the DeviceInfo object, and returns an Item object that represents the device.
ms.assetid: 57f3698c-3f9f-4775-8b53-a65a5591aa3d
title: DeviceInfo.Create method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeviceInfo.Create
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# DeviceInfo.Create method

The **Create** method of the [**DeviceInfo**](-wia-deviceinfo.md) object makes a connection to the Windows Image Acquisition (WIA) device specified by the **DeviceInfo** object, and returns an [**Item**](-wia-item.md) object that represents the device.

## Syntax


```JScript
retVal = DeviceInfo.Create()
```



## Parameters

This method has no parameters.

## Return value

Type: **IWiaDispatchItem**

This method returns the [**Item**](-wia-item.md) object that represents the device that is created.

## Remarks

Use the **Create** method to create a connection to a WIA hardware device after enumerating the [**Devices**](-wia-iwia-devices.md) collection. The method returns an [**Item**](-wia-item.md) object that represents the device (a root item).

## Examples

The following example demonstrates the use of the **Create** method.


```JScript
<SCRIPT LANGUAGE="VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim objItem
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    Set objItem = objDeviceInfo.Create()
Next
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




