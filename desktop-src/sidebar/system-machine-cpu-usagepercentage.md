---
title: System.Machine.CPU.usagePercentage property
description: Gets the percentage of a microprocessors capacity being used.
ms.assetid: 3d6f3ff7-b8ad-4c3c-bf05-16b33c118cde
keywords:
- usagePercentage property Windows Sidebar
- usagePercentage property Windows Sidebar , System.Machine.CPU object
- System.Machine.CPU object Windows Sidebar , usagePercentage property
topic_type:
- apiref
api_name:
- System.Machine.CPU.usagePercentage
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

# System.Machine.CPU.usagePercentage property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the percentage of a microprocessor's capacity being used.

This property is read-only.

## Syntax


```JScript
usagePercentage = System.Machine.CPU.usagePercentage
```



## Property value

A **Floating-point** that receives the percentage of CPU capacity being used.

## Remarks

Individual CPU details are accessible through the [**CPUs**](system-machine-cpus.md) collection of [**System.Machine**](system-machine.md).

## Examples

The following example demonstrates how to access a CPU in the [**CPUs**](system-machine-cpus.md) collection and get a specific property for that CPU.


```JScript
// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{
    // Get the machine details.
    sMachineInfo += "Processor Architecture: " + System.Machine.processorArchitecture + "<br/>";
    sMachineInfo += "Total Memory: " + System.Machine.totalMemory + "<br/>";
    sMachineInfo += "Available Memory: " + System.Machine.availableMemory + "<br/>";
    
    // Get the collection of folders from Windows Mail.
    collCPUs = System.Machine.CPUs;

    // Report the folder details.
    for (var loop = 0; loop < collCPUs.count; loop++)
    {
        oCPU = collCPUs.item(loop);
        sMachineInfo += '<span id="CPU' + 
            loop + '">' + oCPU.name + ':' + oCPU.usagePercentage + '%</span><br/>';
    }    
    
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



 

 





