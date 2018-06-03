---
title: System.Machine.totalMemory property
description: Gets the total amount of memory available in the current user session.
ms.assetid: 449cdb55-2250-42da-a57a-ec0e9d2be207
keywords:
- totalMemory property Windows Sidebar
- totalMemory property Windows Sidebar , System.Machine object
- System.Machine object Windows Sidebar , totalMemory property
topic_type:
- apiref
api_name:
- System.Machine.totalMemory
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

# System.Machine.totalMemory property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the total amount of memory available in the current user session.

This property is read-only.

## Syntax


```JScript
itotalMemory = System.Machine.totalMemory
```



## Property value

An **Integer** that receives the amount of free memory recognized by the computer.

## Remarks

The amount of memory returned is considered virtual and exceeds the amount of actual physical memory available.

Individual CPU details are accessible through the [**CPUs**](system-machine-cpus.md) collection of [**System.Machine**](system-machine.md).

## Examples

The following example demonstrates how to get machine details.


```JScript
/// <summary>
/// Initialize the gadget.
/// </summary>
function Init()
{
    // Get the machine details.
    sMachineInfo += "Processor Architecture: " + System.Machine.processorArchitecture + "<br/>";
    sMachineInfo += "Total Memory: " + System.Machine.totalMemory + "<br/>";
    sMachineInfo += "Available Memory: " + System.Machine.availableMemory + "<br/>";
    
    // Initialize the gadget content.
    SetContentText();
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



 

 





