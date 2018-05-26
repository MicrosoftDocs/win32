---
title: System.Shell.RecycleBin.fileCount property
description: Gets the number of files in the Recycle Bin.
ms.assetid: 51bebbe9-df39-4829-85f3-6c07538a2c6d
keywords:
- fileCount property Windows Sidebar
- fileCount property Windows Sidebar , System.Shell.RecycleBin object
- System.Shell.RecycleBin object Windows Sidebar , fileCount property
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.fileCount
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

# System.Shell.RecycleBin.fileCount property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of files in the **Recycle Bin**.

This property is read-only.

## Syntax


```JScript
ifileCount = System.Shell.RecycleBin.fileCount
```



## Property value

An **Integer** that receives the number of files.

## Remarks

Folders are not included in the **fileCount** total; see [**folderCount**](system-shell-recyclebin-foldercount.md).

## Examples

The following example demonstrates how to get the total number of files in the Recycle Bin.


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



 

 





