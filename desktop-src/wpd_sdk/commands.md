---
description: Commands
ms.assetid: f579745a-5327-4c8b-bfa7-fe81d9657a3b
title: Commands (WPD API)
ms.topic: article
ms.date: 05/31/2018
---

# Commands (WPD API)

The client application and the driver communicate by means of commands that are sent from the client (via the Windows Portable Device API) to the driver (via the User-Mode Driver Framework). A command may or may not include a parameter, and may or may not return a result. A client can send a command explicitly, by calling either the [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand) method or the **IPortableDeviceService:SendCommand** method, or implicitly, by calling any of the methods of the client interfaces. A few commands can only be sent explicitly; these are noted in the command's documentation. The command reference pages describe the purpose of a command, as well as what parameters it expects to receive, and what parameters it is expected to return.

A command is identified by a **PROPERTYKEY** structure. This is made up of two parts: a GUID part (the *fmtid* member) and a DWORD part (the *pid* member). The GUID part is used to indicate the category the command belongs to (related commands belong to the same category, and therefore will have the same *fmtid*). The DWORD part indicates the command ID, and is used to distinguish the individual commands within a command category (the *pid* values for commands in the same category will be different).

The following table lists the categories of commands that Windows Portable Devices defines. Device manufacturers can define their own commands by creating their own command categories and command IDs. However, a manufacturer should not add commands to the categories listed below, since these are reserved by Microsoft.

**Command Categories**



| Command category                         | Description                                                                                                                             |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_CATEGORY\_COMMON**                | Commands that are common to all objects and devices.                                                                                    |
| **WPD\_CATEGORY\_DEVICE\_HINTS**         | Commands that are used to retrieve optional device information that can be used to improve end-user experience.                         |
| **WPD\_CATEGORY\_SMS**                   | Commands that are used for devices that support short message service (SMS) functionality, which is typically exposed on mobile phones. |
| **WPD\_CATEGORY\_STILL\_IMAGE\_CAPTURE** | Commands that are used for devices that support still image capture.                                                                    |
| **WPD\_CATEGORY\_STORAGE**               | Commands that are used for storage functional objects.                                                                                  |



 

The specific commands that are defined for each of these types are given in the following tables, organized by command type.

**WPD\_CATEGORY\_COMMON Category**



| Command                                                                                | Description        |
|----------------------------------------------------------------------------------------|--------------------|
| [**WPD\_COMMAND\_COMMON\_RESET\_DEVICE**](wpd-command-common-reset-device-command.md) | Resets the device. |



 

**WPD\_CATEGORY\_DEVICE\_HINTS Category**



| Command                                                                                                              | Description                                                                      |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**WPD\_COMMAND\_DEVICE\_HINTS\_GET\_CONTENT\_LOCATION**](wpd-command-device-hints-get-content-location-command.md) | Retrieves the object IDs of folders that can hold an object of a specified type. |



 

**WPD\_CATEGORY\_STORAGE Category**



| Command                                                                     | Description                                                         |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**WPD\_COMMAND\_STORAGE\_EJECT**](wpd-command-storage-eject-command.md)   | Ejects a storage medium that can be ejected remotely by the driver. |
| [**WPD\_COMMAND\_STORAGE\_FORMAT**](wpd-command-storage-format-command.md) | Formats a storage functional object on the device.                  |



 

**WPD\_CATEGORY\_SMS Category**



| Command                                                         | Description                                                          |
|-----------------------------------------------------------------|----------------------------------------------------------------------|
| [**WPD\_COMMAND\_SMS\_SEND**](wpd-command-sms-send-command.md) | Initiates the sending of an SMS message by an SMS functional object. |



 

**WPD\_CATEGORY\_STILL\_IMAGE\_CAPTURE Category**



| Command                                                                                                   | Description                                                         |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**WPD\_COMMAND\_STILL\_IMAGE\_CAPTURE\_INITIATE**](wpd-command-still-image-capture-initiate-command.md) | Initiates a still image capture by a still image functional object. |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



