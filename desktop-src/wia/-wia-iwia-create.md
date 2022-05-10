---
description: The Create method of the Wia object makes a connection to the specified Windows Image Acquisition (WIA) device, and returns an Item object that represents the device.
ms.assetid: c33c635a-159c-4ac3-8ad5-6f21a1986702
title: Wia.Create method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Wia.Create
- SafeWia.Create
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Wia.Create method

The **Create** method of the [**Wia**](-wia-wia.md) object makes a connection to the specified Windows Image Acquisition (WIA) device, and returns an [**Item**](-wia-item.md) object that represents the device.

## Syntax


```JScript
retVal = Wia.Create(
  Device
)
```



## Parameters

<dl> <dt>

*Device* \[in\]
</dt> <dd>

Type: **VARIANT\***

Specifies the WIA device to which to connect.

</dd> </dl>

## Return value

Type: **IWiaDispatchItem**

If successful, this method returns an [**Item**](-wia-item.md) object that represents a WIA hardware device (a root item).

## Remarks

The *Device* parameter specifies a [**DeviceInfo**](-wia-deviceinfo.md) object by passing the object itself, its index from a collection object, or the value of its [**Id**](-wia-iwiadeviceinfo-id.md) property. Pass **Nothing** to display a dialog box that allows a user to select a device.

## Examples

The following VBScript examples demonstrate the use of the **Create** method.

The first example passes a [**DeviceInfo**](-wia-deviceinfo.md) object to the **Create** method. Note that passing the object's [**Id**](-wia-iwiadeviceinfo-id.md) property causes exactly the same behavior.


```JScript
<SCRIPT LANGUAGE="VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim objItem
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    Set objItem = objWia.Create(objDeviceInfo)
Next
</SCRIPT>
```



In the next example, the calling application passes the index of the [**DeviceInfo**](-wia-deviceinfo.md) object in the collection to the **Create** method.


```JScript
<SCRIPT LANGUAGE = "VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objItem
 
Set objWia = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For i = 0 To objDeviceInfoCollection.Count-1
    Set objItem = objWia.Create(i)
Next
</SCRIPT>
```



The next example passes **Nothing** to the **Create** method to display a dialog box that allows a user to select a device.


```JScript
<SCRIPT LANGUAGE = "VBScript">
Dim objWia
Dim objItem
 
Set objWia = objWia.Create(Nothing)
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




