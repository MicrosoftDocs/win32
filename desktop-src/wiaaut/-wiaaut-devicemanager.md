---
title: DeviceManager object
description: Manages the imaging devices connected to the computer. The DeviceManager control is an invisible-at-runtime control that you can create using \ 0034;WIA.DeviceManager \ 0034; as the ProgID in a call to CreateObject, or by dropping a DeviceManager object on a form.
ms.assetid: 47a12fe1-f4f9-4b59-b157-513ae159a787
keywords:
- DeviceManager object WIA Automation
- DeviceManager object WIA Automation , described
topic_type:
- apiref
api_name:
- DeviceManager
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# DeviceManager object

Manages the imaging devices connected to the computer. The **DeviceManager** control is an invisible-at-runtime control that you can create using "WIA.DeviceManager" as the ProgID in a call to [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx), or by dropping a **DeviceManager** object on a form.

## Members

The **DeviceManager** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **DeviceManager** object has these events.



| Event                                                    | Description                                                                                                   |
|:---------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md) | Fires for any event registered with [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md).<br/> |



 

### Methods

The **DeviceManager** object has these methods.



| Method                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md)                         | Registers the specified [**EventID Constants**](-wiaaut-consts-eventid.md) for the specified *DeviceID*. If *DeviceID* is "\*" then [**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md) is called whenever the event specified occurs for any device. Otherwise, **OnEvent** is only called if the event specified occurs on the device specified.<br/>                                      |
| [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md)     | Registers the specified *Command* to launch when the specified *EventID* for the specified *DeviceID* occurs. *Command* can be either a CLSID or the full path name and the appropriate command-line arguments needed to invoke the application.<br/>                                                                                                                                              |
| [**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md)                     | Unregisters the specified *EventID* for the specified *DeviceID*. [**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md) should only be called for the *EventID* and *DeviceID* for which you called [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md).<br/>                                                                                                                |
| [**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md) | Unregisters the specified *Command* for the specified *EventID* for the specified *DeviceID*. [**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md) should only be called for the *Command*, *Name*, *Description*, *Icon*, *EventID*, and *DeviceID* for which you called [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md).<br/> |



 

### Properties

The **DeviceManager** object has these properties.



| Property                                                                             | Access type          | Description                                                                          |
|:-------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------|
| [**DeviceInfos (DeviceManager)**](-wiaaut-idevicemanager-deviceinfos.md)<br/> | Read-only<br/> | Retrieves a collection of all imaging devices connected to this computer.<br/> |



 

## Remarks

Note you can call [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md) on all [**DeviceEvent**](-wiaaut-deviceevent.md) objects found in the [**Events**](-wiaaut-idevice-events.md) collection on the [**Device**](-wiaaut-device.md) object. However, you can only call [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md) on **DeviceEvent** objects that have a [**Type (DeviceEvent)**](-wiaaut-ideviceevent-type.md) property containing the ActionEvent flag.

For example code, see [List all Available Devices by Name and DeviceID](https://www.bing.com/search?q=List all Available Devices by Name and DeviceID) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md)
</dt> </dl>

 

 





