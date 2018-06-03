---
title: System.Shell.Drive object
description: Defines the properties used to expose system storage device characteristics.
ms.assetid: 50f168d8-fe13-484d-8457-933e316052f1
keywords:
- System.Shell.Drive object Windows Sidebar
- System.Shell.Drive object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Shell.Drive
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Shell.Drive object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties used to expose system storage device characteristics.

## Members

The **System.Shell.Drive** object has these types of members:

-   [Properties](#properties)

### Properties

The **System.Shell.Drive** object has these properties.



| Property                                                               | Access type           | Description                                                                                                                     |
|:-----------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**driveFormat**](system-shell-drive-driveformat.md)<br/>       | Read-only<br/>  | Gets whether the system storage device is formatted with NTFS or FAT32 permissions. <br/>                                 |
| [**driveLetter**](system-shell-drive-driveletter.md)<br/>       | Read-only<br/>  | Gets the system storage device drive letter. <br/>                                                                        |
| [**driveType**](system-shell-drive-drivetype.md)<br/>           | Read-only<br/>  | Gets the system storage device type. <br/>                                                                                |
| [**freeSpace**](system-shell-drive-freespace.md)<br/>           | Read-only<br/>  | Gets the amount of free space, in MB, on the system storage device. <br/>                                                 |
| [**isReady**](system-shell-drive-isready.md)<br/>               | Read-only<br/>  | Gets whether the system storage device is **ready**. <br/>                                                                |
| [**rootDirectory**](system-shell-drive-rootdirectory.md)<br/>   | Read-only<br/>  | Gets the UNC path to the root folder of a system storage device. <br/>                                                    |
| [**totalFreeSpace**](system-shell-drive-totalfreespace.md)<br/> | Read-only<br/>  | Gets the total amount of free space, in MB, on the system storage device. <br/>                                           |
| [**totalSize**](system-shell-drive-totalsize.md)<br/>           | Read-only<br/>  | Gets the total capacity, in MB, of the system storage device without regard to partition configuration information. <br/> |
| [**volumeLabel**](system-shell-drive-volumelabel.md)<br/>       | Read/write<br/> | Gets or sets the volume label of the system storage device. <br/>                                                         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





