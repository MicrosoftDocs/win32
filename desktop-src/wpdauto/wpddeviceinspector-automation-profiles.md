---
title: WPDDeviceInspector Automation Profiles
description: The WPDDeviceInspector tool is a console application. It generates a comprehensive HTML report that describes the capabilities and content of a device. This application is available in the Windows Driver Kit for Windows 7.
ms.assetid: f83ed2dc-93da-4e10-ab73-86d12f8f037a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPDDeviceInspector Automation Profiles

The WPDDeviceInspector tool is a console application. It generates a comprehensive HTML report that describes the capabilities and content of a device. This application is available in the [Windows Driver Kit](http://go.microsoft.com/fwlink/p/?linkid=135987) for Windows 7.

The WPDDeviceInspector for Windows 7 supports an Automation mode that generates a report of the device capabilities in terms of JScript properties, methods, and events. This report provides a basic guide to the device properties, services, formats, and storages.

The following steps show how to use the WPDDeviceInspector.

1.  Connect a device.
2.  From a Command Prompt, type the following: `WpdDeviceInspector.exe /Automation`
3.  Enter the selection for the device.
4.  The report is generated as **DeviceAutomationInfo.html** in the **DeviceProfiles** folder.

The following is a snapshot of the Device Object capabilities for a sample device:

Device Capabilities

Supported Properties



| JScript                           | Datatype | Access     |
|-----------------------------------|----------|------------|
| ObjectId                          | String   | Read       |
| ObjectContainerFunctionalObjectId | String   | Read       |
| ObjectPersistentUniqueId          | String   | Read       |
| ObjectParentId                    | String   | Read       |
| ObjectFormat                      | String   | Read       |
| ObjectContentType                 | String   | Read       |
| FunctionalObjectCategory          | String   | Read       |
| DevicePowerSource                 | Number   | Read       |
| ObjectCanDelete                   | Boolean  | Read       |
| DeviceType                        | Number   | Read       |
| DeviceTransport                   | Number   | Read       |
| DeviceFirmwareVersion             | String   | Read       |
| DeviceProtocol                    | String   | Read       |
| DeviceManufacturer                | String   | Read       |
| DeviceModel                       | String   | Read       |
| ObjectName                        | String   | Read       |
| DeviceSerialNumber                | String   | Read       |
| DeviceModelUniqueId               | Array    | Read       |
| DeviceFunctionalUniqueId          | Array    | Read       |
| DevicePowerLevel                  | Number   | Read       |
| DeviceSyncPartner                 | String   | Read/Write |
| DeviceFriendlyName                | String   | Read/Write |



 

Methods



| JScript                                                     | Description                                            |
|-------------------------------------------------------------|--------------------------------------------------------|
| `var Collection = deviceObject.storages`                    | Returns a collection of legacy storages on the device. |
| `var Collection = deviceObject.services`                    | Returns a collection of services on the device.        |
| `var Collection = deviceObject.getServicesByType("{GUID}")` | Returns a collection of services for a given type.     |



 

Event Handlers

-   onDeviceReset()
-   onDeviceUpdated()

## Related topics

<dl> <dt>

[Best Practices for Writing WPD Automation Scripts](best-practices-for-writing-wpd-automation-scripts.md)
</dt> </dl>

 

 




