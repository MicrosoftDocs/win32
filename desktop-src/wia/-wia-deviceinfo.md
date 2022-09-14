---
description: The DeviceInfo object provides access to the properties of a Windows Image Acquisition (WIA) hardware device.
ms.assetid: b3cf153b-76f8-4822-8d88-331ab91a1116
title: DeviceInfo object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeviceInfo
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# DeviceInfo object

The **DeviceInfo** object provides access to the properties of a Windows Image Acquisition (WIA) hardware device. It also, through its [**Create**](-wia-iwiadeviceinfo-create.md) method, provides a way for the application or script to connect to the device and obtain an [**Item**](-wia-item.md) object that represents the device. Use the [**Devices**](-wia-iwia-devices.md) method to obtain a collection of **DeviceInfo** objects.

## Members

The **DeviceInfo** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DeviceInfo** object has these methods.



| Method                                                 | Description                                                                                                                                                                                                                                              |
|:-------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Create**](-wia-iwiadeviceinfo-create.md)           | The [**Create**](-wia-iwiadeviceinfo-create.md) method of the **DeviceInfo** object makes a connection to the WIA device specified by the **DeviceInfo** object, and returns an [**Item**](-wia-item.md) object that represents the device.<br/> |
| [**GetPropById**](-wia-iwiadeviceinfo-getpropbyid.md) | The [**GetPropById**](-wia-iwiadeviceinfo-getpropbyid.md) method of the **DeviceInfo** object uses a device property's ID to return its value.<br/>                                                                                               |



 

### Properties

The **DeviceInfo** object has these properties.




| Property | Access type | Description | 
|----------|-------------|-------------|
| <a href="-wia-iwiadeviceinfo-id.md"><strong>Id</strong></a><br /> | Read-only<br /> | Retrieves the ID of the WIA hardware device. <br /> | 
| <a href="-wia-iwiadeviceinfo-manufacturer.md"><strong>Manufacturer</strong></a><br /> | Read-only<br /> | Retrieves the name of the manufacturer of this hardware device.<br /> | 
| <a href="-wia-iwiadeviceinfo-name.md"><strong>Name</strong></a><br /> | Read-only<br /> | The name of the WIA hardware device as it appears in the UI.<br /> | 
| <a href="-wia-iwiadeviceinfo-port.md"><strong>Port</strong></a><br /> | Read-only<br /> | Retrieves the port to which the WIA hardware device is connected.<br /> | 
| <a href="-wia-iwiadeviceinfo-type.md"><strong>Type</strong></a><br /> | Read-only<br /> | Retrieves the type of WIA hardware device. Possible values are: <br /><ul><li>DigitalCamera</li><li>Scanner</li><li>StreamingVideo</li><li>Default</li></ul> | 
| <a href="-wia-iwiadeviceinfo-uiclsid.md"><strong>UIClsid</strong></a><br /> | Read-only<br /> | Retrieves the class id of the manufacturer-provided user interface for this WIA hardware device. The value is a string representation of a GUID. <br /> | 




 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




