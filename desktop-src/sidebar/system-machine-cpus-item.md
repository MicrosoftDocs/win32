---
title: CPUs.item property
description: Gets a System.Machine.CPU object from the CPUs collection.
ms.assetid: 'bd73765f-1dd5-44d7-ab70-971ac9b2fd6c'
keywords: ["item property Windows Sidebar", "item property Windows Sidebar , CPUs collection", "CPUs collection Windows Sidebar , item property"]
topic_type:
- apiref
api_name:
- CPUs.item
api_location:
- Sidebar.Exe
api_type:
- COM
---

# CPUs.item property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Machine.CPU**](system-machine-cpu.md) object from the [**CPUs**](system-machine-cpus.md) collection.

This property is read-only.

## Syntax


```JScript
objitem = CPUs.item
```



## Property value

An **Object** that receives a [**System.Machine.CPU**](system-machine-cpu.md) object from the specified index.

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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
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

[**count**](system-machine-cpus-count.md)
</dt> </dl>

 

 





