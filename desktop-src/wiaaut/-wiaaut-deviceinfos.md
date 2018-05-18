---
title: DeviceInfos object
description: Contains a collection of all the imaging devices currently connected to the computer. For details on accessing the DeviceInfos object, see the DeviceInfos (DeviceManager) property on the DeviceManager object.
ms.assetid: '05cf6e48-5c3c-4d80-9d2e-f3701f3d93e4'
keywords: ["DeviceInfos object WIA Automation", "DeviceInfos object WIA Automation , described"]
topic_type:
- apiref
api_name:
- DeviceInfos
api_location:
- Wiaaut.h
api_type:
- COM
---

# DeviceInfos object

Contains a collection of all the imaging devices currently connected to the computer. For details on accessing the **DeviceInfos** object, see the [**DeviceInfos (DeviceManager)**](-wiaaut-idevicemanager-deviceinfos.md) property on the [**DeviceManager**](-wiaaut-devicemanager.md) object.

## Members

The **DeviceInfos** object has these types of members:

-   [Properties](#properties)

### Properties

The **DeviceInfos** object has these properties.



| Property                                                             | Access type          | Description                                                                                |
|:---------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------|
| [**Count (DeviceInfos)**](-wiaaut-ideviceinfos-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the collection.<br/>                              |
| [**Item (DeviceInfos)**](-wiaaut-ideviceinfos-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the collection either by position or device ID.<br/> |



 

## Remarks

Note that the **DeviceInfos** collection can be accessed by device ID and position.

The following lines do the same thing:


```
Dim d 'As Device
set d = DeviceManager1.DeviceInfos(1).Connect

MsgBox d.Properties("Name").Value & " was successfully created"
```



Or:


```
Dim d 'As Device
set d = DeviceManager1.DeviceInfos(DeviceManager1.DeviceInfos(1).DeviceID).Connect

MsgBox d.Properties("Name").Value & " was successfully created"
```



For more example code, see [List all Available Devices by Name and DeviceID](-wiaaut-shared-samples.md#list-all-available-devices-by-name-and-deviceid) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**DeviceInfos (DeviceManager)**](-wiaaut-idevicemanager-deviceinfos.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**DeviceInfos (DeviceManager)**](-wiaaut-idevicemanager-deviceinfos.md)
</dt> </dl>

 

 





