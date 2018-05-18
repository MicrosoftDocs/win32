---
title: System.Shell.Item.isLink property
description: Gets whether the object is a link (or shortcut).
ms.assetid: '5b824649-92be-4f96-a7ea-6250a24fe7cc'
keywords: ["isLink property Windows Sidebar", "isLink property Windows Sidebar , System.Shell.Item object", "System.Shell.Item object Windows Sidebar , isLink property"]
topic_type:
- apiref
api_name:
- System.Shell.Item.isLink
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Item.isLink property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets whether the object is a link (or shortcut).

This property is read-only.

## Syntax


```JScript
bisLink = System.Shell.Item.isLink
```



## Property value

A **Boolean** that receives **true** if the item is a link; **false** otherwise.

## Remarks

A link object is a file that exists in one location and acts as a virtual mapping to another location (file, folder, or URL).

## Examples

The following example demonstrates how to determine whether an item is a link.


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



 

 





