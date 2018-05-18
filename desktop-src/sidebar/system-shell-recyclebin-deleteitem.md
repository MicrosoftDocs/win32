---
title: System.Shell.RecycleBin.deleteItem method
description: Deletes an item from the system by moving it to the Recycle Bin.
ms.assetid: 'f41e549d-e21a-48a4-a5f6-6174f0ca7625'
keywords: ["deleteItem method Windows Sidebar", "deleteItem method Windows Sidebar , System.Shell.RecycleBin object", "System.Shell.RecycleBin object Windows Sidebar , deleteItem method"]
topic_type:
- apiref
api_name:
- System.Shell.RecycleBin.deleteItem
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.RecycleBin.deleteItem method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Deletes an item from the system by moving it to the **Recycle Bin**.

## Syntax


```JScript
strRetVal = System.Shell.RecycleBin.deleteItem(
  strItemToDelete
)
```



## Parameters

<dl> <dt>

*strItemToDelete* \[in\]
</dt> <dd>

**String** that specifies the item to delete.

</dd> </dl>

## Remarks

The **Recycle Bin Properties** settings determine how file deletion is handled. For example, whether files are deleted immediately or stored until the Recycle Bin is emptied, whether the Recycle Bin is system-wide or operates on a per-drive basis, and whether confirmation dialogs are displayed.

## Examples

The following example demonstrates how to delete objects from the system.


```JScript
// --------------------------------------------------------------------
// Display the names of objects dropped on the gadget.
// Objects are deleted as required.
// --------------------------------------------------------------------
function GetItemFromDrop()
{    
    spFeedback.innerHTML = "Item(s) dropped.<br/>";
    var intIndex = 0;
    var oItem;
    var sItem = "Other:";
    while(oItem = System.Shell.itemFromFileDrop(event.dataTransfer, intIndex))
    {
        // Display object properties and increment the index.
        if (oItem.isFileSystem == true)
        {
            sItem = "File: ";
        }
        if (oItem.isFolder == true)
        {
            sItem = "Folder: ";
        }
        if (oItem.isLink == true)
        {
            sItem = "Link: ";
        }
        spFeedback.innerHTML += sItem;
        spFeedback.innerHTML += oItem.name + "<br/>"; 
        
        // Delete object as required.
        if (deleteDrop.checked == true)
        {
            System.Shell.RecycleBin.deleteItem(oItem.path);
            spFeedback.innerHTML += "Item deleted.<br/>";
        }
        
        intIndex++;
    }
    System.Shell.refreshDesktop();
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



 

 





