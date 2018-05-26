---
title: System.Machine.PowerStatus.batteryCapacityTotal property
description: Gets the total capacity of the computer battery in seconds.
ms.assetid: 1b5399af-fd44-4ebe-801e-919131365912
keywords:
- batteryCapacityTotal property Windows Sidebar
- batteryCapacityTotal property Windows Sidebar , System.Machine.PowerStatus object
- System.Machine.PowerStatus object Windows Sidebar , batteryCapacityTotal property
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus.batteryCapacityTotal
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Machine.PowerStatus.batteryCapacityTotal property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the total capacity of the computer battery in seconds.

This property is read-only.

## Syntax


```JScript
ibatteryCapacityTotal = System.Machine.PowerStatus.batteryCapacityTotal
```



## Property value

An **Integer** that receives the number of seconds.

## Remarks

The value of **batteryCapacityTotal** is an estimate only.

## Examples

The following example demonstrates how to get the power supply information for the computer.


```JScript
// --------------------------------------------------------------------
// Get the machine power information.
// --------------------------------------------------------------------
function GetPowerStatus()
{
    if (System.Machine.PowerStatus.isPowerLineConnected == false)
    {
        sMachinePowerInfo = "Power Supply: Battery<br/>";
        sMachinePowerInfo += "Battery Capacity Remaining: " + System.Machine.batteryCapacityRemaining + "<br/>";
        sMachinePowerInfo += "Battery Capacity Total: " + System.Machine.batteryCapacityTotal + "<br/>";
        sMachinePowerInfo += "Battery Percent Remaining: " + System.Machine.batteryPercentRemaining + "<br/>";
        sMachinePowerInfo += "Battery Status: " + System.Machine.batteryStatus + "<br/>";
        sMachinePowerInfo += "Is Battery Charging: " + System.Machine.isBatteryCharging + "<br/>";
        sMachinePowerInfo += "Available Memory: " + System.Machine.availableMemory + "<br/>";
    }
    else
    {
        sMachinePowerInfo += "Power Supply: Plugged in<br/>";
    }
    return sMachinePowerInfo;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





