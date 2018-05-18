---
title: System.Machine.CPU object
description: Defines the properties and methods of each member of the System.Machine.CPU collection.
ms.assetid: 'de2bd7aa-1e6a-4d25-8e29-80cd75fca083'
keywords: ["System.Machine.CPU object Windows Sidebar", "System.Machine.CPU object Windows Sidebar , described"]
topic_type:
- apiref
api_name:
- System.Machine.CPU
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Machine.CPU object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods of each member of the **System.Machine.CPU** collection.

## Members

The **System.Machine.CPU** object has these types of members:

-   [Properties](#properties)

### Properties

The **System.Machine.CPU** object has these properties.



| Property                                                                 | Access type          | Description                                                               |
|:-------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------|
| [**name**](system-machine-cpu-name.md)<br/>                       | Read-only<br/> | Gets the CPU name. <br/>                                            |
| [**usagePercentage**](system-machine-cpu-usagepercentage.md)<br/> | Read-only<br/> | Gets the percentage of a microprocessor's capacity being used.<br/> |



 

## Remarks

Each **System.Machine.CPU** in the [**CPUs**](system-machine-cpus.md) collection corresponds to a CPU present on the machine.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





