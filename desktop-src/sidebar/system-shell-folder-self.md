---
title: System.Shell.Folder.Self property
description: Gets a duplicate System.Shell.Folder object.
ms.assetid: 3fbd763a-e5de-4378-963f-d9eac18457d9
keywords:
- Self property Windows Sidebar
- Self property Windows Sidebar , System.Shell.Folder object
- System.Shell.Folder object Windows Sidebar , Self property
topic_type:
- apiref
api_name:
- System.Shell.Folder.Self
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

# System.Shell.Folder.Self property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a duplicate [**System.Shell.Folder**](system-shell-folder.md) object.

This property is read-only.

## Syntax


```JScript
objSelf = System.Shell.Folder.Self
```



## Property value

[**System.Shell.Folder**](system-shell-folder.md) that receives the duplicate.

## Remarks

Folder information is not provided if the object is a file or a shortcut (.Lnk) file.

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

 

 





