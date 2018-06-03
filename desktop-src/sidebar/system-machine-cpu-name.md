---
title: System.Machine.CPU.name property
description: Gets the CPU name.
ms.assetid: e4477452-7324-421d-967c-27669e3e28a4
keywords:
- name property Windows Sidebar
- name property Windows Sidebar , System.Machine.CPU object
- System.Machine.CPU object Windows Sidebar , name property
topic_type:
- apiref
api_name:
- System.Machine.CPU.name
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

# System.Machine.CPU.name property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the CPU name.

This property is read-only.

## Syntax


```JScript
strname = System.Machine.CPU.name
```



## Property value

A **String** that receives the processor name.

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



 

 





