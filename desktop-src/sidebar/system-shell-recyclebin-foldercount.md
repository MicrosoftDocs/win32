---
title: System.Shell.RecycleBin.folderCount property
description: Gets the number of folders in the Recycle Bin.
ms.assetid: 05094833-9a28-460e-9744-370e812b3ce0
keywords:
- folderCount property Windows Sidebar
- folderCount property Windows Sidebar , System.Shell.RecycleBin object
- System.Shell.RecycleBin object Windows Sidebar , folderCount property
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.folderCount
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

# System.Shell.RecycleBin.folderCount property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of folders in the **Recycle Bin**.

This property is read-only.

## Syntax


```JScript
ifolderCount = System.Shell.RecycleBin.folderCount
```



## Property value

An **Integer** that receives the number of folders.

## Remarks

Files are not included in the **folderCount** total; see [**fileCount**](system-shell-recyclebin-filecount.md).

## Examples

The following example demonstrates how to get the total number of folders in the Recycle Bin.


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



 

 





