---
description: The Wia object is the entry point for all Windows Image Acquisition (WIA) scripting functionality.
ms.assetid: 1905e344-32cc-41ec-885f-bfabd8edd419
title: Wia object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Wia
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Wia object

The **Wia** object is the entry point for all Windows Image Acquisition (WIA) scripting functionality. Any application that uses the WIA scripting model must create a [**SafeWia**](-wia-safewia.md) or **Wia** object. Use that object to enumerate and create devices and to receive notification of hardware events.

> [!Note]  
> This object is not safe for scripting. For a version of this object that is safe for scripting, see [**SafeWia**](-wia-safewia.md).

 

## Members

The **Wia** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **Wia** object has these events.



| Event                                                                 | Description                                                                  |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**OnDeviceConnected**](-wia--iwiaevents-ondeviceconnected.md)       | Event that occurs when a new WIA hardware device is connected.<br/>    |
| [**OnDeviceDisconnected**](-wia--iwiaevents-ondevicedisconnected.md) | Event that occurs when a new WIA hardware device is disconnected.<br/> |
| [**OnTransferComplete**](-wia--iwiaevents-ontransfercomplete.md)     | Event that occurs when a data transfer is completed successfully.<br/> |



 

### Methods

The **Wia** object has these methods.



| Method                             | Description                                                                                                                                                                                                |
|:-----------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Create**](-wia-iwia-create.md) | The [**Create**](-wia-iwia-create.md) method of the **Wia** object makes a connection to the specified WIA device, and returns an [**Item**](-wia-item.md) object that represents the device.<br/> |



 

### Properties

The **Wia** object has these properties.




| Property | Access type | Description | 
|----------|-------------|-------------|
| <a href="-wia-iwia-devices.md"><strong>Devices</strong></a><br /> | Read-only<br /> | Collection of <a href="-wia-deviceinfo.md"><strong>DeviceInfo</strong></a> objects that represents all of the devices installed on the computer. Read-only. <br /><blockquote>[!Note]<br />This collection is 0-based.</blockquote><br /> | 




 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |
| IID<br/>                      | CLSID\_Wia<br/>                                                                                         |



 

 




