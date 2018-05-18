---
title: DeviceInfo object
description: Describes the unchanging (static) properties of an imaging device that is currently connected to the computer.
ms.assetid: 'aaaa3df8-839d-4243-a482-efa7e88f16cc'
keywords: ["DeviceInfo object WIA Automation", "DeviceInfo object WIA Automation , described"]
topic_type:
- apiref
api_name:
- DeviceInfo
api_location:
- Wiaaut.h
api_type:
- COM
---

# DeviceInfo object

Describes the unchanging (static) properties of an imaging device that is currently connected to the computer.

## Members

The **DeviceInfo** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **DeviceInfo** object has these methods.



| Method                                         | Description                                        |
|:-----------------------------------------------|:---------------------------------------------------|
| [**Connect**](-wiaaut-ideviceinfo-connect.md) | Establishes a connection with a device.<br/> |



 

### Properties

The **DeviceInfo** object has these properties.



| Property                                                                     | Access type          | Description                                                                                                                       |
|:-----------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**DeviceID (DeviceInfo)**](-wiaaut-ideviceinfo-deviceid.md)<br/>     | Read-only<br/> | Retrieves the [**DeviceID (DeviceInfo)**](-wiaaut-ideviceinfo-deviceid.md) for this **DeviceInfo** object.<br/>            |
| [**Properties (DeviceInfo)**](-wiaaut-ideviceinfo-properties.md)<br/> | Read-only<br/> | Retrieves a collection of all properties for this imaging device that are applicable when the device is not connected.<br/> |
| [**Type (DeviceInfo)**](-wiaaut-ideviceinfo-type.md)<br/>             | Read-only<br/> | Retrieves the type of **DeviceInfo** object.<br/>                                                                           |



 

## Remarks

You can use the [**Connect**](-wiaaut-ideviceinfo-connect.md) method to get an active connection to the imaging device described in this **DeviceInfo** object.

For example code, see [List all Available Devices by Name and DeviceID](-wiaaut-shared-samples.md#list-all-available-devices-by-name-and-deviceid) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Item (DeviceInfos)**](-wiaaut-ideviceinfos-item.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item (DeviceInfos)**](-wiaaut-ideviceinfos-item.md)
</dt> </dl>

 

 





