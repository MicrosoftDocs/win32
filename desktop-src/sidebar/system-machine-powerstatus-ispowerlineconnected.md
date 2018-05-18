---
title: System.Machine.PowerStatus.isPowerLineConnected property
description: Gets the power supply state.
ms.assetid: 'f411b575-447b-4a7a-bd66-df82bd1e8a85'
keywords: ["isPowerLineConnected property Windows Sidebar", "isPowerLineConnected property Windows Sidebar , System.Machine.PowerStatus object", "System.Machine.PowerStatus object Windows Sidebar , isPowerLineConnected property"]
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus.isPowerLineConnected
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Machine.PowerStatus.isPowerLineConnected property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the power supply state.

This property is read-only.

## Syntax


```JScript
bisPowerLineConnected = System.Machine.PowerStatus.isPowerLineConnected
```



## Property value

A **Boolean** that receives whether the computer is plugged in or drawing on the battery.

<dt>



 (true)


</dt> <dd>

The computer is plugged in.

</dd> <dt>



 (false)


</dt> <dd>

Power is being supplied by the battery.

</dd> </dl>

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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





