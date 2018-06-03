---
title: System.Shell.Item.path property
description: Gets the Universal Naming Convention (UNC) path (with filename) of the System.Shell.Item.
ms.assetid: 86d291ee-145b-43e3-8607-0fbdad034541
keywords:
- path property Windows Sidebar
- path property Windows Sidebar , System.Shell.Item object
- System.Shell.Item object Windows Sidebar , path property
topic_type:
- apiref
api_name:
- System.Shell.Item.path
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

# System.Shell.Item.path property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Universal Naming Convention (UNC) path (with filename) of the [**System.Shell.Item**](system-shell-item.md).

This property is read-only.

## Syntax


```JScript
strpath = System.Shell.Item.path
```



## Property value

A **String** that receives the UNC path and filename.

## Examples

The following example demonstrates how to determine the path of a linked item.


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
            oLinkItem = oItem.link;
            sItem = "Link (" + oLinkItem.path + "): ";
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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





