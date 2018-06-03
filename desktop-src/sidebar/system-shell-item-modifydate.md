---
title: System.Shell.Item.modifyDate property
description: Gets the last modified date of the System.Shell.Item.
ms.assetid: d81f4805-d278-4472-8225-5132698abba1
keywords:
- modifyDate property Windows Sidebar
- modifyDate property Windows Sidebar , System.Shell.Item object
- System.Shell.Item object Windows Sidebar , modifyDate property
topic_type:
- apiref
api_name:
- System.Shell.Item.modifyDate
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

# System.Shell.Item.modifyDate property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the last modified date of the [**System.Shell.Item**](system-shell-item.md).

This property is read-only.

## Syntax


```JScript
strmodifyDate = System.Shell.Item.modifyDate
```



## Property value

A **String** that receives a date.

## Remarks

If an item has not been modified, the creation date will be returned.

## Examples

The following example demonstrates how to get the last modified date for an object dropped on the gadget.


```JScript
// --------------------------------------------------------------------
// Display the names of objects dropped on the gadget.
// Objects are deleted, copied, or moved as required.
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
        spFeedback.innerHTML += "Modified date: " + oItem.modifyDate + "<br/>";
                
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



 

 





