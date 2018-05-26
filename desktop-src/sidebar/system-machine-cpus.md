---
title: System.Machine.CPUs property
description: A collection of System.Machine.CPU objects.
ms.assetid: 9918f4d2-0104-4cfd-9137-dd4c7eed858c
keywords:
- CPUs property Windows Sidebar
- CPUs property Windows Sidebar , System.Machine object
- System.Machine object Windows Sidebar , CPUs property
topic_type:
- apiref
api_name:
- System.Machine.CPUs
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

# System.Machine.CPUs property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

A collection of [**System.Machine.CPU**](system-machine-cpu.md) objects.

> [!Note]  
> Objects of type [**System.Machine.CPU**](system-machine-cpu.md) can only be accessed through the **CPUs** collection. This collection is a member of [**System.Machine**](system-machine.md).

 

This property is read-only.

## Syntax


```JScript
objCPUs = System.Machine.CPUs
```



## Property value

A collection of [**System.Machine.CPU**](system-machine-cpu.md) objects.

## Examples

The following example shows how to select the [**System.Machine.CPU**](system-machine-cpu.md) object at index `0` from the **CPUs** collection, then access the `name` property of that **System.Machine.CPU** object.


```JScript
var collCPU = System.Machine.CPUs; 
            
var oCPU = collCPU.item(0);  
            
var strCPUName = oCPU.name;
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

[**System.Machine**](system-machine.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**count**](system-machine-cpus-count.md)
</dt> <dt>

[**item**](system-machine-cpus-item.md)
</dt> <dt>

[**System.Machine.CPU**](system-machine-cpu.md)
</dt> </dl>

 

 





