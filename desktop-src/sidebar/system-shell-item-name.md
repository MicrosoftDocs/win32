---
title: System.Shell.Item.name property
description: Gets the name of the System.Shell.Item.
ms.assetid: 'e4599750-1548-4a78-86e1-5dfd0c00476b'
keywords: ["name property Windows Sidebar", "name property Windows Sidebar , System.Shell.Item object", "System.Shell.Item object Windows Sidebar , name property"]
topic_type:
- apiref
api_name:
- System.Shell.Item.name
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Item.name property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the name of the [**System.Shell.Item**](system-shell-item.md).

This property is read-only.

## Syntax


```JScript
strname = System.Shell.Item.name
```



## Property value

A **String** that receives the name.

## Remarks

Honors the "Hide extensions for known file types" setting in Windows Explorer.

## Examples

The following example demonstrates how to get the name for an object dropped on the gadget.


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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





