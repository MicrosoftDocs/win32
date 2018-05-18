---
title: System.Shell.Folder.newFolder method
description: Creates a new folder.
ms.assetid: '1bda6b9a-a6a7-4033-9be2-b74cc2b44651'
keywords: ["newFolder method Windows Sidebar", "newFolder method Windows Sidebar , System.Shell.Folder object", "System.Shell.Folder object Windows Sidebar , newFolder method"]
topic_type:
- apiref
api_name:
- System.Shell.Folder.newFolder
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Folder.newFolder method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Creates a new folder.

## Syntax


```JScript
System.Shell.Folder.newFolder(
  strNewFolder,
  [ intOptions ]
)
```



## Parameters

<dl> <dt>

*strNewFolder* \[in\]
</dt> <dd>

**String** that specifies the name of the new folder.

</dd> <dt>

*intOptions* \[in, optional\]
</dt> <dd>

This value is not defined.

</dd> </dl>

## Return value

This method does not return a value.

## Examples

The following example demonstrates how to select a location and create a new folder.


```JScript
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
// --------------------------------------------------------------------
function CreateFolder(folderName)
{
    try
    {
        if (oShellFolder)
        {
            oShellFolder.newFolder(folderName, 0);
            spFolderFeedback.innerHTML = folderName + " folder created.<br/>";
        }
        else
        {
            spFolderFeedback.innerHTML = "Unable to create folder. No location specified.<br/>Please select a parent folder.<br/>";
        }
    }
    catch (e)
    {
        // Error handling.
    }
}
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



 

 





