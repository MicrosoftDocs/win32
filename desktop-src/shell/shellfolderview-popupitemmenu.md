---
Description: Creates a shortcut menu for the specified item and returns the selected command string.
title: ShellFolderView.PopupItemMenu method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderView.PopupItemMenu
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellFolderView.PopupItemMenu method

Creates a shortcut menu for the specified item and returns the selected command string.

## Syntax


```JScript
retVal = ShellFolderView.PopupItemMenu(
  vItem,
  [ vx ],
  [ vy ]
)
```



## Parameters

<dl> <dt>

*vItem* \[in\]
</dt> <dd>

Type: **Variant**

The [**FolderItem**](folderitem.md) object for which the shortcut menu will be created.

</dd> <dt>

*vx* \[in, optional\]
</dt> <dd>

Type: **Variant**

The horizontal position of the menu, in screen coordinates.

</dd> <dt>

*vy* \[in, optional\]
</dt> <dd>

Type: **Variant**

The vertical position of the menu, in screen coordinates.

</dd> </dl>

## Return value

Type: **[**BSTR**](https://msdn.microsoft.com/en-us/library/ms221069(v=VS.71).aspx)\***

The **String** that receives the command string.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




