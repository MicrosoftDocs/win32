---
title: System.Machine.processorArchitecture property
description: Gets the microprocessor type.
ms.assetid: 424db042-f085-4628-92f1-64473156eb32
keywords:
- processorArchitecture property Windows Sidebar
- processorArchitecture property Windows Sidebar , System.Machine object
- System.Machine object Windows Sidebar , processorArchitecture property
topic_type:
- apiref
api_name:
- System.Machine.processorArchitecture
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

# System.Machine.processorArchitecture property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the microprocessor type.

This property is read-only.

## Syntax


```JScript
strprocessorArchitecture = System.Machine.processorArchitecture
```



## Property value

A **String** that receives the processor type.

## Remarks

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
| Header<br/>                   | <dl> <dt>Windows.system.h</dt> </dl>                    |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





