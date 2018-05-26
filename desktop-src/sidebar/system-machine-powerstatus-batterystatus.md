---
title: System.Machine.PowerStatus.batteryStatus property
description: Gets the charge state of the computers battery.
ms.assetid: 72fca465-bd32-460b-ae0d-06eae3fae6d2
keywords:
- batteryStatus property Windows Sidebar
- batteryStatus property Windows Sidebar , System.Machine.PowerStatus object
- System.Machine.PowerStatus object Windows Sidebar , batteryStatus property
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus.batteryStatus
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

# System.Machine.PowerStatus.batteryStatus property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the charge state of the computer's battery.

This property is read-only.

## Syntax


```JScript
ibatteryStatus = System.Machine.PowerStatus.batteryStatus
```



## Property value

An **Integer** that receives the charge state of the battery.

<dt>



 (0)


</dt> <dd>

**BATTERYSTATUS\_MEDIUM**: The battery capacity is between 33% and 66%.

</dd> <dt>



 (1)


</dt> <dd>

**BATTERYSTATUS\_HIGH**: The battery capacity is over 66%.

</dd> <dt>



 (2)


</dt> <dd>

**BATTERYSTATUS\_LOW**: The battery capacity is under 33%.

</dd> <dt>



 (4)


</dt> <dd>

**BATTERYSTATUS\_CRITICAL**: The battery capacity is under 5%.

</dd> <dt>



 (128)


</dt> <dd>

**BATTERYSTATUS\_NOBATTERY**: No battery detected. The battery is not connected, not charging, and not providing power to the computer.

</dd> <dt>



 (255)


</dt> <dd>

**BATTERYSTATUS\_UNKNOWN**: Unknown battery status. The battery is not responding.

</dd> </dl>

## Remarks

If the computer is plugged in, **batteryStatus** will not indicate the charge state.

Users can redefine **LOW** and **CRITICAL** charge states in **Control Panel\|Power Options\|Change plan settings\|Change advanced power settings\|Battery settings**.

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
| Header<br/>                   | <dl> <dt>Windows.system.power.h</dt> </dl>              |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





