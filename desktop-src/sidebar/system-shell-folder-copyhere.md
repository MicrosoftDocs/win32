---
title: System.Shell.Folder.copyHere method
description: Copies a System.Shell.Item to a folder.
ms.assetid: '630aff20-d892-48ac-a4ea-93d4cf6b590d'
keywords: ["copyHere method Windows Sidebar", "copyHere method Windows Sidebar , System.Shell.Folder object", "System.Shell.Folder object Windows Sidebar , copyHere method"]
topic_type:
- apiref
api_name:
- System.Shell.Folder.copyHere
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Folder.copyHere method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Copies a [**System.Shell.Item**](system-shell-item.md) to a folder.

## Syntax


```JScript
System.Shell.Folder.copyHere(
  oItem,
  [ intOptions = 0 ]
)
```



## Parameters

<dl> <dt>

*oItem* \[in\]
</dt> <dd>

The [**System.Shell.Item**](system-shell-item.md) to copy.

</dd> <dt>

*intOptions* \[in, optional\]
</dt> <dd>

**Integer** that specifies any combination of copy operation options.

> [!Note]  
> These values are based on flags defined for use with the fFlags member of the C++ SHFILEOPSTRUCT structure. These flags are not defined for Microsoft Visual Basic, Visual Basic Scripting Edition (VBScript), or Microsoft JScript, so you must define the values or use their numeric equivalents.

 

<dt>



 (0)


</dt> <dd>

Default. No options specified.

</dd> <dt>



 (4)


</dt> <dd>

Do not display a progress dialog box.

</dd> <dt>



 (8)


</dt> <dd>

Rename the target file if a file exists at the target location with the same name.

</dd> <dt>



 (16)


</dt> <dd>

Click "Yes to All" in any dialog box displayed.

</dd> <dt>



 (64)


</dt> <dd>

Preserve undo information, if possible.

</dd> <dt>



 (128)


</dt> <dd>

Perform the operation only if a wildcard file name (\*.\*) is specified.

</dd> <dt>



 (256)


</dt> <dd>

Display a progress dialog box but do not show the file names.

</dd> <dt>



 (512)


</dt> <dd>

Do not confirm the creation of a new directory if the operation requires one to be created.

</dd> <dt>



 (1024)


</dt> <dd>

Do not display a user interface if an error occurs.

</dd> <dt>



 (4096)


</dt> <dd>

Disable recursion.

</dd> <dt>



 (8192)


</dt> <dd>

Do not copy connected files as a group. Only copy the specified files.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

A Shell folder object must be obtained from a [**System.Shell.Item**](system-shell-item.md) using the [**SHFolder**](system-shell-item-shfolder.md) property in order to perform this call.

## Examples

The following example demonstrates how to copy an object to a system folder.


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
        // Get a folder object from the System.Shell.Item.
        oShellFolder = oShellFolderItem.SHFolder;
    }
}

// --------------------------------------------------------------------
// Display the names of objects dropped on the gadget.
// Objects are deleted, copied, or moved as required.
// --------------------------------------------------------------------
function GetItemFromDrop()
{    
    var intIndex = 0;
    var oItem;
    while(oItem = System.Shell.itemFromFileDrop(event.dataTransfer, intIndex))
    {
        // Delete object as required.
        if (deleteDrop.checked == true)
        {
            System.Shell.RecycleBin.deleteItem(oItem.path);
        }
        
        // Copy object as required.
        if ((copyDrop.checked == true) &amp;&amp; (oShellFolder!= null))
        {
            try
            {
                oShellFolder.copyHere(oItem, 8);
            }
            catch (e)
            {
                // Error handling.
            }
        }
        
        // Move object as required.
        if ((moveDrop.checked == true) &amp;&amp; (oShellFolder != null))
        {
            try
            {
                oShellFolder.moveHere(oItem, 8);
            }
            catch (e)
            {
                // Error handling.
            }
        }
        
        intIndex++;
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



 

 





