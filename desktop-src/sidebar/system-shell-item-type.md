---
title: System.Shell.Item.type property
description: Gets the verbose file type (not the extension) of the Windows Shell item.
ms.assetid: 1df6476a-4f07-41c7-b4d3-cd5a036f8fa8
keywords:
- type property Windows Sidebar
- type property Windows Sidebar , System.Shell.Item object
- System.Shell.Item object Windows Sidebar , type property
topic_type:
- apiref
api_name:
- System.Shell.Item.type
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

# System.Shell.Item.type property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the verbose file type (not the extension) of the Windows Shell item.

This property is read-only.

## Syntax


```JScript
strtype = System.Shell.Item.type
```



## Property value

A **String** that receives the file type.

## Examples

The following example demonstrates how to get the verbose type of an object dropped on the gadget.


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
        spFeedback.innerHTML += oItem.type + "<br/>"; 
                
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



 

 





