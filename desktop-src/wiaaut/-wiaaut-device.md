---
title: Device object
description: Represents an active connection to an imaging device.
ms.assetid: 8ea24ff9-772c-480b-a558-0a86520dd6f8
keywords:
- Device object WIA Automation
- Device object WIA Automation , described
topic_type:
- apiref
api_name:
- Device
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

# Device object

Represents an active connection to an imaging device.

## Members

The **Device** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Device** object has these methods.



| Method                                                            | Description                                          |
|:------------------------------------------------------------------|:-----------------------------------------------------|
| [**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md) | Issues the command to the imaging device.<br/> |
| [**GetItem**](-wiaaut-idevice-getitem.md)                        | Retrieves the specified item.<br/>             |



 

### Properties

The **Device** object has these properties.



| Property                                                             | Access type          | Description                                                                                                                                        |
|:---------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Commands (Device)**](-wiaaut-idevice-commands.md)<br/>     | Read-only<br/> | Retrieves a collection of all commands for this imaging device.<br/>                                                                         |
| [**DeviceID (Device)**](-wiaaut-idevice-deviceid.md)<br/>     | Read-only<br/> | Retrieves the [**DeviceID (Device)**](-wiaaut-idevice-deviceid.md) for this **Device**.<br/>                                                |
| [**Events**](-wiaaut-idevice-events.md)<br/>                  | Read-only<br/> | Retrieves a collection of all events for this imaging device.<br/>                                                                           |
| [**Items (Device)**](-wiaaut-idevice-items.md)<br/>           | Read-only<br/> | Retrieves a collection of all items for this imaging device.<br/>                                                                            |
| [**Properties (Device)**](-wiaaut-idevice-properties.md)<br/> | Read-only<br/> | Retrieves a collection of all properties for this imaging device.<br/>                                                                       |
| [**Type (Device)**](-wiaaut-idevice-type.md)<br/>             | Read-only<br/> | Retrieves the type of **Device**.<br/>                                                                                                       |
| [**WiaItem (Device)**](-wiaaut-idevice-wiaitem.md)<br/>       | Read-only<br/> | Retrieves the underlying [IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface for this **Device** object.<br/> |



 

## Remarks

The imaging device that the **Device** object represents is independent of the **Device** object. A user can disconnect an imaging device while your application is using it. Accessing a **Device** object's properties or methods after this occurs can result in errors.

For example code, see [Display all the Properties for the Selected Device](-wiaaut-shared-samples.md#display-all-the-properties-for-the-selected-device---1) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Connect**](-wiaaut-ideviceinfo-connect.md)

[**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)



 

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

[**ShowAcquisitionWizard**](-wiaaut-icommondialog-showacquisitionwizard.md)
</dt> <dt>

[**ShowDeviceProperties**](-wiaaut-icommondialog-showdeviceproperties.md)
</dt> <dt>

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**Connect**](-wiaaut-ideviceinfo-connect.md)
</dt> <dt>

[**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)
</dt> </dl>

 

 





