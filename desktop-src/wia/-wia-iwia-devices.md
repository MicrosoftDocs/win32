---
description: Collection of DeviceInfo objects that represents all of the devices installed on the computer.
ms.assetid: 2f124188-2b66-46cc-9b26-bfef3709a1af
title: Wia.Devices property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Wia.Devices
- SafeWia.Devices
api_type: 
- COM
api_location: 
- Wiascr.dll
api_location: 
- Wiascr.dll
---

# Wia.Devices property

Collection of [**DeviceInfo**](-wia-deviceinfo.md) objects that represents all of the devices installed on the computer. Read-only.

> [!Note]  
> This collection is 0-based.

 

This property is read-only.

## Syntax


```JScript
propVal = Wia.Devices
```



## Property value

## Examples

The following example illustrates the use of the **Devices** collection to enumerate the devices on a system.


```JScript
<SCRIPT LANGUAGE = "VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
 
Set objWia = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    ! Do something with the DeviceInfo object
Next
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




