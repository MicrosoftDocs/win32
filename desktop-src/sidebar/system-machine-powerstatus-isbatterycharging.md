---
title: System.Machine.PowerStatus.isBatteryCharging property
description: Gets the battery charging status.
ms.assetid: 54fb5fe3-cb9c-4c50-84ad-5a3c44c8056f
keywords:
- isBatteryCharging property Windows Sidebar
- isBatteryCharging property Windows Sidebar , System.Machine.PowerStatus object
- System.Machine.PowerStatus object Windows Sidebar , isBatteryCharging property
topic_type:
- apiref
api_name:
- System.Machine.PowerStatus.isBatteryCharging
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Machine.PowerStatus.isBatteryCharging property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the battery charging status.

This property is read-only.

## Syntax


```JScript
bisBatteryCharging = System.Machine.PowerStatus.isBatteryCharging
```



## Property value

A **Boolean** that receives whether the battery is charging.

<dt>



 (true)


</dt> <dd>

The battery is charging.

</dd> <dt>



 (false)


</dt> <dd>

The battery is not charging.

</dd> </dl>

## Remarks

Returns **false** if the computer is plugged in but the battery is not attached.

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



 

 





