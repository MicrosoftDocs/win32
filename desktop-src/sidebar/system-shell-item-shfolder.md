---
title: System.Shell.Item.SHFolder property
description: Gets a System.Shell.Folder object from the System.Shell.Item.
ms.assetid: 6291a81c-5b6a-4cbe-8617-e3295759a00a
keywords:
- SHFolder property Windows Sidebar
- SHFolder property Windows Sidebar , System.Shell.Item object
- System.Shell.Item object Windows Sidebar , SHFolder property
topic_type:
- apiref
api_name:
- System.Shell.Item.SHFolder
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

# System.Shell.Item.SHFolder property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Shell.Folder**](system-shell-folder.md) object from the [**System.Shell.Item**](system-shell-item.md).

This property is read-only.

## Syntax


```JScript
objSHFolder = System.Shell.Item.SHFolder
```



## Property value

[**System.Shell.Folder**](system-shell-folder.md) that represents the [**System.Shell.Item**](system-shell-item.md).

## Remarks

Useful for performing folder operations on a [**System.Shell.Item**](system-shell-item.md) object that represents a system folder.

**SHFolder** does not get the parent folder of a [**System.Shell.Item**](system-shell-item.md) that represents a file or link.

## Examples

The following example demonstrates how to select a location, get a [**System.Shell.Folder**](system-shell-folder.md) object and create a new folder at that location.


```JScript
// Member variables.
var oShellFolderItem;
var oShellFolder;

// --------------------------------------------------------------------
// Display the folder picker dialog and get a Shell.Item object 
// from the selection. A Shell folder object is also obtained.
// --------------------------------------------------------------------
function ChooseAFolder()
{
    oShellFolderItem = System.Shell.chooseFolder("SDK Choose Folder Example", 0);
    if (oShellFolderItem)
    {
        spFeedback.innerHTML = oShellFolderItem.name + "<br/>";
        // Get a folder object from the System.Shell.Item.
        oShellFolder = oShellFolderItem.SHFolder;
    }
}

// --------------------------------------------------------------------
// Create a new folder.
// folderName: the user specified folder name.
// --------------------------------------------------------------------
function CreateFolder(folderName)
{
    if (folderName)
    {
        if (oShellFolder)
        {
            try
            {
                oShellFolder.newFolder(folderName);
                spFolderFeedback.innerHTML = oShellFolderItem.name + " folder created.<br/>";
            }
            catch (e)
            {
                spFolderFeedback.innerHTML = e.description ;
                // Error handling.
            }
        }
        else
        {
            spFolderFeedback.innerHTML = "Unable to create folder. No location specified.<br/>Please select a parent folder.<br/>";
        }
    }
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



 

 





