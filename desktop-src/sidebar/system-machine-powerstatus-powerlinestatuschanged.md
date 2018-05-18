---
title: System.Machine.PowerStatus.powerLineStatusChanged event
description: Event fired when the computer's power supply state changes between plugged-in and battery-powered.
ms.assetid: '7ef9bbf1-73aa-4027-ba4b-4b834167c261'
keywords: ["powerLineStatusChanged event Windows Sidebar", "powerLineStatusChanged event Windows Sidebar , System.Machine.PowerStatus object", "System.Machine.PowerStatus object Windows Sidebar , powerLineStatusChanged event"]
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus.powerLineStatusChanged
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Machine.PowerStatus.powerLineStatusChanged event

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Event fired when the computer's power supply state changes between plugged-in and battery-powered.

## Syntax


```JScript
iRetVal = System.Machine.PowerStatus.powerLineStatusChanged(
  handler
)
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

The name of the function to call when the event is fired.

</dd> </dl>

## Remarks

Useful for toggling the display of a battery gauge when the computer is unplugged.

## Examples

The following example demonstrates how to get the power supply information for the computer.


```JScript
// Delegate for the power status change event.
System.Machine.PowerStatus.powerLineStatusChanged = PowerStatus;

// --------------------------------------------------------------------
// Handle the power status changed event.
// --------------------------------------------------------------------
function PowerStatus()
{
    machinePowerInfo.innerHTML = GetPowerStatus();
}

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



 

 





