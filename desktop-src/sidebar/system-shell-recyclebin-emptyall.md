---
title: System.Shell.RecycleBin.emptyAll method
description: Deletes all items from the Recycle Bin.
ms.assetid: b3c0267c-1f0a-4f01-8937-d0a189a6df2e
keywords:
- emptyAll method Windows Sidebar
- emptyAll method Windows Sidebar , System.Shell.RecycleBin object
- System.Shell.RecycleBin object Windows Sidebar , emptyAll method
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.emptyAll
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

# System.Shell.RecycleBin.emptyAll method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Deletes all items from the Recycle Bin.

## Syntax


```JScript
System.Shell.RecycleBin.emptyAll()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **Recycle Bin Properties** settings determine how file deletion is handled. For example, whether files are deleted immediately or stored until the Recycle Bin is emptied, whether the Recycle Bin is system-wide or operates on a per-drive basis, and whether confirmation dialogs are displayed.

## Examples

The following example demonstrates how to empty the Recycle Bin.


```JScript
// --------------------------------------------------------------------
// Empty the Recycle Bin.
// --------------------------------------------------------------------
function EmptyRecycleBin()
{
    var intFileCount = System.Shell.RecycleBin.fileCount;
    var intFolderCount = System.Shell.RecycleBin.folderCount;
    System.Shell.RecycleBin.emptyAll();
    spFeedback.innerHTML = intFileCount + " file(s) deleted.<br/>";
    spFeedback.innerHTML += intFolderCount + " folder(s) deleted.";
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



 

 





