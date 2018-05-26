---
title: System.Machine.PowerStatus.batteryCapacityRemaining property
description: Gets the remaining capacity of the computer battery in seconds.
ms.assetid: a24b9c19-c049-4b31-bf65-8c2fdd12d844
keywords:
- batteryCapacityRemaining property Windows Sidebar
- batteryCapacityRemaining property Windows Sidebar , System.Machine.PowerStatus object
- System.Machine.PowerStatus object Windows Sidebar , batteryCapacityRemaining property
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus.batteryCapacityRemaining
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

# System.Machine.PowerStatus.batteryCapacityRemaining property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the remaining capacity of the computer battery in seconds.

This property is read-only.

## Syntax


```JScript
ibatteryCapacityRemaining = System.Machine.PowerStatus.batteryCapacityRemaining
```



## Property value

An **Integer** that receives the number of seconds.

## Remarks

The value of **batteryCapacityRemaining** is an estimate only.

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



 

 





