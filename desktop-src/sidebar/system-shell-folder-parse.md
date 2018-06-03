---
title: System.Shell.Folder.parse method
description: Retrieves a System.Shell.Folder object that represents the folder containing the specified file.
ms.assetid: c42cb102-f5a7-4745-9a79-cae58f57d8b2
keywords:
- parse method Windows Sidebar
- parse method Windows Sidebar , System.Shell.Folder object
- System.Shell.Folder object Windows Sidebar , parse method
topic_type:
- apiref
api_name:
- System.Shell.Folder.parse
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

# System.Shell.Folder.parse method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves a [**System.Shell.Folder**](system-shell-folder.md) object that represents the folder containing the specified file.

## Syntax


```JScript
objRetVal = System.Shell.Folder.parse(
  strFilePath
)
```



## Parameters

<dl> <dt>

*strFilePath* \[in\]
</dt> <dd>

**String** that specifies the name of the file.

</dd> </dl>

## Return value

[**System.Shell.Folder**](system-shell-folder.md) object that represents the parent folder.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





