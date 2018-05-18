---
title: System.Shell.Item.isFolder property
description: Gets whether the object is a folder.
ms.assetid: '8b4b50da-5fdb-4049-a566-3f7194f45ca6'
keywords: ["isFolder property Windows Sidebar", "isFolder property Windows Sidebar , System.Shell.Item object", "System.Shell.Item object Windows Sidebar , isFolder property"]
topic_type:
- apiref
api_name:
- System.Shell.Item.isFolder
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Item.isFolder property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets whether the object is a folder.

This property is read-only.

## Syntax


```JScript
bisFolder = System.Shell.Item.isFolder
```



## Property value

A **Boolean** that receives **true** if the item is a folder; **false** otherwise.

## Examples

The following example demonstrates how to determine whether an item is a folder.


```JScript
// --------------------------------------------------------------------
// Display the names of objects dropped on the gadget.
// --------------------------------------------------------------------
function GetItemFromDrop()
{    
    spFeedback.innerHTML = "Item(s) dropped.<br/>";
    var intIndex = 0;
    var oItem;
    var sItem;
    while(oItem = System.Shell.itemFromFileDrop(event.dataTransfer, intIndex))
    {
        // Display object properties and increment the index.
        sItem = "Other: ";
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



 

 





