---
title: System.Shell.RecycleBin.sizeUsed property
description: Gets the amount of space, in kilobytes (KB), used by the content of the Recycle Bin.
ms.assetid: 2cee75d4-ca6e-4a07-a699-93feb53c9f52
keywords:
- sizeUsed property Windows Sidebar
- sizeUsed property Windows Sidebar , System.Shell.RecycleBin object
- System.Shell.RecycleBin object Windows Sidebar , sizeUsed property
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.sizeUsed
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

# System.Shell.RecycleBin.sizeUsed property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the amount of space, in kilobytes (KB), used by the content of the Recycle Bin.

This property is read-only.

## Syntax


```JScript
strsizeUsed = System.Shell.RecycleBin.sizeUsed
```



## Property value

A **String** that receives the amount of space.

## Examples

The following example demonstrates how to get the size of the Recycle Bin content.


```JScript
// --------------------------------------------------------------------
// Display the Recycle Bin size.
// --------------------------------------------------------------------
function SizeReport()
{
    spRCFeedback.innerHTML = "Recycle Bin size: " + System.Shell.RecycleBin.sizeUsed + " kb";
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



 

 





