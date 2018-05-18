---
title: System.Shell.chooseFolder method
description: Displays a folder picker dialog box and retrieves a System.Shell.Item object that represents the selected folder.
ms.assetid: '5da15812-57de-4d00-bd53-2c38e37807ae'
keywords: ["chooseFolder method Windows Sidebar", "chooseFolder method Windows Sidebar , System.Shell object", "System.Shell object Windows Sidebar , chooseFolder method"]
topic_type:
- apiref
api_name:
- System.Shell.chooseFolder
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.chooseFolder method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Displays a folder picker dialog box and retrieves a [**System.Shell.Item**](system-shell-item.md) object that represents the selected folder.

## Syntax


```JScript
objRetVal = System.Shell.chooseFolder(
  strTitle,
  intOptions
)
```



## Parameters

<dl> <dt>

*strTitle* \[in\]
</dt> <dd>

**String** that specifies the title for the folder picker dialog box.

</dd> <dt>

*intOptions* \[in\]
</dt> <dd>

**Integer** that specifies the folder picker dialog box options.

> [!Note]  
> The only supported value is zero (0); effectively no options.

 

</dd> </dl>

## Return value

A [**System.Shell.Item**](system-shell-item.md) that represents the selected folder.

## Remarks

The root directory is set to the path for the users profile (%USERPROFILE%).

The **chooseFolder** dialog box:

![folder picker dialog box.](images/reference/choosefolder.png)

## Examples

The following example shows how to display the folder picker dialog box.


```JScript
// Create a shell item object.
var oSystemShellItem = System.Shell.chooseFolder("SDK Choose Folder Example", 0);
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





