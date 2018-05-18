---
title: DeviceCommand object
description: Describes the CommandID Constants that you can use when you call ExecuteCommand (Device) or ExecuteCommand (Item).
ms.assetid: 'ac7676da-4e8f-4c53-8f43-0e28b0073937'
keywords: ["DeviceCommand object WIA Automation", "DeviceCommand object WIA Automation , described"]
topic_type:
- apiref
api_name:
- DeviceCommand
api_location:
- Wiaaut.h
api_type:
- COM
---

# DeviceCommand object

Describes the [**CommandID Constants**](-wiaaut-consts-commandid.md) that you can use when you call [**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md) or [**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md).

## Members

The **DeviceCommand** object has these types of members:

-   [Properties](#properties)

### Properties

The **DeviceCommand** object has these properties.



| Property                                                                             | Access type          | Description                                                                                                  |
|:-------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------|
| [**CommandID**](-wiaaut-idevicecommand-commandid.md)<br/>                     | Read-only<br/> | Retrieves the [**CommandID Constants**](-wiaaut-consts-commandid.md) for this **DeviceCommand**.<br/> |
| [**Description (DeviceCommand)**](-wiaaut-idevicecommand-description.md)<br/> | Read-only<br/> | Retrieves the **DeviceCommand** description.<br/>                                                      |
| [**Name (DeviceCommand)**](-wiaaut-idevicecommand-name.md)<br/>               | Read-only<br/> | Retrieves the **DeviceCommand** name.<br/>                                                             |



 

## Remarks

Note that while the most common CommandIDs are provided as constants, not all CommandIDs work for all imaging devices.

For example code, see [Enumerate Supported Commands in Commands Collection](-wiaaut-shared-samples.md#enumerate-supported-commands-in-commands-collection) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Item (DeviceCommands)**](-wiaaut-idevicecommands-item.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item (DeviceCommands)**](-wiaaut-idevicecommands-item.md)
</dt> </dl>

 

 





