---
title: DeviceCommands object
description: Contains a collection of all the supported DeviceCommand objects for an imaging device. For more details on determining the collection of supported device commands, see the Commands (Device) property or Commands (Item) property.
ms.assetid: 266bb2d9-4219-4af7-891d-82db5bcd3acd
keywords:
- DeviceCommands object WIA Automation
- DeviceCommands object WIA Automation , described
topic_type:
- apiref
api_name:
- DeviceCommands
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DeviceCommands object

Contains a collection of all the supported [**DeviceCommand**](-wiaaut-devicecommand.md) objects for an imaging device. For more details on determining the collection of supported device commands, see the [**Commands (Device)**](-wiaaut-idevice-commands.md) property or [**Commands (Item)**](-wiaaut-iitem-commands.md) property.

## Members

The **DeviceCommands** object has these types of members:

-   [Properties](#properties)

### Properties

The **DeviceCommands** object has these properties.



| Property                                                                   | Access type          | Description                                                                               |
|:---------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------|
| [**Count (DeviceCommands)**](-wiaaut-idevicecommands-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **DeviceCommands** collection.<br/>          |
| [**Item (DeviceCommands)**](-wiaaut-idevicecommands-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the **DeviceCommands** collection by position.<br/> |



 

## Remarks

Note that the supported commands vary from one imaging device to the next.

For example code, see [Enumerate Supported Commands in Commands Collection](-wiaaut-shared-samples.md#enumerate-supported-commands-in-commands-collection) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Commands (Item)**](-wiaaut-iitem-commands.md)

[**Commands (Device)**](-wiaaut-idevice-commands.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Commands (Device)**](-wiaaut-idevice-commands.md)
</dt> <dt>

[**Commands (Item)**](-wiaaut-iitem-commands.md)
</dt> </dl>

 

 





