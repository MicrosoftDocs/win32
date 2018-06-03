---
title: System.Shell.RecycleBin.showRecycleSettings method
description: Displays the Recycle Bin Properties dialog.
ms.assetid: 11668a68-1b7a-4f42-a539-898480d12ad5
keywords:
- showRecycleSettings method Windows Sidebar
- showRecycleSettings method Windows Sidebar , System.Shell.RecycleBin object
- System.Shell.RecycleBin object Windows Sidebar , showRecycleSettings method
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.showRecycleSettings
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

# System.Shell.RecycleBin.showRecycleSettings method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Displays the **Recycle Bin Properties** dialog.

## Syntax


```JScript
System.Shell.RecycleBin.showRecycleSettings()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **Recycle Bin Properties** settings determine how file deletion is handled. For example, whether files are deleted immediately or stored until the Recycle Bin is emptied, whether the Recycle Bin is system-wide or operates on a per-drive basis, and whether confirmation dialogs are displayed.

## Examples

The following example demonstrates how to display the Recycle Bin Properties dialog.


```JScript
// --------------------------------------------------------------------
// Display the Recycle Bin Properties dialog.
// --------------------------------------------------------------------
function RecycleBinProperties()
{
    System.Shell.RecycleBin.showRecycleSettings();
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



 

 





