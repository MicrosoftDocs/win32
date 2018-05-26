---
title: System.Shell.Folder.Parent property
description: Gets a System.Shell.Item object that represents the parent folder.
ms.assetid: 62c67281-c930-4ea6-b486-003dae19d094
keywords:
- Parent property Windows Sidebar
- Parent property Windows Sidebar , System.Shell.Folder object
- System.Shell.Folder object Windows Sidebar , Parent property
topic_type:
- apiref
api_name:
- System.Shell.Folder.Parent
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

# System.Shell.Folder.Parent property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Shell.Item**](system-shell-item.md) object that represents the parent folder.

This property is read-only.

## Syntax


```JScript
objParent = System.Shell.Folder.Parent
```



## Property value

[**System.Shell.Item**](system-shell-item.md) that receives the parent folder.

## Remarks

If the folder is a well-known Windows folder, such as the My Documents folder, then no parent value is returned.

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

[**System.Shell.Folder**](system-shell-folder.md)
</dt> <dt>

[**System.Shell**](system-shell.md)
</dt> </dl>

 

 





