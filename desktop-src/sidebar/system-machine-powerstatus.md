---
title: System.Machine.PowerStatus object
description: Defines the properties and events for the computer's power status.
ms.assetid: 5ed6827a-049e-40e5-af67-098e12b30ef5
keywords:
- System.Machine.PowerStatus object Windows Sidebar
- System.Machine.PowerStatus object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Machine.PowerStatus object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and events for the computer's power status.

## Members

The **System.Machine.PowerStatus** object has these types of members:

-   [Events](#events)
-   [Properties](#properties)

### Events

The **System.Machine.PowerStatus** object has these events.



| Event                                                                               | Description                                                                                                    |
|:------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**powerLineStatusChanged**](system-machine-powerstatus-powerlinestatuschanged.md) | Event fired when the computer's power supply state changes between plugged-in and battery-powered. <br/> |



 

### Properties

The **System.Machine.PowerStatus** object has these properties.



| Property                                                                                           | Access type          | Description                                                                                        |
|:---------------------------------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------|
| [**batteryCapacityRemaining**](system-machine-powerstatus-batterycapacityremaining.md)<br/> | Read-only<br/> | Gets the remaining capacity of the computer battery in seconds. <br/>                        |
| [**batteryCapacityTotal**](system-machine-powerstatus-batterycapacitytotal.md)<br/>         | Read-only<br/> | Gets the total capacity of the computer battery in seconds. <br/>                            |
| [**batteryPercentRemaining**](system-machine-powerstatus-batterypercentremaining.md)<br/>   | Read-only<br/> | Gets the remaining capacity of the computer battery as a percentage of total capacity. <br/> |
| [**batteryStatus**](system-machine-powerstatus-batterystatus.md)<br/>                       | Read-only<br/> | Gets the charge state of the computer's battery. <br/>                                       |
| [**isBatteryCharging**](system-machine-powerstatus-isbatterycharging.md)<br/>               | Read-only<br/> | Gets the battery charging status. <br/>                                                      |
| [**isPowerLineConnected**](system-machine-powerstatus-ispowerlineconnected.md)<br/>         | Read-only<br/> | Gets the power supply state. <br/>                                                           |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





