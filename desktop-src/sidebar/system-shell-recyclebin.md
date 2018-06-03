---
title: System.Shell.RecycleBin object
description: Defines the properties, methods, and events used to expose Recycle Bin characteristics.
ms.assetid: 0553c848-b42a-4725-995e-c8261108dcc7
keywords:
- System.Shell.RecycleBin object Windows Sidebar
- System.Shell.RecycleBin object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin
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

# System.Shell.RecycleBin object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties, methods, and events used to expose **Recycle Bin** characteristics.

## Members

The **System.Shell.RecycleBin** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **System.Shell.RecycleBin** object has these events.



| Event                                                                      | Description                                                                  |
|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**onRecycleBinChanged**](system-shell-recyclebin-onrecyclebinchanged.md) | Event fired when the content of the **Recycle Bin** is modified. <br/> |



 

### Methods

The **System.Shell.RecycleBin** object has these methods.



| Method                                                                     | Description                                                                      |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**deleteItem**](system-shell-recyclebin-deleteitem.md)                   | Deletes an item from the system by moving it to the **Recycle Bin**. <br/> |
| [**emptyAll**](system-shell-recyclebin-emptyall.md)                       | Deletes all items from the Recycle Bin. <br/>                              |
| [**showRecycleSettings**](system-shell-recyclebin-showrecyclesettings.md) | Displays the **Recycle Bin Properties** dialog. <br/>                      |



 

### Properties

The **System.Shell.RecycleBin** object has these properties.



| Property                                                              | Access type          | Description                                                                          |
|:----------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------|
| [**fileCount**](system-shell-recyclebin-filecount.md)<br/>     | Read-only<br/> | Gets the number of files in the **Recycle Bin**. <br/>                         |
| [**folderCount**](system-shell-recyclebin-foldercount.md)<br/> | Read-only<br/> | Gets the number of folders in the **Recycle Bin**. <br/>                       |
| [**sizeUsed**](system-shell-recyclebin-sizeused.md)<br/>       | Read-only<br/> | Gets the amount of space, in KB, used by the content of the Recycle Bin. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





