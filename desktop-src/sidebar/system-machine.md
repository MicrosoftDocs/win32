---
title: System.Machine object
description: Defines the properties for determining machine processor and memory characteristics as well as the properties for the CPUs collection.
ms.assetid: 74de3c08-6a30-48e8-a377-344db2dd5451
keywords:
- System.Machine object Windows Sidebar
- System.Machine object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Machine
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Machine object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties for determining machine processor and memory characteristics as well as the properties for the [**CPUs**](system-machine-cpus.md) collection.

> [!Note]  
> Objects of type [**System.Machine.CPU**](system-machine-cpu.md) can only be accessed through the [**CPUs**](system-machine-cpus.md) collection. This collection is a member of **System.Machine**.

 

## Members

The **System.Machine** object has these types of members:

-   [Collections](#events)
-   [Properties](#properties)

### Collections

The **System.Machine** object has these collections.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Collection</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>CPUs</strong>](system-machine-cpus.md)</td>
<td style="text-align: left;">A collection of [<strong>System.Machine.CPU</strong>](system-machine-cpu.md) objects. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Machine.CPU</strong>](system-machine-cpu.md) can only be accessed through the [<strong>CPUs</strong>](system-machine-cpus.md) collection. This collection is a member of <strong>System.Machine</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **System.Machine** object has these properties.



| Property                                                                         | Access type          | Description                                                                        |
|:---------------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------|
| [**availableMemory**](system-machine-availablememory.md)<br/>             | Read-only<br/> | Gets the amount of available memory in MB. <br/>                             |
| [**processorArchitecture**](system-machine-processorarchitecture.md)<br/> | Read-only<br/> | Gets the microprocessor type. <br/>                                          |
| [**totalMemory**](system-machine-totalmemory.md)<br/>                     | Read-only<br/> | Gets the total amount of memory available in the current user session. <br/> |



 

## Remarks

Each [**System.Machine.CPU**](system-machine-cpu.md) in the [**CPUs**](system-machine-cpus.md) collection corresponds to a CPU present on the machine.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





