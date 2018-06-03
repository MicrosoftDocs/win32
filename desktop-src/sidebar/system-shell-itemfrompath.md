---
title: System.Shell.itemFromPath method
description: Retrieves a System.Shell.Item that represents an object at the specified Universal Naming Convention (UNC) path.
ms.assetid: 9e0cfff4-bd1e-4f62-a436-21b1d5617c8f
keywords:
- itemFromPath method Windows Sidebar
- itemFromPath method Windows Sidebar , System.Shell object
- System.Shell object Windows Sidebar , itemFromPath method
topic_type:
- apiref
api_name:
- System.Shell.itemFromPath
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

# System.Shell.itemFromPath method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves a [**System.Shell.Item**](system-shell-item.md) that represents an object at the specified Universal Naming Convention (UNC) path.

## Syntax


```JScript
objRetVal = System.Shell.itemFromPath(
  strPath
)
```



## Parameters

<dl> <dt>

*strPath* \[in\]
</dt> <dd>

**String** that specifies the UNC path.

</dd> </dl>

## Return value

[**System.Shell.Item**](system-shell-item.md) that represents the object at the specified UNC location, or null if the item cannot be determined.

## Examples

The following example demonstrates how to obtain a [**System.Shell.Item**](system-shell-item.md) based on its UNC location.


```JScript
// --------------------------------------------------------------------
// Display the name of an object obtained from the UNC path.
// --------------------------------------------------------------------
function GetItemFromPath()
{
    var oItem = System.Shell.itemFromPath(System.Gadget.path + "\\test.txt");
    spFeedback.innerHTML = oItem.name + "<br/>";
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



 

 





