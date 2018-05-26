---
title: CPUs.count property
description: Gets the number of System.Machine.CPU items in the CPUs collection.
ms.assetid: fc24ce24-a32a-4f8a-9c2b-6d134764d71e
keywords:
- count property Windows Sidebar
- count property Windows Sidebar , CPUs collection
- CPUs collection Windows Sidebar , count property
topic_type:
- apiref
api_name:
- CPUs.count
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

# CPUs.count property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of [**System.Machine.CPU**](system-machine-cpu.md) items in the [**CPUs**](system-machine-cpus.md) collection.

This property is read-only.

## Syntax


```JScript
icount = CPUs.count
```



## Property value

An **Integer** that receives the number of items.

## Examples

The following example demonstrates how to access properties for a specific CPU in the [**CPUs**](system-machine-cpus.md) collection.


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



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Machine**](system-machine.md)
</dt> <dt>

[**CPUs**](system-machine-cpus.md)
</dt> <dt>

[**System.Machine.CPU**](system-machine-cpu.md)
</dt> <dt>

[**item**](system-machine-cpus-item.md)
</dt> </dl>

 

 





